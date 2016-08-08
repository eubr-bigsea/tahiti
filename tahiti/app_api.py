#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import argparse

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
    else:
        parser.print_usage()


main()
