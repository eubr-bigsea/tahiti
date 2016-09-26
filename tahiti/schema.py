# -*- coding: utf-8 -*-

from copy import deepcopy
from marshmallow import Schema, fields, post_load
from marshmallow.validate import OneOf
from models import *


def PartialSchemaFactory(schema_cls):
    schema = schema_cls(partial=True)
    for field_name, field in schema.fields.items():
        if isinstance(field, fields.Nested):
            new_field = deepcopy(field)
            new_field.schema.partial = True
            schema.fields[field_name] = new_field
    return schema

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
    description = fields.String(False)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    size = fields.Integer(False)
    precision = fields.Integer(False)
    nullable = fields.Boolean(required=True)
    enumeration = fields.Boolean(required=True)
    missing_representation = fields.String(False)
    feature = fields.Boolean(required=True, missing=True,
                             default=True)
    label = fields.Boolean(required=True, missing=True,
                           default=True)
    distinct_values = fields.Integer(False)
    mean_value = fields.Float(False)
    median_value = fields.String(False)
    max_value = fields.String(False)
    min_value = fields.String(False)
    std_deviation = fields.Float(False)
    missing_total = fields.String(False)
    deciles = fields.String(False)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Attribute"""
        return Attribute(**data)


class AttributeItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(False)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    size = fields.Integer(False)
    precision = fields.Integer(False)
    nullable = fields.Boolean(required=True)
    enumeration = fields.Boolean(required=True)
    missing_representation = fields.String(False)
    feature = fields.Boolean(required=True, missing=True,
                             default=True)
    label = fields.Boolean(required=True, missing=True,
                           default=True)
    distinct_values = fields.Integer(False)
    mean_value = fields.Float(False)
    median_value = fields.String(False)
    max_value = fields.String(False)
    min_value = fields.String(False)
    std_deviation = fields.Float(False)
    missing_total = fields.String(False)
    deciles = fields.String(False)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Attribute"""
        return Attribute(**data)


class AttributeCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(False)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    size = fields.Integer(False)
    precision = fields.Integer(False)
    nullable = fields.Boolean(required=True)
    enumeration = fields.Boolean(required=True)
    missing_representation = fields.String(False)
    feature = fields.Boolean(required=True, missing=True,
                             default=True)
    label = fields.Boolean(required=True, missing=True,
                           default=True)
    distinct_values = fields.Integer(False)
    mean_value = fields.Float(False)
    median_value = fields.String(False)
    max_value = fields.String(False)
    min_value = fields.String(False)
    std_deviation = fields.Float(False)
    missing_total = fields.String(False)
    deciles = fields.String(False)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Attribute"""
        return Attribute(**data)


class DataSourceExecuteRequestSchema(Schema):
    """ JSON schema for executing tasks """
    id = fields.Integer(required=True)
    name = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of DataSource"""
        return DataSource(**data)


class DataSourceListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(False)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    read_only = fields.Boolean(required=True, missing=True,
                               default=True)
    url = fields.String(required=True)
    created = fields.DateTime(required=True, missing=func.now(),
                             default=func.now())
    format = fields.String(required=True,
                           validate=[OneOf(DataSourceFormat.__dict__.keys())])
    provenience = fields.String(False)
    estimated_rows = fields.Integer(False)
    estimated_size_in_mega_bytes = fields.Decimal(False)
    expiration = fields.String(False)
    user_id = fields.Integer(False)
    user_login = fields.String(False)
    user_name = fields.String(False)
    tags = fields.String(False)
    temporary = fields.Boolean(required=True, missing=False,
                               default=False)
    workflow_id = fields.Integer(False)
    task_id = fields.Integer(False)
    attributes = fields.Nested('schema.AttributeListResponseSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('schema.StorageListResponseSchema',
                            required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of DataSource"""
        return DataSource(**data)


class DataSourceCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    description = fields.String(False)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    read_only = fields.Boolean(required=True, missing=True,
                               default=True)
    url = fields.String(required=True)
    format = fields.String(required=True,
                           validate=[OneOf(DataSourceFormat.__dict__.keys())])
    provenience = fields.String(False)
    expiration = fields.String(False)
    user_id = fields.Integer(False)
    user_login = fields.String(False)
    user_name = fields.String(False)
    tags = fields.String(False)
    temporary = fields.Boolean(required=True, missing=False,
                               default=False)
    workflow_id = fields.Integer(False)
    task_id = fields.Integer(False)
    attributes = fields.Nested('schema.AttributeCreateRequestSchema',
                               required=True,
                               many=True)
    storage_id = fields.Integer(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of DataSource"""
        return DataSource(**data)


class DataSourceItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(False)
    enabled = fields.Boolean(required=True, missing=True,
                             default=True)
    read_only = fields.Boolean(required=True, missing=True,
                               default=True)
    url = fields.String(required=True)
    created = fields.DateTime(required=True, missing=func.now(),
                             default=func.now())
    format = fields.String(required=True,
                           validate=[OneOf(DataSourceFormat.__dict__.keys())])
    provenience = fields.String(False)
    estimated_rows = fields.Integer(False)
    estimated_size_in_mega_bytes = fields.Decimal(False)
    expiration = fields.String(False)
    user_id = fields.Integer(False)
    user_login = fields.String(False)
    user_name = fields.String(False)
    tags = fields.String(False)
    temporary = fields.Boolean(required=True, missing=False,
                               default=False)
    workflow_id = fields.Integer(False)
    task_id = fields.Integer(False)
    attributes = fields.Nested('schema.AttributeItemResponseSchema',
                               required=True,
                               many=True)
    storage = fields.Nested('schema.StorageItemResponseSchema',
                            required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of DataSource"""
        return DataSource(**data)


class ExecutionExecuteResponseSchema(Schema):
    """ JSON schema for response """
    id = fields.Integer(required=True)
    created = fields.DateTime(required=True)
    started = fields.DateTime(False)
    status = fields.String(required=True,
                           validate=[OneOf(StatusExecution.__dict__.keys())])
    workflow_id = fields.Integer(required=True)
    message = fields.String()
    status_url = fields.Url(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Execution"""
        return Execution(**data)


class ExecutionStatusRequestSchema(Schema):
    """ JSON schema for executing tasks """
    token = fields.String()

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Execution"""
        return Execution(**data)


class ExecutionItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    created = fields.DateTime(required=True)
    started = fields.DateTime(False)
    finished = fields.DateTime(False)
    status = fields.String(required=True,
                           validate=[OneOf(StatusExecution.__dict__.keys())])
    workflow_id = fields.Integer(required=True)
    workflow_name = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    tasks_execution = fields.Nested('schema.TaskExecutionItemResponseSchema',
                                    required=True,
                                    many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Execution"""
        return Execution(**data)


class ExecutionListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    created = fields.DateTime(required=True)
    started = fields.DateTime(False)
    finished = fields.DateTime(False)
    status = fields.String(required=True,
                           validate=[OneOf(StatusExecution.__dict__.keys())])
    workflow_id = fields.Integer(required=True)
    workflow_name = fields.String(required=True)
    workflow_definition = fields.String(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    tasks_execution = fields.Nested('schema.TaskExecutionListResponseSchema',
                                    required=True,
                                    many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Execution"""
        return Execution(**data)


class ExecutionCreateRequestSchema(Schema):
    """ JSON serialization schema """
    started = fields.DateTime(False)
    finished = fields.DateTime(False)
    status = fields.String(required=True,
                           validate=[OneOf(StatusExecution.__dict__.keys())])
    workflow_id = fields.Integer(required=True)
    workflow_name = fields.String(required=True)
    workflow_definition = fields.String(required=True)
    tasks_execution = fields.Nested('schema.TaskExecutionCreateRequestSchema',
                                    required=True,
                                    many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Execution"""
        return Execution(**data)


class OperationListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
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

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
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

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    command = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationType.__dict__.keys())])
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

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationUpdateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(False)
    enabled = fields.Boolean(False)
    description = fields.String(False)
    command = fields.String(False)
    type = fields.String(False,
                         validate=[OneOf(OperationType.__dict__.keys())])
    input_form = fields.String(False)
    icon = fields.String(False)
    categories = fields.Nested('schema.OperationCategoryUpdateRequestSchema',
                               many=True)
    forms = fields.Nested('schema.OperationFormUpdateRequestSchema',
                          many=True)
    ports = fields.Nested('schema.OperationPortUpdateRequestSchema',
                          many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Operation"""
        return Operation(**data)


class OperationCategoryCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)


class OperationCategoryListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)
    type = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationCategory"""
        return OperationCategory(**data)


class OperationFormListResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldListResponseSchema',
                           required=True,
                           many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)


class OperationFormCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldCreateRequestSchema',
                           required=True,
                           many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)


class OperationFormItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    fields = fields.Nested('schema.OperationFormFieldItemResponseSchema',
                           required=True,
                           many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationForm"""
        return OperationForm(**data)


class OperationFormFieldListResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    required = fields.Boolean(required=True)
    suggested_widget = fields.String(False)
    values_url = fields.String(False)
    values = fields.String(False)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationFormField"""
        return OperationFormField(**data)


class OperationFormFieldCreateRequestSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    required = fields.Boolean(required=True)
    suggested_widget = fields.String(False)
    values_url = fields.String(False)
    values = fields.String(False)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationFormField"""
        return OperationFormField(**data)


class OperationFormFieldItemResponseSchema(Schema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(DataType.__dict__.keys())])
    required = fields.Boolean(required=True)
    suggested_widget = fields.String(False)
    values_url = fields.String(False)
    values = fields.String(False)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationFormField"""
        return OperationFormField(**data)


class OperationPortListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(False)
    order = fields.Integer(False)
    multiplicity = fields.String(required=True, missing=1,
                                  default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested('schema.OperationPortInterfaceListResponseSchema',
                               required=True,
                               many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)


class OperationPortCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(False)
    order = fields.Integer(False)
    multiplicity = fields.String(required=True, missing=1,
                                  default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested('schema.OperationPortInterfaceCreateRequestSchema',
                               required=True,
                               many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)


class OperationPortItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(OperationPortType.__dict__.keys())])
    description = fields.String(required=True)
    tags = fields.String(False)
    order = fields.Integer(False)
    multiplicity = fields.String(required=True, missing=1,
                                  default=1,
                                 validate=[OneOf(OperationPortMultiplicity.__dict__.keys())])
    interfaces = fields.Nested('schema.OperationPortInterfaceItemResponseSchema',
                               required=True,
                               many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPort"""
        return OperationPort(**data)


class OperationPortInterfaceCreateRequestSchema(Schema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)


class OperationPortInterfaceListResponseSchema(Schema):
    """ JSON schema for response """
    name = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)


class StorageListResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(StorageType.__dict__.keys())])

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Storage"""
        return Storage(**data)


class StorageItemResponseSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(StorageType.__dict__.keys())])

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Storage"""
        return Storage(**data)


class StorageCreateRequestSchema(Schema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Storage"""
        return Storage(**data)


class TaskExecuteRequestSchema(Schema):
    """ JSON schema for executing tasks """
    id = fields.Integer(required=True)
    order = fields.Integer(required=True)
    log_level = fields.String(required=True)
    is_start = fields.Boolean(required=True, missing=False,
                              default=False)
    is_end = fields.Boolean(required=True, missing=False,
                            default=False)
    operation_id = fields.Integer(required=True)
    operation_name = fields.String(required=True)
    next_task_id = fields.Integer()
    parameters = fields.Nested('schema.KeyValuePairExecuteRequestSchema',
                               many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Task"""
        return Task(**data)


class TaskExecutionItemResponseSchema(Schema):
    """ JSON serialization schema """
    date = fields.DateTime(required=True)
    status = fields.String(required=True,
                           validate=[OneOf(StatusExecution.__dict__.keys())])
    task_id = fields.Integer(required=True)
    operation_id = fields.Integer(required=True)
    operation_name = fields.String(required=True)
    message = fields.String()
    std_out = fields.String()
    std_err = fields.String()
    exit_code = fields.Integer()

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of TaskExecution"""
        return TaskExecution(**data)


class TaskExecutionListResponseSchema(Schema):
    """ JSON serialization schema """
    date = fields.DateTime(required=True)
    status = fields.String(required=True,
                           validate=[OneOf(StatusExecution.__dict__.keys())])
    task_id = fields.Integer(required=True)
    operation_id = fields.Integer(required=True)
    operation_name = fields.String(required=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of TaskExecution"""
        return TaskExecution(**data)


class WorkflowExecuteRequestSchema(Schema):
    """ JSON schema for executing workflow """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    user_id = fields.Integer(False)
    user_login = fields.String(False)
    user_name = fields.String(False)
    token = fields.String()
    tasks = fields.Nested('schema.TaskExecuteRequestSchema',
                          required=True,
                          many=True)

    @post_load
    def make_object(self, data):
        """ Deserializes data into an instance of Workflow"""
        return Workflow(**data)
