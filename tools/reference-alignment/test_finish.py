import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import alignment as a
import finish as f
import models as m
import test_models as fixtures


class FinishTests(unittest.TestCase):
    def setUp(self):
        scratch = a.ROOT/'.tmp/alignment-finish-tests'
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch)
        self.root = Path(self.temp.name)
        self.anchors, self.maps, self.locators = fixtures.ModelTests().registry()
        self.run_id = self.anchors[0]['run_id']
        self.path = self.root/'reference/working/alignment/EP-01'/self.run_id
        self.path.mkdir(parents=True)
        base = self.root/'reference/indexes/animehistory'
        (base/'CSVs').mkdir(parents=True)
        (base/'CSVs/episode-01.csv').write_text('fixture locator bytes')
        self.frame = self.path/'frame-00000.png'
        self.frame.write_bytes(b'synthetic decoded frame')
        recipe = dict(implementation_sha256='f'*64, commands=[['ffmpeg']], tools={'ffmpeg': 'fixture'})
        results = []
        for row in self.anchors:
            results.append(dict(image_id=row['image_id'], image_sha256=row['image_sha256'],
                                role=row['role'],search_start=row['search_start_seconds'],
                                search_end=row['search_end_seconds'],frames=[dict(pts=int(row['local_start_pts']),
                                image=self.frame.name, sha256=a.digest(self.frame))]))
        self.manifest = dict(owner=a.VERSION,run_id=self.run_id,status='COMPLETE_CANDIDATES',
                             input_id=self.anchors[0]['input_id'],recipe=recipe,results=results)
        self.save_manifest()
        for row in self.anchors:
            row['recipe_json'] = json.dumps(dict(**recipe,web_seconds=int(self.locators[('EP-01',row['image_id'])]['web_seconds']),
                run_manifest_sha256=a.digest(self.path/'run.json'),reviewed_frame_hashes={row['local_start_pts']:a.digest(self.frame)}))
        self.save_registers()
        self.loc_patch = patch.object(m,'locators',return_value=self.locators)
        self.loc_patch.start()

    def tearDown(self):
        self.loc_patch.stop()
        self.temp.cleanup()

    def save_manifest(self):
        (self.path/'run.json').write_bytes(a.encode(self.manifest))

    def save_registers(self):
        base=self.root/'reference/indexes/animehistory'
        (base/'alignment-anchors.csv').write_bytes(m.csv_bytes(self.anchors,m.ANCHORS))
        (base/'alignment-mappings.csv').write_bytes(m.csv_bytes(self.maps,m.MAPPINGS))

    def test_preview_keep_apply_idempotence_preserve_registers_and_other_media(self):
        sentinel=self.root/'reference/cache/retained.png'
        sentinel.parent.mkdir(parents=True);sentinel.write_bytes(b'keep')
        before={p:a.digest(p) for p in (self.root/'reference/indexes/animehistory').glob('*.csv')}
        plan=f.finish(self.root,1)
        self.assertTrue(plan['runs'][0]['eligible']);self.assertTrue(self.path.exists())
        self.assertEqual(f.finish(self.root,1,keep_output=True)['action'],'KEEP_OUTPUT')
        result=f.finish(self.root,1,apply=True,preview_sha256=plan['preview_sha256'])
        self.assertEqual(result['removed_runs'],[self.run_id]);self.assertFalse(self.path.exists())
        self.assertEqual(f.finish(self.root,1)['runs'],[])
        self.assertEqual(before,{p:a.digest(p) for p in before});self.assertTrue(sentinel.exists())

    def test_stale_preview_refused_for_frame_and_register_change(self):
        plan=f.finish(self.root,1)
        (self.path/'new.log').write_text('changed')
        with self.assertRaisesRegex(ValueError,'stale'):f.finish(self.root,1,apply=True,preview_sha256=plan['preview_sha256'])
        plan=f.finish(self.root,1)
        self.anchors[0]['notes']='Revised rationale';self.save_registers()
        with self.assertRaisesRegex(ValueError,'stale'):f.finish(self.root,1,apply=True,preview_sha256=plan['preview_sha256'])
        self.assertTrue(self.path.exists())

    def test_missing_assessment_and_candidate_block_all_deletion(self):
        self.anchors.pop();self.maps=[];self.save_registers()
        plan=f.finish(self.root,1);self.assertFalse(plan['runs'][0]['eligible'])
        with self.assertRaisesRegex(ValueError,'Unresolved'):f.finish(self.root,1,apply=True,preview_sha256=plan['preview_sha256'])
        self.assertTrue(self.path.exists())
        row=self.anchors[0];row.update(status='CANDIDATE',local_start_pts='',local_end_pts='',match_kind='UNASSESSED')
        self.manifest['results']=self.manifest['results'][:-1];self.save_manifest();self.save_registers()
        self.assertFalse(f.finish(self.root,1)['runs'][0]['eligible'])

    def test_corrupt_retained_manifest_or_frame_blocks_cleanup(self):
        self.frame.write_bytes(b'changed')
        self.assertFalse(f.finish(self.root,1)['runs'][0]['eligible'])
        self.frame.write_bytes(b'synthetic decoded frame')
        self.manifest['extra']='changed';self.save_manifest()
        self.assertFalse(f.finish(self.root,1)['runs'][0]['eligible'])

    def test_registered_discard_bypass_refused(self):
        with self.assertRaisesRegex(ValueError,'bypass'):f.finish(self.root,1,[self.run_id])

    def test_explicit_failed_or_abandoned_unregistered_discard(self):
        self.anchors=[];self.maps=[];self.save_registers()
        for status in ['FAILED','COMPLETE_CANDIDATES']:
            self.manifest['status']=status;self.save_manifest()
            self.assertFalse(f.finish(self.root,1)['runs'][0]['eligible'])
            plan=f.finish(self.root,1,[self.run_id]);self.assertTrue(plan['runs'][0]['eligible'])
        f.finish(self.root,1,[self.run_id],True,plan['preview_sha256'])
        self.assertFalse(self.path.exists())

    def test_running_unknown_owner_traversal_and_missing_run_refused(self):
        for status in ['RUNNING','UNKNOWN']:
            self.manifest['status']=status;self.save_manifest()
            with self.assertRaisesRegex(ValueError,'Active'):f.finish(self.root,1)
        self.manifest.update(status='FAILED',owner='other');self.save_manifest()
        with self.assertRaisesRegex(ValueError,'Unowned'):f.finish(self.root,1)
        for episode in [0,27]:
            with self.assertRaises(ValueError):f.finish(self.root,episode)
        with self.assertRaises(ValueError):f.finish(self.root,1,['../escape'])

    def test_symlink_or_reparse_guard(self):
        # Mock the platform reparse signal; Windows symlink creation may require elevation.
        real=a.safe_path
        def checked(base,relative):
            target=Path(base)/relative
            if target.name==self.frame.name:raise ValueError('Symlink/reparse point refused')
            return real(base,relative)
        with patch.object(a,'safe_path',side_effect=checked):
            with self.assertRaisesRegex(ValueError,'reparse'):f.finish(self.root,1)
        self.assertTrue(self.path.exists())

    def test_failed_deletion_is_reported_and_retry_preserves_evidence(self):
        plan=f.finish(self.root,1)
        with patch.object(f.shutil,'rmtree',side_effect=PermissionError('locked')):
            with self.assertRaises(PermissionError):f.finish(self.root,1,apply=True,preview_sha256=plan['preview_sha256'])
        self.assertTrue(self.path.exists());m.validate(*m.load(self.root),self.locators)

    def test_unexpected_file_blocks_even_explicit_discard(self):
        (self.path/'unique-review-notes.txt').write_text('only copy')
        self.assertFalse(f.finish(self.root,1)['runs'][0]['eligible'])
        self.anchors=[];self.maps=[];self.save_registers()
        self.assertFalse(f.finish(self.root,1,[self.run_id])['runs'][0]['eligible'])

    def test_absent_discard_duplicate_discard_and_unknown_entry_refused(self):
        with self.assertRaisesRegex(ValueError,'absent'):f.finish(self.root,1,['ALNRUN-'+'a'*32])
        with self.assertRaisesRegex(ValueError,'Invalid'):f.finish(self.root,1,[self.run_id,self.run_id])
        (self.path.parent/'unexpected').mkdir()
        with self.assertRaisesRegex(ValueError,'Unexpected'):f.finish(self.root,1)


if __name__=='__main__':unittest.main()
