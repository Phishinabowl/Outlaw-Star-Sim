"""Exact timing models and reviewed evidence registers; no workbook or source-media writes."""
import argparse
import csv
from datetime import datetime, timezone
from fractions import Fraction as F
import io
import json
from pathlib import Path
import re
from statistics import median
import sys

import alignment as a

ANCHORS = 'anchor_id episode_id image_id input_id video_source video_sha256 video_stream_index video_time_base media_origin_seconds subtitle_stream_index subtitle_sha256 subtitle_time_basis subtitle_shift_seconds locator_sha256 image_sha256 run_id role method recipe_json search_start_seconds search_end_seconds match_kind status local_start_pts local_end_pts player_timestamp player_precision_seconds candidate_score runner_up_gap reviewer reviewed_utc supersedes_anchor_id notes'.split()
MAPPINGS = 'mapping_id episode_id input_id segment_label web_start_seconds web_end_seconds model scale offset_seconds fit_anchor_ids holdout_anchor_ids status max_fit_interval_error_seconds median_holdout_interval_error_seconds max_holdout_interval_error_seconds max_anchor_width_seconds estimated_half_window_seconds method_version reviewer reviewed_utc supersedes_mapping_ids limitations'.split()
IDENTITY = 'episode_id video_source video_sha256 video_stream_index video_time_base media_origin_seconds subtitle_stream_index subtitle_sha256 subtitle_time_basis subtitle_shift_seconds locator_sha256'.split()
METRICS = 'max_fit_interval_error_seconds median_holdout_interval_error_seconds max_holdout_interval_error_seconds max_anchor_width_seconds'.split()


def rational(value):
    result=F(value)
    if a.ratio(result)!=value:raise ValueError('Noncanonical rational')
    return result


def utc(value):
    stamp=datetime.fromisoformat(value.replace('Z','+00:00'))
    if stamp.utcoffset() is None or stamp.utcoffset().total_seconds()!=0:raise ValueError('Review time must be UTC')


def load(root):
    base=Path(root)/'reference/indexes/animehistory'
    result=[]
    for name,fields in [('alignment-anchors.csv',ANCHORS),('alignment-mappings.csv',MAPPINGS)]:
        path=base/name
        if not path.exists():result.append([]);continue
        with path.open(encoding='utf-8',newline='') as stream:
            reader=csv.DictReader(stream)
            if reader.fieldnames!=fields:raise ValueError('Alignment CSV schema mismatch')
            rows=list(reader)
            if any(None in row or None in row.values() for row in rows):raise ValueError('Malformed CSV row')
            result.append(rows)
    return result


def csv_bytes(rows,fields):
    stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=fields,lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
    return stream.getvalue().encode('utf-8')


def interval(row):
    base=F(row['video_time_base']);origin=F(row['media_origin_seconds'])
    return int(row['local_start_pts'])*base-origin,int(row['local_end_pts'])*base-origin


def fit(points,model):
    """Points are (web, inclusive local start, inclusive local end), FIT only."""
    if not points:raise ValueError('No fitting points')
    x=[F(p[0]) for p in points]; y=[(F(p[1])+F(p[2]))/2 for p in points]
    if len(set(x))!=len(x):raise ValueError('Duplicate fitting web label')
    if model=='OFFSET':return F(1),median([yy-xx for xx,yy in zip(x,y)])
    if model!='LINEAR' or len(x)<2:raise ValueError('Insufficient/unknown model')
    n=len(x);den=n*sum(xx*xx for xx in x)-sum(x)**2
    scale=(n*sum(xx*yy for xx,yy in zip(x,y))-sum(x)*sum(y))/den
    return scale,(sum(y)-scale*sum(x))/n


def errors(points,scale,offset):
    return [max(F(lo)-(scale*F(web)+offset),F(0),scale*F(web)+offset-F(hi)) for web,lo,hi in points]


