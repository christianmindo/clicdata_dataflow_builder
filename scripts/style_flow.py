"""Apply explicit light/dark annotation styling and center node groups.
Node dimensions are estimates; verify actual ClicData rendering after import.
"""
import argparse,copy,json,math
from pathlib import Path

ANNOTATIONS={'label','background-panel'}
def position_captions(flow,node_width=119,node_height=68):
 """Center captions in the header-to-group gap; leave every node untouched."""
 flow=copy.deepcopy(flow)
 for n in flow:
  if n['Code']!='background-panel':continue
  panel=n['Properties']
  def inside(p):
   return panel['Left']<=p['Left'] and p['Left']+p.get('Width',node_width)<=panel['Left']+panel['Width'] and panel['Top']<=p['Top'] and p['Top']+p.get('Height',node_height)<=panel['Top']+panel['Height']
  nodes=[n['Properties'] for n in flow if n['Code'] not in ANNOTATIONS and inside(n['Properties'])]
  labels=[n['Properties'] for n in flow if n['Code']=='label' and inside(n['Properties'])]
  headers=[p for p in labels if p['Top']==panel['Top'] and p['Width']==panel['Width']]
  if not nodes or not headers:continue
  start=max(p['Top']+p['Height'] for p in headers)
  end=min(p['Top'] for p in nodes) # Full group's top edge, not mean node centers.
  captions=[p for p in labels if p not in headers and p['Top']<end]
  if len(captions)>1:raise ValueError('Use one description label per section; combine caption text first')
  for p in captions:
   gap=end-start
   if gap<51:raise ValueError('Insufficient caption space between header and nodes')
   # Equal 17-unit margins require gap and label height to have equal parity.
   steps=min(round(p['Height']/17),int(gap/17)-2)
   if steps%2!=round(gap/17)%2:steps-=1
   if steps<1:raise ValueError('Caption cannot fit with symmetric margins')
   p['Height']=steps*17
   p['Top']=int(start+(gap-p['Height'])/2)
   # Match panel width with identical one-grid-step horizontal insets.
   p['Left']=panel['Left']+17;p['Width']=panel['Width']-34
 return flow

def apply_style(flow,theme,node_width=119,node_height=68):
 if theme not in ('light','dark'):raise ValueError('Choose light or dark explicitly')
 flow=copy.deepcopy(flow)
 snap=lambda v:int(math.floor(v/17+0.5)*17)
 if node_width%17 or node_height%17:raise ValueError('Full node footprint must use multiples of 17')
 panels=[n['Properties'] for n in flow if n['Code']=='background-panel']
 def inside(p,q):
  return q['Left']<=p['Left'] and q['Top']<=p['Top'] and p['Left']+p.get('Width',node_width)<=q['Left']+q['Width'] and p['Top']+p.get('Height',node_height)<=q['Top']+q['Height']
 for panel in panels:
  labels=[n['Properties'] for n in flow if n['Code']=='label' and inside(n['Properties'],panel)]
  nodes=[n['Properties'] for n in flow if n['Code'] not in ANNOTATIONS and inside(n['Properties'],panel)]
  # Capture section membership before changing any geometry.
  old_top=panel['Top']
  headers=[p for p in labels if p['Top']==old_top and p['Height'] in (34,40,51)]
  for p in [panel]+labels:
   for k in ('Left','Top','Width','Height'):p[k]=snap(p[k])
  # An odd number of 17-unit columns centers a 119-unit node exactly.
  units=math.ceil(panel['Width']/17)
  panel['Width']=(units if units%2 else units+1)*17
  for p in headers:p.update(Left=panel['Left'],Top=panel['Top'],Width=panel['Width'],Height=51)
  for p in labels:
   if p not in headers:p['Left']=panel['Left']+(panel['Width']-p['Width'])/2
  panel['Border']['Color']='rgba(180, 180, 180, 1)' if theme=='dark' else 'rgba(50, 50, 50, 1)'
  for p in labels:
   header=p in headers
   if not header:
    p['Font']['Color']='rgba(240, 240, 240, 1)' if theme=='dark' else 'rgba(50, 50, 50, 1)'
  if not nodes:continue
  # Reserve all labels above the original processing row. Center the group,
  # preserving relative positions (including parallel rows/helper branches).
  for p in nodes:p['Left']=snap(p['Left']);p['Top']=snap(p['Top'])
  first_top=min(p['Top'] for p in nodes)
  upper=[p['Top']+p['Height'] for p in labels if p['Top']<first_top]
  lower=[p['Top'] for p in labels if p['Top']>=max(n['Top']+node_height for n in nodes)]
  content_top=max(upper,default=panel['Top']+51)+17
  content_bottom=min(lower,default=panel['Top']+panel['Height'])-17
  left=min(p['Left'] for p in nodes);right=max(p['Left']+node_width for p in nodes)
  top=min(p['Top'] for p in nodes);bottom=max(p['Top']+node_height for p in nodes)
  if right-left>panel['Width']-34:
   raise ValueError('Panel too small for centered nodes and annotation clearance; enlarge it first')
  dx=panel['Left']+panel['Width']/2-(left+right)/2
  # Keep the established node row/branch geometry; position captions around it.
  dy=0
  for p in nodes:p['Left']=snap(p['Left']+dx);p['Top']=snap(p['Top']+dy)
 # Snap remaining labels/objects too; no fractional coordinates or sizes.
 for n in flow:
  for k in ('Left','Top','Width','Height'):
   if k in n['Properties']:n['Properties'][k]=snap(n['Properties'][k])
 return position_captions(flow,node_width,node_height)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');p.add_argument('--theme',required=True,choices=['light','dark']);p.add_argument('--out',required=True);p.add_argument('--node-width',type=int,default=119);p.add_argument('--node-height',type=int,default=68);a=p.parse_args()
 flow=apply_style(json.loads(Path(a.input).read_text()),a.theme,a.node_width,a.node_height)
 output=Path(a.out);output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(flow,indent=2)+'\n');print('Wrote',output)
