"""Offline recovery/safety tests using disposable images, locators and real RAR CLI."""
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

from episode_gallery import (Gallery, ROOT, archive, checked_path, episode_lock,
                             member_name, prune, rar_path, restore)
import episode_gallery
import category_index


class FakeDownload:
    def __init__(self, fail_at=None):
        self.calls = []
        self.fail_at = fail_at

    def image(self, url):
        self.calls.append(url)
        if len(self.calls) == self.fail_at:
            raise OSError('Simulated interrupted request')
        buffer = io.BytesIO()
        Image.new('RGB', (80, 60), (len(self.calls)*20, 70, 150)).save(buffer, format='JPEG')
        return buffer.getvalue(), url


class GalleryTests(unittest.TestCase):
    def test_authored_review_counts_are_separate_from_cache(self):
        index = self.root / 'reference/indexes/animehistory'
        fields = list(self.gallery.rows[0])
        with (index / 'all-episodes.csv').open('w', newline='', encoding='utf-8') as output:
            writer = csv.DictWriter(output, fieldnames=fields)
            writer.writeheader(); writer.writerows(self.gallery.rows)
        target = index / 'category-index.csv'
        rows = category_index.initialize(target, self.gallery.rows)
        rows[0].update(screening_status='NEEDS_RECHECK', uncertainties='Identity uncertain.',
                       detail_status='INITIAL_REVIEW_COMPLETE',
                       visual_summary='Candidate ship.', screened_by='Test', screened_utc='2026-10-26T17:00:00Z')
        with target.open('w', newline='', encoding='utf-8') as output:
            writer = csv.DictWriter(output, fieldnames=category_index.FIELDS)
            writer.writeheader(); writer.writerows(rows)
        before = target.read_bytes()
        status = self.gallery.status()
        self.assertEqual((status['cached'], status['category_screened'], status['category_needs_recheck'],
                          status['category_unreviewed'], status['detail_reviewed']), (0, 0, 1, 5, 0))
        self.assertEqual(target.read_bytes(), before)
        self.assertEqual(status['initial_review_complete'], 1)

    def setUp(self):
        parent = ROOT / '.tmp/episode-gallery-tests'
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=parent)
        self.root = Path(self.temp.name)
        folder = self.root / 'reference/indexes/animehistory/CSVs'
        folder.mkdir(parents=True)
        fields = ['episode_id', 'image_id', 'image_url', 'web_timestamp', 'web_seconds']
        with (folder / 'episode-04.csv').open('w', newline='', encoding='utf-8') as output:
            writer = csv.DictWriter(output, fieldnames=fields)
            writer.writeheader()
            for n in range(6):
                writer.writerow(dict(episode_id='EP-04', image_id=str(100+n),
                                     image_url=f'https://animehistory.org/uploads/screencaps/test/{n}.jpg',
                                     web_timestamp=f'00:01:{n:02}', web_seconds=60+n))
        self.gallery = Gallery(4, self.root)

    def tearDown(self):
        self.temp.cleanup()

    def test_resume_and_deterministic_sheets(self):
        download = FakeDownload(fail_at=3)
        with self.assertRaises(OSError):
            self.gallery.prepare(downloader=download)
        self.assertEqual(self.gallery.status()['cached'], 2)
        self.assertEqual(self.gallery.status()['failed'], 1)
        old_hash = self.gallery.load()['images']['100']['sha256']
        resumed = FakeDownload()
        self.gallery.prepare(downloader=resumed)
        self.assertEqual(len(resumed.calls), 4)
        self.assertEqual(self.gallery.load()['images']['100']['sha256'], old_hash)
        first = self.gallery.sheet_registry()
        self.gallery.prepare(offline=True)
        self.assertEqual(first, self.gallery.sheet_registry())
        self.assertIsNone(self.gallery.status()['category_screened'])

    def test_interrupted_rename_recovery(self):
        self.gallery.prepare(limit=1, downloader=FakeDownload())
        target = self.gallery.folder / 'images/100.jpg'
        target.replace(target.with_suffix('.jpg.part'))
        self.gallery.prepare(limit=1, offline=True)
        self.assertTrue(target.exists())
        self.assertFalse(target.with_suffix('.jpg.part').exists())

    def test_corruption_preserves_other_data(self):
        self.gallery.prepare(limit=2, downloader=FakeDownload())
        untouched = (self.gallery.folder / 'images/101.jpg').read_bytes()
        damaged = self.gallery.folder / 'images/100.jpg'
        damaged.write_bytes(b'not an image')
        with self.assertRaises(OSError):
            self.gallery.prepare(limit=2, offline=True)
        self.assertEqual(damaged.read_bytes(), b'not an image')
        self.assertEqual((self.gallery.folder / 'images/101.jpg').read_bytes(), untouched)

    def test_cleanup_requires_ack_and_rejects_unknown_files(self):
        self.gallery.prepare(limit=2, downloader=FakeDownload())
        with self.assertRaises(ValueError):
            self.gallery.cleanup()
        extra = self.gallery.sheets / 'personal-note.txt'
        extra.write_text('preserve')
        with self.assertRaises(ValueError):
            self.gallery.cleanup(True)
        self.assertTrue(extra.exists())
        extra.unlink()
        self.assertEqual(self.gallery.cleanup(True)['removed_sheets'], 1)
        self.assertTrue(self.gallery.manifest_path.exists())

    def test_member_paths_and_containment(self):
        for path in ('../manifest.json', '/manifest.json', 'C:/manifest.json', 'images/../100.jpg', 'images/100.jpg:stream', 'notes.txt'):
            with self.assertRaises(ValueError):
                member_name(path)
        with self.assertRaises(ValueError):
            checked_path(self.root / '../escape', self.root)
        with self.assertRaises(ValueError):
            checked_path(self.root, self.root)

    def test_symlink_boundary(self):
        outside = self.root / 'outside'
        outside.mkdir()
        link = self.root / 'link'
        try:
            link.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest('Host does not permit creating test symlinks')
        try:
            with self.assertRaises(ValueError):
                checked_path(link / 'file', self.root)
        finally:
            link.unlink()

    def test_real_rar_roundtrip_prune_restore_and_replacement(self):
        try:
            rar_path()
        except ValueError:
            self.skipTest('RAR unavailable')
        self.gallery.prepare(limit=4, downloader=FakeDownload())
        before = self.gallery.sheet_registry()
        with self.assertRaises(ValueError):
            archive(self.gallery)
        result = archive(self.gallery, allow_partial=True)
        self.assertEqual(result['cached'], 4)
        self.assertFalse(result['complete'])
        old_archive = self.gallery.archive_path.read_bytes()
        with self.assertRaises(ValueError):
            archive(self.gallery, allow_partial=True)
        self.assertEqual(old_archive, self.gallery.archive_path.read_bytes())
        archive(self.gallery, allow_partial=True, replace=True)
        with self.assertRaises(ValueError):
            prune(self.gallery)
        self.assertTrue(self.gallery.folder.exists())
        prune(self.gallery, True)
        self.assertFalse(self.gallery.folder.exists())
        self.assertEqual(before, self.gallery.sheet_registry())
        self.assertTrue(self.gallery.archive_path.exists())
        self.assertEqual(self.gallery.status()['archived_images'], 4)
        restore(self.gallery)
        self.gallery.make_sheets(limit=4)
        self.assertEqual(before, self.gallery.sheet_registry())
        with self.assertRaises(ValueError):
            restore(self.gallery)
        self.gallery.archive_path.write_bytes(self.gallery.archive_path.read_bytes() + b'corrupt')
        with self.assertRaises(ValueError):
            prune(self.gallery, True)
        self.assertTrue(self.gallery.folder.exists())

    def test_archive_inventory_conflict(self):
        self.gallery.prepare(limit=1, downloader=FakeDownload())
        (self.gallery.folder / 'extra.txt').write_text('preserve')
        with self.assertRaises(ValueError):
            archive(self.gallery, allow_partial=True)
        self.assertFalse(self.gallery.archive_path.exists())

    def add_supplement(self):
        image = io.BytesIO()
        Image.new('RGB', (32, 24), 'red').save(image, format='PNG')
        data = image.getvalue()
        relative = 'reference/working/manual-supplements/EP-04/EP-04-MAN-001.png'
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        row = {**dict.fromkeys(category_index.SUPPLEMENT_FIELDS, ''), **category_index.DEFAULTS}
        row.update(episode_id='EP-04', image_id='EP-04-MAN-001',
                   media_path=relative, media_sha256=episode_gallery.digest(data), media_bytes=str(len(data)),
                   local_timestamp='01:00', local_seconds='60', timestamp_basis='PLAYER_UI_WHOLE_SECONDS',
                   alignment_status='UNRECONCILED', related_gallery_ids='100', source_description='Fixture screenshot.')
        index = self.root / 'reference/indexes/animehistory/supplemental-index.csv'
        with index.open('w', encoding='utf-8', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=category_index.SUPPLEMENT_FIELDS)
            writer.writeheader(); writer.writerow(row)
        return target, data, index

    def test_supplement_roundtrip_recovery_conflict_and_retained_sheets(self):
        self.gallery.prepare(limit=2, downloader=FakeDownload())
        target, data, index = self.add_supplement()
        source_index = index.read_bytes()
        sheets = self.gallery.sheet_registry()
        receipt = archive(self.gallery, allow_partial=True)
        self.assertEqual(receipt['supplements'], 1)
        gallery_before = self.gallery.manifest_path.read_bytes()
        target.unlink()
        restore(self.gallery, supplements_only=True)
        self.assertEqual(target.read_bytes(), data)
        self.assertEqual(self.gallery.manifest_path.read_bytes(), gallery_before)
        target.write_bytes(b'changed')
        with self.assertRaises((ValueError, OSError)):
            prune(self.gallery, True)
        self.assertTrue(self.gallery.folder.exists())
        target.write_bytes(data)
        prune(self.gallery, True)
        self.assertEqual(self.gallery.sheet_registry(), sheets)
        self.assertEqual(self.gallery.status()['archived_supplements'], 1)
        self.assertFalse(target.exists())  # Prune removes archived supplemental originals too.
        restore(self.gallery)
        self.assertEqual(target.read_bytes(), data)
        self.assertEqual(index.read_bytes(), source_index)
        self.assertEqual(self.gallery.status()['cached'], 2)
        self.gallery.validate_cache(self.gallery.folder, self.gallery.load())
        prune(self.gallery, True)
        self.assertEqual(prune(self.gallery, True)['removed_supplements'], 0)
        target.parent.mkdir(parents=True)
        target.write_bytes(b'personal conflicting content')
        with self.assertRaises(ValueError):
            restore(self.gallery)
        self.assertEqual(target.read_bytes(), b'personal conflicting content')
        self.assertFalse(self.gallery.folder.exists())
        self.assertEqual(index.read_bytes(), source_index)

    def test_unarchived_supplement_blocks_prune_until_refresh(self):
        self.gallery.prepare(limit=1, downloader=FakeDownload())
        archive(self.gallery, allow_partial=True)
        self.add_supplement()
        with self.assertRaises(ValueError):
            prune(self.gallery, True)
        self.assertTrue(self.gallery.folder.exists())
        archive(self.gallery, allow_partial=True, replace=True)
        prune(self.gallery, True)
        self.assertTrue(self.gallery.sheets.exists())
        self.assertFalse(self.gallery.folder.exists())

    def test_supplement_member_and_recovery_path_validation(self):
        snapshot = episode_gallery.empty_supplements(self.gallery)
        good = dict(image_id='EP-04-MAN-001', file='supplements/EP-04-MAN-001.png',
                    media_path='reference/working/manual-supplements/EP-04/EP-04-MAN-001.png',
                    sha256='a'*64, bytes=100)
        snapshot['records'] = [good]
        episode_gallery.validate_supplement_snapshot(self.gallery, snapshot)
        for field, value in [('file', '../outside.png'), ('image_id', 'EP-05-MAN-001'),
                             ('media_path', 'README.md'), ('bytes', -1)]:
            bad = {**snapshot, 'records': [{**good, field: value}]}
            with self.subTest(field=field), self.assertRaises(ValueError):
                episode_gallery.validate_supplement_snapshot(self.gallery, bad)
        with self.assertRaises(ValueError):
            member_name('supplements/../EP-04-MAN-001.png')

    def test_changed_supplement_payload_fails_restored_hash(self):
        self.gallery.prepare(limit=1, downloader=FakeDownload())
        target, original, index = self.add_supplement()
        archive(self.gallery, allow_partial=True)
        prune(self.gallery, True)
        forged = self.root / 'forged'
        member = forged / 'supplements/EP-04-MAN-001.png'
        member.parent.mkdir(parents=True)
        Image.new('RGB', (32, 24), 'blue').save(member, format='PNG')
        episode_gallery.rar(rar_path(), ['a', '-cfg-', '-idq', '-p-', str(self.gallery.archive_path),
                                         'supplements/EP-04-MAN-001.png'], cwd=forged)
        receipt = json.loads(self.gallery.receipt_path.read_text())
        receipt['archive_sha256'] = episode_gallery.digest(self.gallery.archive_path.read_bytes())
        episode_gallery.write_json(self.gallery.receipt_path, receipt)
        with self.assertRaises(ValueError):
            restore(self.gallery)
        self.assertFalse(self.gallery.folder.exists())
        self.assertFalse(target.exists())

    def test_legacy_gallery_only_archive_remains_restorable(self):
        self.gallery.prepare(limit=1, downloader=FakeDownload())
        archive(self.gallery, allow_partial=True)
        legacy = self.gallery.archives / 'legacy.rar'
        episode_gallery.rar(rar_path(), ['a', '-cfg-', '-idq', '-p-', str(legacy), 'manifest.json',
                                         'images/100.jpg'], cwd=self.gallery.folder)
        legacy.replace(self.gallery.archive_path)
        receipt = json.loads(self.gallery.receipt_path.read_text())
        receipt['archive_sha256'] = episode_gallery.digest(self.gallery.archive_path.read_bytes())
        receipt.pop('archive_format'); receipt.pop('supplements')
        episode_gallery.write_json(self.gallery.receipt_path, receipt)
        prune(self.gallery, True)
        restore(self.gallery)
        self.assertEqual(self.gallery.status()['cached'], 1)

    def test_episode_lock_releases_after_exception(self):
        with self.assertRaises(RuntimeError):
            with episode_lock(self.gallery):
                with self.assertRaises(OSError):
                    with episode_lock(self.gallery):
                        self.fail('Concurrent episode lock unexpectedly acquired')
                raise RuntimeError('Simulated command interruption')
        with episode_lock(self.gallery):
            pass

    def test_archive_and_restore_failure_keep_recoverable_data(self):
        self.gallery.prepare(limit=2, downloader=FakeDownload())
        archive(self.gallery, allow_partial=True)
        original_archive = self.gallery.archive_path.read_bytes()
        original_rar = episode_gallery.rar

        def fail_integrity(executable, args, cwd=None):
            if args[0] == 't':
                raise OSError('Simulated archive integrity/process failure')
            return original_rar(executable, args, cwd)

        with patch('episode_gallery.rar', side_effect=fail_integrity):
            with self.assertRaises(OSError):
                archive(self.gallery, allow_partial=True, replace=True)
        self.assertEqual(self.gallery.archive_path.read_bytes(), original_archive)
        self.assertTrue(self.gallery.folder.exists())
        self.assertEqual(list(self.gallery.archives.glob('*.candidate.rar')), [])
        prune(self.gallery, True)

        def fail_image(executable, args, cwd=None):
            if args[0] == 'p' and args[-1].endswith('101.jpg'):
                raise OSError('Simulated interrupted restore')
            return original_rar(executable, args, cwd)

        with patch('episode_gallery.rar', side_effect=fail_image):
            with self.assertRaises(OSError):
                restore(self.gallery)
        self.assertFalse(self.gallery.folder.exists())
        self.assertEqual(self.gallery.archive_path.read_bytes(), original_archive)
        restore(self.gallery)
        self.assertEqual(self.gallery.status()['cached'], 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