def evaluate(fitting,holdouts,model):
    """Never estimate coefficients with holdouts; retain failed observed values."""
    scale,offset=fit(fitting,model)
    fe=errors(fitting,scale,offset); he=errors(holdouts,scale,offset)
    width=max(F(hi)-F(lo) for _,lo,hi in fitting+holdouts)
    metrics=[max(fe),median(he) if he else None,max(he) if he else None,width]
    reasons=[]
    nf,nh=(3,2) if model=='OFFSET' else (5,3)
    if len(fitting)<nf or len(holdouts)<nh:reasons.append('insufficient independent fit/holdout count')
    if width>F(1,2):reasons.append('anchor width exceeds 0.5 s')
    if max(fe)>1 or not he or median(he)>F(1,2) or max(he)>1:reasons.append('residual limits failed')
    if model=='LINEAR':
        span=max(F(p[0]) for p in fitting)-min(F(p[0]) for p in fitting)
        if span<300:reasons.append('linear span below 300 s')
        if not F(95,100)<=scale<=F(105,100):reasons.append('linear scale outside supported range')
        if abs(scale-1)*span<1:reasons.append('linear drift below 1 s')
        baseline=evaluate(fitting,holdouts,'OFFSET')
        if not baseline['reasons']:reasons.append('OFFSET already passes')
        if not he or not baseline['metrics'][1] or baseline['metrics'][1]-median(he)<F(1,4):reasons.append('linear holdout improvement below 0.25 s')
    return dict(scale=scale,offset=offset,metrics=metrics,reasons=reasons)


def points(rows,locator):
    return [(F(locator[(r['episode_id'],r['image_id'])]['web_seconds']),*interval(r)) for r in rows]


def locators(root):
    return {(r['episode_id'],r['image_id']):r for path in (Path(root)/'reference/indexes/animehistory/CSVs').glob('episode-*.csv') for r in a.read_csv(path)}


