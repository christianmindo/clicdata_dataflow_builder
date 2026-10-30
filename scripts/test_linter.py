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
report=dict(result='PASS',negativeCases=len(tests),tests=tests,evidence='Static tests only; not engine execution')
(R/'reference/linter-regression-results.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS:',len(tests),'invalid patterns rejected')
