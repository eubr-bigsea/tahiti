import logging

import sqlalchemy_utils
import os
from flask import Flask
from flask_admin import Admin
from flask_babel import Babel
from flask_babel import get_locale
from flask_caching import Cache
from flask_cors import CORS
from flask_restful import Api

from tahiti.admin import OperationModelView, OperationCategoryModelView
from tahiti.application_api import ApplicationListApi, ApplicationDetailApi
from tahiti.models import db, Operation, OperationCategory
from tahiti.operation_api import OperationDetailApi
from tahiti.operation_api import OperationListApi
from tahiti.platform_api import PlatformListApi, PlatformDetailApi
from tahiti.workflow_api import WorkflowDetailApi
from tahiti.workflow_api import WorkflowListApi

def create_app(settings_override=None, log_level=logging.DEBUG, config_file=''):
    if config_file:
        os.environ['TAHITI_CONFIG'] = config_file

    from tahiti.configuration import tahiti_configuration

    app = Flask(__name__, static_url_path='')
    sqlalchemy_utils.i18n.get_locale = get_locale

    app.config["RESTFUL_JSON"] = {
        'cls': app.json_encoder,
        'sort_keys': False,
    }
    app.secret_key = 'l3m0n4d1'
    config = tahiti_configuration
    app.config['TAHITI_CONFIG'] = config['tahiti']

    server_config = config['tahiti'].get('servers', {})
    app.config['SQLALCHEMY_DATABASE_URI'] = server_config.get('database_url')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update(config.get('config', {}))
    app.debug = config['tahiti'].get('debug', False)

    if settings_override:
        app.config.update(settings_override)

    db.init_app(app)

    # Flask Admin
    admin = Admin(app, name='Stand', template_mode='bootstrap3')

    # Logging configuration
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(log_level)
    logging.getLogger('werkzeug').setLevel(log_level)

    # CORS configuration
    CORS(app, resources={r"/*": {"origins": "*"}})

    # API configuration
    api = Api(app)
    mappings = {
        '/applications': ApplicationListApi,
        '/applications/<int:application_id>': ApplicationDetailApi,
        '/operations': OperationListApi,
        '/operations/<int:operation_id>': OperationDetailApi,
        '/platforms': PlatformListApi,
        '/platforms/<int:platform_id>': PlatformDetailApi,
        '/workflows': WorkflowListApi,
        '/workflows/<int:workflow_id>': WorkflowDetailApi,
    }
    for path, view in mappings.iteritems():
        api.add_resource(view, path)

    # Cache configuration for API
    app.config['CACHE_TYPE'] = 'simple'
    cache = Cache(config={'CACHE_TYPE': 'simple'})
    cache.init_app(app)

    if config.get('environment', 'dev') == 'dev':
        admin.add_view(OperationModelView(Operation, db.session))
        admin.add_view(OperationCategoryModelView(OperationCategory, db.session))

    return app


def create_babel_i18n(_app):
    """ i18n configuration
    :param _app: Flask app
    :return: Babel configuration
    """
    return Babel(_app)
