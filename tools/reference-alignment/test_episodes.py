"""Cross-episode plans and register/model/cleanup regression coverage."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import alignment as a
import finish as f
import models as m
import projection as p
import reproduce as r
import test_models as fixtures


class EpisodeTests(unittest.TestCase):
    def setUp(self):
        base=a.ROOT/'.tmp/alignment-episode-tests'
        base.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=base)
        self.root=Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def plan(self,episode=2):
        return dict(schema_version=1,episode_id=f'EP-{episode:02d}',selections=[
            dict(image_id='847151',role='FIT',search_start_seconds='180',search_end_seconds='192'),
            dict(image_id='847191',role='HOLDOUT',search_start_seconds='330',search_end_seconds='342')])

    def test_all_26_episodes_accept_explicit_bounded_plans(self):
        for episode in range(1,27):
            with self.subTest(episode=episode):
                result=a.selection_plan(self.plan(episode),episode,['847151'])
                self.assertEqual(result['847151']['search_end_seconds'],'192/1')

    def test_bad_plan_refused_before_search_io(self):
        def wrong_episode(p):p['episode_id']='EP-01'
        def duplicate(p):p['selections'].append(deepcopy(p['selections'][0]))
        def role(p):p['selections'][0]['role']='AUTO'
        def wide(p):p['selections'][0]['search_end_seconds']='193'
        def negative(p):p['selections'][0]['search_start_seconds']='-1'
        def reverse(p):p['selections'][0]['search_end_seconds']='180'
        def zero(p):p['selections'][0]['search_end_seconds']='1/0'
        def numeric(p):p['selections'][0]['search_start_seconds']=180
        def extra(p):p['command']='execute arbitrary text'
        for mutate in [wrong_episode,duplicate,role,wide,negative,reverse,zero,numeric,extra]:
            plan=self.plan();mutate(plan)
            with self.subTest(mutate=mutate.__name__),self.assertRaises(ValueError):
                a.search(self.root,2,['847151'],'unused','unused',[],plan=plan)
        with self.assertRaises(ValueError):
            a.search(self.root,2,['999'],'unused','unused',[],plan=self.plan())
        self.assertEqual(list(self.root.iterdir()),[])

    def fixture(self,episode):
        anchors,_,loc=fixtures.ModelTests().registry()
        name=f'EP-{episode:02d}'
        for row in anchors:
            row['episode_id']=name
            identity={k:row[k] for k in m.IDENTITY}
            identity['video_stream_index']=int(identity['video_stream_index'])
            identity['subtitle_stream_index']=int(identity['subtitle_stream_index'])
            row['input_id']=a.input_id(identity)
        loc={(name,image):value for (_,image),value in loc.items()}
        return anchors,loc,identity

    def inspect(self,identity,anchors):
        images=[dict(image_id=r['image_id'],image_sha256=r['image_sha256']) for r in anchors]
        return None,images,identity,None,None,None

    def test_record_frozen_fit_holdout_model_verify_and_cleanup_ep02_ep26(self):
        for episode in [2,26]:
            with self.subTest(episode=episode):
                root=self.root/str(episode);root.mkdir()
                anchors,loc,identity=self.fixture(episode)
                run_id='ALNRUN-'+f'{episode:032x}'
                run=root/f'reference/working/alignment/EP-{episode:02d}'/run_id
                run.mkdir(parents=True)
                frame=run/'frame-00000.png';frame.write_bytes(b'fixture decoded bytes')
                recipe=dict(implementation_sha256='f'*64,commands=[['ffmpeg']],tools={'ffmpeg':'fixture'})
                results=[dict(image_id=r['image_id'],web_seconds=int(loc[(r['episode_id'],r['image_id'])]['web_seconds']),
                    image_sha256=r['image_sha256'],role=r['role'],search_start=r['search_start_seconds'],search_end=r['search_end_seconds'],
                    clusters=[dict(score='1/1')],runner_up_gap='1/10',diagnostic='FIXTURE',
                    frames=[dict(pts=int(r['local_start_pts']),local_seconds=a.ratio(int(r['local_start_pts'])/1000),image=frame.name,sha256=a.digest(frame))]) for r in anchors]
                manifest=dict(owner=a.VERSION,run_id=run_id,status='COMPLETE_CANDIDATES',identity=identity,
                    input_id=a.input_id(identity),declared_roles={r['image_id']:r['role'] for r in anchors},recipe=recipe,results=results)
                (run/'run.json').write_bytes(a.encode(manifest))
                assessments=[dict(image_id=r['image_id'],status='MATCHED',match_kind='CORRESPONDING_FRAME',
                    start_pts=int(r['local_start_pts']),end_pts=int(r['local_end_pts']),reviewer='Fixture',notes='Synthetic corresponding-frame fixture') for r in anchors]
                base=root/'reference/indexes/animehistory';(base/'CSVs').mkdir(parents=True)
                def inspect(root_arg,episode_arg,selected,*args):
                    return self.inspect(identity,[r for r in anchors if r['image_id'] in selected])
                with patch.object(m,'locators',return_value=loc),patch.object(a,'inspect_inputs',side_effect=inspect) as inspected:
                    with self.assertRaisesRegex(ValueError,'outside declared'):
                        m.record_run(root,run_id,[dict(image_id='999')],'fixture',episode)
                    ids=m.record_run(root,run_id,assessments,'fixture',episode)
                    self.assertEqual(inspected.call_args.args[1],episode)
                    changed=deepcopy(manifest)
                    changed['results'][0]['role']='HOLDOUT'
                    (run/'run.json').write_bytes(a.encode(changed))
                    with self.assertRaisesRegex(ValueError,'predeclared role'):
                        m.record_run(root,run_id,assessments[:1],'fixture',episode)
                    changed['declared_roles'][anchors[0]['image_id']]='HOLDOUT'
                    (run/'run.json').write_bytes(a.encode(changed))
                    with self.assertRaisesRegex(ValueError,'Cannot swap'):
                        m.record_run(root,run_id,assessments[:1],'fixture',episode)
                    (run/'run.json').write_bytes(a.encode(manifest))
                    frozen=m.propose(root,ids[:3],[],'OFFSET','fixture','Synthetic only','fixture')
                    checked=m.propose(root,ids[:3],ids[3:],'OFFSET','fixture','Synthetic only','fixture',True,frozen['mapping_id'])
                    self.assertEqual(checked['episode_id'],f'EP-{episode:02d}')
                    self.assertEqual(checked['status'],'VALIDATED')
                    recorded,_=m.load(root)
                    self.assertEqual(m.verify_current(root,recorded,'fixture'),f'VERIFIED_CURRENT_EP{episode:02d}')
                    # A wrong explicit episode cannot locate/record the same run.
                    with self.assertRaises(FileNotFoundError):m.record_run(root,run_id,assessments,'fixture',1)
                    preview=f.finish(root,episode)
                    self.assertTrue(preview['runs'][0]['eligible'])
                    f.finish(root,episode,apply=True,preview_sha256=preview['preview_sha256'])
                    self.assertFalse(run.exists())
                    self.assertEqual(m.validate(*m.load(root),loc)['validated'],1)

    def test_ep26_projection_and_bounded_hash_reproduction(self):
        anchors,loc,identity=self.fixture(26)
        _,maps,_=fixtures.ModelTests().registry()
        maps[0].update(episode_id='EP-26',input_id=anchors[0]['input_id'])
        sources=[dict(episode_id=ep,image_id=image,**value) for (ep,image),value in loc.items()]
        sources.extend([dict(episode_id='EP-26',image_id='6',web_seconds='250'),
                        dict(episode_id='EP-02',image_id='7',web_seconds='250')])
        availability={anchors[0]['input_id']:dict(state='VERIFIED_CURRENT',reason='Fixture',checked_utc='2026-10-28T00:00:00Z')}
        projected=p.project(sources,[],anchors,maps,availability)['gallery_timing']
        self.assertEqual(projected[0]['timing_basis'],'DIRECT_MATCH')
        self.assertEqual(projected[0]['estimated_local_seconds'],98.0)
        self.assertEqual(projected[-2]['estimated_local_seconds'],248.0)
        self.assertEqual(projected[-1]['timing_basis'],'UNMAPPED')
        row=anchors[0];source=self.root/row['video_source']
        source.parent.mkdir(parents=True);source.write_bytes(b'fixture media')
        recipe=json.loads(row['recipe_json'])
        recipe.update(tools={'ffmpeg':'fixture version'},commands=[['ffmpeg','-ss','97.5','-t','1',
            f"reference/working/alignment/EP-26/{row['run_id']}/1/fine-0/frame-%05d.png"]],
            reviewed_frame_hashes={'98000':a.hashlib.sha256(b'frame').hexdigest()})
        row['recipe_json']=json.dumps(recipe)
        def decode(*args):
            folder=args[7];folder.mkdir();frame=folder/'frame-00000.png';frame.write_bytes(b'frame')
            return [dict(pts=98000,path=frame)],[]
        with patch.object(m,'load',return_value=(anchors,maps)),patch.object(m,'locators',return_value=loc),\
                patch.object(a,'inspect_inputs',return_value=self.inspect(identity,[row])) as inspected,\
                patch.object(a,'run_process',return_value=b'fixture version\n'),patch.object(a,'decode',side_effect=decode):
            result=r.reproduce(self.root,row['anchor_id'],'ffmpeg','ffprobe')
            self.assertEqual(inspected.call_args.args[1],26)
            self.assertEqual(result['status'],'REPRODUCED')
        self.assertEqual(list((self.root/'.tmp/alignment-reproduction').iterdir()),[])

    def test_current_verification_groups_episodes_and_rejects_stale_bytes(self):
        first,_,identity1=self.fixture(1);last,_,identity26=self.fixture(26)
        def inspect(root,episode,*args):
            return self.inspect(identity1,first) if episode==1 else self.inspect(identity26,last)
        with patch.object(a,'inspect_inputs',side_effect=inspect) as calls:
            self.assertEqual(m.verify_current(self.root,first+last,'fixture'),'VERIFIED_CURRENT_EP01_EP26')
            self.assertEqual([c.args[1] for c in calls.call_args_list],[1,26])
            broken=deepcopy(last);broken[0]['image_sha256']='0'*64
            with self.assertRaisesRegex(ValueError,'differs'):m.verify_current(self.root,broken,'fixture')
        for episode in ['EP-00','EP-27','EP-2','../EP-02']:
            with self.assertRaises(ValueError):m.episode_number(episode)


if __name__=='__main__':unittest.main()
