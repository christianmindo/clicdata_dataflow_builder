"""Synthetic location schema regressions; no target bindings or execution."""
import copy
import uuid
from lint_flow import lint

def node(code, cls, fields, upstream=None, **settings):
    return {'Code': code, 'Id': str(uuid.uuid4()), 'Name': code, 'Properties': {
        '__type': cls + ':#Infinis.DataFlows', 'CheckpointType': None,
        'OutputColumns': [{'Name': k, 'InternalType': v} for k, v in fields.items()],
        'Sources': [] if upstream is None else [{'Id': upstream['Id'], 'SourceSide': 'right', 'TargetSide': 'left'}],
        **settings}}

source_fields = {'City': 'textsimple(250)', 'IPAddress': 'textsimple(250)'}
src = node('table-input', 'DataFlowNodeTableInputProperties', source_fields,
           DataCloneRecId=900001, SelectedColumns=[])
geo_fields = dict(source_fields, GeocodeCountryCode='textsimple(10)')
geo = node('geocoding', 'DataFlowNodeGeocodingProperties', geo_fields, src,
           GeocodeInputColumns=[{'Column': 'City', 'Type': 'city'}],
           GeocodeOutputColumns=[{'Column': 'GeocodeCountryCode', 'Type': 'country_code'}])
ip_fields = dict(geo_fields, IPLatitude='double', IPLongitude='double')
ip = node('iplocation', 'DataFlowNodeIPToLocationProperties', ip_fields, geo,
          SourceColumn='IPAddress', ProcessOutputColumns=[
              {'Name': 'IPLatitude', 'Type': 'latitude'}, {'Name': 'IPLongitude', 'Type': 'longitude'}])
out = node('table-output', 'DataFlowNodeTableOutputProperties', ip_fields, ip,
           ProcessMode='rebuild', SelectedColumns=[
               {'SourceName': k, 'OutputName': k, 'InternalType': v} for k, v in ip_fields.items()])
flow = [src, geo, ip, out]
assert not lint(flow)['errors'], lint(flow)

def rejects(mutated, expected):
    errors = lint(mutated)['errors']
    assert any(expected in e for e in errors), errors

v = copy.deepcopy(flow)
v[1]['Properties']['OutputColumns'].append({'Name': 'GeocodeLatitude', 'InternalType': 'decimalstrict(28,9)'})
rejects(v, 'explicitly selected outputs only')
v = copy.deepcopy(flow)
v[2]['Properties']['ProcessOutputColumns'][0]['Name'] = 'WrongLatitude'
rejects(v, 'explicitly selected outputs only')
v = copy.deepcopy(flow)
v[3]['Properties']['SelectedColumns'].append({'SourceName': 'GeocodeLatitude', 'OutputName': 'GeocodeLatitude', 'InternalType': 'decimalstrict(28,9)'})
rejects(v, 'output source/type mismatch')
v = copy.deepcopy(flow)
v[3]['Properties']['OutputColumns'].append({'Name': 'GeocodeLongitude', 'InternalType': 'decimalstrict(28,9)'})
rejects(v, 'output mappings disagree')
print('PASS: selected geocoding/IP fields accepted; 4 stale/mismatched schema mutations rejected')
