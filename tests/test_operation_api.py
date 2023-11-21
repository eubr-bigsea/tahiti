import pytest
from tahiti.models import Operation, OperationTranslation, Platform, Workflow, db
from flask import current_app


@pytest.mark.parametrize('platform', [1, 4, 5, 10000])
def test_list_operations_per_platform_success(client, platform):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'platform': platform, 'simple': 'true'}
    rv = client.get('/operations', headers=headers, query_string=params)

    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json

    with current_app.app_context():
        current_translation = db.aliased(Operation.current_translation)
        total = Operation.query.join(Operation.platforms).join(
            current_translation).filter(
            Operation.enabled,
            Platform.id == platform,
            Operation.platforms.any(enabled=True),
            OperationTranslation.locale == 'en',)
        ops1 = [op.id for op in total]
        ops2 = [op['id'] for op in resp['data']]
        assert set(ops1) == set(ops2)

def test_list_operations_filtered_disabled_success(client):
    pass


def test_list_operations_filtered_subset_success(client):
    pass


def test_list_operations_filtered_workflow_success(client):
    workflow_id = 1
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'workflow': workflow_id, 'simple': 'true'}
    rv = client.get('/operations', headers=headers, query_string=params)

    with current_app.app_context():
        wf = Workflow.query.get(workflow_id)
        ops1 = [t.operation.id for t in wf.tasks]
    
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json

    ops2 = [op['id'] for op in resp['data']]
    assert set(ops1) == set(ops2)


def test_list_operations_filtered_name_success(client):
    pass
