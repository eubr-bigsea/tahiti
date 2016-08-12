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
from workflow_api import WorkflowExecuteListApi

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

mappings = {
    '/operations': OperationListApi,
    '/operations/<int:operation_id>': OperationDetailApi,
    '/datasources': DataSourceListApi,
    '/datasources/<int:data_source_id>': DataSourceDetailApi,
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
        parser = ConfigParser.ConfigParser()
        parser.read(args.config)

        app.config["RESTFUL_JSON"] = {"cls": app.json_encoder}

        app.config['SQLALCHEMY_DATABASE_URI'] = parser.get(
            'Servers', 'database')

        db.init_app(app)
        with app.app_context():
            db.create_all()

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
