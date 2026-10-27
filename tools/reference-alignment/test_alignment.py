"""Offline Stage 2 regressions. Synthetic media only; all fixtures removed afterward."""
from fractions import Fraction as F
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image
import alignment as a


class MatcherTests(unittest.TestCase):
    def setUp(self):
        base=a.ROOT/'reference/working/alignment/tests'
        base.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=base)
        self.root=Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def png(self,name='frame-00000.png',color='black'):
        path=self.root/name
        Image.new('RGB',(32,24),color).save(path)
        return path

    def test_exact_rationals_and_identity(self):
        self.assertEqual(a.ratio('0.125'),'1/8')
        self.assertEqual(a.input_id({'b':2,'a':1}),a.input_id({'a':1,'b':2}))
        self.assertNotEqual(a.input_id({'hash':'old'}),a.input_id({'hash':'new'}))

    def test_mask_overlap_union_and_threshold(self):
        mask,count=a.masks_checked([[0,0,320,72],[0,0,320,20]])
        self.assertEqual(count,320*168)
        with self.assertRaises(ValueError):a.masks_checked([[0,0,320,73]])
        for box in [[0,0,321,2],[2,0,1,3],[-1,0,2,3],[0,0,1]]:
            with self.assertRaises(ValueError):a.masks_checked([box])

    def test_mae_and_overlay_mask(self):
        black=Image.new('L',(320,240),0); white=Image.new('L',(320,240),255)
        mask,n=a.masks_checked([])
        self.assertEqual(a.score(black,black,mask,n),1)
        self.assertEqual(a.score(black,white,mask,n),0)
        overlay=black.copy();overlay.paste(255,(0,204,320,240))
        mask,n=a.masks_checked([[0,204,320,240]])
        self.assertEqual(a.score(black,overlay,mask,n),1)

    def test_aspect_rejected(self):
        path=self.png()
        self.assertEqual(a.normalized(path,F(4,3))[1],F(4,3))
        with self.assertRaises(ValueError):a.normalized(path,F(16,9))

    def test_holds_repeats_low_score_and_empty(self):
        records=[dict(local=F(i,4),score=F(1)) for i in range(5)]
        self.assertEqual(a.candidate_state(a.clusters(records))[0],'BROAD_SCORE_REGION')
        records.append(dict(local=F(9),score=F(1)))
        self.assertEqual(a.candidate_state(a.clusters(records))[0],'AMBIGUOUS_CLUSTERS')
        self.assertEqual(a.candidate_state(a.clusters([dict(local=F(1),score=F(89,100))]))[0],'LOW_SCORE_REVIEW')
        self.assertEqual(a.candidate_state([])[0],'NO_CANDIDATES')

    def test_ranking_threshold_edges(self):
        groups=[[dict(local=F(1),score=F(9,10))],[dict(local=F(2),score=F(89,100))]]
        self.assertEqual(a.candidate_state(groups)[0],'CANDIDATE_REQUIRES_VISUAL_REVIEW')
        groups[1][0]['score']+=F(1,10000)
        self.assertEqual(a.candidate_state(groups)[0],'AMBIGUOUS_CLUSTERS')

    def parsed(self,points,base=F(1,1000),origin=F(0),start=F(0),end=F(2)):
        paths=[self.png(f'frame-{i:05d}.png') for i in range(len(points))]
        log=self.root/'decode.log'
        log.write_text(f'config in time_base: {a.ratio(base)}\n'+''.join(f'n: {i} pts: {p} pts_time: ignored\n' for i,p in enumerate(points)))
        return a.parse_frames(log,paths,base,origin,start,end)

    def test_actual_pts_variable_intervals_and_origins(self):
        values=self.parsed([1000,1033,1100],origin=F(1))
        self.assertEqual([r['local'] for r in values],[F(0),F(33,1000),F(1,10)])
        self.assertEqual(self.parsed([-1000,-960],origin=F(-1))[1]['local'],F(1,25))

    def test_duplicate_disordered_and_out_of_range_refused(self):
        for points in [[100,100],[200,100],[-1],[2000]]:
            with self.assertRaises(ValueError):self.parsed(points)

    def test_missing_timestamp_and_corrupt_output_refused(self):
        path=self.png(); log=self.root/'decode.log'
        log.write_text('config in time_base: 1/1000\n')
        with self.assertRaises(ValueError):a.parse_frames(log,[path],F(1,1000),F(0),F(0),F(1))
        path.write_bytes(b'corrupt')
        log.write_text('config in time_base: 1/1000\nn: 0 pts: 0 pts_time: 0\n')
        with self.assertRaises(OSError):a.parse_frames(log,[path],F(1,1000),F(0),F(0),F(1))

    def test_hash_change_and_during_read_detection(self):
        path=self.png();first=a.digest(path);path.write_bytes(b'changed')
        self.assertNotEqual(first,a.digest(path))
        with patch.object(a,'signature',side_effect=[(1,),(2,)]):
            with self.assertRaises(ValueError):a.digest(path)

    def test_frame_disk_wall_caps(self):
        self.png()
        for args in [dict(frames=0),dict(size=1),dict(wall=-1)]:
            with self.assertRaises(ValueError):a.Budget(self.root,**args).check()

    def test_subprocess_failure_timeout_and_interrupt(self):
        with self.assertRaises(subprocess.CalledProcessError):
            a.run_process([sys.executable,'-c','raise SystemExit(2)'],a.Budget(self.root))
        with self.assertRaises(subprocess.TimeoutExpired):
            a.run_process([sys.executable,'-c','import time;time.sleep(5)'],a.Budget(self.root,wall=.2))
        budget=a.Budget(self.root)
        with patch.object(budget,'check',side_effect=[(0,0),KeyboardInterrupt]):
            with self.assertRaises(KeyboardInterrupt):
                a.run_process([sys.executable,'-c','import time;time.sleep(5)'],budget,self.root/'process.log')

    def test_failed_run_manifest_retained_and_no_authored_writes(self):
        marker=self.root/'untouched.csv';marker.write_text('keep')
        with patch.object(a,'inspect_inputs',side_effect=ValueError('fixture failure')):
            with self.assertRaises(ValueError):a.search(self.root,1,['846774'],'unused','unused',[])
        manifests=list(self.root.rglob('run.json'))
        self.assertEqual(len(manifests),1)
        self.assertEqual(json.loads(manifests[0].read_text())['status'],'FAILED')
        self.assertEqual(marker.read_text(),'keep')
        a.cleanup(self.root,manifests[0].parent.name,1)
        self.assertFalse(manifests[0].parent.exists())

    def test_scope_guard_before_any_io(self):
        for ep,ids in [(2,['846774']),(1,['later']),(1,['846774','846774'])]:
            with self.assertRaises(ValueError):a.search(self.root,ep,ids,'unused','unused',[])
        self.assertEqual(list(self.root.iterdir()),[])

    def fixture_inputs(self):
        source=self.root/'_source_episodes/fixture.mkv';source.parent.mkdir();source.write_bytes(b'video fixture')
        subtitle=self.root/'fixture.ass';subtitle.write_text('Dialogue: 0,0:00:01.00,x\nDialogue: 0,0:00:02.00,x\nDialogue: 0,0:00:03.00,x\n')
        ep=self.root/'reference/indexes/performance-subtitle-coverage.json';ep.parent.mkdir(parents=True)
        entry=dict(episode_id='EP-01',source='_source_episodes/fixture.mkv',source_bytes=source.stat().st_size,subtitle_stream=1,subtitle_codec='ass',local_subtitle='fixture.ass',subtitle_sha256=a.digest(subtitle))
        ep.write_text(json.dumps(dict(episodes=[entry])))
        locator=self.root/'reference/indexes/animehistory/CSVs/episode-01.csv';locator.parent.mkdir(parents=True)
        locator.write_text('episode_id,image_id,web_seconds\nEP-01,846774,106\n')
        cache=self.root/'reference/cache/animehistory-review/EP-01';cache.mkdir(parents=True)
        gallery=cache/'gallery.png';Image.new('RGB',(32,24)).save(gallery)
        manifest=dict(csv_sha256=a.digest(locator),images={'846774':dict(state='cached',file='gallery.png',sha256=a.digest(gallery))})
        (cache/'manifest.json').write_text(json.dumps(manifest))
        probe=dict(format=dict(start_time='0',duration='10'),streams=[dict(index=0,codec_type='video',sample_aspect_ratio='1:1',width=32,height=24,time_base='1/1000'),dict(index=1,codec_type='subtitle',codec_name='ass')])
        return source,subtitle,locator,gallery,probe

    def inspect_fixture(self,probe,times=('1','2','3')):
        values=[json.dumps(probe).encode(),json.dumps(dict(packets=[dict(pts_time=t) for t in times])).encode()]
        with patch.object(a,'run_process',side_effect=values):
            return a.inspect_inputs(self.root,1,['846774'],'unused',a.Budget(self.root))

    def test_input_identity_and_unknown_subtitle_axis(self):
        source,subtitle,locator,gallery,probe=self.fixture_inputs()
        identity=self.inspect_fixture(probe)[2]
        self.assertEqual(identity['video_sha256'],a.digest(source))
        self.assertEqual(identity['subtitle_time_basis'],'MEDIA_RELATIVE')
        self.assertEqual(self.inspect_fixture(probe,('4','5','6'))[2]['subtitle_time_basis'],'UNVERIFIED')

    def test_changed_gallery_and_locator_refused(self):
        source,subtitle,locator,gallery,probe=self.fixture_inputs()
        before=gallery.read_bytes();gallery.write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError,'Gallery image digest'):self.inspect_fixture(probe)
        gallery.write_bytes(before);locator.write_text(locator.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'Stale gallery'):self.inspect_fixture(probe)

    def test_changed_subtitle_and_wrong_stream_refused(self):
        source,subtitle,locator,gallery,probe=self.fixture_inputs()
        before=subtitle.read_bytes();subtitle.write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError,'Subtitle digest'):self.inspect_fixture(probe)
        subtitle.write_bytes(before);probe['streams'][1]['codec_name']='subrip'
        with self.assertRaisesRegex(ValueError,'Subtitle stream'):self.inspect_fixture(probe)

    def test_unvalidated_nonzero_origin_and_missing_source_refused(self):
        source,subtitle,locator,gallery,probe=self.fixture_inputs()
        probe['format']['start_time']='-1'
        with self.assertRaisesRegex(ValueError,'Nonzero container origin'):self.inspect_fixture(probe)
        source.unlink()
        with self.assertRaises(FileNotFoundError):self.inspect_fixture(probe)

    def test_video_size_and_ambiguous_stream_refused(self):
        source,subtitle,locator,gallery,probe=self.fixture_inputs()
        before=source.read_bytes();source.write_bytes(b'x')
        with self.assertRaisesRegex(ValueError,'Video size'):self.inspect_fixture(probe)
        source.write_bytes(before);probe['streams'].append(dict(probe['streams'][0]))
        with self.assertRaisesRegex(ValueError,'Ambiguous video stream'):self.inspect_fixture(probe)

    def test_writer_conflict_and_link_guard(self):
        with a.writer(self.root):
            with self.assertRaises((ValueError,OSError)):
                with a.writer(self.root):pass
        # Test the Windows reparse predicate without requiring symlink-creation privileges.
        path=self.png()
        actual=path.lstat()
        class Reparse:
            st_mode=actual.st_mode
            st_file_attributes=0x400
        with patch.object(Path,'lstat',return_value=Reparse()):
            with self.assertRaisesRegex(ValueError,'reparse'):a.safe_path(self.root,path.name)

    def test_cleanup_ownership_and_path_guard(self):
        with self.assertRaises(ValueError):a.cleanup(self.root,'../escape',1)
        run='ALNRUN-'+'a'*32
        folder=self.root/'reference/working/alignment/EP-01'/run;folder.mkdir(parents=True)
        (folder/'run.json').write_text(json.dumps(dict(owner='other',run_id=run)))
        with self.assertRaises(ValueError):a.cleanup(self.root,run,1)
        self.assertTrue(folder.exists())
        for value in ['../escape',str(self.root.absolute())]:
            with self.assertRaises(ValueError):a.safe_path(self.root,value)

    @unittest.skipUnless(os.environ.get('ALIGNMENT_TEST_FFMPEG'),'Set ALIGNMENT_TEST_FFMPEG for synthetic decode integration')
    def test_real_synthetic_decode_pts_and_cleanup(self):
        exe=os.environ['ALIGNMENT_TEST_FFMPEG']; source=self.root/'synthetic.mkv'
        subprocess.run([exe,'-v','error','-f','lavfi','-i','testsrc2=size=64x48:rate=20:duration=3','-c:v','ffv1',str(source)],check=True,capture_output=True)
        before=a.digest(source)
        records,_=a.decode(exe,source,0,F(1,1000),F(0),F(1),F(2),self.root/'decode',a.Budget(self.root),False)
        self.assertEqual([r['pts'] for r in records],list(range(1000,2000,50)))
        self.assertEqual(a.digest(source),before)


if __name__=='__main__':unittest.main()
