#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import argparse

from flask_cors import CORS, cross_origin
from flask import Flask
from flask_restful import Api

from data_source_api import DataSourceListApi, DataSourceDetailApi
from models import db
from operation_api import OperationDetailApi, OperationListApi
from storage_api import StorageListApi
from tahiti.execution_api import ExecutionListApi, ExecutionDetailApi
from workflow_api import WorkflowExecuteListApi

import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

mappings = {
    '/operations': OperationListApi,
    '/operations/<int:operation_id>': OperationDetailApi,
    '/datasources': DataSourceListApi,
    '/datasources/<int:data_source_id>': DataSourceDetailApi,
    '/executions': ExecutionListApi,
    '/executions/<int:execution_id>': ExecutionDetailApi,

    '/storages': StorageListApi,
    '/workflows/execute': WorkflowExecuteListApi,
}
for path, view in mappings.iteritems():
    api.add_resource(view, path)


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
        if parser.get('Servers', 'environment') == 'dev':
            app.run(debug=False)
    else:
        parser.print_usage()
main()
