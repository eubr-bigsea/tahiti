# -*- coding: utf-8 -*-
from marshmallow import Schema, fields


# region Protected
class KeyValueSchema(Schema):
    name = fields.String(required=True)
    value = fields.String(required=True)


class KeyValuePairExecuteRequestSchema(KeyValueSchema):
    pass


# endregion


class AttributeListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String()
    type = fields.String(required=True)
    size = fields.Integer()
    precision = fields.Integer()
    enumeration = fields.Boolean(required=True)
    data_source = fields.Nested('DataSourceListResponseSchema',
                                required=True)


class AttributeItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String()
    type = fields.String(required=True)
    size = fields.Integer()
    precision = fields.Integer()
    enumeration = fields.Boolean(required=True)
    data_source = fields.Nested('DataSourceItemResponseSchema',
                                required=True)


class DataSourceExecuteRequestSchema(Schema):
    """ JSON schema for executing tasks """
    id = fields.Integer(required=True)
    name = fields.String(required=True)


class DataSourceListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String()
    enabled = fields.Boolean(required=True)
    read_only = fields.Boolean(required=True)
    url = fields.String(required=True)
    created = fields.DateTime(required=True)
    format = fields.String(required=True)
    provenience = fields.String()
    estimated_rows = fields.Integer(required=True)
    estimated_size_in_mega_bytes = fields.Decimal(required=True)
    selection = fields.String()
    projection = fields.String()
    expiration = fields.String()
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    tags = fields.String()
    attributes = fields.Nested('AttributeListResponseSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('StorageListResponseSchema',
                            required=True)


class DataSourceCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String()
    enabled = fields.Boolean(required=True)
    read_only = fields.Boolean(required=True)
    url = fields.String(required=True)
    created = fields.DateTime(required=True)
    format = fields.String(required=True)
    provenience = fields.String()
    estimated_rows = fields.Integer(required=True)
    estimated_size_in_mega_bytes = fields.Decimal(required=True)
    selection = fields.String()
    projection = fields.String()
    expiration = fields.String()
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    tags = fields.String()
    attributes = fields.Nested('AttributeCreateRequestSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('StorageCreateRequestSchema',
                            required=True)


class DataSourceItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String()
    enabled = fields.Boolean(required=True)
    read_only = fields.Boolean(required=True)
    url = fields.String(required=True)
    created = fields.DateTime(required=True)
    format = fields.String(required=True)
    provenience = fields.String()
    estimated_rows = fields.Integer(required=True)
    estimated_size_in_mega_bytes = fields.Decimal(required=True)
    selection = fields.String()
    projection = fields.String()
    expiration = fields.String()
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    tags = fields.String()
    attributes = fields.Nested('AttributeItemResponseSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('StorageItemResponseSchema',
                            required=True)


class ExecutionExecuteResponseSchema(Schema):
    """ JSON schema for response """
    id = fields.Integer(required=True)
    started = fields.DateTime(required=True)
    status = fields.String(required=True)
    workflow_id = fields.Integer(required=True)
    message = fields.String()
    status_url = fields.Url(required=True)


class ExecutionStatusRequestSchema(Schema):
    """ JSON schema for executing tasks """
    token = fields.String(required=True)


class ExecutionStatusResponseSchema(Schema):
    """ JSON schema for response """
    id = fields.Integer(required=True)
    started = fields.DateTime(required=True)
    finished = fields.DateTime(required=True)
    status = fields.String(required=True)
    workflow_id = fields.Integer(required=True)
    message = fields.String()
    status_url = fields.Url(required=True)
    tasks_execution = fields.Nested('TaskExecutionStatusResponseSchema',
                                    required=True,
                                    many=True)


class OperationListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    enabled = fields.Boolean(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True)
    input_form = fields.String(required=True)
    allow_multiple_inputs = fields.Boolean(required=True)
    allow_multiple_outputs = fields.Boolean(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('OperationCategoryListResponseSchema',
                               required=True,
                               many=True)


class OperationCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    enabled = fields.Boolean(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True)
    input_form = fields.String(required=True)
    allow_multiple_inputs = fields.Boolean(required=True)
    allow_multiple_outputs = fields.Boolean(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('OperationCategoryCreateRequestSchema',
                               required=True,
                               many=True)


class OperationItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    enabled = fields.Boolean(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True)
    input_form = fields.String(required=True)
    allow_multiple_inputs = fields.Boolean(required=True)
    allow_multiple_outputs = fields.Boolean(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('OperationCategoryItemResponseSchema',
                               required=True,
                               many=True)


class OperationUpdateRequestSchema(Schema):
    """ JSON serialization schema """
    enabled = fields.Boolean()
    name = fields.String()
    description = fields.String()
    command = fields.String()
    type = fields.String()
    input_form = fields.String()
    allow_multiple_inputs = fields.Boolean()
    allow_multiple_outputs = fields.Boolean()
    icon = fields.String()
    categories = fields.Nested('OperationCategoryUpdateRequestSchema',
                               many=True)


class OperationCategoryCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)


class OperationCategoryListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)
    type = fields.String(required=True)


class StorageListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)


class StorageItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)


class TaskExecuteRequestSchema(Schema):
    """ JSON schema for executing tasks """
    id = fields.Integer(required=True)
    order = fields.Integer(required=True)
    log_level = fields.String(required=True)
    is_start = fields.Boolean(required=True)
    is_end = fields.Boolean(required=True)
    operation_id = fields.Integer(required=True)
    operation_name = fields.String(required=True)
    next_task_id = fields.Integer()
    parameters = fields.Nested('KeyValuePairExecuteRequestSchema',
                               required=True,
                               many=True)


class TaskExecutionStatusResponseSchema(Schema):
    """ JSON schema for executing tasks """
    id = fields.Integer(required=True)
    date = fields.DateTime(required=True)
    status = fields.String(required=True)
    task_id = fields.Integer(required=True)
    task_name = fields.String(required=True)
    operation_id = fields.Integer(required=True)
    operation_name = fields.String(required=True)
    message = fields.String()
    std_out = fields.String()
    std_err = fields.String()
    exit_code = fields.Integer()


class WorkflowExecuteRequestSchema(Schema):
    """ JSON schema for executing workflow """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    token = fields.String(required=True)
    tasks = fields.Nested('TaskExecuteRequestSchema',
                          required=True,
                          many=True)
