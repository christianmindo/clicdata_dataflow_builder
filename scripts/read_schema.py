"""Read a user-supplied ClicData schema CSV locally. No network/client-data access.
This produces schema metadata, not paste-ready clipboard JSON.
"""
import argparse,csv,json,re
from pathlib import Path

HEADERS={'column_name','source_column_name','type','visible','key'}
def read_schema(path,dataset_id=None,dataset_name=None):
 path=Path(path)
 match=re.fullmatch(r'schema_(\d{6})\.csv',path.name,re.I)
 filename_id=int(match.group(1)) if match else None
 if dataset_id is not None and filename_id is not None and dataset_id!=filename_id:
  raise ValueError('Explicit dataset ID conflicts with the six-digit schema filename ID; resolve the filename/mapping first')
 if dataset_id is None:dataset_id=filename_id
 if dataset_id is not None and (isinstance(dataset_id,bool) or not isinstance(dataset_id,int) or dataset_id<=0):
  raise ValueError('Dataset ID must be an explicitly supplied positive integer')
 with path.open(encoding='utf-8-sig',newline='') as handle:
  reader=csv.DictReader(handle)
  if reader.fieldnames is None or len(reader.fieldnames)!=5 or set(reader.fieldnames)!=HEADERS:
   raise ValueError('Expected exactly the five schema headers: '+', '.join(sorted(HEADERS)))
  columns=[];seen=set()
  for line,row in enumerate(reader,2):
   if None in row or any(v is None for v in row.values()):raise ValueError(f'Line {line}: wrong number of cells')
   for name in ('column_name','source_column_name','type'):
    if not row[name].strip():raise ValueError(f'Line {line}: empty {name}')
   name=row['column_name']
   if name.casefold() in seen:raise ValueError(f'Line {line}: duplicate column name ignoring case')
   seen.add(name.casefold())
   if row['visible'] not in ('0','1') or row['key'] not in ('0','1'):raise ValueError(f'Line {line}: flags must be 0 or 1')
   columns.append(dict(name=name,sourceColumnName=row['source_column_name'],internalType=row['type'],visible=row['visible']=='1',keyFlag=row['key']=='1',columnId=None))
 if not columns:raise ValueError('Schema has no columns')
 unresolved=[]
 if dataset_id is None:unresolved.append('Dataset ID is not supplied and the filename does not match the confirmed schema_<six-digit-ID>.csv convention.')
 if not dataset_name:unresolved.append('Target dataset display name is not supplied.')
 unresolved.append('Numeric source-column RecIds are absent from this CSV. Obtain a user-supplied Table Input export or explicit verified mapping before constructing a bound input.')
 return dict(kind='SCHEMA_METADATA_NOT_CLIPBOARD_JSON',sourceFile=path.name,datasetId=dataset_id,datasetIdEvidence='user-confirmed filename convention' if filename_id is not None else 'explicit user metadata' if dataset_id is not None else None,datasetName=dataset_name,columns=columns,importReady=False,unresolvedBindings=unresolved,evidence='Names/types/flags observed in local user-supplied CSV; no data rows, key uniqueness, target bindings, import or engine execution verified.')

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('schema');p.add_argument('--dataset-id',type=int);p.add_argument('--dataset-name');p.add_argument('--out',required=True);args=p.parse_args()
 try:result=read_schema(args.schema,args.dataset_id,args.dataset_name)
 except (ValueError,UnicodeError,csv.Error,OSError) as exc:p.exit(1,f'Schema error: {exc}\n')
 output=Path(args.out);output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
 print(f"Read {len(result['columns'])} field definitions. Bindings unresolved; output is schema metadata, not clipboard JSON.")
