"""Connected Table Merge reference checks; no editor or engine execution."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(settings):
    inputs = {item['Id']: item for item in settings['MergeInputs']}
    upstream = settings['Sources'][0]['Id']
    node_input = inputs[upstream]
    assert node_input['SourceNodeId'] == upstream
    assert node_input['ConnectorCode'] is None
    assert node_input['DataCloneRecId'] == 0
    assert all(c['RecId'] == 0 for c in node_input['SelectedColumns'])
    assert settings['Sources'][0] == {
        'Id': upstream, 'SourceSide': 'right', 'TargetSide': 'left'}
    connection = settings['Connections'][0]
    assert connection['JoinType'] in ('inner', 'right')
    assert connection['TargetId'] == upstream
    assert connection['SourceId'] in inputs
    assert connection['SourceSide'] == 'left'
    assert connection['TargetSide'] == 'right'
    parts = connection['Conditions'][0]['Parts']
    assert [p['Source'] for p in parts] == [connection['SourceId'], upstream]
    embedded = inputs[connection['SourceId']]
    assert embedded['DataCloneRecId'] > 0
    assert 'RecId' not in embedded
    assert 'DataClones' not in settings


def run():
    reference = json.loads((ROOT / 'reference/nodes/table-merge.json').read_text())
    example = reference['connectedInputExample']
    for join_type in example['observedJoinTypes']:
        settings = copy.deepcopy(example['settings'])
        settings['Connections'][0]['JoinType'] = join_type
        validate(settings)
    for key in ('Id', 'SourceNodeId'):
        broken = copy.deepcopy(example['settings'])
        broken['MergeInputs'][1][key] = 'unresolved-node'
        try:
            validate(broken)
        except (AssertionError, KeyError):
            pass
        else:
            raise AssertionError('Unresolved upstream reference accepted: ' + key)
    assert 'DataClones' in reference['exampleSettings']
    catalog = json.loads((ROOT / 'reference/node-catalog.json').read_text())
    assert next(n for n in catalog if n['code'] == 'table-merge')['observedUpstreamCounts'] == [0, 1]
    print('PASS: inner/right reference relationships, broken-ID checks and legacy preservation (static only)')


if __name__ == '__main__':
    run()