def validate(anchors,mappings,locator):
    if any(set(r)!=set(ANCHORS) for r in anchors) or any(set(r)!=set(MAPPINGS) for r in mappings):raise ValueError('Row schema mismatch')
    by_id={r['anchor_id']:r for r in anchors}; by_map={r['mapping_id']:r for r in mappings}
    if len(by_id)!=len(anchors) or len(by_map)!=len(mappings):raise ValueError('Duplicate stable ID')
    accepted=set(); identities={}
    for r in anchors:
        if not re.fullmatch('ALNANC-[0-9]{6}',r['anchor_id']):raise ValueError('Invalid anchor ID')
        key=(r['episode_id'],r['image_id'])
        if key not in locator:raise ValueError('Unknown gallery key')
        identity={k:r[k] for k in IDENTITY}
        for key_name in ['video_stream_index','subtitle_stream_index']:identity[key_name]=int(identity[key_name])
        if a.input_id(identity)!=r['input_id']:raise ValueError('Input identity mismatch')
        if r['input_id'] in identities and identities[r['input_id']]!=identity:raise ValueError('Inconsistent identity tuple')
        identities[r['input_id']]=identity
        path=Path(r['video_source'])
        if path.is_absolute() or '..' in path.parts or not r['video_source'].startswith('_source_episodes/'):raise ValueError('Unsafe source reference')
        for field in ['input_id','video_sha256','subtitle_sha256','locator_sha256','image_sha256']:
            if not re.fullmatch('[a-f0-9]{64}',r[field]):raise ValueError('Invalid digest')
        for field in ['video_time_base','media_origin_seconds','search_start_seconds','search_end_seconds']:rational(r[field])
        if F(r['video_time_base'])<=0 or not 0<=F(r['search_start_seconds'])<F(r['search_end_seconds']):raise ValueError('Invalid timing domain')
        if r['subtitle_time_basis'] not in ['UNVERIFIED','MEDIA_RELATIVE','SHIFTED_TO_MEDIA']:raise ValueError('Unknown subtitle axis')
        if r['subtitle_time_basis']=='UNVERIFIED':
            if r['subtitle_shift_seconds']:raise ValueError('Unknown subtitle axis has a shift')
        else:
            rational(r['subtitle_shift_seconds'])
            if r['subtitle_time_basis']=='MEDIA_RELATIVE' and F(r['subtitle_shift_seconds'])!=0:raise ValueError('Wrong relative subtitle shift')
        if r['role'] not in ['LEAD','FIT','HOLDOUT'] or r['status'] not in ['CANDIDATE','MATCHED','AMBIGUOUS','NO_MATCH','REJECTED','SUPERSEDED']:raise ValueError('Unknown anchor state/role')
        if r['method']!='BOUNDED_FRAME_SEARCH_V1' or r['match_kind'] not in ['UNASSESSED','CORRESPONDING_FRAME','SHOT_INTERVAL','NONE']:raise ValueError('Unsupported prototype method/kind')
        if not re.fullmatch('ALNRUN-[a-f0-9]{32}',r['run_id']):raise ValueError('Invalid run ID')
        recipe=json.loads(r['recipe_json'])
        if not recipe.get('implementation_sha256') or not recipe.get('commands') or not recipe.get('reviewed_frame_hashes') and r['status']=='MATCHED':raise ValueError('Missing reproducibility recipe')
        if recipe.get('web_seconds')!=int(locator[key]['web_seconds']):raise ValueError('Stale web label recipe')
        for field in ['candidate_score','runner_up_gap']:
            if r[field] and not 0<=rational(r[field])<=1:raise ValueError('Invalid score')
        if bool(r['reviewer'])!=bool(r['reviewed_utc']):raise ValueError('Incomplete review provenance')
        if r['reviewed_utc']:utc(r['reviewed_utc'])
        if r['status'] in ['MATCHED','AMBIGUOUS','NO_MATCH','REJECTED','SUPERSEDED'] and (not r['notes'] or not r['reviewer']):raise ValueError('Missing assessment provenance')
        if r['status']=='MATCHED':
            lo,hi=interval(r)
            if not F(r['search_start_seconds'])<=lo<=hi<F(r['search_end_seconds']):raise ValueError('Match outside bounded search')
            if r['match_kind'] not in ['CORRESPONDING_FRAME','SHOT_INTERVAL']:raise ValueError('Unassessed match')
            active=(r['input_id'],r['image_id'])
            if active in accepted:raise ValueError('Competing active matches')
            accepted.add(active)
        elif r['local_start_pts'] or r['local_end_pts']:raise ValueError('Unaccepted anchor cannot project local time')
        previous=r['supersedes_anchor_id'];seen={r['anchor_id']}
        while previous:
            if previous in seen or previous not in by_id:raise ValueError('Anchor supersession cycle/missing target')
            old=by_id[previous]
            if (old['image_id'],old['input_id'])!=(r['image_id'],r['input_id']) or old['status']!='SUPERSEDED':raise ValueError('Invalid anchor supersession')
            seen.add(previous);previous=old['supersedes_anchor_id']
    active_maps=[]
    for r in mappings:
        if not re.fullmatch('ALNMAP-[0-9]{6}',r['mapping_id']):raise ValueError('Invalid mapping ID')
        if r['status'] not in ['PROPOSED','VALIDATED','REJECTED','SUPERSEDED'] or r['model'] not in ['OFFSET','LINEAR']:raise ValueError('Unknown mapping state/model')
        if r['method_version']!='ALIGNMENT_MODEL_V1' or not r['limitations']:raise ValueError('Missing model method/limitations')
        for name in ['scale','offset_seconds','estimated_half_window_seconds']:rational(r[name])
        if F(r['scale'])<=0 or (r['model']=='OFFSET' and F(r['scale'])!=1):raise ValueError('Invalid scale')
        start,end=int(r['web_start_seconds']),int(r['web_end_seconds'])
        if not 0<=start<end:raise ValueError('Invalid mapping domain')
        def selected(field,role):
            ids=r[field].split(';') if r[field] else []
            if ids!=sorted(set(ids)):raise ValueError('Duplicate/unsorted model votes')
            selected_rows=[by_id[k] for k in ids]
            if any(x['role']!=role or x['status']!='MATCHED' or x['input_id']!=r['input_id'] or x['episode_id']!=r['episode_id'] for x in selected_rows):raise ValueError('Role leakage/stale/unmatched model vote')
            return selected_rows
        fitting=selected('fit_anchor_ids','FIT');holdout=selected('holdout_anchor_ids','HOLDOUT')
        votes=fitting+holdout
        if not votes or len({x['image_id'] for x in votes})!=len(votes):raise ValueError('Duplicate-image vote')
        web=[int(locator[(x['episode_id'],x['image_id'])]['web_seconds']) for x in votes]
        if start!=min(web) or end!=max(web)+1:raise ValueError('Model extrapolation outside checked labels')
        result=evaluate(points(fitting,locator),points(holdout,locator),r['model'])
        if (F(r['scale']),F(r['offset_seconds']))!=(result['scale'],result['offset']):raise ValueError('Coefficients differ from FIT-only calculation')
        for name,value in zip(METRICS,result['metrics']):
            if r[name]!=(a.ratio(value) if value is not None else ''):raise ValueError('Stored model metrics differ')
        if r['status'] in ['VALIDATED','REJECTED']:
            if not r['reviewer']:raise ValueError('Missing model review')
            utc(r['reviewed_utc'])
        if r['status']=='VALIDATED':
            if result['reasons']:raise ValueError('Validated model fails gates: '+', '.join(result['reasons']))
            for old in active_maps:
                if old['input_id']==r['input_id'] and old['episode_id']==r['episode_id'] and start<int(old['web_end_seconds']) and int(old['web_start_seconds'])<end:raise ValueError('Conflicting validated coverage')
            active_maps.append(r)
        previous=r['supersedes_mapping_ids'].split(';') if r['supersedes_mapping_ids'] else []
        def chain(ids,seen):
            for identity in ids:
                if identity in seen or identity not in by_map:raise ValueError('Mapping supersession cycle/missing target')
                old=by_map[identity]
                if old['status']!='SUPERSEDED' or (old['episode_id'],old['input_id'])!=(r['episode_id'],r['input_id']):raise ValueError('Invalid mapping supersession')
                chain(old['supersedes_mapping_ids'].split(';') if old['supersedes_mapping_ids'] else [],seen|{identity})
        chain(previous,{r['mapping_id']})
    return dict(anchors=len(anchors),mappings=len(mappings),validated=sum(r['status']=='VALIDATED' for r in mappings))


