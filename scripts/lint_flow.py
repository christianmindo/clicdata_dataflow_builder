"""Static checks for clipboard JSON. Does not prove ClicData execution.
Usage: python3 scripts/lint_flow.py path/to/flow.json [--require-disabled-outputs]
"""
import argparse,json,re,uuid
from pathlib import Path
R=Path(__file__).resolve().parents[1]

def lint(flow,disabled=False):
 errors=[];warnings=[]
 def require(ok,msg):
  if not ok:errors.append(msg)
 if not isinstance(flow,list):return dict(result='FAIL',errors=['Clipboard root must be a raw JSON array'],warnings=[])
 ids={};processing=[];classes={x['code']:x['propertyClass'] for x in json.loads((R/'reference/node-catalog.json').read_text())}
 for index,n in enumerate(flow):
  if not isinstance(n,dict):errors.append('Object '+str(index)+' must be an object');continue
  id=n.get('Id');name=n.get('Name',n.get('Code',str(index)))
  try:uuid.UUID(id)
  except (ValueError,TypeError,AttributeError):errors.append(str(name)+': invalid object UUID')
  require(id not in ids,str(name)+': duplicate object ID');ids[id]=n
  p=n.get('Properties',{})
  if n.get('Code') in ['label','background-panel']:
   for k in ['Left','Top','Width','Height','Text','Background','Border','Font','Shadow']:require(k in p,str(name)+': missing annotation '+k)
   continue
  processing.append(n)
  require(p.get('CheckpointType') is None,str(name)+': checkpoints are prohibited')
  require('CheckpointStatus' not in p and 'CheckpointIsOutdated' not in p,str(name)+': checkpoint status metadata is prohibited')
  if n.get('Code') in classes:require(p.get('__type')==classes[n['Code']],str(name)+': property class does not match Code')
  else:warnings.append(str(name)+': undocumented node Code; settings need evidence')
  for k in ['Name','Code','Id','Properties']:require(k in n,str(name)+': missing '+k)
  names=[c.get('Name','') for c in p.get('OutputColumns',[])];require(len(names)==len({s.casefold() for s in names}),str(name)+': duplicate output names ignoring case')
  for c in p.get('OutputColumns',[]):require(bool(c.get('InternalType')),str(name)+': output type missing')
 # Graph cycle detection must not assume array order or Sequence controls evaluation.
 graph={n['Id']:[e.get('Id') for e in n['Properties'].get('Sources',[])] for n in processing}
 state={}
 def visit(id):
  if state.get(id)==1:errors.append('Graph has a cycle at '+str(id));return
  if state.get(id)==2:return
  state[id]=1
  for up in graph.get(id,[]):
   require(up in graph,str(id)+': unresolved upstream graph reference '+str(up))
   if up in graph:visit(up)
  state[id]=2
 for id in graph:visit(id)
 def fields(n):return {c['Name']:c['InternalType'] for c in n.get('Properties',{}).get('OutputColumns',[])}
 for n in processing:
  p=n['Properties'];name=n['Name'];code=n['Code'];edges=p.get('Sources',[]);up=[ids[e['Id']] for e in edges if e.get('Id') in graph];incoming=fields(up[0]) if up else {};out=fields(n)
  for e in edges:
   require(e.get('SourceSide') in ['left','right','top','bottom'] and e.get('TargetSide') in ['left','right','top','bottom'],name+': unknown connection port')
  if code=='table-input':
   require(isinstance(p.get('DataCloneRecId'),int),name+': numeric dataset ID required')
   for c in p.get('SelectedColumns',[]):require(isinstance(c.get('RecId'),int),name+': numeric source-column RecId required')
  elif code in ['json-to-rows','json-to-columns','calculated-columns']:
   setting='Columns' if code in ['json-to-rows','json-to-columns'] else 'CalculatedColumns';added=[c['Name'] for c in p.get(setting,[])];existing={k.casefold() for k in incoming}
   require(len(added)==len({k.casefold() for k in added}),name+': duplicate added aliases ignoring case')
   require(not existing&{k.casefold() for k in added},name+': added alias duplicates an incoming column')
   if code in ['json-to-rows','json-to-columns']:require(p.get('SourceColumn') in incoming,name+': JSON source column is unavailable')
   for c in p.get(setting,[]):
    if code=='calculated-columns':
     expr=c.get('Expression','');require(not re.search(r'\bCOLLATE\b',expr,re.I),name+': explicit COLLATE is prohibited')
     require(set(re.findall(r'\[([^\]]+)\]',expr))<=incoming.keys(),name+': expression uses missing fields or unverified same-node aliases')
     if 'CONCAT' in expr.upper():
      textcols=[k for k in set(re.findall(r'\[([^\]]+)\]',expr)) if incoming.get(k,'').startswith('text')]
      if len(textcols)>1:warnings.append(name+': CONCAT combines multiple text columns; implicit collation needs engine verification')
  elif code=='column-selector':
   for c in p.get('RenamedColumns',[]):require(c['Name'] in incoming,name+': rename source is missing')
   aliases={c['Name']:c['Alias'] for c in p.get('RenamedColumns',[])};mapped={aliases.get(k,k):v for k,v in incoming.items()}
   require(all(k in mapped and mapped[k]==v for k,v in out.items()),name+': selector fields/types disagree with incoming schema')
  elif code=='convert-type':
   changed={c['Name']:c['InternalType'] for c in p.get('ConvertedColumns',[])}
   require(changed.keys()<=incoming.keys(),name+': converted field missing upstream')
   require(out=={k:changed.get(k,v) for k,v in incoming.items()},name+': conversion schema mismatch')
  elif code=='group-rows':
   for key in ['AggregateColumns','AggregatedColumns']:
    require(key not in p,name+': unsupported Group Rows '+key+'; use documented GroupedValues')
   require(bool(p.get('GroupedValues')),name+': Group Rows requires at least one aggregate')
   for value in p.get('GroupedValues',[]):
    require(all(value.get(k) for k in ['Name','Alias','Aggregation','InternalType']),name+': aggregate requires Name, Alias, Aggregation and InternalType')
    require(out.get(value.get('Alias'))==value.get('InternalType'),name+': aggregate Alias/type does not match OutputColumns')
    if value.get('Aggregation')=='string_agg':require('Separator' in value,name+': string_agg requires explicit Separator')
   require(all(c['Name'] in incoming for c in p.get('GroupByColumns',[])+p.get('GroupedValues',[])),name+': grouping/aggregate source missing')
  elif code=='lookup-columns':
   require(p.get('LookupNodeId') in [e.get('Id') for e in edges],name+': LookupNodeId must reference an incoming source')
   dimension=fields(ids.get(p.get('LookupNodeId'),{}));main=next((fields(s) for s in up if s['Id']!=p.get('LookupNodeId')), {})
   for c in p.get('Conditions',[]):
    require(c['ColumnName'] in dimension,name+': lookup condition field missing from lookup source')
    if c.get('ValueType')=='column':require(set(c.get('Values',[]))<=main.keys(),name+': lookup main-side condition field missing')
   for c in p.get('Values',[]):require(c['Name'] in dimension,name+': selected lookup value is missing')
  elif code=='combine-tables':
   sourceids={e['Id'] for e in edges};require(p.get('SchemaSourceId') in sourceids,name+': SchemaSourceId is not an incoming source')
   declared={c['Name']:c['InternalType'] for c in p.get('Columns',[])};require(declared==out,name+': combine declaration/output schema mismatch')
   for c in p.get('Columns',[]):
    matched=set(c.get('sources',[]));actions={a['SourceId']:a for a in c.get('Actions',[])}
    require(matched.isdisjoint(actions) and matched|actions.keys()==sourceids,name+': every source/column pair must have exactly one match or action: '+c['Name'])
    for id in matched:
     actual=fields(ids.get(id,{}));require(actual.get(c['Name'])==c['InternalType'],name+': match column/type missing: '+c['Name'])
    for id,a in actions.items():
     if a.get('Action')=='settonull':
      require(a.get('MatchedColumnName') is None,name+': settonull must not name a match')
      require({'id':id,'status':'notmatched'} in c.get('invalidSources',[]),name+': missing notmatched metadata')
     else:warnings.append(name+': action '+str(a.get('Action'))+' requires separate review; this linter only models settonull')
  elif code=='table-output':
   require(p.get('ProcessMode') in ['rebuild','append','updateappend'],name+': explicit supported write mode required')
   if p.get('DataCloneRecId') is None:
    warnings.append(name+': unbound dummy output; create/select its destination table in the editor before execution')
   else:require(isinstance(p.get('DataCloneRecId'),int) and not isinstance(p.get('DataCloneRecId'),bool),name+': destination ID must be numeric when supplied')
   if disabled:require(p.get('Enabled') is False,name+': teaching output must be disabled')
   for c in p.get('SelectedColumns',[]):require(incoming.get(c['SourceName'])==c['InternalType'],name+': output source/type mismatch')
  elif code=='filter-query':require(set(re.findall(r'\[([^\]]+)\]',p.get('Expression','')))<=incoming.keys(),name+': filter references unavailable fields')
 return dict(result='FAIL' if errors else 'PASS',errors=errors,warnings=warnings,processingNodes=len(processing),objects=len(flow),scope='Static documented checks; no resource existence, collation, engine execution or output semantics guarantee')
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('path');parser.add_argument('--require-disabled-outputs',action='store_true');args=parser.parse_args();report=lint(json.loads(Path(args.path).read_text()),args.require_disabled_outputs);print(json.dumps(report,indent=2));raise SystemExit(1 if report['errors'] else 0)
