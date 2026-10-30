"""Rebuild generic teaching flows from the documented clipboard structures.
Uses synthetic resources/data only. Does not contact ClicData.
"""
import copy,json,re,uuid,html,shutil
from style_flow import apply_style
from pathlib import Path
R=Path(__file__).resolve().parents[1]
NS=uuid.UUID('9415fc49-639e-4a95-a958-057740f19e06')
def uid(s):return str(uuid.uuid5(NS,s))
def write(p,v):
 p=R/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
# The active reference is already generalized; rebuild only from generic sources.
A=json.loads((R/'reference/annotation-templates.json').read_text())
NODE_CLASSES={n['code']:n['propertyClass'] for n in json.loads((R/'reference/node-catalog.json').read_text())}
T='textsimple(250)';I='int64';M='decimalstrict(28,9)'
PALETTE={'input':(112,173,71),'output':(112,173,71),'prepare':(255,192,2),'expand':(0,176,240),'grouping':(68,114,196),'calculate':(197,91,18),'combine':(197,91,18),'filter':(68,114,196)}
CATALOG=[]
class Example:
 def __init__(self,slug,title,purpose):self.slug=slug;self.title=title;self.purpose=purpose;self.nodes=[];self.data={};self.groups=[];self.bindings={}
 def node(self,code,name,schema,src=None,**extra):
  cls=NODE_CLASSES[code]
  n=dict(Code=code,Description='',Error=None,Id=uid(self.slug+'/'+name),Name=name,Sequence=len(self.nodes)+1,Warning=None,Properties={'__type':cls,'_AppVersion':'2026.4.204.0','_PatchVersion':0,'CheckpointType':None,'Enabled':True,'Left':0,'Top':0,'OutputColumns':[dict(Name=k,InternalType=t,traceId=uid(self.slug+'/'+name+'/'+k)) for k,t in schema],'Sources':[dict(Id=x['Id'],SourceSide='right',TargetSide='left') for x in src or []],**extra})
  self.nodes.append(n);return n
 def input(self,name,schema,rows):
  dataset=900000+len(self.data)+1;fields=[dict(Name=k,InternalType=t,RecId=800000+len(self.data)*100+i) for i,(k,t) in enumerate(schema,1)]
  self.data[str(dataset)]=rows;self.bindings[str(dataset)]=dict(name=name,columns=fields,synthetic=True)
  return self.node('table-input',name,schema,DataCloneName=name,DataCloneRecId=dataset,SelectedColumns=fields)
 def select(self,n,name,fields,aliases=None):
  aliases=aliases or {};return self.node('column-selector',name,fields,[n],RenamedColumns=[dict(Name=k,Alias=v) for k,v in aliases.items()],SortedColumnNames=[],UnselectedColumnNames=[k for k,t in shape(n) if aliases.get(k,k) not in dict(fields)])
 def calculate(self,n,name,items):return self.node('calculated-columns',name,shape(n)+[(k,t) for k,t,e in items],[n],CalculatedColumns=[dict(Name=k,InternalType=t,Expression=e) for k,t,e in items])
 def expand(self,n,name,column,paths):return self.node('json-to-rows',name,shape(n)+[(k,t) for k,t,p in paths],[n],SourceColumn=column,Columns=[dict(Name=k,InternalType=t,Node=p,IsArray=False,IsObject=False) for k,t,p in paths])
 def group(self,n,name,keys,aggs):return self.node('group-rows',name,[(k,dict(shape(n))[k]) for k in keys]+[(alias,t) for k,fn,alias,t in aggs],[n],GroupByColumns=[dict(Name=k) for k in keys],GroupedValues=[dict(Name=k,Aggregation=fn,Alias=alias,InternalType=t) for k,fn,alias,t in aggs])
 def lookup(self,n,g,name,key):
  extra=[(k,t) for k,t in shape(g) if k!=key]
  return self.node('lookup-columns',name,shape(n)+extra,[n,g],LookupNodeId=g['Id'],Conditions=[dict(ColumnName=key,Comparator='equals',Disabled=False,DisabledIfNull=False,Groups=[],Guid=uid(self.slug+'/'+name+'/condition'),LogicalOperator='and',ValueType='column',Values=[key])],Values=[dict(Name=k,Alias=k) for k,t in extra])
 def output(self,n):
  o=self.node('table-output','Example Output — Configure Your Destination',shape(n),[n],DataCloneName='SYNTHETIC EXAMPLE DESTINATION',DataCloneRecId=999999,ProcessMode='rebuild',SelectedColumns=[dict(SourceName=k,OutputName=k,InternalType=t) for k,t in shape(n)]);o['Properties']['Enabled']=False;return o
 def section(self,title,description,kind,x,y,nodes):self.groups.append(dict(title=title,description=description,kind=kind,x=x,y=y,ids=[n['Id'] for n in nodes]))
 def save(self):
  panels=[];labels=[]
  def ann(template,key,x,y,w,h,text):
   a=copy.deepcopy(template);a['Id']=uid(self.slug+'/'+key);a['Properties'].update(Left=x,Top=y,Width=w,Height=h,Text=text);return a
  for g in self.groups:
   x,y=g['x'],g['y'];w=max(221,68+170*(len(g['ids'])-1)+116);top=y-187
   for i,id in enumerate(g['ids']):next(n for n in self.nodes if n['Id']==id)['Properties'].update(Left=x+170*i,Top=y)
   color=lambda a:'rgba('+', '.join(map(str,(*PALETTE[g['kind']],a)))+')'
   p=ann(A[0],g['title']+'/panel',x-34,top,w,306,'');p['Properties']['Background']['Color']=color(.1);panels.append(p)
   p=ann(A[1],g['title']+'/title',x-34,top,w,34,g['title']);p['Properties']['Background']['Color']=color(1);p['Properties']['Font']['Background']['Color']=color(1);p['Properties']['Font']['Color']='rgba(50, 50, 50, 1)' if g['kind'] in ['input','output','prepare','expand'] else 'rgba(255, 255, 255, 1)';labels.append(p)
   labels.append(ann(A[2],g['title']+'/description',x,top+68,w-68,85,g['description']))
  folder='examples/canonical/'+self.slug
  styled=apply_style(panels+self.nodes+labels,'light')
  panels=[n for n in styled if n['Code']=='background-panel']
  labels=[n for n in styled if n['Code']=='label']
  self.nodes=[n for n in styled if n['Code'] not in ['label','background-panel']]
  write(folder+'/flow.clipboard.json',styled)
  # No-output variant removes the corresponding section, not just its node.
  out=self.nodes[-1];assert out['Code']=='table-output' and self.groups[-1]['kind']=='output'
  write(folder+'/preview.clipboard.json',panels[:-1]+self.nodes[:-1]+labels[:-2]);write(folder+'/synthetic-inputs.json',self.data);write(folder+'/bindings.json',self.bindings);write(folder+'/sections.json',self.groups)
  meta=dict(id=self.slug,title=self.title,purpose=self.purpose,processingNodes=len(self.nodes),schema=[dict(name=k,type=t) for k,t in shape(out)],evidence='Generated adaptation of documented structures; local simulation tested separately; ClicData execution unverified',resourcePolicy='Synthetic numeric IDs. Rebind every source/destination and source-column RecId before import into a real account.',outputPolicy='Output is disabled. Example rebuild mode is illustrative; obtain the actual requested write mode.')
  write(folder+'/manifest.json',meta);CATALOG.append(meta)
  render_svg(folder,panels+self.nodes+labels)

