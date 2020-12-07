import logging
import logging.config
import os

import jinja2
import sqlalchemy_utils
from flask import Flask
from flask_babel import Babel
from flask_babel import get_locale
from flask_cors import CORS
from flask_restful import Api

from tahiti.application_api import ApplicationListApi, ApplicationDetailApi
from tahiti.cache import cache
from tahiti.models import db, Operation, OperationCategory
from tahiti.operation_api import OperationDetailApi, OperationClearCacheApi
from tahiti.operation_api import OperationListApi, OperationTreeApi
from tahiti.operation_subset_api import OperationSubsetDetailApi, \
        OperationSubsetListApi, OperationSubsetOperationApi
from tahiti.platform_api import PlatformListApi, PlatformDetailApi
from tahiti.views import AttributeSuggestionView
from tahiti.workflow_api import WorkflowDetailApi, WorkflowImportApi, \
    WorkflowAddFromTemplateApi, WorkflowPermissionApi
from tahiti.workflow_api import WorkflowListApi, WorkflowHistoryApi


def create_app(settings_override=None, log_level=logging.DEBUG, config_file=''):
    if config_file:
        os.environ['TAHITI_CONFIG'] = config_file

    from tahiti.configuration import tahiti_configuration

    os.chdir(os.environ.get('TAHITI_HOME', '.'))

    base_dir = os.path.dirname(os.path.dirname(__file__))
    static_folder = os.path.join(base_dir, 'public')
    tmpl_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'templates')
    app = Flask(__name__, static_url_path='/public',
                static_folder=static_folder, template_folder=tmpl_folder)

    sqlalchemy_utils.i18n.get_locale = get_locale

    app.config["RESTFUL_JSON"] = {
        'cls': app.json_encoder,
        'sort_keys': False,
        'indent': None
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
    # admin = Admin(app, name='Tahiti', template_mode='bootstrap3')

    # Logging configuration
    logging.config.fileConfig('logging_config.ini')

    # CORS configuration
    CORS(app, resources={r"/*": {"origins": "*"}})

    # API configuration
    api = Api(app)
    mappings = {
        '/applications': ApplicationListApi,
        '/applications/<int:application_id>': ApplicationDetailApi,
        '/operations': OperationListApi,
        '/operations/clear-cache': OperationClearCacheApi,
        '/operations/tree/<int:platform_id>': OperationTreeApi,
        '/operations/<int:operation_id>': OperationDetailApi,
        '/platforms': PlatformListApi,
        '/platforms/<int:platform_id>': PlatformDetailApi,
        '/subsets': OperationSubsetListApi,
        '/subsets/<int:subset_id>': OperationSubsetDetailApi,
        '/subsets/<int:subset_id>/<int:operation_id>': OperationSubsetOperationApi,
        '/workflows': WorkflowListApi,
        '/workflows/<int:workflow_id>': WorkflowDetailApi,
        '/workflows/<int:workflow_id>/permission/<int:user_id>': WorkflowPermissionApi,
        '/workflows/import': WorkflowImportApi,
        '/workflows/from-template': WorkflowAddFromTemplateApi,
        '/workflows/history/<int:workflow_id>': WorkflowHistoryApi,
        '/public/js/tahiti.js': AttributeSuggestionView,
    }
    for path, view in list(mappings.items()):
        api.add_resource(view, path)

    # Cache configuration for API
    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)

    #if config.get('environment', 'dev') == 'dev':
        # admin.add_view(OperationModelView(Operation, db.session))
        #admin.add_view(
        #     OperationCategoryModelView(OperationCategory, db.session))

    return app


def create_babel_i18n(_app):
    """ i18n configuration
    :param _app: Flask app
    :return: Babel configuration
    """
    return Babel(_app)
