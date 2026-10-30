"""Last updated: 2026-10-29. Synthetic regressions; not editor execution."""
import copy,json,uuid
from pathlib import Path
from lint_flow import lint
R=Path(__file__).resolve().parents[1]

def run():
    example=json.loads((R/'reference/nodes/group-rows.json').read_text())['sumExample']
    source_id,group_id=str(uuid.uuid4()),str(uuid.uuid4())
    flow=[{'Code':'table-input','Id':source_id,'Name':'Synthetic input','Properties':{
        '__type':'DataFlowNodeTableInputProperties:#Infinis.DataFlows','CheckpointType':None,
        'DataCloneRecId':900001,'SelectedColumns':[],
        'OutputColumns':[{'Name':'SyntheticCategory','InternalType':'textsimple(250)'},{'Name':'SyntheticValue','InternalType':'int64'}],'Sources':[]}},
        {'Code':'group-rows','Id':group_id,'Name':'Sum test','Properties':{
        '__type':'DataFlowNodeGroupRowsProperties:#Infinis.DataFlows','CheckpointType':None,
        **copy.deepcopy(example['settings']),'OutputColumns':copy.deepcopy(example['outputSchema']),
        'Sources':[{'Id':source_id,'SourceSide':'right','TargetSide':'left'}]}}]
    report=lint(flow);assert not report['errors'],report
    cases=[]
    for wrong in ['AggregateColumns','AggregatedColumns']:
        v=copy.deepcopy(flow);p=v[1]['Properties'];p[wrong]=p.pop('GroupedValues');cases.append((wrong,v))
    v=copy.deepcopy(flow);a=v[1]['Properties']['GroupedValues'][0];a['AggregationType']=a.pop('Aggregation');cases.append(('AggregationType substitution',v))
    v=copy.deepcopy(flow);v[1]['Properties']['GroupedValues'][0]['Alias']='Unmapped alias';cases.append(('output alias mismatch',v))
    v=copy.deepcopy(flow);v[1]['Properties']['Sources'][0]['SourceSide']='Right';cases.append(('uppercase port',v))
    v=copy.deepcopy(flow);v[1]['Properties']['Sources']=[{'NodeId':source_id,'Code':'table-input'}];cases.append(('NodeId edge substitution',v))
    v=copy.deepcopy(flow);v[1]['Properties']['GroupedValues'][0]['Aggregation']='string_agg';cases.append(('missing string_agg Separator',v))
    for label,v in cases:
        report=lint(v);assert report['errors'],label
    print('PASS: observed sum shape accepted without Sequence; '+str(len(cases))+' invalid mutations rejected. Static checks only.')

if __name__=='__main__':run()
