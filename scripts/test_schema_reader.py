"""Targeted offline schema-input regressions. Only fictional metadata is used."""
import json,tempfile,unittest
from pathlib import Path
from read_schema import read_schema

HEADER='column_name,source_column_name,type,visible,key\n'
class SchemaReaderTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.path=Path(self.temp.name)/'schema_999999.csv'
 def read(self,text,**kwargs):
  self.path.write_text(text,encoding='utf-8-sig');return read_schema(self.path,**kwargs)
 def test_bom_quoting_exact_types_flags_and_no_inferred_ids(self):
  r=self.read(HEADER+'"Example, Field",original,"decimalstrict(28,9)",0,1\r\nOther,other,futuretype,1,0\r\n')
  self.assertEqual(r['datasetId'],999999);self.assertFalse(r['importReady'])
  self.assertEqual(r['columns'][0],dict(name='Example, Field',sourceColumnName='original',internalType='decimalstrict(28,9)',visible=False,keyFlag=True,columnId=None))
  self.assertEqual(r['columns'][1]['internalType'],'futuretype')
 def test_explicit_dataset_metadata_does_not_resolve_field_ids(self):
  r=self.read(HEADER+'Example,example,int64,1,0\n',dataset_id=999999,dataset_name='Fictional source')
  self.assertEqual(r['datasetId'],999999);self.assertFalse(r['importReady']);self.assertIsNone(r['columns'][0]['columnId'])
 def test_reject_conflicting_id(self):
  with self.assertRaises(ValueError):self.read(HEADER+'Example,example,int64,1,0\n',dataset_id=123456)
 def test_unrecognized_filename_has_no_id(self):
  self.path=Path(self.temp.name)/'orders.csv'
  self.assertIsNone(self.read(HEADER+'Example,example,int64,1,0\n')['datasetId'])
 def test_reordered_headers(self):
  r=self.read('key,visible,type,source_column_name,column_name\n0,1,int64,original,Example\n');self.assertEqual(r['columns'][0]['name'],'Example')
 def test_reject_invalid_inputs(self):
  cases=[HEADER,HEADER+'Name,n,int64,yes,0\n',HEADER+'Name,n,int64,1,0\nname,n,int64,1,0\n',HEADER+',n,int64,1,0\n',HEADER+'Name,n,int64,1\n',HEADER+'Name,n,int64,1,0,extra\n','Name,Value\nExample,123\n',HEADER+'Name,n,int64,,0\n']
  for text in cases:
   with self.subTest(text=text),self.assertRaises(ValueError):self.read(text)
 def test_does_not_turn_key_flag_into_uniqueness_evidence(self):
  r=self.read(HEADER+'Example,example,int64,1,1\n');self.assertNotIn('primaryKey',r);self.assertIn('key uniqueness',r['evidence'])
if __name__=='__main__':unittest.main()
