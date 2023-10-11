import os
import sys

import flask_migrate
import pytest

from tahiti.app import create_app
from tahiti.models import Platform, Task, Workflow, db

sys.path.append(os.path.dirname(os.path.curdir))

TESTDB = 'test.db'
TESTDB_PATH = "{}/{}".format(os.path.dirname(__file__), TESTDB)
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH
TEST_TOKEN = 'T0K3N_T35T'


def _get_workflows():
    return [
        {
            'id': 1, 'name': 'Workflow to test ops',
            'user_id': 1, 'user_login': 'test@lemonade.org.br',
            'user_name': 'Tester',
            'platform_id': 1,
            'tasks': [
                Task(id='aaaa', operation_id=7, left=0, top=0, display_order=0,
                    z_index=0, forms='{}'),
                Task(id='bbb', operation_id=17, left=0, top=0, display_order=0,
                    z_index=0, forms='{}'),
                Task(id='cccc', operation_id=27, left=0, top=0, display_order=0,
                    z_index=0, forms='{}'),
                Task(id='dddd', operation_id=37, left=0, top=0, display_order=0,
                    z_index=0, forms='{}'),
            ]
        }
    ]

def _get_platforms() -> list:
    return [
        Platform(name='Default', slug='default',
                icon='', enabled=True),
        Platform(name='File Platform', slug='file',
                icon='', enabled=True),
        Platform(name='Dummy Platform', slug='dummy',
                icon='', enabled=True),
        Platform(name='SQL Platform', slug='sql',
                icon='', enabled=True),
    ]



@pytest.fixture(scope='session')
def app():
    path = os.path.dirname(os.path.abspath(__name__))
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}/test.db'
    app.config['TESTING'] = True
    app.config['GATEWAY_PORT'] = 18001
    app.debug = False
    yield app

# noinspection PyShadowingNames


@pytest.fixture(scope='session')
def client(app):
    path = os.path.dirname(os.path.abspath(__name__))
    # import pdb; pdb.set_trace()
    with app.test_client() as client:
        with app.test_request_context():
            # flask_migrate.downgrade(revision="base")
            if os.path.exists(os.path.join(path, 'test.db')):
                os.remove(os.path.join(path, 'test.db'))
            flask_migrate.upgrade(revision='head')
            for wf in _get_workflows():
                db.session.add(Workflow(**wf))
            db.session.commit()
        client.secret = app.config['TAHITI_CONFIG']['secret']
        yield client

