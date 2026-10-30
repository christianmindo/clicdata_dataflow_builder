"""Validate generic teaching flows locally, including tiny synthetic expectations.
This is not ClicData engine/import validation.
"""
import json,re,sqlite3,copy
from pathlib import Path
from collections import defaultdict
R=Path(__file__).resolve().parents[1]
EXPECTED={
 '01-select-and-type':[{'Order_ID':1,'OrderDate':'2026-01-01','OrderStatus':'OPEN'},{'Order_ID':2,'OrderDate':'2026-01-02','OrderStatus':'CLOSED'}],
 '02-nested-lines':[{'Order_ID':'O-1','SKU':'SHARED-01','Units':2,'SalesAmount':25},{'Order_ID':'O-1','SKU':'ITEM-02','Units':1,'SalesAmount':8}],
 '03-combine-native-null':[{'Order_ID':'A1','SKU':'SHARED-01','SalesAmount':25,'Category':'Example category','UPC':None},{'Order_ID':'B1','SKU':'SHARED-01','SalesAmount':18,'Category':None,'UPC':'001234567890'}],
 '04-event-rollup-lookup':[{'Line_ID':'L1','SalesAmount':50,'RefundAmount':8,'NetSalesAmount':42},{'Line_ID':'L2','SalesAmount':20,'RefundAmount':None,'NetSalesAmount':20}],
 '05-distinct-key-helper':[{'Item_ID':'A'},{'Item_ID':None}],
 '06-safe-calculations':[{'SKU':'A','ActiveUnits':3,'SalesAmount':30},{'SKU':'B','ActiveUnits':None,'SalesAmount':None},{'SKU':'C','ActiveUnits':2,'SalesAmount':None}],
 '07-filter-before-output':[{'Ticket_ID':1,'Status':'OPEN'}],
 '08-two-source-line-dashboard':[{'SalesAmount':25,'Order_ID':'A-1','OrderDate':'2026-01-01','SourcePlatform':'SOURCE_A','SKU':'SHARED-01','ActiveUnits':2,'OrderStatus':'OPEN'},{'SalesAmount':8,'Order_ID':'A-2','OrderDate':'2026-01-02','SourcePlatform':'SOURCE_A','SKU':'ITEM-02','ActiveUnits':1,'OrderStatus':'CLOSED'},{'SalesAmount':18,'Order_ID':'101','OrderDate':'2026-01-03','SourcePlatform':'SOURCE_B','SKU':'SHARED-01','ActiveUnits':2,'OrderStatus':'SHIPPED'}]}
def rect(n):
 p=n['Properties'];return p['Left'],p['Top'],p.get('Width',116),p.get('Height',68)
