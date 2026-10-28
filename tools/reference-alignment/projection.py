"""Read-only alignment projections for the existing workbook and future report joins."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
import json
from pathlib import Path
import sys

import alignment as a
import models as m

TIMING_FIELDS = 'matched_local_start matched_local_end estimated_local_time timing_basis mapping_id alignment_availability suggested_search_half_window_seconds anchor_id anchor_status alignment_input_id alignment_method alignment_reason alignment_checked_utc matched_local_start_seconds matched_local_end_seconds estimated_local_seconds'.split()
USABLE = {'VERIFIED_CURRENT','RECORDED_UNCHECKED'}


def label(value):
    # Millisecond display is rounded; exact evidence remains in the CSV's integer PTS/rationals.
    millis=round(F(value)*1000)
    if millis<0:raise ValueError('Negative playback time')
    hours,rest=divmod(millis,3600000);minutes,rest=divmod(rest,60000);seconds,ms=divmod(rest,1000)
    return f'{hours:02}:{minutes:02}:{seconds:02}.{ms:03}'


def empty_timing():
    row=dict.fromkeys(TIMING_FIELDS,'')
    row.update(timing_basis='UNMAPPED',alignment_availability='NOT_RECORDED',alignment_reason='NO_ALIGNMENT_RECORD',suggested_search_half_window_seconds=None,matched_local_start_seconds=None,matched_local_end_seconds=None,estimated_local_seconds=None)
    return row


def inspect_availability(root,anchors,verify=False,ffprobe=None):
    """Routine builds do not hash videos. Explicit verification checks recorded episodes."""
    grouped=defaultdict(list)
    for row in anchors:grouped[row['input_id']].append(row)
    result={}
    coverage_path=Path(root)/'reference/indexes/performance-subtitle-coverage.json'
    coverage={r['episode_id']:r for r in a.read_json(coverage_path)['episodes']} if coverage_path.exists() else {}
    for identity,rows in grouped.items():
        record=rows[0];entry=coverage.get(record['episode_id'])
        state='RECORDED_UNCHECKED';reason='Video digest not recomputed by routine workbook build'
        if not entry:
            state,reason='MISSING','Source/subtitle coverage entry unavailable'
        else:
            source=a.safe_path(root,record['video_source']);subtitle=a.safe_path(root,entry['local_subtitle'])
            locator=Path(root)/f"reference/indexes/animehistory/CSVs/episode-{int(record['episode_id'][3:]):02}.csv"
            if not source.exists() or not subtitle.exists() or not locator.exists():
                state,reason='MISSING','Required source/subtitle/locator input unavailable'
            elif record['video_source']!=entry['source'] or source.stat().st_size!=entry['source_bytes'] or record['subtitle_stream_index']!=str(entry['subtitle_stream']) or record['subtitle_sha256']!=entry['subtitle_sha256'] or a.digest(subtitle)!=record['subtitle_sha256'] or a.digest(locator)!=record['locator_sha256']:
                state,reason='MISMATCH','Source profile, size, subtitle or locator differs from recorded identity'
            else:
                cache=Path(root)/'reference/cache/animehistory-review'/record['episode_id']
                manifest=a.read_json(cache/'manifest.json') if (cache/'manifest.json').exists() else {}
                for row in rows:
                    image=manifest.get('images',{}).get(row['image_id'],{})
                    if image.get('file'):
                        path=a.safe_path(cache,image['file'])
                        if path.exists() and a.digest(path)!=row['image_sha256']:
                            state,reason='MISMATCH','Available gallery bytes differ from recorded anchor';break
        result[identity]=dict(state=state,reason=reason,checked_utc='')
    if verify:
        if not ffprobe:raise ValueError('Explicit verification requires --ffprobe')
        # Missing/stale inputs are visible states, never a false verified-current claim.
        candidates=[r for r in anchors if result[r['input_id']]['state'] in USABLE]
        if candidates:
            m.verify_current(Path(root),candidates,ffprobe)
            now=datetime.now(timezone.utc).isoformat()
            for identity in {r['input_id'] for r in candidates}:
                result[identity]=dict(state='VERIFIED_CURRENT',reason='Full source and registered inputs checked during this build',checked_utc=now)
    return result


def project(sources,manual,anchors,mappings,availability):
    """One gallery row per source key; history lives in separate tables/bridges."""
    keys={(r['episode_id'],r['image_id']) for r in sources}
    if len(keys)!=len(sources):raise ValueError('Duplicate gallery key')
    if len({r['anchor_id'] for r in anchors})!=len(anchors) or len({r['mapping_id'] for r in mappings})!=len(mappings):raise ValueError('Duplicate alignment ID')
    by_image=defaultdict(list);image_anchors=[];image_mappings=[];mapping_anchors=[]
    for anchor in anchors:
        key=(anchor['episode_id'],anchor['image_id'])
        if key not in keys:raise ValueError('Anchor outside source key baseline')
        by_image[key].append(anchor)
        image_anchors.append(dict(image_key=':'.join(key),anchor_id=anchor['anchor_id'],input_id=anchor['input_id']))
    for mapping in mappings:
        for field,role in [('fit_anchor_ids','FIT'),('holdout_anchor_ids','HOLDOUT')]:
            for anchor_id in mapping[field].split(';') if mapping[field] else []:
                mapping_anchors.append(dict(mapping_id=mapping['mapping_id'],anchor_id=anchor_id,role=role,mapping_status=mapping['status']))
    gallery=[]
    for source in sources:
        key=(source['episode_id'],source['image_id']);image_key=':'.join(key);web=F(source['web_seconds'])
        related=by_image[key];active=[r for r in related if r['status']!='SUPERSEDED']
        valid=[r for r in mappings if r['episode_id']==source['episode_id'] and r['status']=='VALIDATED' and F(r['web_start_seconds'])<=web<F(r['web_end_seconds'])]
        matched=[r for r in active if r['status']=='MATCHED']
        identities={r['input_id'] for r in active+valid}
        if not identities:
            identities={r['input_id'] for r in anchors+mappings if r['episode_id']==source['episode_id'] and r['status']!='SUPERSEDED'}
        row=dict(episode_id=key[0],image_id=key[1],image_key=image_key,**empty_timing())
        row['anchor_status']=';'.join(sorted({r['status'] for r in active}))
        if identities:
            # Multiple releases require explicit reconciliation; never select a convenient latest row.
            if len(identities)!=1 or len(valid)>1 or len(matched)>1:
                raise ValueError('Conflicting alignment identities/coverage for image '+image_key)
            identity=next(iter(identities));check=availability.get(identity,dict(state='RECORDED_UNCHECKED',reason='No current-input check recorded',checked_utc=''))
            row.update(alignment_input_id=identity,alignment_availability=check['state'],alignment_checked_utc=check['checked_utc'])
            row['alignment_reason']=check['reason'] if check['state'] not in USABLE else 'OUTSIDE_VALIDATED_RANGE' if not valid and not matched else 'RECORDED_ALIGNMENT' if check['state']=='RECORDED_UNCHECKED' else 'CURRENT_INPUT_CHECK_PASSED'
            if check['state'] in USABLE:
                if valid:
                    mapping=valid[0];estimate=F(mapping['scale'])*web+F(mapping['offset_seconds'])
                    row.update(estimated_local_time=label(estimate),estimated_local_seconds=float(estimate),mapping_id=mapping['mapping_id'],suggested_search_half_window_seconds=float(F(mapping['estimated_half_window_seconds'])),timing_basis='MAPPING_ESTIMATE',alignment_method=mapping['method_version'])
                    image_mappings.append(dict(image_key=image_key,mapping_id=mapping['mapping_id'],input_id=identity))
                if matched:
                    anchor=matched[0];lo,hi=m.interval(anchor)
                    row.update(matched_local_start=label(lo),matched_local_end=label(hi),matched_local_start_seconds=float(lo),matched_local_end_seconds=float(hi),anchor_id=anchor['anchor_id'],timing_basis='DIRECT_MATCH',alignment_method=anchor['method'])
        gallery.append(row)
    manual_rows=[]
    for source in manual:
        row=dict(episode_id=source['episode_id'],image_id=source['image_id'],image_key=source['episode_id']+':'+source['image_id'],**empty_timing())
        row.update(timing_basis='PLAYER_LEAD',alignment_reason='UNRECONCILED_PLAYER_LABEL')
        manual_rows.append(row)
    return dict(gallery_timing=gallery,manual_timing=manual_rows,image_anchors=image_anchors,image_mappings=image_mappings,mapping_anchors=mapping_anchors)


def export(root,verify=False,ffprobe=None):
    sys.path.insert(0,str(Path(root)/'tools/reference-extraction'))
    import category_index as ci
    sources=ci.locators();manual=ci.supplements(sources)
    anchors,mappings=m.load(root)
    locator={(r['episode_id'],r['image_id']):r for r in sources}
    m.validate(anchors,mappings,locator)
    availability=inspect_availability(root,anchors,verify,ffprobe)
    data=project(sources,manual,anchors,mappings,availability)
    anchor_views=[]
    for row in anchors:
        check=availability[row['input_id']]
        lo,hi=m.interval(row) if row['status']=='MATCHED' else (None,None)
        anchor_views.append({**row,'image_key':row['episode_id']+':'+row['image_id'],'web_timestamp':locator[(row['episode_id'],row['image_id'])]['web_timestamp'],'matched_local_start':label(lo) if lo is not None else '', 'matched_local_end':label(hi) if hi is not None else '', 'alignment_availability':check['state'],'alignment_checked_utc':check['checked_utc']})
    mapping_views=[]
    for row in mappings:
        check=availability[row['input_id']]
        mapping_views.append({**row,'web_range':f"[{row['web_start_seconds']},{row['web_end_seconds']})",'fit_count':len(row['fit_anchor_ids'].split(';')) if row['fit_anchor_ids'] else 0,'holdout_count':len(row['holdout_anchor_ids'].split(';')) if row['holdout_anchor_ids'] else 0,'alignment_availability':check['state'],'alignment_checked_utc':check['checked_utc']})
    data.update(anchors=anchor_views,mappings=mapping_views,availability=availability,report=dict(gallery_rows=len(sources),manual_rows=len(manual),anchor_rows=len(anchors),mapping_rows=len(mappings),timing_basis=dict(Counter(r['timing_basis'] for r in data['gallery_timing'])),image_mapping_links=len(data['image_mappings']),image_anchor_links=len(data['image_anchors']),mapping_anchor_links=len(data['mapping_anchors']),media_verification_requested=verify))
    return data


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);parser.add_argument('--verify-current',action='store_true');parser.add_argument('--ffprobe')
    args=parser.parse_args();output=args.output.absolute()
    if not output.is_relative_to((a.ROOT/'.tmp').absolute()):raise ValueError('Projection output must remain under repository .tmp')
    a.safe_path(a.ROOT,output.relative_to(a.ROOT))
    data=export(a.ROOT,args.verify_current,args.ffprobe);a.atomic(output,a.encode(data));print(json.dumps(data['report']))


if __name__=='__main__':main()
