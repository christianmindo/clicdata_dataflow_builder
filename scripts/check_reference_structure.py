"""Check the modular reference's routing, local links and catalog integrity.
Maintenance check only; does not establish ClicData behavior.
"""
import json,re
from pathlib import Path
from urllib.parse import unquote
R=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
catalog=json.loads((R/'reference/node-catalog.json').read_text())
check(len(catalog)==len({n['code'] for n in catalog}),'Duplicate node codes')
for n in catalog:
 for key in ['file','guide']:check((R/'reference'/n[key]).is_file(),f"Missing {n['code']} {key}")
 settings=json.loads((R/'reference'/n['file']).read_text())
 check(settings['code']==n['code'] and settings['propertyClass']==n['propertyClass'],f"Mismatched catalog: {n['code']}")
 check(n['code'] in (R/'reference'/n['guide']).read_text(),f"Mismatched guide: {n['code']}")
# Active documentation only: archives/presentations are retained historical material.
paths=[R/'README.md',R/'AGENTS.md',R/'examples/INDEX.md']+list((R/'reference').glob('*.md'))+list((R/'reference/nodes').glob('*.md'))
for p in paths:
 text=p.read_text()
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if target.startswith(('https:','http:','#','mailto:')):continue
  dest=unquote(target.split('#')[0].split(' "')[0].strip('<>'))
  check((p.parent/dest).exists(),f"Broken link in {p.relative_to(R)}: {target}")
 for b in re.findall(r'```json\s*\n(.*?)\n```',text,re.S):
  try:json.loads(b)
  except json.JSONDecodeError as e:errors.append(f"Invalid JSON in {p.relative_to(R)}: {e}")
check(len((R/'README.md').read_text().split())<700,'README has grown beyond its navigation role')
check(len((R/'AGENTS.md').read_text().split())<1100,'Always-loaded instructions exceed focused budget')
builder=(R/'scripts/build_reference_pack.py').read_text()
check("R/'README.md'" not in builder,'Teaching builder depends on README content')
check("write('reference/node-catalog.json'" not in builder,'Teaching builder overwrites maintained node catalog')
manifest=json.loads((R/'reference/PACK-MANIFEST.json').read_text())
check(manifest['nodeSettingsReferences']==len(catalog),'Stale manifest node count')
if errors:
 for e in errors:print('FAIL:',e)
 raise SystemExit(1)
print(f'PASS: {len(catalog)} node settings/guides, active links/JSON, focused entry points, rebuild separation and manifest.')