def next_id(rows,field,prefix):
    return prefix+f'{max([int(r[field].split("-")[1]) for r in rows]+[0])+1:06d}'


def verify_current(root,anchors,ffprobe):
    """Explicit Episode 1 check, no dependence on disposable decoded frames."""
    if not anchors or {r['episode_id'] for r in anchors}!={'EP-01'}:raise ValueError('Current-media pilot checks Episode 1 only')
    _,images,identity,_,_,_=a.inspect_inputs(Path(root),1,sorted({r['image_id'] for r in anchors}),ffprobe,a.Budget(Path(root)/'reference/working/alignment/registry'))
    current=a.input_id(identity);hashes={r['image_id']:r['image_sha256'] for r in images}
    if any(r['input_id']!=current or r['image_sha256']!=hashes[r['image_id']] for r in anchors):raise ValueError('Current source/gallery differs from recorded input')
    return 'VERIFIED_CURRENT_EP01'


def record_run(root,run_id,assessments,ffprobe):
    """Explicit human/agent visual assessments, never automatic score promotion."""
    if not re.fullmatch('ALNRUN-[a-f0-9]{32}',run_id):raise ValueError('Invalid explicit run')
    run=a.safe_path(root,'reference/working/alignment/EP-01/'+run_id);manifest=a.read_json(run/'run.json')
    if manifest['owner']!=a.VERSION or manifest['status']!='COMPLETE_CANDIDATES':raise ValueError('Incomplete/unowned run')
    selected=[r['image_id'] for r in assessments]
    if len(set(selected))!=len(selected) or not selected:raise ValueError('Duplicate/empty assessments')
    with a.writer(Path(root)/'reference/working/alignment/registry'):
        anchors,mappings=load(root); locator=locators(root);validate(anchors,mappings,locator)
        a.Budget(run).check()
        _,current_images,identity,_,_,_=a.inspect_inputs(Path(root),1,selected,ffprobe,a.Budget(Path(root)/'reference/working/alignment/registry'))
        if a.input_id(identity)!=manifest['input_id']:raise ValueError('Run source inputs are stale')
        results={r['image_id']:r for r in manifest['results']}
        if any(image['image_sha256']!=results[image['image_id']]['image_sha256'] for image in current_images):raise ValueError('Run gallery image bytes are stale')
        for assessment in assessments:
            result=results[assessment['image_id']]
            if any(r['run_id']==run_id and r['image_id']==assessment['image_id'] for r in anchors):raise ValueError('Assessment already recorded; use explicit supersession for revision')
            record=dict.fromkeys(ANCHORS,'');record.update({k:str(v) for k,v in identity.items()})
            recipe=dict(manifest['recipe']);recipe.update(web_seconds=result['web_seconds'],diagnostic=result['diagnostic'],candidate_clusters=result['clusters'],run_manifest_sha256=a.digest(run/'run.json'),reviewed_frame_hashes={})
            lo=assessment.get('start_pts');hi=assessment.get('end_pts')
            if assessment['status']=='MATCHED':
                if lo is None or hi is None or lo>hi:raise ValueError('Explicit supported PTS interval required')
                frames=[f for f in result['frames'] if lo<=f['pts']<=hi]
                if not frames or frames[0]['pts']!=lo or frames[-1]['pts']!=hi:raise ValueError('Assessment endpoints not decoded')
                if any(F(right['local_seconds'])-F(left['local_seconds'])>F(1,10) for left,right in zip(frames,frames[1:])):raise ValueError('Interval not covered at native-frame density')
                for frame in frames:
                    if a.digest(a.safe_path(run,frame['image']))!=frame['sha256']:raise ValueError('Reviewed frame changed')
                    recipe['reviewed_frame_hashes'][str(frame['pts'])]=frame['sha256']
                record.update(local_start_pts=str(lo),local_end_pts=str(hi))
            record.update(anchor_id=next_id(anchors,'anchor_id','ALNANC-'),input_id=manifest['input_id'],image_id=result['image_id'],image_sha256=result['image_sha256'],run_id=run_id,role=result['role'],method='BOUNDED_FRAME_SEARCH_V1',recipe_json=a.canonical(recipe).decode(),search_start_seconds=result['search_start'],search_end_seconds=result['search_end'],match_kind=assessment.get('match_kind','UNASSESSED'),status=assessment['status'],candidate_score=result['clusters'][0]['score'] if result['clusters'] else '',runner_up_gap=result['runner_up_gap'] or '',reviewer=assessment['reviewer'],reviewed_utc=datetime.now(timezone.utc).isoformat(),notes=assessment['notes'])
            anchors.append(record)
        validate(anchors,mappings,locator)
        base=Path(root)/'reference/indexes/animehistory'
        a.atomic(base/'alignment-anchors.csv',csv_bytes(anchors,ANCHORS))
        if not (base/'alignment-mappings.csv').exists():a.atomic(base/'alignment-mappings.csv',csv_bytes(mappings,MAPPINGS))
        return [r['anchor_id'] for r in anchors[-len(assessments):]]