def shape(n):return [(c['Name'],c['InternalType']) for c in n['Properties']['OutputColumns']]
def output_section(e,n,x,y):
 o=e.output(n);e.section('Output','Configure destination and write mode.','output',x,y,[o]);return o

def render_svg(folder,flow,theme="light"):
 nodes=[n for n in flow if n['Code'] not in ['label','background-panel']];byid={n['Id']:n for n in nodes};xs=[];ys=[]
 for n in flow:
  p=n['Properties'];xs.extend([p['Left'],p['Left']+p.get('Width',120)]);ys.extend([p['Top'],p['Top']+p.get('Height',80)])
 left=min(xs)-30;top=min(ys)-45;width=max(xs)-left+30;height=max(ys)-top+35
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{left} {top} {width} {height}" role="img"><title>{html.escape(folder.split("/")[-1])} — generated layout guide, not an editor screenshot</title><rect x="{left}" y="{top}" width="{width}" height="{height}" fill="{"#202020" if theme=="dark" else "#fafaf7"}"/><defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#777"/></marker></defs>']
 for n in flow:
  if n['Code']!='background-panel':continue
  p=n['Properties'];svg.append(f'<rect x="{p["Left"]}" y="{p["Top"]}" width="{p["Width"]}" height="{p["Height"]}" rx="4" fill="{p["Background"]["Color"]}" stroke="#b3b3b3"/>')
 for n in nodes:
  p=n['Properties']
  for edge in p['Sources']:
   q=byid[edge['Id']]['Properties'];x1=q['Left']+120;y1=q['Top']+40;x2=p['Left'];y2=p['Top']+40
   if edge.get('SourceSide')=='bottom':x1=q['Left']+60;y1=q['Top']+80
   if edge.get('TargetSide')=='top':x2=p['Left']+60;y2=p['Top']
   svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#999" fill="none" marker-end="url(#arrow)"/>')
 for n in nodes:
  p=n['Properties'];color=('#70ad47' if n['Code'] in ['table-input','table-output','table-merge','table-fusion'] else '#4472c4' if n['Code'] in ['group-rows','filter-query','filter-simple','pivot','unpivot'] else '#ffc002' if n['Code'] in ['column-selector','convert-type','fix-data','standardize-data','remove-duplicates','transform-data','find-replace'] else '#00b0f0' if n['Code'] in ['json-to-rows','text-to-rows','text-to-columns'] else '#c55b12');x=p['Left'];y=p['Top'];svg.append(f'<rect x="{x}" y="{y}" width="120" height="80" rx="3" fill="white" stroke="#ccc"/><rect x="{x}" y="{y}" width="5" height="80" fill="{color}"/>')
  words=n['Name'].replace('—',' ').split();lines=[];line=''
  for word in words:
   if len(line+' '+word)>19 and line:lines.append(line);line=word
   else:line=(line+' '+word).strip()
  if line:lines.append(line)
  for i,t in enumerate(lines[:4]):svg.append(f'<text x="{x+60}" y="{y+20+i*12}" font-family="Arial" font-size="10" text-anchor="middle" fill="#333">{html.escape(t)}</text>')
 for n in flow:
  if n['Code']!='label':continue
  p=n['Properties'];x=p['Left'];y=p['Top'];w=p['Width'];h=p['Height'];bg=p['Background']['Color'];is_header=h in (34,40,51)
  if is_header:svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>')
  words=p['Text'].split();lines=[];line='';limit=max(16,int(w/6))
  for word in words:
   if len(line+' '+word)>limit and line:lines.append(line);line=word
   else:line=(line+' '+word).strip()
  if line:lines.append(line)
  for i,t in enumerate(lines[:5]):svg.append(f'<text x="{x+w/2}" y="{y+(22 if is_header else 15)+i*15}" font-family="Arial" font-size="{11 if is_header else 10}" text-anchor="middle" fill="{p["Font"]["Color"]}">{html.escape(t)}</text>')
 svg.append(f'<text x="{left+5}" y="{top+18}" font-family="Arial" font-size="11" fill="#666">GENERATED LAYOUT GUIDE · SYNTHETIC EXAMPLE · NOT AN EDITOR SCREENSHOT</text></svg>')
 (R/folder/'layout.svg').write_text(''.join(svg))
