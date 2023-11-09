
import pytest
from tahiti.models import SourceCode
from flask import current_app
from tahiti.factory import create_app


def test_source_code_fail_not_authorized(client):
    tests = [
        lambda: client.get('/source_codes'),
        lambda: client.get('/source_codes/1'),
        lambda: client.patch('/source_codes/1'),
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
    rv = client.get('/source_codes', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['pagination']['total'] == SourceCode.query.count(), \
        f"Wrong quantity: {resp['pagination']['total']}"

    with current_app.app_context():
        source_code = SourceCode.query.order_by(
            SourceCode.id).first()

        assert resp['data'][0]['id'] == source_code.id
        assert resp['data'][0]['name'] == source_code.name
        assert resp['data'][0]['enabled'] == source_code.enabled
        assert resp['data'][0]['suspicious'] == source_code.suspicious
        assert resp['data'][0]['requirements'] == source_code.requirements
        assert resp['data'][0]['imports'] == source_code.imports
        assert resp['data'][0]['help'] == source_code.help
        assert resp['data'][0]['code'] == source_code.code


def test_source_code_list_all_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'all': 'true'}
    rv = client.get('/source_codes', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_source_code_list_simple_sucess(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'simple': 'true'}

    rv = client.get('/source_codes', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_source_code_get_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 1
    rv = client.get(f'/source_codes/{source_code_id}', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'

    with current_app.app_context():
        source_code = SourceCode.query.get(1)
        resp = rv.json
        assert resp['data'][0]['id'] == source_code.id
        assert resp['data'][0]['name'] == source_code.name
        assert resp['data'][0]['enabled'] == source_code.enabled
        assert resp['data'][0]['suspicious'] == source_code.suspicious
        assert resp['data'][0]['requirements'] == source_code.requirements
        assert resp['data'][0]['imports'] == source_code.imports
        assert resp['data'][0]['help'] == source_code.help
        assert resp['data'][0]['code'] == source_code.code


def test_source_code_not_found_failure(client):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 999
    rv = client.get(f'/source_codes/{source_code_id}', headers=headers)
    assert 404 == rv.status_code, f'Incorrect status code: {rv.status_code}'


def test_source_code_patch_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 2

    update = {'enabled': True}
    rv = client.patch(f'/source_codes/{source_code_id}',
                      json=update, headers=headers)
    assert rv.status_code == 200

    with app.app_context():
        source_code = SourceCode.query.get(source_code_id)
        assert source_code.enabled


def test_source_code_patch_set_to_null_failure(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 2

    update = {'enabled': True, 'name': None}
    rv = client.patch(f'/source_codes/{source_code_id}',
                      json=update, headers=headers)
    assert rv.status_code == 400
    assert 'name' in rv.json['errors']
    assert 'Field may not be null.' in rv.json['errors']['name']


def test_source_code_delete_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    source_code_id = 2

    rv = client.delete(f'/source_codes/{source_code_id}', headers=headers)
    assert rv.status_code == 204

