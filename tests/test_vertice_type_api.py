
from tahiti.models import VerticeType, db
from flask import current_app


def test_vertice_type_fail_not_authorized(client):
    tests = [
        lambda: client.get('/vertice-types', follow_redirects=True),
        lambda: client.get('/vertice-types/1', follow_redirects=True),
        lambda: client.patch('/vertice-types/1', follow_redirects=True),
    ]
    for i, test in enumerate(tests):
        rv = test()
        assert 401 == rv.status_code, \
            f'Test {i}: Incorrect status code: {rv.status_code}'
        resp = rv.json
        assert resp['status'] == 'ERROR', f'Test {i}: Incorrect status'
        assert 'Thorn' in resp['message'], f'Test {i}: Incorrect message'


def test_vertice_type_list_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    rv = client.get('/vertice-types', headers=headers, follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code' 
    resp = rv.json
    assert resp['pagination']['total'] == VerticeType.query.count(), \
        f"Wrong quantity: {resp['pagination']['total']}"

    with current_app.app_context():
        vertice_type = VerticeType.query.order_by(
            VerticeType.id).first()
        assert resp['data'][0]['id'] == vertice_type.id
        assert resp['data'][0].get('name') == (vertice_type.name)
        assert resp['data'][0].get('description') == (vertice_type.description)
        assert resp['data'][0].get('display_name') == (
            vertice_type.display_name)
        assert resp['data'][0].get('namespace') == (vertice_type.namespace)
        assert resp['data'][0].get('small_icon') == (vertice_type.small_icon)
        assert resp['data'][0].get('icon') == (vertice_type.icon)
        assert resp['data'][0].get('large_icon') == (vertice_type.large_icon)
        assert resp['data'][0].get('display_property') == (
            vertice_type.display_property)
        assert resp['data'][0].get('plural') == (vertice_type.plural)
        assert resp['data'][0].get('category') == (vertice_type.category)
        assert resp['data'][0].get('enabled') == (vertice_type.enabled)
        assert resp['data'][0].get('user_id') == (vertice_type.user_id)
        assert resp['data'][0].get('user_login') == (vertice_type.user_login)
        assert resp['data'][0].get('user_name') == (vertice_type.user_name)
        assert resp['data'][0].get('created') == (
            vertice_type.created.isoformat() if vertice_type.created else None)
        assert resp['data'][0].get('updated') == (
            vertice_type.updated.isoformat() if vertice_type.updated else None)


def test_vertice_type_list_all_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'all': 'true'}
    rv = client.get('/vertice-types', headers=headers, query_string=params,
                    follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_vertice_type_list_simple_sucess(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'simple': 'true'}

    rv = client.get('/vertice-types', headers=headers, query_string=params,
                    follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code'


def test_vertice_type_get_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    vertice_type_id = 1
    rv = client.get(f'/vertice-types/{vertice_type_id}',
                    headers=headers, follow_redirects=True)
    assert 200 == rv.status_code, 'Incorrect status code'

    with current_app.app_context():
        vertice_type = db.session.get(VerticeType, 1)
        resp = rv.json
        assert resp['data'][0]['id'] == vertice_type.id
        assert resp['data'][0].get('name') == (vertice_type.name)
        assert resp['data'][0].get('description') == (vertice_type.description)
        assert resp['data'][0].get('display_name') == (
            vertice_type.display_name)
        assert resp['data'][0].get('namespace') == (vertice_type.namespace)
        assert resp['data'][0].get('small_icon') == (vertice_type.small_icon)
        assert resp['data'][0].get('icon') == (vertice_type.icon)
        assert resp['data'][0].get('large_icon') == (vertice_type.large_icon)
        assert resp['data'][0].get('display_property') == (
            vertice_type.display_property)
        assert resp['data'][0].get('plural') == (vertice_type.plural)
        assert resp['data'][0].get('category') == (vertice_type.category)
        assert resp['data'][0].get('enabled') == (vertice_type.enabled)
        assert resp['data'][0].get('user_id') == (vertice_type.user_id)
        assert resp['data'][0].get('user_login') == (vertice_type.user_login)
        assert resp['data'][0].get('user_name') == (vertice_type.user_name)
        assert resp['data'][0].get('created') == (
            vertice_type.created.isoformat() if vertice_type.created else None)
        assert resp['data'][0].get('updated') == (
            vertice_type.updated.isoformat() if vertice_type.updated else None)


def test_vertice_type_not_found_failure(client):
    headers = {'X-Auth-Token': str(client.secret)}
    vertice_type_id = 999
    rv = client.get(f'/vertice-types/{vertice_type_id}',
                    headers=headers, follow_redirects=True)
    assert 404 == rv.status_code, f'Incorrect status code: {rv.status_code}'


def test_vertice_type_patch_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    vertice_type_id = 2
    update = {'name': 'Updated value'}
    rv = client.patch(f'/vertice-types/{vertice_type_id}',
                      json=update, headers=headers)
    assert rv.status_code == 200

    with app.app_context():
        vertice_type = db.session.get(VerticeType, vertice_type_id)
        assert vertice_type.name == 'Updated value'


def test_vertice_type_patch_set_to_null_failure(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    vertice_type_id = 2

    required_attribute = 'name'
    update = {required_attribute: None}
    rv = client.patch(f'/vertice-types/{vertice_type_id}',
                      json=update, headers=headers)
    assert rv.status_code == 400
    assert required_attribute in rv.json['errors']
    assert 'Field may not be null.' in rv.json['errors'][required_attribute]


def test_vertice_type_delete_success(client, app):
    headers = {'X-Auth-Token': str(client.secret)}
    vertice_type_id = 2

    rv = client.delete(f'/vertice-types/{vertice_type_id}', headers=headers)
    assert rv.status_code == 204