def overlaps(a,b):return a[0]<b[0]+b[2] and b[0]<a[0]+a[2] and a[1]<b[1]+b[3] and b[1]<a[1]+a[3]
def schema(n):return [(c['Name'],c['InternalType']) for c in n['Properties']['OutputColumns']]
REPORT=[]
for folder in sorted((R/'examples/canonical').iterdir()):
 if not folder.is_dir():continue
 flow=json.loads((folder/'flow.clipboard.json').read_text());nodes=[n for n in flow if n['Code'] not in ['label','background-panel']];byid={n['Id']:n for n in nodes}
 data=json.loads((folder/'synthetic-inputs.json').read_text());bindings=json.loads((folder/'bindings.json').read_text());results={};count=0
 def check(name,test):
  global count
  assert test,(folder.name,name)
  count+=1
 db=sqlite3.connect(':memory:')
 def expr(e,row):
  keys=list(dict.fromkeys(re.findall(r'\[([^\]]+)\]',e)));assert set(keys)<=row.keys()
  return db.execute('SELECT '+e+(' FROM (SELECT '+','.join('? AS ['+k+']' for k in keys)+')' if keys else ''),[row[k] for k in keys]).fetchone()[0]
 check('unique IDs',len(flow)==len({n['Id'] for n in flow}))
 for n in nodes:
  p=n['Properties'];names=[k for k,t in schema(n)];code=n['Code']
  check(n['Name']+' schema names',len(names)==len({k.casefold() for k in names}))
  check(n['Name']+' no checkpoints',p.get('CheckpointType') is None and not {'CheckpointStatus','CheckpointIsOutdated'}&p.keys())
  for edge in p['Sources']:assert edge['Id'] in results
  if code=='table-input':
   tid=str(p['DataCloneRecId']);assert tid in data and p['SelectedColumns']==bindings[tid]['columns'];rows=[{k:r[k] for k in names} for r in data[tid]]
  else:
   src=results[p['Sources'][0]['Id']];rows=[]
   if code=='column-selector':
    aliases={c['Name']:c['Alias'] for c in p['RenamedColumns']};types={aliases.get(k,k):t for k,t in schema(byid[p['Sources'][0]['Id']])};assert all(types[k]==t for k,t in schema(n))
    for r in src:
     changed={aliases.get(k,k):v for k,v in r.items()};rows.append({k:changed[k] for k in names})
   elif code=='convert-type':
    for r in src:
     row=dict(r)
     for c in p['ConvertedColumns']:
      k=c['Name'];value=row[k]
      if value is not None:row[k]=str(value)[:10] if c['InternalType']=='date' else str(value)
     rows.append(row)
   elif code=='calculated-columns':
    incoming={k.casefold() for k,t in schema(byid[p['Sources'][0]['Id']])};added=[c['Name'].casefold() for c in p['CalculatedColumns']]
    assert not incoming&set(added) and len(added)==len(set(added))
    for c in p['CalculatedColumns']:assert 'COLLATE' not in c['Expression'].upper()
    for r in src:
     row=dict(r)
     for c in p['CalculatedColumns']:row[c['Name']]=expr(c['Expression'],row)
     rows.append(row)
   elif code=='json-to-rows':
    assert not {k.casefold() for k,t in schema(byid[p['Sources'][0]['Id']])}&{c['Name'].casefold() for c in p['Columns']}
    for r in src:
     for obj in json.loads(r[p['SourceColumn']]):
      row=dict(r)
      for c in p['Columns']:
       assert c['Node'].startswith('$[].') and c['Node'].count('[]')==1
       row[c['Name']]=obj.get(c['Node'][4:])
      rows.append(row)
   elif code=='combine-tables':
    ids={s['Id'] for s in p['Sources']}
    for c in p['Columns']:
     actions={a['SourceId']:a for a in c['Actions']};matched=set(c['sources']);assert matched.isdisjoint(actions) and matched|actions.keys()==ids
     for sid in ids:
      fields=dict(schema(byid[sid]))
      if sid in matched:assert fields[c['Name']]==c['InternalType']
      else:assert c['Name'] not in fields and actions[sid]['Action']=='settonull' and actions[sid]['MatchedColumnName'] is None and {'id':sid,'status':'notmatched'} in c['invalidSources']
    for edge in p['Sources']:
     for r in results[edge['Id']]:rows.append({c['Name']:r[c['Name']] if edge['Id'] in c['sources'] else None for c in p['Columns']})
   elif code=='group-rows':
    assert p['GroupedValues'];groups=defaultdict(list);keys=[c['Name'] for c in p['GroupByColumns']]
    for r in src:groups[tuple(r[k] for k in keys)].append(r)
    for key,items in groups.items():
     row=dict(zip(keys,key))
     for c in p['GroupedValues']:
      vals=[r[c['Name']] for r in items if r[c['Name']] is not None];fn=c['Aggregation'];row[c['Alias']]=len(vals) if fn=='count' else sum(vals) if vals else None
     rows.append(row)
   elif code=='lookup-columns':
    dimension=results[p['LookupNodeId']];key=p['Conditions'][0]['ColumnName'];mainkey=p['Conditions'][0]['Values'][0];index={r[key]:r for r in dimension};assert len(index)==len(dimension)
    for r in src:
     row=dict(r);match=index.get(r[mainkey],{})
     for c in p['Values']:row[c['Alias']]=match.get(c['Name'])
     rows.append(row)
    check('lookup preserves fact count in local model',len(rows)==len(src))
   elif code=='filter-query':rows=[dict(r) for r in src if expr(p['Expression'],r)]
   elif code=='table-output':
    check('disabled synthetic output',p['Enabled'] is False and p['DataCloneRecId']==999999);rows=copy.deepcopy(src)
    assert [(c['SourceName'],c['InternalType']) for c in p['SelectedColumns']]==schema(n)
   else:raise AssertionError(code)
  for row in rows:assert set(row)==set(names)
  results[n['Id']]=rows
 expected=EXPECTED[folder.name];actual=results[nodes[-1]['Id']]
 check('hand-authored expected output',actual==expected)
 (folder/'expected-output.json').write_text(json.dumps(expected,indent=2)+'\n')
 for i,n in enumerate(nodes):
  for z in nodes[i+1:]:assert not overlaps(rect(n),rect(z))
  for z in flow:
   if z['Code']=='label':assert not overlaps(rect(n),rect(z))
 panels=[n for n in flow if n['Code']=='background-panel']
 for i,n in enumerate(panels):
  for z in panels[i+1:]:assert not overlaps(rect(n),rect(z))
 check('estimated geometry',True)
 preview=json.loads((folder/'preview.clipboard.json').read_text());check('preview has no output',not any(n['Code']=='table-output' for n in preview))
 report=dict(example=folder.name,result='PASS',checks=count,processingNodes=len(nodes),expectedRows=len(expected),evidence='Local structural checks and Python/SQLite simulation; NOT ClicData import or execution')
 (folder/'validation.json').write_text(json.dumps(report,indent=2)+'\n');REPORT.append(report)
(R/'reference/validation-summary.json').write_text(json.dumps(dict(result='PASS',examples=len(REPORT),checks=sum(r['checks'] for r in REPORT),results=REPORT),indent=2)+'\n')
print('PASS:',len(REPORT),'examples;',sum(r['checks'] for r in REPORT),'checks; hand-authored expectations matched.')
