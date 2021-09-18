import logging
import logging.config
import os

import jinja2
import sqlalchemy_utils
from flask import Flask
from flask_babel import Babel
from flask_babel import get_locale, Babel
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate

from tahiti.application_api import ApplicationListApi, ApplicationDetailApi
from tahiti.cache import cache
from tahiti.models import db
from tahiti.operation_api import OperationDetailApi, OperationClearCacheApi
from tahiti.operation_api import OperationListApi, OperationTreeApi
from tahiti.operation_subset_api import (OperationSubsetDetailApi,
        OperationSubsetListApi)
from tahiti.operation_subset_operation_api import OperationSubsetOperationApi
from tahiti.platform_api import PlatformListApi, PlatformDetailApi
from tahiti.views import AttributeSuggestionView
from tahiti.workflow_api import WorkflowDetailApi, WorkflowListApi
from tahiti.workflow_from_template_api import WorkflowFromTemplateApi
from tahiti.workflow_permission_api import WorkflowPermissionApi
from tahiti.import_workflow_api import ImportWorkflowApi
from tahiti.workflow_history_api import  WorkflowHistoryApi
from flask_swagger_ui import get_swaggerui_blueprint

def create_app(settings_override=None, log_level=logging.DEBUG, config_file=''):
    if config_file:
        os.environ['TAHITI_CONFIG'] = config_file

    from tahiti.configuration import tahiti_configuration

    os.chdir(os.environ.get('TAHITI_HOME', '.'))

    base_dir = os.path.dirname(os.path.dirname(__file__))
    static_folder = os.path.join(base_dir, 'static')
    tmpl_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'templates')
    app = Flask(__name__, static_url_path='',
                static_folder='static', template_folder=tmpl_folder)

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
    
    migrate = Migrate(app, db)
    # Logging configuration
    logging.config.fileConfig('logging_config.ini')

    # CORS configuration
    CORS(app, resources={r"/*": {"origins": "*"}})

    
    babel = Babel(app)

    # Swagger
    swaggerui_blueprint = get_swaggerui_blueprint(
        '/api/docs',  
        '/static/swagger.yaml',
        config={
            'app_name': "Lemonade Tahiti"
        },
    )
    
    app.register_blueprint(swaggerui_blueprint)

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
        '/workflows/import': ImportWorkflowApi,
        '/workflows/from-template': WorkflowFromTemplateApi,
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
