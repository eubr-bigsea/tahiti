# -*- coding: utf-8 -*-
from sqlalchemy.orm import joinedload
from tahiti.models import *
from flask import current_app


def test_list_operations_simple_data_success(client):
    headers = {'X-Auth-Token': str(client.secret)}
    params = {'simple': 'true'}
    rv = client.get('/operations', headers=headers, query_string=params)

    assert 200 == rv.status_code, 'Incorrect status code'
    resp = rv.json
    assert set(resp['data'][0].keys()) == {'id', 'name', 'slug'}

    with current_app.app_context():
        current_translation = db.aliased(Operation.current_translation)
        total = Operation.query.join(current_translation).filter(
            Operation.enabled,
            Operation.platforms.any(enabled=True),
            OperationTranslation.locale == 'en',).with_entities(
                Operation.id,
                OperationTranslation.name,
            Operation.slug)
        ops1 = list(total)
        ops2 = [tuple(x.values()) for x in resp['data']]
        assert set(ops1) == set(ops2)


def test_list_operations_per_platform_success(client):
    platforms = [4, 1, 5, ]
    headers = {'X-Auth-Token': str(client.secret)}
    for platform in platforms:
        params = {'platform': platform}
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
    pass


def test_list_operations_filtered_name_success(client):
    pass
