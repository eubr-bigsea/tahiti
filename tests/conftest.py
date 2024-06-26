import datetime
import os
import sys

import flask_migrate
import pytest

from tahiti.app import create_app
from tahiti.models import (PipelineStep, PipelineTemplate, PipelineTemplateStep, Platform, SourceCode, Task, Workflow, db,
                           WorkflowType, Pipeline, VerticeType, VerticeTypeProperty)

sys.path.append(os.path.dirname(os.path.curdir))

TESTDB = "test.db"
TESTDB_PATH = "{}/{}".format(os.path.dirname(__file__), TESTDB)
TEST_DATABASE_URI = "sqlite:///" + TESTDB_PATH
TEST_TOKEN = "T0K3N_T35T"


def _get_workflows():
    return [
        {
            "id": 1,
            "name": "Workflow to test ops",
            "user_id": 1,
            "user_login": "test@lemonade.org.br",
            "user_name": "Tester",
            "platform_id": 1,
            "tasks": [
                Task(
                    id="aaaa",
                    operation_id=7,
                    left=0,
                    top=0,
                    display_order=0,
                    z_index=0,
                    forms="{}",
                ),
                Task(
                    id="bbb",
                    operation_id=17,
                    left=0,
                    top=0,
                    display_order=0,
                    z_index=0,
                    forms="{}",
                ),
                Task(
                    id="cccc",
                    operation_id=27,
                    left=0,
                    top=0,
                    display_order=0,
                    z_index=0,
                    forms="{}",
                ),
                Task(
                    id="dddd",
                    operation_id=37,
                    left=0,
                    top=0,
                    display_order=0,
                    z_index=0,
                    forms="{}",
                ),
            ],
        }
    ]


def _get_platforms() -> list:
    return [
        Platform(name="Default", slug="default", icon="", enabled=True),
        Platform(name="File Platform", slug="file", icon="", enabled=True),
        Platform(name="Dummy Platform", slug="dummy", icon="", enabled=True),
        Platform(name="SQL Platform", slug="sql", icon="", enabled=True),
    ]


def _get_source_codes() -> list:
    return [
        dict(
            id=1,
            name="Test source code",
            enabled=True,
            suspicious=False,
            requirements="None",
            imports="import jinja2",
            help="Test code",
            code="ctx = {}",
        ),
        dict(
            id=2,
            name="Test source code 2",
            enabled=True,
            suspicious=True,
            requirements="None",
            imports="import numpy as np",
            help="Test code",
            code="ctx = {}",
        )
    ]
def _get_pipeline_templates() -> list:
    return [
        {
            'id': 1,
            'name': 'Pipeline template test #1',
            'description': 'Pipeline template used in tests',
            'enabled': True,
            'steps': [
                PipelineTemplateStep(**{
                    'id': 1,
                    'name': 'First stage',
                    'order': 1,
                    'description': 'Stage',
                    'enabled': True,
                }),
                PipelineTemplateStep(**{
                    'id': 3,
                    'name': 'Second stage',
                    'order': 2,
                    'description': 'Stage',
                    'enabled': True,
                })
            ]
        },
        {
            'id': 2,
            'name': 'Pipeline template test #2',
            'description': 'Pipeline used in tests',
            'enabled': True,
            'steps': [
                PipelineTemplateStep(**{
                    'id': 2,
                    'name': 'First stage',
                    'order': 1,
                    'description': 'Stage',
                    'enabled': True,
                })
            ]
        },
    ]