def propose(root,fit_ids,holdout_ids,model,label,limitations,ffprobe,assess=False,supersedes=''):
    with a.writer(Path(root)/'reference/working/alignment/registry'):
        anchors,mappings=load(root);locator=locators(root);validate(anchors,mappings,locator)
        by_id={r['anchor_id']:r for r in anchors}
        fitting=[by_id[k] for k in sorted(fit_ids)];holdout=[by_id[k] for k in sorted(holdout_ids)]
        if any(r['role']!='FIT' or r['status']!='MATCHED' for r in fitting) or any(r['role']!='HOLDOUT' or r['status']!='MATCHED' for r in holdout):raise ValueError('Only independently assigned reviewed anchors may participate')
        if len(set(fit_ids+holdout_ids))!=len(fit_ids+holdout_ids):raise ValueError('Duplicate/leaked vote')
        votes=fitting+holdout
        if not fitting or len({r['input_id'] for r in votes})!=1:raise ValueError('Missing/mixed input identities')
        _,current_images,identity,_,_,_=a.inspect_inputs(Path(root),1,[r['image_id'] for r in votes],ffprobe,a.Budget(Path(root)/'reference/working/alignment/registry'))
        if a.input_id(identity)!=fitting[0]['input_id']:raise ValueError('Current source differs from reviewed anchors')
        pinned={r['image_id']:r['image_sha256'] for r in votes}
        if any(image['image_sha256']!=pinned[image['image_id']] for image in current_images):raise ValueError('Current gallery bytes differ from reviewed anchors')
        result=evaluate(points(fitting,locator),points(holdout,locator),model)
        row=dict.fromkeys(MAPPINGS,'')
        web=[int(locator[(r['episode_id'],r['image_id'])]['web_seconds']) for r in votes]
        row.update(mapping_id=next_id(mappings,'mapping_id','ALNMAP-'),episode_id='EP-01',input_id=fitting[0]['input_id'],segment_label=label,web_start_seconds=str(min(web)),web_end_seconds=str(max(web)+1),model=model,scale=a.ratio(result['scale']),offset_seconds=a.ratio(result['offset']),fit_anchor_ids=';'.join(sorted(fit_ids)),holdout_anchor_ids=';'.join(sorted(holdout_ids)),status=('REJECTED' if result['reasons'] else 'VALIDATED') if assess else 'PROPOSED',estimated_half_window_seconds='2/1',method_version='ALIGNMENT_MODEL_V1',reviewer='Codex' if assess else '',reviewed_utc=datetime.now(timezone.utc).isoformat() if assess else '',supersedes_mapping_ids=supersedes,limitations=limitations+(' Gates: '+', '.join(result['reasons']) if result['reasons'] else ''))
        row.update({name:a.ratio(value) if value is not None else '' for name,value in zip(METRICS,result['metrics'])})
        if supersedes:
            old=next(r for r in mappings if r['mapping_id']==supersedes)
            if old['status']!='PROPOSED' or old['fit_anchor_ids']!=row['fit_anchor_ids'] or (old['scale'],old['offset_seconds'])!=(row['scale'],row['offset_seconds']):raise ValueError('Frozen FIT proposal differs; cannot retune against holdouts')
            old['status']='SUPERSEDED'
        mappings.append(row);validate(anchors,mappings,locator)
        a.atomic(Path(root)/'reference/indexes/animehistory/alignment-mappings.csv',csv_bytes(mappings,MAPPINGS))
        return row


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    subs=parser.add_subparsers(dest='command',required=True)
    p=subs.add_parser('validate');p.add_argument('--current',action='store_true');p.add_argument('--ffprobe')
    p=subs.add_parser('record');p.add_argument('--run-id',required=True);p.add_argument('--assessments',type=Path,required=True);p.add_argument('--ffprobe',required=True)
    p=subs.add_parser('propose');p.add_argument('--fit',nargs='+',required=True);p.add_argument('--holdout',nargs='*',default=[]);p.add_argument('--model',choices=['OFFSET','LINEAR'],default='OFFSET');p.add_argument('--label',required=True);p.add_argument('--limitations',required=True);p.add_argument('--ffprobe',required=True);p.add_argument('--assess',action='store_true');p.add_argument('--supersedes',default='')
    args=parser.parse_args()
    if args.command=='validate':
        anchors,mappings=load(a.ROOT);report=validate(anchors,mappings,locators(a.ROOT))
        if args.current and not args.ffprobe:parser.error('--current requires explicit --ffprobe')
        report['current_media_check']=verify_current(a.ROOT,anchors,args.ffprobe) if args.current else 'NOT_PERFORMED'
        print(json.dumps(report))
    elif args.command=='record':print(json.dumps(dict(recorded=record_run(a.ROOT,args.run_id,a.read_json(args.assessments),args.ffprobe))))
    else:print(json.dumps(propose(a.ROOT,args.fit,args.holdout,args.model,args.label,args.limitations,args.ffprobe,args.assess,args.supersedes)))


if __name__=='__main__':main()
