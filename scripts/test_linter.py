"""Regression tests for common model mistakes. No malformed examples are persisted."""
import copy,json
from pathlib import Path
from lint_flow import lint
R=Path(__file__).resolve().parents[1]
def read(slug):return json.loads((R/f'examples/canonical/{slug}/flow.clipboard.json').read_text())
tests=[]
def rejects(label,v):
 report=lint(v,True);assert report['errors'],label;tests.append(label)
rejects('Reject wrapper instead of raw array',{'nodes':[]})
v=read('01-select-and-type');v[1]['Id']=v[0]['Id'];rejects('Reject duplicate object IDs',v)
v=read('01-select-and-type');next(n for n in v if n['Code']=='column-selector')['Properties']['Sources'][0]['Id']='00000000-0000-0000-0000-000000000000';rejects('Reject unresolved graph reference',v)
v=read('01-select-and-type');next(n for n in v if n['Code']=='table-input')['Properties']['CheckpointType']='preview';rejects('Reject checkpoints',v)
v=read('06-safe-calculations');next(n for n in v if n['Code']=='calculated-columns')['Properties']['CalculatedColumns'][0]['Expression']='[RawQuantity] COLLATE Example';rejects('Reject explicit COLLATE',v)
v=read('06-safe-calculations');next(n for n in v if n['Code']=='calculated-columns')['Properties']['CalculatedColumns'][0]['Name']='rawquantity';rejects('Reject case-insensitive incoming alias collision',v)
v=read('05-distinct-key-helper');next(n for n in v if n['Code']=='group-rows')['Properties']['GroupedValues']=[];rejects('Reject empty GroupedValues',v)
v=read('03-combine-native-null');n=next(n for n in v if n['Code']=='combine-tables');next(c for c in n['Properties']['Columns'] if c['Actions'])['Actions']=[];rejects('Reject absent Combine resolution',v)
v=read('01-select-and-type');next(n for n in v if n['Code']=='table-output')['Properties']['Enabled']=True;rejects('Reject enabled teaching output',v)
# Minimal connected Transform Data fixture; no account resources or records.
def transform_fixture():
 source={'Code':'table-input','Id':'11111111-1111-4111-8111-111111111111','Name':'Input','Properties':{'__type':'DataFlowNodeTableInputProperties:#Infinis.DataFlows','DataCloneRecId':1,'SelectedColumns':[{'Name':'Label','InternalType':'textsimple(250)','RecId':2}], 'Sources':[], 'OutputColumns':[{'Name':'Label','InternalType':'textsimple(250)'}]}}
 transform={'Code':'transform-data','Id':'22222222-2222-4222-8222-222222222222','Name':'Transform','Properties':{'__type':'DataFlowNodeTransformDataProperties:#Infinis.DataFlows','Sources':[{'Id':source['Id'],'SourceSide':'right','TargetSide':'left'}],'OutputColumns':[{'Name':'Label','InternalType':'textsimple(250)'}],'TransformedColumns':[{'Name':'Label','InternalType':'textsimple(250)','Expression':"COALESCE([Label], 'NULL')"}]}}
 return [source,transform]
v=transform_fixture();assert not lint(v)['errors'],lint(v)
v=transform_fixture();v[1]['Properties']['Sources']=[];r=lint(v);assert not r['errors'] and any('standalone Transform Data' in w for w in r['warnings']),r
for label,change in [
 ('Reject empty transformations',lambda p:p.update(TransformedColumns=[])),
 ('Reject malformed transformation',lambda p:p.update(TransformedColumns=[None])),
 ('Reject incomplete transformation',lambda p:p['TransformedColumns'][0].pop('Expression')),
 ('Reject unknown transform expression field',lambda p:p['TransformedColumns'][0].update(Expression='[Missing]')),
 ('Reject transform missing output field',lambda p:p.update(OutputColumns=[])),
 ('Reject transform output type mismatch',lambda p:p['TransformedColumns'][0].update(InternalType='int64')),
 ('Reject transform missing upstream field',lambda p:p['TransformedColumns'][0].update(Name='Missing')),
 ('Reject duplicate transform fields ignoring case',lambda p:p['TransformedColumns'].append(dict(p['TransformedColumns'][0],Name='label'))),
 ('Reject transform COLLATE',lambda p:p['TransformedColumns'][0].update(Expression='[Label] COLLATE Example')),
 ('Reject multiple transform sources',lambda p:p['Sources'].append(dict(p['Sources'][0]))),
 ('Reject dropped passthrough field',lambda p:None),
]:
 v=transform_fixture()
 if label=='Reject dropped passthrough field':v[0]['Properties']['OutputColumns'].append({'Name':'Keep','InternalType':'int64'})
 change(v[1]['Properties']);rejects(label,v)
# A deliberate type conversion is valid; brackets in literals are not field references.
v=transform_fixture();p=v[1]['Properties'];p['TransformedColumns'][0].update(InternalType='int64',Expression="CASE WHEN [Label] = '[Missing]' THEN 0 ELSE 1 END");p['OutputColumns'][0]['InternalType']='int64';assert not lint(v)['errors'],lint(v)

report=dict(result='PASS',negativeCases=len(tests),tests=tests,evidence='Static tests only; not engine execution')
(R/'reference/linter-regression-results.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS:',len(tests),'invalid patterns rejected')
