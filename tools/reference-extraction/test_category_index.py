"""Annotation identity, progress and validation regression tests; no source changes."""
from copy import deepcopy
import hashlib
import tempfile
from pathlib import Path
import unittest

import category_index as ci


class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.sources = [dict(episode_id='EP-04', image_id=str(n)) for n in range(10, 13)]
        parent = ci.ROOT / '.tmp/category-index-tests'
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=parent)
        self.path = Path(self.temp.name) / 'category.csv'
        self.rows = ci.initialize(self.path, self.sources)

    def tearDown(self):
        self.temp.cleanup()

    def screened(self):
        self.rows[0].update(screening_status='SCREENED', presentation='STORY', subjects='xgp',
                            categories='machinery_controls;ships_vehicles',
                            identification_confidence='HIGH', visual_summary='Ship beside a station.',
                            research_priority='HIGH', revisit_reason='Exterior profile.',
                            screened_by='Test reviewer', screened_utc='2026-10-26T17:00:00Z')

    def test_initialization_and_no_overwrite(self):
        ci.validate(self.rows, self.sources)
        with self.assertRaises(FileExistsError):
            ci.initialize(self.path, self.sources)
        self.assertTrue(all(r['screening_status'] == 'UNREVIEWED' for r in self.rows))

    def test_resume_by_key_and_overlapping_tags(self):
        self.screened()
        before = deepcopy(self.rows)
        result = ci.validate(list(reversed(self.rows)), self.sources)
        self.assertEqual(result['EP-04:10']['categories'], 'machinery_controls;ships_vehicles')
        self.assertEqual(self.rows, before)
        self.assertEqual(result['EP-04:12']['screening_status'], 'UNREVIEWED')

    def test_missing_duplicate_and_bad_values(self):
        self.screened()
        for bad in (self.rows[:-1], [self.rows[0], self.rows[0], self.rows[2]]):
            with self.assertRaises(ValueError):
                ci.validate(bad, self.sources)
        for field, value in [('categories', 'ships_vehicles;ships_vehicles'),
                             ('subjects', 'made_up_ship'), ('screened_utc', '2026-10-26'),
                             ('revisit_reason', ''), ('screening_status', 'UNREVIEWED')]:
            bad = deepcopy(self.rows); bad[0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                ci.validate(bad, self.sources)

    def test_recheck_unavailable_and_detail_remain_distinct(self):
        self.screened()
        self.rows[0].update(screening_status='NEEDS_RECHECK', identification_confidence='LOW',
                            uncertainties='Candidate ship identity uncertain.')
        self.rows[1].update(screening_status='UNAVAILABLE', uncertainties='Image could not decode.',
                            screened_by='Test reviewer', screened_utc='2026-10-26T17:00:00Z')
        ci.validate(self.rows, self.sources)
        bad = deepcopy(self.rows); bad[0]['detail_status'] = 'REVIEWED'
        with self.assertRaises(ValueError):
            ci.validate(bad, self.sources)

    def test_groups_require_contiguity_and_consistent_summary(self):
        for row in self.rows:
            row.update(screening_status='SCREENED', visual_summary='A view.',
                       screened_by='Test reviewer', screened_utc='2026-10-26T17:00:00Z')
        for row in (self.rows[0], self.rows[2]):
            row.update(scene_group_id='EP-04-S001', scene_summary='Continuous sampled views.')
        with self.assertRaises(ValueError):
            ci.validate(self.rows, self.sources)
        self.rows[1].update(scene_group_id='EP-04-S001', scene_summary='Continuous sampled views.')
        ci.validate(self.rows, self.sources)
        self.rows[1]['scene_summary'] = 'Conflicting summary.'
        with self.assertRaises(ValueError):
            ci.validate(self.rows, self.sources)

    def manual_row(self):
        row = {**dict.fromkeys(ci.SUPPLEMENT_FIELDS, ''), **ci.DEFAULTS}
        row.update(episode_id='EP-04', image_id='EP-04-MAN-001',
                   media_path='reference/working/manual-supplements/EP-04/EP-04-MAN-001.png',
                   media_sha256=hashlib.sha256(b'image').hexdigest(), media_bytes='5',
                   local_timestamp='01:56', local_seconds='116',
                   timestamp_basis='PLAYER_UI_WHOLE_SECONDS', alignment_status='UNRECONCILED',
                   related_gallery_ids='10', source_description='Test-supplied player screenshot.')
        return row

    def test_manual_timing_does_not_extend_gallery_coverage(self):
        ci.validate_supplements([self.manual_row()], self.sources)
        ci.validate(self.rows, self.sources)
        self.assertEqual(len(self.rows), 3)
        self.assertEqual(self.manual_row()['local_seconds'], '116')

    def test_manual_bad_times_keys_associations_and_paths(self):
        row = self.manual_row()
        for field, value in [('local_seconds', '117'), ('alignment_status', 'VERIFIED'),
                             ('media_path', '../outside.png'), ('related_gallery_ids', '999'),
                             ('image_id', '10')]:
            bad = dict(row); bad[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                ci.validate_supplements([bad], self.sources)
        with self.assertRaises(ValueError):
            ci.validate_supplements([row, row], self.sources)

    def test_manual_media_integrity_check(self):
        from unittest.mock import patch
        row = self.manual_row()
        with patch.object(Path, 'read_bytes', return_value=b'image'):
            ci.validate_supplements([row], self.sources, verify_media=True)
        with patch.object(Path, 'read_bytes', return_value=b'changed'), self.assertRaises(ValueError):
            ci.validate_supplements([row], self.sources, verify_media=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
