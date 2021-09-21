# -*- coding: utf-8 -*-
import datetime
import json
from copy import deepcopy
from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE, INCLUDE
from marshmallow.validate import OneOf
from flask_babel import gettext
from tahiti.models import *


def partial_schema_factory(schema_cls):
    schema = schema_cls(partial=True)
    for field_name, field in list(schema.fields.items()):
        if isinstance(field, fields.Nested):
            new_field = deepcopy(field)
            new_field.schema.partial = True
            schema.fields[field_name] = new_field
    return schema


def translate_validation(validation_errors):
    for field, errors in list(validation_errors.items()):
        if isinstance(errors, dict):
            validation_errors[field] = translate_validation(errors)
        else:
            validation_errors[field] = [gettext(error) for error in errors]
        return validation_errors


def load_json(str_value):
    try:
        return json.loads(str_value)
    except BaseException:
        return None


# region Protected
class KeyValueSchema(Schema):
    name = fields.String(required=True)
    value = fields.String(required=True)


class UserCreateRequestSchema(Schema):
    id = fields.Integer(required=True)
    login = fields.String(required=True)
    name = fields.String(required=True)


class KeyValuePairExecuteRequestSchema(KeyValueSchema):
    pass

# endregion


class BaseSchema(Schema):
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if value is not None  # Empty lists must be kept!
        }


class ApplicationCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(ApplicationType.__dict__.keys()))])
    execution_parameters = fields.String(required=False, allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Application"""
        return Application(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class ApplicationListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(ApplicationType.__dict__.keys()))])
    execution_parameters = fields.Function(
        lambda x: load_json(x.execution_parameters))

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Application"""
        return Application(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class ApplicationItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(ApplicationType.__dict__.keys()))])
    execution_parameters = fields.Function(
        lambda x: load_json(x.execution_parameters))

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Application"""
        return Application(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class FlowListResponseSchema(BaseSchema):
    """ JSON schema for listing """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_port_name = fields.String(required=False, allow_none=True)
    target_port_name = fields.String(required=False, allow_none=True)
    environment = fields.String(required=False, allow_none=True, missing=DiagramEnvironment.DESIGN, default=DiagramEnvironment.DESIGN,
                                validate=[OneOf(list(DiagramEnvironment.__dict__.keys()))])
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class FlowItemResponseSchema(BaseSchema):
    """ JSON schema for listing """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_port_name = fields.String(required=False, allow_none=True)
    target_port_name = fields.String(required=False, allow_none=True)
    environment = fields.String(required=False, allow_none=True, missing=DiagramEnvironment.DESIGN, default=DiagramEnvironment.DESIGN,
                                validate=[OneOf(list(DiagramEnvironment.__dict__.keys()))])
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class FlowCreateRequestSchema(BaseSchema):
    """ JSON schema for new instance """
    source_port = fields.Integer(required=True)
    target_port = fields.Integer(required=True)
    source_port_name = fields.String(required=False, allow_none=True)
    target_port_name = fields.String(required=False, allow_none=True)
    environment = fields.String(required=False, allow_none=True, missing=DiagramEnvironment.DESIGN, default=DiagramEnvironment.DESIGN,
                                validate=[OneOf(list(DiagramEnvironment.__dict__.keys()))])
    source_id = fields.String(required=True)
    target_id = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Flow"""
        return Flow(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationSimpleListResponseSchema(BaseSchema):
    """ JSON simple """
    id = fields.Integer(allow_none=True)
    name = fields.String(required=False, allow_none=True)
    slug = fields.String(required=False, allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(OperationType.__dict__.keys()))])
    icon = fields.String(required=True)
    css_class = fields.String(required=False, allow_none=True)
    doc_link = fields.String(required=False, allow_none=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryListResponseSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformListResponseSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormListResponseSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortListResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(OperationType.__dict__.keys()))])
    icon = fields.String(required=True)
    css_class = fields.String(required=False, allow_none=True)
    doc_link = fields.String(required=False, allow_none=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryCreateRequestSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformCreateRequestSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormCreateRequestSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortCreateRequestSchema',
        required=True,
        many=True)
    scripts = fields.Nested(
        'tahiti.schema.OperationScriptCreateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(OperationType.__dict__.keys()))])
    icon = fields.String(required=True)
    css_class = fields.String(required=False, allow_none=True)
    doc_link = fields.String(required=False, allow_none=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryItemResponseSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformItemResponseSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormItemResponseSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortItemResponseSchema',
        required=True,
        many=True)
    scripts = fields.Nested(
        'tahiti.schema.OperationScriptItemResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationUpdateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=False, allow_none=True)
    slug = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(required=False, allow_none=True)
    description = fields.String(required=False, allow_none=True)
    type = fields.String(required=False, allow_none=True,
                         validate=[OneOf(list(OperationType.__dict__.keys()))])
    icon = fields.String(required=False, allow_none=True)
    css_class = fields.String(required=False, allow_none=True)
    doc_link = fields.String(required=False, allow_none=True)
    categories = fields.Nested(
        'tahiti.schema.OperationCategoryUpdateRequestSchema',
        required=True,
        many=True)
    platforms = fields.Nested(
        'tahiti.schema.PlatformUpdateRequestSchema',
        required=True,
        many=True)
    forms = fields.Nested(
        'tahiti.schema.OperationFormUpdateRequestSchema',
        required=True,
        many=True)
    ports = fields.Nested(
        'tahiti.schema.OperationPortUpdateRequestSchema',
        required=True,
        many=True)
    scripts = fields.Nested(
        'tahiti.schema.OperationScriptUpdateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Operation"""
        return Operation(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationCategoryCreateRequestSchema(BaseSchema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    order = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)
    default_order = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationCategoryListResponseSchema(BaseSchema):
    """ JSON schema for response """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    order = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)
    default_order = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationCategoryItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True)
    order = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)
    default_order = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationCategory"""
        return OperationCategory(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationFormListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    order = fields.Integer(required=True)
    category = fields.String(required=True)
    fields = fields.Nested(
        'tahiti.schema.OperationFormFieldListResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationFormCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    order = fields.Integer(required=True)
    category = fields.String(required=True)
    fields = fields.Nested(
        'tahiti.schema.OperationFormFieldCreateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationFormItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    order = fields.Integer(required=True)
    category = fields.String(required=True)
    fields = fields.Nested(
        'tahiti.schema.OperationFormFieldItemResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationForm"""
        return OperationForm(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationFormFieldListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(DataType.__dict__.keys()))])
    required = fields.Boolean(required=True)
    order = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    default = fields.String(required=False, allow_none=True)
    suggested_widget = fields.String(required=False, allow_none=True)
    values_url = fields.String(required=False, allow_none=True)
    values = fields.String(required=False, allow_none=True)
    scope = fields.String(required=False, allow_none=True, missing='BOTH', default='BOTH',
                          validate=[OneOf(list(OperationFieldScope.__dict__.keys()))])
    enable_conditions = fields.String(required=False, allow_none=True)
    editable = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationFormField"""
        return OperationFormField(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationFormFieldCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(DataType.__dict__.keys()))])
    required = fields.Boolean(required=True)
    order = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    default = fields.String(required=False, allow_none=True)
    suggested_widget = fields.String(required=False, allow_none=True)
    values_url = fields.String(required=False, allow_none=True)
    values = fields.String(required=False, allow_none=True)
    scope = fields.String(required=False, allow_none=True, missing='BOTH', default='BOTH',
                          validate=[OneOf(list(OperationFieldScope.__dict__.keys()))])
    enable_conditions = fields.String(required=False, allow_none=True)
    editable = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationFormField"""
        return OperationFormField(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationFormFieldItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    label = fields.String(required=True)
    help = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(DataType.__dict__.keys()))])
    required = fields.Boolean(required=True)
    order = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    default = fields.String(required=False, allow_none=True)
    suggested_widget = fields.String(required=False, allow_none=True)
    values_url = fields.String(required=False, allow_none=True)
    values = fields.String(required=False, allow_none=True)
    scope = fields.String(required=False, allow_none=True, missing='BOTH', default='BOTH',
                          validate=[OneOf(list(OperationFieldScope.__dict__.keys()))])
    enable_conditions = fields.String(required=False, allow_none=True)
    editable = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationFormField"""
        return OperationFormField(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationPortListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(OperationPortType.__dict__.keys()))])
    description = fields.String(required=True)
    tags = fields.String(required=False, allow_none=True)
    order = fields.Integer(required=False, allow_none=True)
    multiplicity = fields.String(required=False, allow_none=True, missing=1, default=1,
                                 validate=[OneOf(list(OperationPortMultiplicity.__dict__.keys()))])
    interfaces = fields.Nested(
        'tahiti.schema.OperationPortInterfaceListResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationPortCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(OperationPortType.__dict__.keys()))])
    description = fields.String(required=True)
    tags = fields.String(required=False, allow_none=True)
    order = fields.Integer(required=False, allow_none=True)
    multiplicity = fields.String(required=False, allow_none=True, missing=1, default=1,
                                 validate=[OneOf(list(OperationPortMultiplicity.__dict__.keys()))])
    interfaces = fields.Nested(
        'tahiti.schema.OperationPortInterfaceCreateRequestSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationPortItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(OperationPortType.__dict__.keys()))])
    description = fields.String(required=True)
    tags = fields.String(required=False, allow_none=True)
    order = fields.Integer(required=False, allow_none=True)
    multiplicity = fields.String(required=False, allow_none=True, missing=1, default=1,
                                 validate=[OneOf(list(OperationPortMultiplicity.__dict__.keys()))])
    interfaces = fields.Nested(
        'tahiti.schema.OperationPortInterfaceItemResponseSchema',
        required=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationPort"""
        return OperationPort(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationPortInterfaceCreateRequestSchema(BaseSchema):
    """ JSON schema for request """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    color = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationPortInterfaceListResponseSchema(BaseSchema):
    """ JSON schema for response """
    name = fields.String(required=True)
    color = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationPortInterfaceItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    color = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationPortInterface"""
        return OperationPortInterface(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationScriptListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(ScriptType.__dict__.keys()))])
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    body = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationScript"""
        return OperationScript(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationScriptCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(ScriptType.__dict__.keys()))])
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    body = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationScript"""
        return OperationScript(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationScriptItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(ScriptType.__dict__.keys()))])
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    body = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationScript"""
        return OperationScript(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationSubsetListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformListResponseSchema',
        required=True)
    operations = fields.Nested(
        'tahiti.schema.OperationListResponseSchema',
        allow_none=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationSubset"""
        return OperationSubset(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationSubsetCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformCreateRequestSchema',
        required=True,
        only=['id'])
    operations = fields.Nested(
        'tahiti.schema.OperationCreateRequestSchema',
        allow_none=True,
        many=True,
        only=['id'])

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationSubset"""
        return OperationSubset(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class OperationSubsetItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformItemResponseSchema',
        required=True)
    operations = fields.Nested(
        'tahiti.schema.OperationItemResponseSchema',
        allow_none=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of OperationSubset"""
        return OperationSubset(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class PlatformListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    icon = fields.String(required=True)
    version = fields.String(
        required=False,
        allow_none=True,
        missing=1.0,
        default=1.0)
    plugin = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    subsets = fields.Nested(
        'tahiti.schema.OperationSubsetListResponseSchema',
        allow_none=True,
        many=True,
        only=['id', 'name'])

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Platform"""
        return Platform(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class PlatformCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    icon = fields.String(required=True)
    version = fields.String(
        required=False,
        allow_none=True,
        missing=1.0,
        default=1.0)
    subsets = fields.Nested(
        'tahiti.schema.OperationSubsetCreateRequestSchema',
        allow_none=True,
        many=True,
        only=['id', 'name'])

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Platform"""
        return Platform(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class PlatformItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    enabled = fields.Boolean(required=True)
    description = fields.String(required=True)
    icon = fields.String(required=True)
    version = fields.String(
        required=False,
        allow_none=True,
        missing=1.0,
        default=1.0)
    plugin = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    subsets = fields.Nested(
        'tahiti.schema.OperationSubsetItemResponseSchema',
        allow_none=True,
        many=True,
        only=['id', 'name'])

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Platform"""
        return Platform(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class PlatformPluginItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    version = fields.String(required=False, allow_none=True)
    copyright = fields.String(required=False, allow_none=True)
    status = fields.String(required=False, allow_none=True,
                           validate=[OneOf(list(PluginStatus.__dict__.keys()))])
    message = fields.String(required=False, allow_none=True)
    manifest = fields.String(required=False, allow_none=True)
    ids_offset = fields.Integer(required=True)
    uuid = fields.String(required=True)
    url = fields.String(required=False, allow_none=True)
    use_compiler = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    use_executor = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of PlatformPlugin"""
        return PlatformPlugin(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class PlatformPluginListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    version = fields.String(required=False, allow_none=True)
    copyright = fields.String(required=False, allow_none=True)
    status = fields.String(required=False, allow_none=True,
                           validate=[OneOf(list(PluginStatus.__dict__.keys()))])
    message = fields.String(required=False, allow_none=True)
    manifest = fields.String(required=False, allow_none=True)
    ids_offset = fields.Integer(required=True)
    uuid = fields.String(required=True)
    url = fields.String(required=False, allow_none=True)
    use_compiler = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    use_executor = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of PlatformPlugin"""
        return PlatformPlugin(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class RoleOperationSubsetCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    role_name = fields.String(required=True)
    role_id = fields.Integer(required=True)
    subset = fields.Nested(
        'tahiti.schema.OperationSubsetCreateRequestSchema',
        required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of RoleOperationSubset"""
        return RoleOperationSubset(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class RoleOperationSubsetItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    role_name = fields.String(required=True)
    role_id = fields.Integer(required=True)
    subset = fields.Nested(
        'tahiti.schema.OperationSubsetItemResponseSchema',
        required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of RoleOperationSubset"""
        return RoleOperationSubset(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class TaskListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.String(required=True)
    name = fields.String(required=False, allow_none=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.Function(lambda x: load_json(x.forms))
    version = fields.Integer(required=True)
    environment = fields.String(required=False, allow_none=True, missing=DiagramEnvironment.DESIGN, default=DiagramEnvironment.DESIGN,
                                validate=[OneOf(list(DiagramEnvironment.__dict__.keys()))])
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    width = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    height = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    display_order = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    group_id = fields.String(required=False, allow_none=True)
    operation = fields.Nested(
        'tahiti.schema.OperationSimpleListResponseSchema',
        allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Task"""
        return Task(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class TaskCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.String(required=True)
    name = fields.String(required=False, allow_none=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.Dict(required=True)
    environment = fields.String(required=False, allow_none=True, missing=DiagramEnvironment.DESIGN, default=DiagramEnvironment.DESIGN,
                                validate=[OneOf(list(DiagramEnvironment.__dict__.keys()))])
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    width = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    height = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    display_order = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    group_id = fields.String(required=False, allow_none=True)
    operation_id = fields.Integer(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Task"""
        data['forms'] = json.dumps(data.get('forms', []))
        return Task(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class TaskItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.String(required=True)
    name = fields.String(required=False, allow_none=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.Function(lambda x: load_json(x.forms))
    version = fields.Integer(required=True)
    environment = fields.String(required=False, allow_none=True, missing=DiagramEnvironment.DESIGN, default=DiagramEnvironment.DESIGN,
                                validate=[OneOf(list(DiagramEnvironment.__dict__.keys()))])
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    width = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    height = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    display_order = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    group_id = fields.String(required=False, allow_none=True)
    operation = fields.Nested(
        'tahiti.schema.OperationSimpleListResponseSchema',
        allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Task"""
        return Task(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class TaskExecuteRequestSchema(BaseSchema):
    """ JSON schema for executing tasks """
    id = fields.String(required=True)
    name = fields.String(required=False, allow_none=True)
    left = fields.Integer(required=True)
    top = fields.Integer(required=True)
    z_index = fields.Integer(required=True)
    forms = fields.String(required=True)
    version = fields.Integer(required=True)
    environment = fields.String(required=False, allow_none=True, missing=DiagramEnvironment.DESIGN, default=DiagramEnvironment.DESIGN,
                                validate=[OneOf(list(DiagramEnvironment.__dict__.keys()))])
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    width = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    height = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    display_order = fields.Integer(
        required=False,
        allow_none=True,
        missing=0,
        default=0)
    group_id = fields.String(required=False, allow_none=True)
    next_task_id = fields.String(allow_none=True)
    operation = fields.Nested(
        'tahiti.schema.OperationExecuteRequestSchema',
        required=True)
    parameters = fields.Nested(
        'tahiti.schema.KeyValuePairExecuteRequestSchema',
        allow_none=True,
        many=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Task"""
        return Task(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowExecuteRequestSchema(BaseSchema):
    """ JSON schema for executing workflow """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    created = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    updated = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    version = fields.Integer(required=True)
    image = fields.String(required=False, allow_none=True)
    is_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_system_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_public = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    template_code = fields.String(required=False, allow_none=True)
    forms = fields.String(required=False, allow_none=True)
    deployment_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_status = fields.String(required=False, allow_none=True,
                                      validate=[OneOf(list(PublishingStatus.__dict__.keys()))])
    type = fields.String(required=False, allow_none=True, missing=WorkflowType.WORKFLOW, default=WorkflowType.WORKFLOW,
                         validate=[OneOf(list(WorkflowType.__dict__.keys()))])
    preferred_cluster_id = fields.Integer(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskExecuteRequestSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowExecuteRequestSchema',
        allow_none=True,
        many=True)
    variables = fields.Nested(
        'tahiti.schema.WorkflowVariableExecuteRequestSchema',
        allow_none=True,
        many=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformExecuteRequestSchema',
        required=True)
    subset = fields.Nested(
        'tahiti.schema.OperationSubsetExecuteRequestSchema',
        allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    created = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    updated = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    version = fields.Integer(required=True)
    image = fields.String(required=False, allow_none=True)
    is_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_system_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_public = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    deployment_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_status = fields.String(required=False, allow_none=True,
                                      validate=[OneOf(list(PublishingStatus.__dict__.keys()))])
    type = fields.String(required=False, allow_none=True, missing=WorkflowType.WORKFLOW, default=WorkflowType.WORKFLOW,
                         validate=[OneOf(list(WorkflowType.__dict__.keys()))])
    preferred_cluster_id = fields.Integer(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskListResponseSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowListResponseSchema',
        allow_none=True,
        many=True)
    variables = fields.Nested(
        'tahiti.schema.WorkflowVariableListResponseSchema',
        allow_none=True,
        many=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformListResponseSchema',
        required=True)
    subset = fields.Nested(
        'tahiti.schema.OperationSubsetListResponseSchema',
        allow_none=True)
    user = fields.Function(
        lambda x: {
            "id": x.user_id,
            "name": x.user_name,
            "login": x.user_login})

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    image = fields.String(required=False, allow_none=True)
    is_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_system_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_public = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    forms = fields.Function(lambda x: load_json(x.forms))
    deployment_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_status = fields.String(required=False, allow_none=True,
                                      validate=[OneOf(list(PublishingStatus.__dict__.keys()))])
    type = fields.String(required=False, allow_none=True, missing=WorkflowType.WORKFLOW, default=WorkflowType.WORKFLOW,
                         validate=[OneOf(list(WorkflowType.__dict__.keys()))])
    preferred_cluster_id = fields.Integer(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskCreateRequestSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowCreateRequestSchema',
        allow_none=True,
        many=True)
    variables = fields.Nested(
        'tahiti.schema.WorkflowVariableCreateRequestSchema',
        allow_none=True,
        many=True)
    platform_id = fields.Integer(required=True)
    subset_id = fields.Integer(required=False, allow_none=True)
    user = fields.Nested(
        'tahiti.schema.UserCreateRequestSchema',
        allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=True,
        default=True)
    created = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    updated = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    version = fields.Integer(required=True)
    image = fields.String(required=False, allow_none=True)
    is_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_system_template = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    is_public = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    forms = fields.Function(lambda x: load_json(x.forms))
    deployment_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_enabled = fields.Boolean(
        required=False,
        allow_none=True,
        missing=False,
        default=False)
    publishing_status = fields.String(required=False, allow_none=True,
                                      validate=[OneOf(list(PublishingStatus.__dict__.keys()))])
    type = fields.String(required=False, allow_none=True, missing=WorkflowType.WORKFLOW, default=WorkflowType.WORKFLOW,
                         validate=[OneOf(list(WorkflowType.__dict__.keys()))])
    preferred_cluster_id = fields.Integer(required=False, allow_none=True)
    tasks = fields.Nested(
        'tahiti.schema.TaskItemResponseSchema',
        allow_none=True,
        many=True)
    flows = fields.Nested(
        'tahiti.schema.FlowItemResponseSchema',
        allow_none=True,
        many=True)
    variables = fields.Nested(
        'tahiti.schema.WorkflowVariableItemResponseSchema',
        allow_none=True,
        many=True)
    platform = fields.Nested(
        'tahiti.schema.PlatformItemResponseSchema',
        required=True,
        only=['id', 'name', 'slug'])
    subset = fields.Nested(
        'tahiti.schema.OperationSubsetItemResponseSchema',
        allow_none=True,
        only=['id', 'name'])
    user = fields.Function(
        lambda x: {
            "id": x.user_id,
            "name": x.user_name,
            "login": x.user_login})

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of Workflow"""
        return Workflow(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowHistoryListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    version = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    date = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    content = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowHistory"""
        return WorkflowHistory(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowHistoryItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    version = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)
    date = fields.DateTime(
        required=False,
        allow_none=True,
        missing=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow)
    content = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowHistory"""
        return WorkflowHistory(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowPermissionListResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    permission = fields.String(required=True,
                               validate=[OneOf(list(PermissionType.__dict__.keys()))])
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowPermission"""
        return WorkflowPermission(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowPermissionItemResponseSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    permission = fields.String(required=True,
                               validate=[OneOf(list(PermissionType.__dict__.keys()))])
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowPermission"""
        return WorkflowPermission(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowPermissionCreateRequestSchema(BaseSchema):
    """ JSON serialization schema """
    id = fields.Integer(required=True)
    permission = fields.String(required=True,
                               validate=[OneOf(list(PermissionType.__dict__.keys()))])
    user_id = fields.Integer(required=True)
    user_login = fields.String(required=True)
    user_name = fields.String(required=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowPermission"""
        return WorkflowPermission(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowVariableListResponseSchema(BaseSchema):
    """ JSON schema for listing """
    name = fields.String(required=True)
    label = fields.String(required=False, allow_none=True)
    description = fields.String(required=False, allow_none=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(DataType.__dict__.keys()))])
    multiplicity = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)
    suggested_widget = fields.String(required=False, allow_none=True)
    default_value = fields.String(required=False, allow_none=True)
    parameters = fields.String(required=False, allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowVariable"""
        return WorkflowVariable(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowVariableItemResponseSchema(BaseSchema):
    """ JSON schema for listing """
    name = fields.String(required=True)
    label = fields.String(required=False, allow_none=True)
    description = fields.String(required=False, allow_none=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(DataType.__dict__.keys()))])
    multiplicity = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)
    suggested_widget = fields.String(required=False, allow_none=True)
    default_value = fields.String(required=False, allow_none=True)
    parameters = fields.String(required=False, allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowVariable"""
        return WorkflowVariable(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE


class WorkflowVariableCreateRequestSchema(BaseSchema):
    """ JSON schema for new instance """
    name = fields.String(required=True)
    label = fields.String(required=False, allow_none=True)
    description = fields.String(required=False, allow_none=True)
    type = fields.String(required=True,
                         validate=[OneOf(list(DataType.__dict__.keys()))])
    multiplicity = fields.Integer(
        required=False,
        allow_none=True,
        missing=1,
        default=1)
    suggested_widget = fields.String(required=False, allow_none=True)
    default_value = fields.String(required=False, allow_none=True)
    parameters = fields.String(required=False, allow_none=True)

    # noinspection PyUnresolvedReferences
    @post_load
    def make_object(self, data, **kwargs):
        """ Deserialize data into an instance of WorkflowVariable"""
        return WorkflowVariable(**data)

    class Meta:
        ordered = True
        unknown = EXCLUDE

