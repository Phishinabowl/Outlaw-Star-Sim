from copy import deepcopy
from fractions import Fraction as F
import unittest
import models as m
import alignment as a
from pathlib import Path
import tempfile
from unittest.mock import patch


class ModelTests(unittest.TestCase):
    def pts(self,web,scale=F(1),offset=F(-2),width=F(0)):
        return [(F(x),scale*F(x)+offset-width/2,scale*F(x)+offset+width/2) for x in web]

    def test_offset_sign_and_independent_holdouts(self):
        fit=self.pts([100,300,500]);test=self.pts([200,400])
        result=m.evaluate(fit,test,'OFFSET')
        self.assertEqual(result['offset'],-2);self.assertEqual(result['reasons'],[])
        self.assertEqual(result['metrics'],[0,0,0,0])

    def test_even_median_and_exact_residual_edges(self):
        self.assertEqual(m.fit([(1,0,0),(2,2,2)],'OFFSET'),(1,F(-1,2)))
        fit=self.pts([100,300,500]);test=[(200,F(397,2),F(397,2)),(400,F(795,2),F(795,2))]
        self.assertEqual(m.evaluate(fit,test,'OFFSET')['reasons'],[])
        test[0]=(200,F(397,2)+F(1,100000),F(397,2)+F(1,100000))
        self.assertIn('residual limits failed',m.evaluate(fit,test,'OFFSET')['reasons'])

    def test_holdouts_never_change_coefficients(self):
        fit=self.pts([100,300,500]);bad=self.pts([200,400],offset=F(20))
        result=m.evaluate(fit,bad,'OFFSET')
        self.assertEqual(result['offset'],-2)
        self.assertTrue(result['reasons'])

    def test_linear_drift_recovers_without_tuning_holdouts(self):
        fit=self.pts([100,300,500,700,900],F(101,100));test=self.pts([200,600,800],F(101,100))
        self.assertTrue(m.evaluate(fit,test,'OFFSET')['reasons'])
        result=m.evaluate(fit,test,'LINEAR')
        self.assertEqual((result['scale'],result['offset']),(F(101,100),-2))
        self.assertEqual(result['reasons'],[])

    def test_linear_refuses_short_span_and_bad_scale(self):
        result=m.evaluate(self.pts([0,10,20,30,40],F(11,10)),self.pts([5,15,25],F(11,10)),'LINEAR')
        self.assertIn('linear span below 300 s',result['reasons'])
        self.assertIn('linear scale outside supported range',result['reasons'])

    def test_unnecessary_linear_and_small_improvement_refused(self):
        result=m.evaluate(self.pts([100,300,500,700,900]),self.pts([200,600,800]),'LINEAR')
        self.assertIn('OFFSET already passes',result['reasons'])
        self.assertIn('linear holdout improvement below 0.25 s',result['reasons'])

    def test_step_change_cannot_be_hidden_by_global_model(self):
        fit=self.pts([100,200,300])+self.pts([500,600,700],offset=F(8))
        test=self.pts([150,250])+self.pts([550,650],offset=F(8))
        self.assertTrue(m.evaluate(fit,test,'OFFSET')['reasons'])
        self.assertTrue(m.evaluate(fit,test,'LINEAR')['reasons'])
        self.assertFalse(m.evaluate(fit[:3],test[:2],'OFFSET')['reasons'])
        self.assertFalse(m.evaluate(fit[3:],test[2:],'OFFSET')['reasons'])

    def test_insufficient_counts_and_wide_intervals_refused(self):
        self.assertTrue(m.evaluate(self.pts([100,300]),self.pts([200]),'OFFSET')['reasons'])
        fit=self.pts([100,300,500],width=F(501,1000))
        self.assertIn('anchor width exceeds 0.5 s',m.evaluate(fit,self.pts([200,400]),'OFFSET')['reasons'])

    def test_duplicate_fit_labels_and_noncanonical_rational_refused(self):
        with self.assertRaises(ValueError):m.fit(self.pts([100,100]),'OFFSET')
        for text in ['1.0','2/2','-0/1']:
            with self.assertRaises(ValueError):m.rational(text)

    def registry(self):
        identity=dict(episode_id='EP-01',video_source='_source_episodes/fixture.mkv',video_sha256='a'*64,video_stream_index=0,video_time_base='1/1000',media_origin_seconds='0/1',subtitle_stream_index=1,subtitle_sha256='b'*64,subtitle_time_basis='MEDIA_RELATIVE',subtitle_shift_seconds='0/1',locator_sha256='c'*64)
        anchors=[];locator={}
        for n,web in enumerate([100,300,500,200,400],1):
            row=dict.fromkeys(m.ANCHORS,'');row.update({k:str(v) for k,v in identity.items()})
            image=str(n);locator[('EP-01',image)]=dict(web_seconds=str(web))
            row.update(anchor_id=f'ALNANC-{n:06}',image_id=image,input_id=a.input_id(identity),image_sha256='d'*64,run_id='ALNRUN-'+'e'*32,role='FIT' if n<=3 else 'HOLDOUT',method='BOUNDED_FRAME_SEARCH_V1',recipe_json=a.canonical(dict(implementation_sha256='f'*64,commands=[['ffmpeg']],reviewed_frame_hashes={str((web-2)*1000):'a'*64},web_seconds=web)).decode(),search_start_seconds=a.ratio(web-6),search_end_seconds=a.ratio(web+6),match_kind='CORRESPONDING_FRAME',status='MATCHED',local_start_pts=str((web-2)*1000),local_end_pts=str((web-2)*1000),reviewer='Fixture',reviewed_utc='2026-10-27T00:00:00Z',notes='Synthetic reviewed fixture')
            anchors.append(row)
        mapping=dict.fromkeys(m.MAPPINGS,'')
        mapping.update(mapping_id='ALNMAP-000001',episode_id='EP-01',input_id=anchors[0]['input_id'],segment_label='fixture',web_start_seconds='100',web_end_seconds='501',model='OFFSET',scale='1/1',offset_seconds='-2/1',fit_anchor_ids=';'.join(r['anchor_id'] for r in anchors[:3]),holdout_anchor_ids=';'.join(r['anchor_id'] for r in anchors[3:]),status='VALIDATED',max_fit_interval_error_seconds='0/1',median_holdout_interval_error_seconds='0/1',max_holdout_interval_error_seconds='0/1',max_anchor_width_seconds='0/1',estimated_half_window_seconds='2/1',method_version='ALIGNMENT_MODEL_V1',reviewer='Fixture',reviewed_utc='2026-10-27T00:00:00Z',limitations='Synthetic fixture only')
        return anchors,[mapping],locator

    def test_registry_valid_and_csv_roundtrip(self):
        import csv,io
        anchors,maps,loc=self.registry()
        self.assertEqual(m.validate(anchors,maps,loc)['validated'],1)
        self.assertEqual(list(csv.DictReader(io.StringIO(m.csv_bytes(anchors,m.ANCHORS).decode()))),anchors)

    def test_identity_roles_votes_states_and_metrics_refused(self):
        def role(x,y):x[3]['role']='FIT'
        def identity(x,y):x[0]['video_sha256']='e'*64
        def duplicate(x,y):y[0]['fit_anchor_ids']+=';ALNANC-000001'
        def stale(x,y):x[0]['status']='CANDIDATE';x[0]['local_start_pts']='';x[0]['local_end_pts']=''
        def precision(x,y):y[0]['max_fit_interval_error_seconds']='1/1000'
        def coefficient(x,y):y[0]['offset_seconds']='-1999/1000'
        for mutate in [role,identity,duplicate,stale,precision,coefficient]:
            x,y,loc=self.registry();mutate(x,y)
            with self.assertRaises(ValueError):m.validate(x,y,loc)

    def test_mapping_half_open_domain_and_overlap_refused(self):
        x,y,loc=self.registry();y[0]['web_end_seconds']='502'
        with self.assertRaisesRegex(ValueError,'extrapolation'):m.validate(x,y,loc)
        x,y,loc=self.registry();other=dict(y[0]);other['mapping_id']='ALNMAP-000002';y.append(other)
        with self.assertRaisesRegex(ValueError,'Conflicting'):m.validate(x,y,loc)

    def test_supersession_cycle_and_duplicate_active_anchor_refused(self):
        x,y,loc=self.registry();x[0]['supersedes_anchor_id']=x[0]['anchor_id']
        with self.assertRaises(ValueError):m.validate(x,y,loc)
        x,y,loc=self.registry();other=dict(x[0]);other['anchor_id']='ALNANC-000006';x.append(other)
        with self.assertRaisesRegex(ValueError,'Competing'):m.validate(x,y,loc)
        x,y,loc=self.registry();y[0]['supersedes_mapping_ids']=y[0]['mapping_id']
        with self.assertRaises(ValueError):m.validate(x,y,loc)

    def test_wide_anchor_and_inadequate_counts_cannot_validate(self):
        x,y,loc=self.registry();x[0]['local_end_pts']=str(int(x[0]['local_start_pts'])+501)
        with self.assertRaises(ValueError):m.validate(x,y,loc)

    def test_stale_source_refused_before_any_registry_write(self):
        x,y,loc=self.registry()
        base=a.ROOT/'reference/working/alignment/tests';base.mkdir(exist_ok=True,parents=True)
        with tempfile.TemporaryDirectory(dir=base) as temp:
            root=Path(temp);marker=root/'reference/indexes/animehistory/alignment-mappings.csv';marker.parent.mkdir(parents=True);marker.write_bytes(b'preserve original bytes')
            before=marker.read_bytes()
            with patch.object(m,'load',return_value=(x,y)),patch.object(m,'locators',return_value=loc),patch.object(a,'inspect_inputs',return_value=(None,None,{'changed':'source'},None,None,None)):
                with self.assertRaisesRegex(ValueError,'Current source differs'):
                    m.propose(root,[r['anchor_id'] for r in x[:3]],[],'OFFSET','fixture','limits','unused')
            self.assertEqual(marker.read_bytes(),before)

    def test_changed_gallery_with_same_video_identity_is_refused(self):
        x,y,loc=self.registry();identity={k:x[0][k] for k in m.IDENTITY}
        for field in ['video_stream_index','subtitle_stream_index']:identity[field]=int(identity[field])
        images=[dict(image_id=r['image_id'],image_sha256='e'*64) for r in x[:3]]
        base=a.ROOT/'reference/working/alignment/tests'
        with tempfile.TemporaryDirectory(dir=base) as temp:
            with patch.object(m,'load',return_value=(x,y)),patch.object(m,'locators',return_value=loc),patch.object(a,'inspect_inputs',return_value=(None,images,identity,None,None,None)):
                with self.assertRaisesRegex(ValueError,'Current gallery bytes differ'):
                    m.propose(Path(temp),[r['anchor_id'] for r in x[:3]],[],'OFFSET','fixture','limits','unused')
        x,y,loc=self.registry();y[0]['holdout_anchor_ids']='ALNANC-000004'
        with self.assertRaises(ValueError):m.validate(x,y,loc)


if __name__=='__main__':unittest.main()
