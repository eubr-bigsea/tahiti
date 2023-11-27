
from tahiti.models import PipelineTemplate
from flask import current_app


def test_pipeline_template_fail_not_authorized(client):
    tests = [
        lambda: client.get('/pipeline-templates'),
        lambda: client.get('/pipeline-templates/1'),
        lambda: client.patch('/pipeline-templates/1'),
    ]
    for i, test in enumerate(tests):
        rv = test()
        assert 401 == rv.status_code, \
            f'Test {i}: Incorrect status code: {rv.status_code}'
        resp = rv.json
        assert resp['status'] == 'ERROR', f'Test {i}: Incorrect status'
        assert 'Thorn' in resp['message'], f'Test {i}: Incorrect message'


def test_pipeline_template_list_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    rv = client.get('/pipeline-templates', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['pagination']['total'] == PipelineTemplate.query.count(), \
        f"Wrong quantity: {resp['pagination']['total']}"

    with current_app.app_context():
        pipeline_template = PipelineTemplate.query.order_by(
            PipelineTemplate.id).first()

        assert resp['data'][0]['id'] == pipeline_template.id
        assert resp['data'][0]['name'] == pipeline_template.name
        assert resp['data'][0]['description'] == pipeline_template.description
        assert resp['data'][0]['enabled'] == pipeline_template.enabled


def test_pipeline_template_list_all_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'all': 'true'}
    rv = client.get(
        '/pipeline-templates',
        headers=headers,
        query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_pipeline_template_list_simple_sucess(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'simple': 'true'}

    rv = client.get(
        '/pipeline-templates',
        headers=headers,
        query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_pipeline_template_get_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_template_id = 1
    rv = client.get(
        f'/pipeline-templates/{pipeline_template_id}',
        headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'

    with current_app.app_context():
        pipeline_template = PipelineTemplate.query.get(1)
        resp = rv.json
        assert resp['data'][0]['id'] == pipeline_template.id
        assert resp['data'][0]['name'] == pipeline_template.name
        assert resp['data'][0]['description'] == pipeline_template.description
        assert resp['data'][0]['enabled'] == pipeline_template.enabled


def test_pipeline_template_not_found_failure(client):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_template_id = 999
    rv = client.get(
        f'/pipeline-templates/{pipeline_template_id}',
        headers=headers)
    assert 404 == rv.status_code, f'Incorrect status code: {rv.status_code}'


def test_pipeline_template_patch_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_template_id = 2

    update = {'enabled': True}
    rv = client.patch(f'/pipeline-templates/{pipeline_template_id}',
                      json=update, headers=headers)
    assert rv.status_code == 200

    with app.app_context():
        pipeline_template = PipelineTemplate.query.get(pipeline_template_id)
        assert pipeline_template.enabled


def test_pipeline_template_patch_set_to_null_failure(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_template_id = 2

    update = {'enabled': True, 'name': None}
    rv = client.patch(f'/pipeline-templates/{pipeline_template_id}',
                      json=update, headers=headers)
    assert rv.status_code == 400
    assert 'name' in rv.json['errors']
    assert 'Field may not be null.' in rv.json['errors']['name']


def test_pipeline_template_delete_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    pipeline_template_id = 2

    rv = client.delete(
        f'/pipeline-templates/{pipeline_template_id}',
        headers=headers)
    assert rv.status_code == 204

