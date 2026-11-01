"""Offline output-routing regressions; synthetic sources and mocked media processes only."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[2]

class OutputRoutingTests(unittest.TestCase):
    def setUp(self):
        parent=ROOT/'.tmp/output-routing-tests';parent.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=parent);self.root=Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def load(self,name):
        spec=importlib.util.spec_from_file_location('routing_'+name,ROOT/'tools/reference-extraction'/f'{name}.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        module.ROOT=self.root
        return module

    def source(self,episode=7):
        p=self.root/'_source_episodes'/f'fixture_-_{episode:02}_-_example.mkv'
        p.parent.mkdir(exist_ok=True);p.write_bytes(b'synthetic source; never decoded')
        return p

    def test_inventory_manifest_has_owned_source_directory(self):
        module=self.load('inventory');source=self.source()
        (self.root/'_source_settei').mkdir()
        with contextlib.redirect_stdout(io.StringIO()):module.main()
        output=self.root/'reference/indexes/sources/source-manifest.json'
        self.assertEqual(json.loads(output.read_text())['episodes'][0]['path'],source.relative_to(self.root).as_posix())
        self.assertFalse((self.root/'reference/indexes/source-manifest.json').exists())
        self.assertEqual(source.read_bytes(),b'synthetic source; never decoded')

    def test_metadata_routes_to_selected_episode_preparation(self):
        module=self.load('inspect_episode');source=self.source()
        def run(command,**kwargs):
            output='fake ffprobe version' if '-version' in command else json.dumps({'format':{'filename':str(source)},'streams':[]})
            return subprocess.CompletedProcess(command,0,stdout=output)
        with patch.object(module.shutil,'which',return_value='fake-ffprobe'),patch.object(module.subprocess,'run',side_effect=run),patch.object(sys,'argv',['inspect_episode.py','7']),contextlib.redirect_stdout(io.StringIO()):
            module.main()
        output=self.root/'reference/indexes/episodes/EP-07/preparation/episode-07-metadata.json'
        self.assertEqual(json.loads(output.read_text())['source'],source.relative_to(self.root).as_posix())
        self.assertFalse((self.root/'reference/indexes/episode-07-metadata.json').exists())

    def frame_runner(self,command,**kwargs):
        if '-show_format' in command:
            output=json.dumps({'format':{'duration':'120'},'streams':[{'index':0,'codec_type':'video','width':1,'height':1}]})
            return subprocess.CompletedProcess(command,0,stdout=output)
        if '-version' in command:return subprocess.CompletedProcess(command,0,stdout='fake ffmpeg version')
        path=Path(command[-1]);self.assertTrue(path.is_relative_to(self.root))
        path.write_bytes(b'synthetic frame')
        return subprocess.CompletedProcess(command,0,stderr='config in time_base: 1/1000\nn: 0 pts: 1000 pts_time:1.000\n')

    def test_frame_manifest_routes_and_refuses_existing_batch(self):
        module=self.load('extract_reference_frames');source=self.source()
        with patch.object(module.shutil,'which',return_value='fake-media'),patch.object(module.subprocess,'run',side_effect=self.frame_runner),patch.object(sys,'argv',['extract_reference_frames.py','7','--batch','routing-proof','--time','1']),contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
            module.main()
            output=self.root/'reference/indexes/episodes/EP-07/evidence/episode-07-routing-proof-frames.json'
            record=json.loads(output.read_text())['records'][0]
            self.assertEqual(record['decoded_pts'],1000)
            self.assertEqual(record['image'],'reference/extracted-frames/episode07/routing-proof/frame-01.png')
            self.assertFalse((self.root/'reference/indexes/episode-07-routing-proof-frames.json').exists())
            before=output.read_bytes()
            with self.assertRaises(SystemExit):module.main()
            self.assertEqual(output.read_bytes(),before)
        self.assertEqual(source.read_bytes(),b'synthetic source; never decoded')

    def test_subtitle_coverage_routes_without_moving_subtitle_outputs(self):
        module=self.load('scan_performance_subtitles')
        for episode in range(1,27):self.source(episode)
        def run(command,**kwargs):
            if '-version' in command:return subprocess.CompletedProcess(command,0,stdout='fake ffmpeg version')
            if '-show_streams' in command:
                output=json.dumps({'streams':[{'index':4,'codec_type':'subtitle','codec_name':'ass','tags':{'language':'eng','title':'English Subtitles'}}]})
                return subprocess.CompletedProcess(command,0,stdout=output)
            out=Path(command[-1]);self.assertTrue(out.is_relative_to(self.root))
            out.write_text('Dialogue: 0,0:00:01.00,0:00:02.00,Default,,0,0,0,,10 km\n',encoding='utf-8')
            return subprocess.CompletedProcess(command,0)
        with patch.object(module.shutil,'which',return_value='fake-media'),patch.object(module.subprocess,'run',side_effect=run),contextlib.redirect_stdout(io.StringIO()):
            module.main()
            output=self.root/'reference/indexes/performance/performance-subtitle-coverage.json'
            records=json.loads(output.read_text())['episodes']
            self.assertEqual(len(records),26)
            self.assertEqual(records[0]['local_subtitle'],'reference/working/performance-subtitles/episode-01.ass')
            self.assertFalse((self.root/'reference/indexes/performance-subtitle-coverage.json').exists())
            with self.assertRaises(FileExistsError):module.main()

if __name__=='__main__':unittest.main()