# 01: Smallest complete selection / rename / conversion / output path.
e=Example('01-select-and-type','Select, rename and type fields','Start here for flat input tables and simple output mapping.')
a=e.input('Example Orders',[('order_id',I),('created_at','datetime'),('status',T)],[dict(order_id=1,created_at='2026-01-01T12:00:00',status='OPEN'),dict(order_id=2,created_at='2026-01-02T09:00:00',status='CLOSED')]);e.section('Input','Read the synthetic orders.','input',0,0,[a]);b=e.select(a,'Select Dashboard Fields',[('Order_ID',I),('OrderDate','datetime'),('OrderStatus',T)],{'order_id':'Order_ID','created_at':'OrderDate','status':'OrderStatus'});c=e.node('convert-type','Convert Reporting Date',[('Order_ID',I),('OrderDate','date'),('OrderStatus',T)],[b],ConvertedColumns=[dict(Name='OrderDate',InternalType='date')]);e.section('Prepare','Rename fields and set the reporting date.','prepare',323,0,[b,c]);output_section(e,c,850,0);e.save()
# 02: Parent order ID stays repeated on item rows.
e=Example('02-nested-lines','Nested JSON lines with parent IDs','Use when expanding an array while retaining parent context.')
a=e.input('Example Nested Orders',[('Order_ID',T),('items','json')],[dict(Order_ID='O-1',items=json.dumps([dict(sku='SHARED-01',quantity=2,unit_price=12.5),dict(sku='ITEM-02',quantity=1,unit_price=8)])),dict(Order_ID='O-2',items='[]')]);e.section('Input','Read orders with nested item arrays.','input',0,0,[a]);b=e.expand(a,'Expand Order Items','items',[('SKU',T,'$[].sku'),('Units',I,'$[].quantity'),('UnitPrice',M,'$[].unit_price')]);e.section('Expand Lines','Repeat Order_ID once per item.','expand',323,0,[b]);c=e.calculate(b,'Calculate Line Sales',[('SalesAmount',M,'[Units]*[UnitPrice]')]);d=e.select(c,'Keep Dashboard Columns',[('Order_ID',T),('SKU',T),('Units',I),('SalesAmount',M)]);e.section('Line Values','Calculate sales and remove helper fields.','calculate',646,0,[c,d]);output_section(e,d,1173,0);e.save()
# 03: Explicit native Combine NULL actions on genuinely absent fields.
e=Example('03-combine-native-null','Combine with source-specific fields','Use for unions, matching columns and explicit missing-source NULLs.')
a=e.input('Example Source A',[('Order_ID',T),('SKU',T),('SalesAmount',M),('Category',T)],[dict(Order_ID='A1',SKU='SHARED-01',SalesAmount=25,Category='Example category')]);e.section('Input A','Read source A fields.','input',0,0,[a]);b=e.input('Example Source B',[('Order_ID',T),('SKU',T),('SalesAmount',M),('UPC',T)],[dict(Order_ID='B1',SKU='SHARED-01',SalesAmount=18,UPC='001234567890')]);e.section('Input B','Read source B fields.','input',0,400,[b]);fields=[('Order_ID',T),('SKU',T),('SalesAmount',M),('Category',T),('UPC',T)];cs=[]
for k,t in fields:
 yes=[n['Id'] for n in [a,b] if k in dict(shape(n))];no=[n['Id'] for n in [a,b] if k not in dict(shape(n))];cs.append(dict(Name=k,InternalType=t,internalType=t,Actions=[dict(Action='settonull',MatchedColumnName=None,SourceId=id) for id in no],sources=yes,invalidSources=[dict(id=id,status='notmatched') for id in no],error=False))
