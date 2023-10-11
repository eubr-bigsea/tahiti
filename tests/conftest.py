import os
import sys

import flask_migrate
import pytest

from tahiti.app import create_app
from tahiti.models import Platform, db

sys.path.append(os.path.dirname(os.path.curdir))

TESTDB = 'test.db'
TESTDB_PATH = "{}/{}".format(os.path.dirname(__file__), TESTDB)
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH
TEST_TOKEN = 'T0K3N_T35T'


def _get_platforms():
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
    # path = os.path.dirname(os.path.abspath(__name__))
    # import pdb; pdb.set_trace()
    with app.test_client() as client:
        with app.test_request_context():
            # flask_migrate.downgrade(revision="base")
            ##if os.path.exists(os.path.join(path, 'test.db')):
            ##    os.remove(os.path.join(path, 'test.db'))
            flask_migrate.upgrade(revision='head')
            db.session.commit()
        client.secret = app.config['TAHITI_CONFIG']['secret']
        yield client

