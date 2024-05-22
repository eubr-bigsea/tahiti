
from tahiti.models import SourceCode, db
from flask import current_app


def test_source_code_fail_not_authorized(client):
    tests = [
        lambda: client.get('/source-codes', follow_redirects=True),
        lambda: client.get('/source-codes/1', follow_redirects=True),
        lambda: client.patch('/source-codes/1', follow_redirects=True),
    ]
    for i, test in enumerate(tests):
        rv = test()
        assert 401 == rv.status_code, \
            f'Test {i}: Incorrect status code: {rv.status_code}'
        resp = rv.json
        assert resp['status'] == 'ERROR', f'Test {i}: Incorrect status'
        assert 'Thorn' in resp['message'], f'Test {i}: Incorrect message'


def test_source_code_list_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    rv = client.get('/source-codes', headers=headers, follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['pagination']['total'] == SourceCode.query.count(), \
        f"Wrong quantity: {resp['pagination']['total']}"

    with current_app.app_context():
        source_code = SourceCode.query.order_by(
            SourceCode.id).first()
        assert resp['data'][0]['id'] == source_code.id
        assert resp['data'][0].get('name') == (source_code.name)
        assert resp['data'][0].get('enabled') == (source_code.enabled)
        assert resp['data'][0].get('suspicious') == (source_code.suspicious)
        assert resp['data'][0].get('requirements') == (
            source_code.requirements)
        assert resp['data'][0].get('imports') == (source_code.imports)
        assert resp['data'][0].get('help') == (source_code.help)
        assert resp['data'][0].get('code') == (source_code.code)


def test_source_code_list_all_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'all': 'true'}
    rv = client.get('/source-codes', headers=headers, query_string=params,
                    follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_source_code_list_simple_sucess(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'simple': 'true'}

    rv = client.get('/source-codes', headers=headers, query_string=params,
                    follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_source_code_get_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 1
    rv = client.get(f'/source-codes/{source_code_id}',
                    headers=headers, follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code'

    with current_app.app_context():
        source_code = db.session.get(SourceCode, 1)
        resp = rv.json
        assert resp['data'][0]['id'] == source_code.id
        assert resp['data'][0].get('name') == (source_code.name)
        assert resp['data'][0].get('enabled') == (source_code.enabled)
        assert resp['data'][0].get('suspicious') == (source_code.suspicious)
        assert resp['data'][0].get('requirements') == (
            source_code.requirements)
        assert resp['data'][0].get('imports') == (source_code.imports)
        assert resp['data'][0].get('help') == (source_code.help)
        assert resp['data'][0].get('code') == (source_code.code)


def test_source_code_not_found_failure(client):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 999
    rv = client.get(f'/source-codes/{source_code_id}',
                    headers=headers, follow_redirects=True)
    assert 404 == rv.status_code, f'Incorrect status code: {rv.status_code}'


def test_source_code_patch_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 2
    update = {'name': 'Updated value'}
    rv = client.patch(f'/source-codes/{source_code_id}',
                      json=update, headers=headers)
    assert rv.status_code == 200

    with app.app_context():
        source_code = db.session.get(SourceCode, source_code_id)
        assert source_code.name == 'Updated value'


def test_source_code_patch_set_to_null_failure(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 2

    required_attribute = 'name'
    update = {required_attribute: None}
    rv = client.patch(f'/source-codes/{source_code_id}',
                      json=update, headers=headers)
    assert rv.status_code == 400
    assert required_attribute in rv.json['errors']
    assert 'Field may not be null.' in rv.json['errors'][required_attribute]


def test_source_code_delete_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 2

    rv = client.delete(f'/source-codes/{source_code_id}', headers=headers)
    assert rv.status_code == 204

