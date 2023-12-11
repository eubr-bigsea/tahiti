
from tahiti.models import Pipeline
from flask import current_app


def test_pipeline_fail_not_authorized(client):
    tests = [
        lambda: client.get('/pipelines'),
        lambda: client.get('/pipelines/1'),
        lambda: client.patch('/pipelines/1'),
    ]
    for i, test in enumerate(tests):
        rv = test()
        assert 401 == rv.status_code, \
            f'Test {i}: Incorrect status code: {rv.status_code}'
        resp = rv.json
        assert resp['status'] == 'ERROR', f'Test {i}: Incorrect status'
        assert 'Thorn' in resp['message'], f'Test {i}: Incorrect message'


def test_pipeline_list_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    rv = client.get('/pipelines', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['pagination']['total'] == Pipeline.query.count(), \
        f"Wrong quantity: {resp['pagination']['total']}"

    with current_app.app_context():
        pipeline = Pipeline.query.order_by(
            Pipeline.id).first()

        assert resp['data'][0]['id'] == pipeline.id
        assert resp['data'][0]['name'] == pipeline.name
        assert resp['data'][0]['description'] == pipeline.description
        assert resp['data'][0]['enabled'] == pipeline.enabled
        assert resp['data'][0]['user_id'] == pipeline.user_id
        assert resp['data'][0]['user_login'] == pipeline.user_login
        assert resp['data'][0]['user_name'] == pipeline.user_name
        assert resp['data'][0]['created'] == pipeline.created.isoformat()
        assert resp['data'][0]['updated'] == pipeline.updated.isoformat()
        assert resp['data'][0]['version'] == pipeline.version
        assert resp['data'][0]['execution_window'] == pipeline.execution_window
        assert resp['data'][0]['variables'] == pipeline.variables
        assert resp['data'][0]['preferred_cluster_id'] == pipeline.preferred_cluster_id


def test_pipeline_list_all_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'all': 'true'}
    rv = client.get('/pipelines', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_pipeline_list_simple_sucess(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'simple': 'true'}

    rv = client.get('/pipelines', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_pipeline_get_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_id = 1
    rv = client.get(f'/pipelines/{pipeline_id}', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'

    with current_app.app_context():
        pipeline = Pipeline.query.get(1)
        resp = rv.json
        assert resp['data'][0]['id'] == pipeline.id
        assert resp['data'][0]['name'] == pipeline.name
        assert resp['data'][0]['description'] == pipeline.description
        assert resp['data'][0]['enabled'] == pipeline.enabled
        assert resp['data'][0]['user_id'] == pipeline.user_id
        assert resp['data'][0]['user_login'] == pipeline.user_login
        assert resp['data'][0]['user_name'] == pipeline.user_name
        assert resp['data'][0]['created'] == pipeline.created.isoformat()
        assert resp['data'][0]['updated'] == pipeline.updated.isoformat()
        assert resp['data'][0]['version'] == pipeline.version
        assert resp['data'][0]['execution_window'] == pipeline.execution_window
        assert resp['data'][0]['variables'] == pipeline.variables
        assert resp['data'][0]['preferred_cluster_id'] == pipeline.preferred_cluster_id


def test_pipeline_not_found_failure(client):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_id = 999
    rv = client.get(f'/pipelines/{pipeline_id}', headers=headers)
    assert 404 == rv.status_code, f'Incorrect status code: {rv.status_code}'


def test_pipeline_patch_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_id = 2

    update = {'enabled': True}
    rv = client.patch(f'/pipelines/{pipeline_id}',
                      json=update, headers=headers)
    assert rv.status_code == 200

    with app.app_context():
        pipeline = Pipeline.query.get(pipeline_id)
        assert pipeline.enabled


def test_pipeline_patch_set_to_null_failure(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_id = 2

    update = {'enabled': True, 'name': None}
    rv = client.patch(f'/pipelines/{pipeline_id}',
                      json=update, headers=headers)
    assert rv.status_code == 400
    assert 'name' in rv.json['errors']
    assert 'Field may not be null.' in rv.json['errors']['name']


def test_pipeline_delete_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_id = 2

    rv = client.delete(f'/pipelines/{pipeline_id}', headers=headers)
    assert rv.status_code == 204

