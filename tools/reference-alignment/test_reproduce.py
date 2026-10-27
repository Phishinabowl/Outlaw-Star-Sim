import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import alignment as a
import models as m
import reproduce as r
import test_models as fixtures


class ReproductionTests(unittest.TestCase):
    def setUp(self):
        base=a.ROOT/'.tmp/alignment-reproduction-tests'
        base.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=base)
        self.root=Path(self.temp.name)
        self.anchors,self.maps,self.loc=fixtures.ModelTests().registry()
        self.row=self.anchors[0]
        recipe=json.loads(self.row['recipe_json'])
        recipe.update(tools={'ffmpeg':'fixture version'},commands=[['ffmpeg','-ss','97.5','-t','1',
            f"reference/working/alignment/EP-01/{self.row['run_id']}/1/fine-0/frame-%05d.png"]],
            reviewed_frame_hashes={'98000':a.hashlib.sha256(b'frame').hexdigest()})
        self.row['recipe_json']=json.dumps(recipe)
        source=self.root/self.row['video_source'];source.parent.mkdir(parents=True);source.write_bytes(b'source')
        self.patches=[patch.object(m,'load',return_value=(self.anchors,self.maps)),
                      patch.object(m,'locators',return_value=self.loc),
                      patch.object(m,'verify_current',return_value='VERIFIED_CURRENT_EP01'),
                      patch.object(a,'run_process',return_value=b'fixture version\n')]
        for p in self.patches:p.start()

    def tearDown(self):
        for p in reversed(self.patches):p.stop()
        self.temp.cleanup()

    def decode(self,*args):
        folder=args[7];folder.mkdir();path=folder/'frame-00000.png';path.write_bytes(b'frame')
        return [dict(pts=98000,path=path)],[]

    def assert_no_output(self):
        self.assertEqual(list((self.root/'.tmp/alignment-reproduction').iterdir()),[])

    def test_reproduction_hashes_and_auto_cleanup(self):
        with patch.object(a,'decode',side_effect=self.decode):
            self.assertEqual(r.reproduce(self.root,self.row['anchor_id'],'ffmpeg','ffprobe')['status'],'REPRODUCED')
        self.assert_no_output()

    def test_wrong_decoder_version_refused_and_cleaned(self):
        with patch.object(a,'run_process',return_value=b'other version\n'):
            with self.assertRaisesRegex(ValueError,'version differs'):r.reproduce(self.root,self.row['anchor_id'],'ffmpeg','ffprobe')
        self.assert_no_output()

    def test_failed_decode_and_hash_mismatch_cleaned(self):
        with patch.object(a,'decode',side_effect=RuntimeError('interrupted')):
            with self.assertRaises(RuntimeError):r.reproduce(self.root,self.row['anchor_id'],'ffmpeg','ffprobe')
        self.assert_no_output()
        with patch.object(a,'decode',return_value=([dict(pts=98001,path=self.root/self.row['video_source'])],[])):
            with self.assertRaisesRegex(ValueError,'hashes differ'):r.reproduce(self.root,self.row['anchor_id'],'ffmpeg','ffprobe')
        self.assert_no_output()

    def test_unknown_anchor_and_unbounded_recipe_refused(self):
        with self.assertRaisesRegex(ValueError,'accepted anchor'):r.reproduce(self.root,'missing','ffmpeg','ffprobe')
        recipe=json.loads(self.row['recipe_json']);recipe['commands'][0][4]='12'
        self.row['recipe_json']=json.dumps(recipe)
        with self.assertRaisesRegex(ValueError,'one-second'):r.reproduce(self.root,self.row['anchor_id'],'ffmpeg','ffprobe')
        self.assert_no_output()


if __name__=='__main__':unittest.main()
