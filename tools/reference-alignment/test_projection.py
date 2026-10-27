from copy import deepcopy
from fractions import Fraction as F
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import alignment as a
import models as m
import projection as v
import test_models as fixtures


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.anchors,self.maps,locator=fixtures.ModelTests().registry()
        self.sources=[dict(episode_id=ep,image_id=image,web_seconds=row['web_seconds']) for (ep,image),row in locator.items()]
        self.identity=self.anchors[0]['input_id']
        self.check={self.identity:dict(state='RECORDED_UNCHECKED',reason='Not rehashed',checked_utc='')}

    def project(self):return v.project(self.sources,[],self.anchors,self.maps,self.check)

    def test_direct_intervals_and_model_estimates_are_separate(self):
        result=self.project()['gallery_timing'][0]
        self.assertEqual(result['timing_basis'],'DIRECT_MATCH')
        self.assertEqual(result['matched_local_start'],'00:01:38.000')
        self.assertEqual(result['estimated_local_time'],'00:01:38.000')
        self.assertEqual(result['matched_local_start_seconds'],98)
        self.assertEqual(result['mapping_id'],'ALNMAP-000001')
        self.assertEqual(result['alignment_availability'],'RECORDED_UNCHECKED')

    def test_half_open_boundaries_and_unmapped_blanks(self):
        self.sources.extend([dict(episode_id='EP-01',image_id='6',web_seconds='99'),dict(episode_id='EP-01',image_id='7',web_seconds='501')])
        rows=self.project()['gallery_timing']
        self.assertEqual(rows[0]['timing_basis'],'DIRECT_MATCH')
        for row in rows[-2:]:
            self.assertEqual(row['timing_basis'],'UNMAPPED')
            self.assertEqual(row['estimated_local_time'],'')
            self.assertIsNone(row['estimated_local_seconds'])
            self.assertEqual(row['alignment_reason'],'OUTSIDE_VALIDATED_RANGE')

    def test_ambiguous_candidate_rejected_and_superseded_never_direct(self):
        for status in ['AMBIGUOUS','CANDIDATE','REJECTED','SUPERSEDED','NO_MATCH']:
            self.anchors[0].update(status=status,local_start_pts='',local_end_pts='')
            row=self.project()['gallery_timing'][0]
            self.assertEqual(row['timing_basis'],'MAPPING_ESTIMATE')
            self.assertEqual(row['matched_local_start'],'')

    def test_missing_and_mismatch_disable_derived_times(self):
        for state in ['MISSING','MISMATCH']:
            self.check[self.identity]['state']=state
            for row in self.project()['gallery_timing']:
                self.assertEqual(row['timing_basis'],'UNMAPPED')
                self.assertEqual(row['mapping_id'],'')
                self.assertEqual(row['matched_local_start'],'')
                self.assertIsNone(row['estimated_local_seconds'])
                self.assertEqual(row['alignment_availability'],state)
        self.assertTrue(self.anchors[0]['local_start_pts'])

    def test_manual_player_lead_has_own_grain_and_keeps_label(self):
        manual=[dict(episode_id='EP-04',image_id='EP-04-MAN-001',local_timestamp='17:15')]
        before=deepcopy(manual)
        data=v.project(self.sources,manual,self.anchors,self.maps,self.check)
        self.assertEqual(len(data['gallery_timing']),5)
        self.assertEqual(len(data['manual_timing']),1)
        self.assertEqual(data['manual_timing'][0]['timing_basis'],'PLAYER_LEAD')
        self.assertEqual(data['manual_timing'][0]['estimated_local_time'],'')
        self.assertEqual(manual,before)

    def test_bridges_do_not_multiply_image_counts_or_mutate_sources(self):
        before=deepcopy((self.sources,self.anchors,self.maps))
        result=self.project()
        self.assertEqual(len(result['gallery_timing']),5)
        self.assertEqual(len(result['image_anchors']),5)
        self.assertEqual(len(result['image_mappings']),5)
        self.assertEqual(len(result['mapping_anchors']),5)
        self.assertEqual(before,(self.sources,self.anchors,self.maps))

    def test_conflicting_coverage_and_duplicate_keys_refused(self):
        self.maps.append(dict(self.maps[0],mapping_id='ALNMAP-000002'))
        with self.assertRaises(ValueError):self.project()
        self.maps.pop();self.sources.append(dict(self.sources[0]))
        with self.assertRaises(ValueError):self.project()

    def test_multiple_input_identity_not_silently_selected(self):
        other=dict(self.anchors[0],anchor_id='ALNANC-000006',input_id='a'*64)
        self.anchors.append(other)
        with self.assertRaises(ValueError):self.project()

    def test_zero_and_millisecond_carry_display(self):
        self.assertEqual(v.label(F(0)),'00:00:00.000')
        self.assertEqual(v.label(F(599999,10000)),'00:01:00.000')
        self.assertIsNone(v.empty_timing()['estimated_local_seconds'])

    def availability_fixture(self,root):
        source=root/'_source_episodes/fixture.mkv';source.parent.mkdir();source.write_bytes(b'fixture')
        sub=root/'fixture.ass';sub.write_bytes(b'subtitle')
        locator=root/'reference/indexes/animehistory/CSVs/episode-01.csv';locator.parent.mkdir(parents=True);locator.write_bytes(b'fixture')
        entry=dict(episode_id='EP-01',source='_source_episodes/fixture.mkv',source_bytes=7,local_subtitle='fixture.ass',subtitle_stream=1,subtitle_sha256=a.digest(sub))
        coverage=root/'reference/indexes/performance-subtitle-coverage.json';coverage.write_text(json.dumps(dict(episodes=[entry])))
        row=self.anchors[0];row.update(subtitle_sha256=a.digest(sub),locator_sha256=a.digest(locator))
        return source,sub

    def test_availability_default_does_not_hash_video_and_detects_mismatch(self):
        base=a.ROOT/'.tmp/alignment-view-tests';base.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=base) as name:
            root=Path(name);source,sub=self.availability_fixture(root)
            real_digest=a.digest;calls=[]
            def tracked(path):calls.append(Path(path));return real_digest(path)
            with patch.object(a,'digest',side_effect=tracked):
                result=v.inspect_availability(root,[self.anchors[0]])
            self.assertEqual(result[self.identity]['state'],'RECORDED_UNCHECKED')
            self.assertNotIn(source,calls)
            sub.write_bytes(b'changed')
            self.assertEqual(v.inspect_availability(root,[self.anchors[0]])[self.identity]['state'],'MISMATCH')
            source.unlink()
            self.assertEqual(v.inspect_availability(root,[self.anchors[0]])[self.identity]['state'],'MISSING')

    def test_explicit_verification_is_distinct(self):
        base=a.ROOT/'.tmp/alignment-view-tests';base.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=base) as name:
            root=Path(name);self.availability_fixture(root)
            with patch.object(m,'verify_current',return_value='VERIFIED_CURRENT_EP01') as call:
                result=v.inspect_availability(root,[self.anchors[0]],True,'ffprobe')
            self.assertEqual(call.call_count,1)
            self.assertEqual(result[self.identity]['state'],'VERIFIED_CURRENT')
            self.assertTrue(result[self.identity]['checked_utc'])


if __name__=='__main__':unittest.main()
