#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from flask_cors import CORS, cross_origin
from flask import Flask, session, request
from flask_restful import Api
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

from models import db, Operation, OperationForm, OperationFormField
from operation_api import OperationDetailApi, OperationListApi

import sqlalchemy_utils
from flask_babel import get_locale, Babel
sqlalchemy_utils.i18n.get_locale = get_locale

import json
app = Flask(__name__)
babel = Babel(app)

app.secret_key = 'l3m0n4d1'
# Flask Admin 
admin = Admin(app, name='Lemonade', template_mode='bootstrap3')

# CORS
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

mappings = {
    '/operations': OperationListApi,
    '/operations/<int:operation_id>': OperationDetailApi,
}
for path, view in mappings.iteritems():
    api.add_resource(view, path)

#@app.before_request
def before():
    print request.args
    if request.args and 'lang' in request.args:
        if request.args['lang'] not in ('es', 'en'):
            return abort(404)

@babel.localeselector
def get_locale():
    return request.args.get('lang', 'en')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Config file")

    args = parser.parse_args()
    if args.config:
        with open(args.config) as f:
            config = json.load(f)

        app.config["RESTFUL_JSON"] = {"cls": app.json_encoder}

        server_config = config.get('servers', {})
        app.config['SQLALCHEMY_DATABASE_URI'] = server_config.get(
            'database_url')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)
        with app.app_context():
            db.create_all()

        if server_config.get('environment', 'dev') == 'dev':

            admin.add_view(ModelView(Operation, db.session))
            admin.add_view(ModelView(OperationForm, db.session))
            admin.add_view(ModelView(OperationFormField, db.session))
            app.run(debug=True)
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
main()
