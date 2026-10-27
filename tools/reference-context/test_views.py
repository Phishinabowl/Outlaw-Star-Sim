"""Combined projections keep source, review and image availability states separate."""
import copy
import csv
from pathlib import Path
import unittest
from unittest.mock import patch

import core
import views
import test_context
from test_context import sample, receipt, tempdir


class ProjectionTests(unittest.TestCase):
    def fixture(self, directory):
        fixture = test_context.TableTests()
        fixture.setUp()
        tables = fixture.tables
        index = Path(directory) / 'index'
        index.mkdir()
        for name, fields in core.FIELDS.items():
            with (index / (name + '.csv')).open('w', encoding='utf-8', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                writer.writerows(tables[name])
        store = core.Store(Path(directory) / 'cache')
        store.put(sample(), b'payload', receipt())
        return index, store, tables

    def test_joined_view_preserves_draft_and_inputs(self):
        with tempdir() as directory:
            index, store, _ = self.fixture(directory)
            before = {p.name: p.read_bytes() for p in index.glob('*.csv')}
            with patch.object(views, 'caches', return_value=store), patch.object(views, 'image_inventory', return_value=({}, {'EP-04'})):
                result = views.build_view(index)
            row = result['sheets']['Context'][0]
            self.assertEqual(row['about_subjects'], 'Horus')
            self.assertEqual(row['review_status'], 'DRAFT')
            self.assertEqual(row['evidence_status'], 'SECONDARY_ONLY')
            self.assertEqual(result['metrics']['Draft'], 1)
            self.assertEqual(result['metrics']['Source checked'], 0)
            self.assertIsInstance(row['linked_images'], int)
            self.assertEqual(before, {p.name: p.read_bytes() for p in index.glob('*.csv')})

    def test_missing_snapshot_stops_projection(self):
        with tempdir() as directory:
            index, _, _ = self.fixture(directory)
            with patch.object(views, 'caches', return_value=core.Store(Path(directory) / 'empty')), patch.object(views, 'image_inventory', return_value=({}, set())):
                with self.assertRaisesRegex(ValueError, 'pinned snapshot'):
                    views.build_view(index)

    def test_bridges_do_not_multiply_facts(self):
        tables = {'links': []}
        kinds = ['SUBJECT', 'EPISODE', 'IMAGE', 'CONTEXT', 'EVIDENCE']
        for kind in kinds:
            tables['links'].append(dict(context_id='CTX-000001', relation='example', target_type=kind, target_id=kind, notes='scoped'))
        before = copy.deepcopy(tables)
        bridges = views.bridge_tables(tables)
        self.assertEqual([len(rows) for rows in bridges.values()], [1] * 5)
        self.assertEqual(sum(map(len, bridges.values())), len(tables['links']))
        self.assertEqual(tables, before)

    def test_source_metadata_is_not_editorial_review(self):
        capture = sample()
        before = copy.deepcopy(capture)
        row = core.source_row(capture, 'CTXSRC-000001')
        self.assertEqual(set(row), set(core.FIELDS['sources']))
        self.assertEqual(row['content_sha256'], capture['content_sha256'])
        self.assertNotIn('review_status', row)
        self.assertIn('separate review', row['notes'])
        self.assertEqual(capture, before)
        with self.assertRaises(ValueError):
            core.source_row(capture, '../bad')

    def test_manual_availability_and_hash_failure_are_explicit(self):
        with tempdir() as directory:
            root = Path(directory)
            base = root / 'reference/indexes/animehistory'
            base.mkdir(parents=True)
            (base / 'all-episodes.csv').write_text('episode_id,image_id,image_url,web_timestamp\nEP-04,001,https://example.invalid/1,00:01\n', encoding='utf-8')
            (base / 'supplemental-index.csv').write_text('episode_id,image_id,media_path,media_sha256\nEP-04,MAN001,manual.png,' + core.sha(b'image') + '\n', encoding='utf-8')
            with patch.object(views, 'ROOT', root):
                images, episodes = views.image_inventory()
                self.assertEqual(images['EP-04:MAN001']['availability'], 'NOT_LOCAL')
                self.assertEqual(episodes, {'EP-04'})
                (root / 'manual.png').write_bytes(b'image')
                self.assertEqual(views.image_inventory()[0]['EP-04:MAN001']['availability'], 'LOCAL_VERIFIED')
                (root / 'manual.png').write_bytes(b'changed')
                with self.assertRaisesRegex(ValueError, 'registered hash'):
                    views.image_inventory()


if __name__ == '__main__':
    unittest.main()
