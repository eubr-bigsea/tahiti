#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
import logging

import sqlalchemy_utils
from flask import Flask, request, g

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import get_locale, Babel
from flask_cors import CORS
from flask_restful import Api
from cache import cache

from models import db, Operation, OperationForm, OperationFormField
from application_api import ApplicationDetailApi, ApplicationListApi
from platform_api import PlatformDetailApi, PlatformListApi
from operation_api import OperationDetailApi, OperationListApi
from workflow_api import WorkflowDetailApi, WorkflowListApi

sqlalchemy_utils.i18n.get_locale = get_locale

app = Flask(__name__)
babel = Babel(app)

app.secret_key = 'l3m0n4d1'
# Flask Admin 
admin = Admin(app, name='Lemonade', template_mode='bootstrap3')

# CORS
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

# Cache
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger('werkzeug').setLevel(logging.DEBUG)

mappings = {
    '/applications': ApplicationListApi,
    '/applications/<int:application_id>': ApplicationDetailApi,
    '/operations': OperationListApi,
    '/operations/<int:operation_id>': OperationDetailApi,
    '/platforms': PlatformListApi,
    '/platforms/<int:operation_id>': PlatformDetailApi,
    '/workflows': WorkflowListApi,
    '/workflows/<int:workflow_id>': WorkflowDetailApi,
}
for path, view in mappings.iteritems():
    api.add_resource(view, path)


# @app.before_request
def before():
    print request.args
    if request.args and 'lang' in request.args:
        if request.args['lang'] not in ('es', 'en'):
            return abort(404)


@babel.localeselector
def get_locale_from_query():
    return request.args.get('lang', 'en')


@app.before_request
def func():
    g.locale = get_locale()


def main(config=None, manager_mode=False):
    print 'Starting'
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Config file")
    if config is None:
        args = parser.parse_args()
        config_path = args.config
    else:
        config_path = config

    if config_path:
        with open(config_path) as f:
            config_json = json.load(f)

        app.config["RESTFUL_JSON"] = {
            'cls': app.json_encoder,
            'indent': 2,
            'sort_keys': False,
        }

        server_config = config_json.get('servers', {})
        app.config['SQLALCHEMY_DATABASE_URI'] = server_config.get(
            'database_url')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_POOL_SIZE'] = 10
        app.config['SQLALCHEMY_POOL_RECYCLE'] = 240

        db.init_app(app)
        with app.app_context():
            db.create_all()

        if server_config.get('environment', 'dev') == 'dev':
            admin.add_view(ModelView(Operation, db.session))
            admin.add_view(ModelView(OperationForm, db.session))
            admin.add_view(ModelView(OperationFormField, db.session))

            if not manager_mode:
                app.run(debug=True, host='0.0.0.0')
            '''
            # Create the Flask-Restless API manager.
            manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

            # Create API endpoints, which will be available at /api/<tablename> by
            # default. Allowed HTTP methods can be specified as well.
            prefix = '/api/v1'
            manager.create_api(Operation, methods=['GET', 'POST', 'DELETE'],
                               url_prefix=prefix)
            manager.create_api(Execution, methods=['GET'], url_prefix=prefix)
            '''
    else:
        parser.print_usage()


if __name__ == '__main__':
    main()
main()