def _get_vertice_types() -> list:
    return [
        {
            'id': 1,
            'name': 'Person',
            'description': 'Person',
            'enabled': True,
            'user_id': 1,
            'user_login': 'admin',
            'user_name': 'Admin',
            'created': datetime.datetime.now(),
            'updated': datetime.datetime.now(),
            'display_name': 'Person',
            'plural': 'People',
            'category': 'Human',
            'icon': 'people.png',
            'small_icon': 'people.png',
            'large_icon': 'people.png',
            'parent_id': None,
            'properties': [
                VerticeTypeProperty(**{
                    'id': 1,
                    'name': 'name',
                    'order': 1,
                    'display_name': 'Name',
                    'description': 'Name',
                    'data_type': 'String'
                }),
                VerticeTypeProperty(**{
                    'id': 3,
                    'name': 'age',
                    'display_name': 'Age',
                    'order': 2,
                    'description': 'Age',
                    'data_type': 'integer',
                })
            ]
        },
        {
            'id': 3,
            'name': 'Driver',
            'description': 'Driver',
            'enabled': True,
            'user_id': 1,
            'user_login': 'admin',
            'user_name': 'Admin',
            'created': datetime.datetime.now(),
            'updated': datetime.datetime.now(),
            'display_name': 'Driver',
            'plural': 'Drivers',
            'category': 'Human',
            'icon': 'people.png',
            'small_icon': 'people.png',
            'large_icon': 'people.png',
            'parent_id': 1,
            'properties': [
                VerticeTypeProperty(**{
                    'id': 10,
                    'name': 'license',
                    'order': 1,
                    'display_name': 'license',
                    'description': 'license',
                    'data_type': 'String'
                }),
                VerticeTypeProperty(**{
                    'id': 11,
                    'name': 'plate',
                    'display_name': 'Plate',
                    'order': 2,
                    'data_type': 'string',
                    'description': 'Plate number',
                })
            ]
        }
   ]

def _get_pipelines() -> list:
    return [
        {
            'id': 1,
            'name': 'Pipeline test #1',
            'description': 'Pipeline used in tests',
            'enabled': True,
            'user_id': 1,
            'user_login': 'admin',
            'user_name': 'Admin',
            'created': datetime.datetime.now(),
            'updated': datetime.datetime.now(),
            'version': 1,
            'execution_window': 30,
            'variables': '',
            'preferred_cluster_id': 1,
            'steps': [
                PipelineStep(**{
                    'id': 1,
                    'name': 'First stage',
                    'order': 1,
                    'scheduling': '{}',
                    'description': 'Stage',
                    'enabled': True,
                    'workflow_type': WorkflowType.WORKFLOW,
                    'workflow_id': 1,
                }),
                PipelineStep(**{
                    'id': 3,
                    'name': 'Second stage',
                    'order': 2,
                    'scheduling': '{}',
                    'description': 'Stage',
                    'enabled': True,
                    'workflow_type': WorkflowType.WORKFLOW,
                    'workflow_id': 1,
                })
            ]
        },
        {
            'id': 2,
            'name': 'Pipeline test #1',
            'description': 'Pipeline used in tests',
            'enabled': True,
            'user_id': 1,
            'user_login': 'admin',
            'user_name': 'Admin',
            'created': datetime.datetime.now(),
            'updated': datetime.datetime.now(),
            'version': 1,
            'steps': [
                PipelineStep(**{
                    'id': 2,
                    'name': 'First stage',
                    'order': 1,
                    'scheduling': '{}',
                    'description': 'Stage',
                    'enabled': True,
                    'workflow_type': WorkflowType.WORKFLOW,
                    'workflow_id': 1,
                })
            ]
        },
    ]

@pytest.fixture(scope="session")
def app():
    path = os.path.dirname(os.path.abspath(__name__))
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{path}/test.db"
    app.config["TESTING"] = True
    app.config["GATEWAY_PORT"] = 18001
    app.debug = False
    yield app


# noinspection PyShadowingNames


@pytest.fixture(scope="session")
def client(app):
    path = os.path.dirname(os.path.abspath(__name__))
    # import pdb; pdb.set_trace()
    with app.test_client() as client:
        with app.test_request_context():
            # flask_migrate.downgrade(revision="base")

            if os.path.exists(os.path.join(path, "test.db")):
                os.remove(os.path.join(path, "test.db"))
            flask_migrate.upgrade(revision="head")
            for wf in _get_workflows():
                db.session.add(Workflow(**wf))
            for sc in _get_source_codes():
                db.session.add(SourceCode(**sc))
            for pipe in _get_pipelines():
                db.session.add(Pipeline(**pipe))
            for pipe in _get_pipeline_templates():
                db.session.add(PipelineTemplate(**pipe))

            for vt in _get_vertice_types():
                db.session.add(VerticeType(**vt))
            db.create_all()
            db.session.commit()
        client.secret = app.config["TAHITI_CONFIG"]["secret"]
        yield client