c=e.node('combine-tables','Combine Sources',fields,[a,b],SchemaSourceId=a['Id'],Columns=cs);e.section('Combine','Match shared fields; set unavailable values to NULL.','combine',323,200,[c]);output_section(e,c,646,200);e.save()
# 04: Aggregate events separately and attach one result per parent.
e=Example('04-event-rollup-lookup','Event rollup and lookup','Use to prevent event expansion from multiplying the final fact.')
a=e.input('Example Line Facts',[('Line_ID',T),('SalesAmount',M)],[dict(Line_ID='L1',SalesAmount=50),dict(Line_ID='L2',SalesAmount=20)]);e.section('Facts','Keep one row per line.','input',0,300,[a]);b=e.input('Example Refund Events',[('Line_ID',T),('Amount',M)],[dict(Line_ID='L1',Amount=5),dict(Line_ID='L1',Amount=3)]);e.section('Events','Read multiple events per line.','input',0,-100,[b]);c=e.group(b,'Refund Total per Line',['Line_ID'],[('Amount','sum','RefundAmount',M)]);e.section('Aggregate','Reduce events to one row per key.','grouping',323,-100,[c]);d=e.lookup(a,c,'Attach Refund Total','Line_ID');next(s for s in d['Properties']['Sources'] if s['Id']==c['Id']).update(SourceSide='bottom',TargetSide='top');f=e.calculate(d,'Refund Adjusted Sales',[('NetSalesAmount',M,'[SalesAmount]-COALESCE([RefundAmount],0)')]);e.section('Enrich Facts','Attach totals without multiplying line rows.','calculate',323,300,[d,f]);output_section(e,f,850,300);e.save()
# 05: Group Rows cannot use an empty aggregate list for distinct keys.
e=Example('05-distinct-key-helper','Distinct keys with a count helper','Use this instead of Group Rows with empty GroupedValues.')
a=e.input('Example Activity',[('Item_ID',T),('Record_ID',I)],[dict(Item_ID='A',Record_ID=1),dict(Item_ID='A',Record_ID=2),dict(Item_ID=None,Record_ID=3)]);e.section('Input','Read repeated and null item keys.','input',0,0,[a]);b=e.group(a,'Count per Item',['Item_ID'],[('Record_ID','count','HelperCount',I)]);c=e.select(b,'Remove Helper Count',[('Item_ID',T)]);e.section('Distinct Keys','Group with an aggregate; remove the helper.','grouping',323,0,[b,c]);output_section(e,c,850,0);e.save()
# 06: Replacement uses a raw name; dependent calculations use another node.
e=Example('06-safe-calculations','Safe calculation aliases and NULLs','Use distinct raw names and sequential nodes for dependent formulas.')
a=e.input('Example Quantities',[('SKU',T),('RawQuantity',I),('RawCancelled',I),('RawUnitPrice',M)],[dict(SKU='A',RawQuantity=3,RawCancelled=None,RawUnitPrice=10),dict(SKU='B',RawQuantity=1,RawCancelled=2,RawUnitPrice=5),dict(SKU='C',RawQuantity=2,RawCancelled=0,RawUnitPrice=None)]);e.section('Input','Read raw counters and prices.','input',0,0,[a]);b=e.calculate(a,'Active Units',[('ActiveUnits',I,'CASE WHEN [RawQuantity]-COALESCE([RawCancelled],0) < 0 THEN NULL ELSE [RawQuantity]-COALESCE([RawCancelled],0) END')]);c=e.calculate(b,'Line Sales',[('SalesAmount',M,'[ActiveUnits]*[RawUnitPrice]')]);d=e.select(c,'Final Columns',[('SKU',T),('ActiveUnits',I),('SalesAmount',M)]);e.section('Calculate','Avoid collisions and keep missing amounts unknown.','calculate',323,0,[b,c,d]);output_section(e,d,1020,0);e.save()
# 07: A small filter example distinct from calculations/lookup.
e=Example('07-filter-before-output','Filter a reporting subset','Use for a supported Filter Query expression and clear row filtering.')
a=e.input('Example Tickets',[('Ticket_ID',I),('Status',T)],[dict(Ticket_ID=1,Status='OPEN'),dict(Ticket_ID=2,Status='CLOSED')]);e.section('Input','Read example tickets.','input',0,0,[a]);b=e.node('filter-query','Keep Open Tickets',shape(a),[a],Expression="[Status] = 'OPEN'");e.section('Filter','Keep only the requested reporting subset.','filter',323,0,[b]);output_section(e,b,646,0);e.save()
# 08: Complete two-source nested-line dashboard recipe with an explicit synthetic rule.
e=Example('08-two-source-line-dashboard','Two-source line dashboard','Use for a complete nested-array-to-common-schema pipeline with two sources.')
final=[('SalesAmount',M),('Order_ID',T),('OrderDate','date'),('SourcePlatform',T),('SKU',T),('ActiveUnits',I),('OrderStatus',T)]
ends=[]
for source,y in [('A',0),('B',650)]:
 if source=='A':
  schema=[('order_id',T),('created_at','datetime'),('state',T),('items','json')]
  rows=[dict(order_id='A-1',created_at='2026-01-01T12:00:00',state='ready',items=json.dumps([dict(sku='SHARED-01',quantity=2,unit_price=12.5)])),dict(order_id='A-2',created_at='2026-01-02T12:00:00',state='done',items=json.dumps([dict(sku='ITEM-02',quantity=1,unit_price=8)]))]
  rename={'order_id':'Order_ID','created_at':'OrderDate','state':'RawStatus','items':'ItemsJson'}
 else:
  schema=[('orderId',I),('createdAt','datetime'),('status',T),('lines','json')]
  rows=[dict(orderId=101,createdAt='2026-01-03T12:00:00',status='dispatched',lines=json.dumps([dict(productCode='SHARED-01',qty=3,cancelled=1,price=9)]))]
  rename={'orderId':'Order_ID','createdAt':'OrderDate','status':'RawStatus','lines':'ItemsJson'}
 a=e.input('Example Source '+source,schema,rows);e.section('Source '+source+' Input','Read synthetic parent orders and line arrays.','input',0,y,[a]);start=len(e.nodes)
 a=e.select(a,'Map Source '+source,[(rename[k],t) for k,t in shape(a)],rename)
 if source=='B':a=e.node('convert-type','Source B Order ID Type',[(k,T if k=='Order_ID' else t) for k,t in shape(a)],[a],ConvertedColumns=[dict(Name='Order_ID',InternalType=T)])
 e.section('Source '+source+' Mapping','Select and normalize the parent order fields.','prepare',323,y,e.nodes[start:]);start=len(e.nodes)
 paths=[('SKU',T,'$[].sku'),('ActiveUnits',I,'$[].quantity'),('RawUnitPrice',M,'$[].unit_price')] if source=='A' else [('SKU',T,'$[].productCode'),('RawQuantity',I,'$[].qty'),('RawCancelled',I,'$[].cancelled'),('RawUnitPrice',M,'$[].price')]
 a=e.expand(a,'Expand Source '+source+' Lines','ItemsJson',paths);e.section('Source '+source+' Lines','Expand the array and retain the parent ID.','expand',867,y,e.nodes[start:]);start=len(e.nodes)
 if source=='B':a=e.calculate(a,'Source B Active Units',[('ActiveUnits',I,'CASE WHEN [RawQuantity]-COALESCE([RawCancelled],0) < 0 THEN NULL ELSE [RawQuantity]-COALESCE([RawCancelled],0) END')])
 state="CASE WHEN [RawStatus] = 'ready' THEN 'OPEN' WHEN [RawStatus] = 'done' THEN 'CLOSED' ELSE 'UNKNOWN' END" if source=='A' else "CASE WHEN [RawStatus] = 'dispatched' THEN 'SHIPPED' ELSE 'UNKNOWN' END"
 a=e.calculate(a,'Source '+source+' Dashboard Values',[('SalesAmount',M,'[RawUnitPrice]*[ActiveUnits]'),('SourcePlatform',T,"'SOURCE_"+source+"'"),('OrderStatus',T,state)])
 a=e.select(a,'Source '+source+' Common Columns',[(k,'datetime' if k=='OrderDate' else t) for k,t in final]);e.section('Source '+source+' Values','Apply this example rule and project common fields.','calculate',1190,y,e.nodes[start:]);ends.append(a)
pre=[(k,'datetime' if k=='OrderDate' else t) for k,t in final]
a=e.node('combine-tables','Combine Source Lines',pre,ends,SchemaSourceId=ends[0]['Id'],Columns=[dict(Name=k,InternalType=t,internalType=t,Actions=[],sources=[n['Id'] for n in ends],invalidSources=[],error=False) for k,t in pre]);b=e.node('convert-type','Dashboard Date',final,[a],ConvertedColumns=[dict(Name='OrderDate',InternalType='date')]);e.section('Unified Dashboard','Match identical schemas and set the date.','combine',2057,325,[a,b]);output_section(e,b,2600,325);e.save()
write('examples/canonical/catalog.json',CATALOG)
# Node references and annotation templates are maintained sources, not rebuild outputs.
print('Built',len(CATALOG),'canonical examples; retained',len(NODE_CLASSES),'node settings references.')
