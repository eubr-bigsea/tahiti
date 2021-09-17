# -*- coding: utf-8 -*-
from tahiti.models import *
from flask import current_app


def test_platform_fail_not_authorized(client):
    tests = [
        lambda: client.get('/platforms'),
        lambda: client.get('/platforms/1'),
        lambda: client.patch('/platforms/1'),
    ]
    for i, test in enumerate(tests):
        rv = test()
        assert 401 == rv.status_code, \
            f'Test {i}: Incorrect status code: {rv.status_code}'
        resp = rv.json
        assert resp['status'] == 'ERROR', f'Test {i}: Incorrect status'
        assert 'Thorn' in resp['message'], f'Test {i}: Incorrect message'


def test_platform_list_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    rv = client.get('/platforms', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['pagination']['total'] == 4, \
        f"Wrong quantity: {resp['pagination']['total']}"

    with current_app.app_context():
        default_platform = Platform.query.join(
            db.aliased(Platform.current_translation, 
                name='platform_translation')).order_by(
            PlatformTranslation.name).first()

        assert resp['data'][0]['id'] == default_platform.id
        assert resp['data'][0]['slug'] == default_platform.slug
        assert resp['data'][0]['name'] == default_platform.name
        assert resp['data'][0]['enabled'] == default_platform.enabled
    

def test_platform_list_simple_sucess(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'simple': 'true'}

    rv = client.get('/platforms', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['pagination']['total'] == 4, \
        f"Wrong quantity: {resp['pagination']['total']}"
    assert set(resp['data'][0].keys()) == {'id', 'name', 'slug'}


def test_platform_list_no_page_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'page': 'false'}

    rv = client.get('/platforms', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert 'pagination' not in resp
    assert len(resp['data']) == 4


def test_platform_get_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    platform_id = 1
    rv = client.get(f'/platforms/{platform_id}', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'

    with current_app.app_context():
        default_platform = Platform.query.get(1)
        resp = rv.json
        assert resp['data'][0]['id'] == default_platform.id
        assert resp['data'][0]['slug'] == default_platform.slug
        assert resp['data'][0]['name'] == default_platform.name
        assert resp['data'][0]['enabled'] == default_platform.enabled


def test_platform_fail_not_found_error(client):
    headers = {'X-Auth-Token': str(client.secret)}
    platform_id = 999
    rv = client.get(f'/platforms/{platform_id}', headers=headers)
    assert 404 == rv.status_code, f'Incorrect status code: {rv.status_code}'


def test_platform_patch_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    platform_id = 2

    update = {'enabled': True}
    rv = client.patch(f'/platforms/{platform_id}',
                      json=update, headers=headers)
    assert rv.status_code == 200

    with app.app_context():
        platform = Platform.query.get(platform_id)
        assert platform.enabled == True
