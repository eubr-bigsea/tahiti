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
    nullable = fields.Boolean(required=True)
    enumeration = fields.Boolean(required=True)
    missing_representation = fields.String(required=True)
    feature = fields.Boolean(required=True)
    label = fields.Boolean(required=True)
    distinct_values = fields.Integer()
    mean_value = fields.Float()
    median_value = fields.String()
    max_value = fields.String()
    min_value = fields.String()
    std_deviation = fields.Float()
    missing_total = fields.String()
    deciles = fields.String()


class AttributeItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String()
    type = fields.String(required=True)
    size = fields.Integer()
    precision = fields.Integer()
    nullable = fields.Boolean(required=True)
    enumeration = fields.Boolean(required=True)
    missing_representation = fields.String(required=True)
    feature = fields.Boolean(required=True)
    label = fields.Boolean(required=True)
    distinct_values = fields.Integer()
    mean_value = fields.Float()
    median_value = fields.String()
    max_value = fields.String()
    min_value = fields.String()
    std_deviation = fields.Float()
    missing_total = fields.String()
    deciles = fields.String()


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
    expiration = fields.String()
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    tags = fields.String()
    attributes = fields.Nested('schema.AttributeListResponseSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('schema.StorageListResponseSchema',
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
    expiration = fields.String()
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    tags = fields.String()
    attributes = fields.Nested('schema.AttributeCreateRequestSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('schema.StorageCreateRequestSchema',
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
    expiration = fields.String()
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    tags = fields.String()
    attributes = fields.Nested('schema.AttributeItemResponseSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('schema.StorageItemResponseSchema',
                            required=True)


class ExecutionExecuteResponseSchema(Schema):
    """ JSON schema for response """
    id = fields.Integer(required=True)
    created = fields.DateTime(required=True)
    started = fields.DateTime()
    status = fields.String(required=True)
    workflow_id = fields.Integer(required=True)
    message = fields.String()
    status_url = fields.Url(required=True)


class ExecutionStatusRequestSchema(Schema):
    """ JSON schema for executing tasks """
    token = fields.String()


class ExecutionItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    created = fields.DateTime(required=True)
    started = fields.DateTime()
    finished = fields.DateTime()
    status = fields.String(required=True)
    workflow_id = fields.Integer(required=True)
    workflow_name = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    tasks_execution = fields.Nested('schema.TaskExecutionItemResponseSchema',
                                    required=True,
                                    many=True)


class ExecutionListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    created = fields.DateTime(required=True)
    started = fields.DateTime()
    finished = fields.DateTime()
    status = fields.String(required=True)
    workflow_id = fields.Integer(required=True)
    workflow_name = fields.String(required=True)
    workflow_definition = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    tasks_execution = fields.Nested('schema.TaskExecutionListResponseSchema',
                                    required=True,
                                    many=True)


class ExecutionCreateRequestSchema(Schema):
    """ JSON serialization schema """
    started = fields.DateTime()
    finished = fields.DateTime()
    status = fields.String(required=True)
    workflow_id = fields.Integer(required=True)
    workflow_name = fields.String(required=True)
    workflow_definition = fields.String(required=True)
    tasks_execution = fields.Nested('schema.TaskExecutionCreateRequestSchema',
                                    required=True,
                                    many=True)


class OperationListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True)
    input_form = fields.String(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('schema.OperationCategoryListResponseSchema',
                               required=True,
                               many=True)
    forms = fields.Nested('schema.OperationFormListResponseSchema',
                          required=True,
                          many=True)
    ports = fields.Nested('schema.OperationPortListResponseSchema',
                          required=True,
                          many=True)


class OperationCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True)
    input_form = fields.String(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('schema.OperationCategoryCreateRequestSchema',
                               required=True,
                               many=True)
    forms = fields.Nested('schema.OperationFormCreateRequestSchema',
                          required=True,
                          many=True)
    ports = fields.Nested('schema.OperationPortCreateRequestSchema',
                          required=True,
                          many=True)


class OperationItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True)
    input_form = fields.String(required=True)
    icon = fields.String(required=True)
    categories = fields.Nested('schema.OperationCategoryItemResponseSchema',
                               required=True,
                               many=True)
    forms = fields.Nested('schema.OperationFormItemResponseSchema',
                          required=True,
                          many=True)
    ports = fields.Nested('schema.OperationPortItemResponseSchema',
                          required=True,
                          many=True)


class OperationUpdateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String()
    enabled = fields.Boolean()
    description = fields.String()
    command = fields.String()
    type = fields.String()
    input_form = fields.String()
    icon = fields.String()
    categories = fields.Nested('schema.OperationCategoryUpdateRequestSchema',
                               many=True)
    forms = fields.Nested('schema.OperationFormUpdateRequestSchema',
                          many=True)
    ports = fields.Nested('schema.OperationPortUpdateRequestSchema',
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


class OperationFormListResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldListResponseSchema',
                           required=True,
                           many=True)


class OperationFormCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldCreateRequestSchema',
                           required=True,
                           many=True)


class OperationFormItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldItemResponseSchema',
                           required=True,
                           many=True)


class OperationFormFieldListResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True)
    required = fields.Boolean(required=True)
    suggested_widget = fields.String()
    values_url = fields.String()
    values = fields.String()


class OperationFormFieldCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True)
    required = fields.Boolean(required=True)
    suggested_widget = fields.String()
    values_url = fields.String()
    values = fields.String()


class OperationFormFieldItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True)
    required = fields.Boolean(required=True)
    suggested_widget = fields.String()
    values_url = fields.String()
    values = fields.String()


class OperationPortListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    description = fields.String(required=True)
    tags = fields.String()
    order = fields.Integer()
    multiplicity = fields.String(required=True)
    interfaces = fields.Nested('schema.OperationPortInterfaceListResponseSchema',
                               required=True,
                               many=True)


class OperationPortCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    description = fields.String(required=True)
    tags = fields.String()
    order = fields.Integer()
    multiplicity = fields.String(required=True)
    interfaces = fields.Nested('schema.OperationPortInterfaceCreateRequestSchema',
                               required=True,
                               many=True)


class OperationPortItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    description = fields.String(required=True)
    tags = fields.String()
    order = fields.Integer()
    multiplicity = fields.String(required=True)
    interfaces = fields.Nested('schema.OperationPortInterfaceItemResponseSchema',
                               required=True,
                               many=True)


class OperationPortInterfaceCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)


class OperationPortInterfaceListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)


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
    parameters = fields.Nested('schema.KeyValuePairExecuteRequestSchema',
                               many=True)


class TaskExecutionItemResponseSchema(Schema):
    """ JSON serialization schema """
    date = fields.DateTime(required=True)
    status = fields.String(required=True)
    task_id = fields.Integer(required=True)
    operation_id = fields.Integer(required=True)
    operation_name = fields.String(required=True)
    message = fields.String()
    std_out = fields.String()
    std_err = fields.String()
    exit_code = fields.Integer()


class TaskExecutionListResponseSchema(Schema):
    """ JSON serialization schema """
    date = fields.DateTime(required=True)
    status = fields.String(required=True)
    task_id = fields.Integer(required=True)
    operation_id = fields.Integer(required=True)
    operation_name = fields.String(required=True)


class WorkflowExecuteRequestSchema(Schema):
    """ JSON schema for executing workflow """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    user_id = fields.Integer()
    user_login = fields.String()
    user_name = fields.String()
    token = fields.String()
    tasks = fields.Nested('schema.TaskExecuteRequestSchema',
                          required=True,
                          many=True)
