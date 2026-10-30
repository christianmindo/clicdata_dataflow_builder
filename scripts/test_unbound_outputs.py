"""User-confirmed manual Table Output binding; no engine execution."""
import copy
import json
from pathlib import Path
from lint_flow import lint

base=json.loads((Path(__file__).resolve().parents[1]/'examples/canonical/01-select-and-type/flow.clipboard.json').read_text())
v=copy.deepcopy(base)
out=next(n for n in v if n['Code']=='table-output')
out['Properties'].pop('DataCloneRecId',None)
out['Properties']['Enabled']=True
r=lint(v)
assert not r['errors'],r
assert any('unbound dummy output' in s for s in r['warnings']),r
assert lint(v,True)['errors'],'Teaching fixture enabled-output rule must remain strict'
for invalid in ['fake-destination',True]:
    out['Properties']['DataCloneRecId']=invalid
    assert lint(v)['errors'],invalid
source=next(n for n in v if n['Code']=='table-input')
source['Properties'].pop('DataCloneRecId')
out['Properties'].pop('DataCloneRecId')
assert lint(v)['errors'],'Source IDs remain mandatory'
assert not lint(base,True)['errors'],'Existing bound teaching output must still pass'
print('PASS: unbound outputs accepted with binding notice; invalid IDs and enabled teaching outputs rejected; source bindings remain required')
