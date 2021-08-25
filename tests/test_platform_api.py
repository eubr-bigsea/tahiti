# -*- coding: utf-8 -*-
from tahiti.models import *
from flask import current_app


def test_platform_fail_not_authorized(client):
    tests = [
        lambda: client.get('/platforms'),
        lambda: client.post('/platforms'),
        lambda: client.get('/platforms/1'),
        lambda: client.patch('/platforms/1'),
        lambda: client.delete('/platforms/1'),
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
    assert resp['pagination']['total'] == 5, 'Wrong quantity'

    with current_app.app_context():
        default_platform = Platform.query.order_by(Platform.name).first()

    assert resp['data'][0]['id'] == default_platform.id
    assert resp['data'][0]['type'] == default_platform.type
    assert resp['data'][0]['url'] == default_platform.url
    assert resp['data'][0]['name'] == default_platform.name
    assert resp['data'][0]['enabled'] == default_platform.enabled


def test_platform_list_with_parameters_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'enabled': 'true', 'fields': 'id,name',
              'asc': 'false', 'query': 'platform', 'sort': 'created'}

    rv = client.get('/platforms', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['pagination']['total'] == 3, 'Wrong quantity'


def test_platform_list_no_page_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'page': 'false'}

    rv = client.get('/platforms', headers=headers, query_string=params)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert len(resp['data']) == 5, 'Wrong quantity'


def test_platform_post_missing_data(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {}

    rv = client.post('/platforms', headers=headers, json=params)
    assert 400 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert resp['status'] == 'ERROR', 'Wrong status'


def test_platform_post_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'url': 'hdfs://server-hdfs/test',
              'name': 'Test platform', 'type': 'HDFS'}

    rv = client.post('/platforms', headers=headers, json=params)
    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    # assert resp['status'] == 'OK', 'Wrong status'


def test_platform_get_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    platform_id = 1
    rv = client.get(f'/platforms/{platform_id}', headers=headers)
    assert 200 == rv.status_code, 'Incorrect status code'

    with current_app.app_context():
        default_platform = Platform.query.get(1)
    resp = rv.json
    assert resp['data'][0]['id'] == default_platform.id
    assert resp['data'][0]['type'] == default_platform.type
    assert resp['data'][0]['url'] == default_platform.url
    assert resp['data'][0]['name'] == default_platform.name
    assert resp['data'][0]['enabled'] == default_platform.enabled


def test_platform_fail_not_found_error(client):
    headers = {'X-Auth-Token': str(client.secret)}
    platform_id = 999
    rv = client.get(f'/platforms/{platform_id}', headers=headers)
    assert 404 == rv.status_code, f'Incorrect status code: {rv.status_code}'


def test_platform_delete_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    platform_id = 9999

    rv = client.get(f'/platforms/{platform_id}', headers=headers)
    assert rv.status_code == 404

    with current_app.app_context():
        platform = Platform(
            id=platform_id, url='file:///tmp', type='HDFS', name='Deleted')
        db.session.add(platform)
        db.session.commit()

    rv = client.delete(f'/platforms/{platform_id}', headers=headers)
    assert 204 == rv.status_code, f'Incorrect status code: {rv.status_code}'

    with current_app.app_context():
        platform = Platform.query.get(platform_id)
        assert not platform.enabled

def test_platform_patch_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    platform_id = 8888

    with app.app_context():
        platform = Platform(
            id=platform_id, url='file:///tmp', type='HDFS', name='Updated')
        db.session.add(platform)
        db.session.commit()

    update = {'url': 'hdfs://teste.com', 'name': 'Fixed'}
    rv = client.patch(f'/platforms/{platform_id}', json=update, headers=headers)
    assert rv.status_code == 200

    with app.app_context():
        platform = Platform.query.get(platform_id)
        assert platform.name == update['name']
        assert platform.url == update['url']
