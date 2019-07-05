# -*- coding: utf-8 -*-
"""Keras Core Layer operation - Activation.

Revision ID: 4a4b7df125b7
Revises: 8647edf5eaad
Create Date: 2018-10-31 15:34:43.126831

"""
from alembic import op
import sqlalchemy as sa
import json
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '4a4b7df125b7'
down_revision = '8647edf5eaad'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    data = [
        (5014, KERAS_PLATAFORM_ID),# Activation

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer),)

    columns = ('id', 'slug', 'enabled', 'type', 'icon')
    data = [
        (5014, "activation", 1, 'ACTION', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category():
    tb = table(
        'operation_category',
        column('id', Integer),
        column('type', String),
        column('order', Integer),
        column('default_order', Integer),
        )

    columns = ('id', 'type', 'order', 'default_order')
    data = [
        (5014, "subgroup", 7, 7),# Activation
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_category_id', 'operation_id')
    data = [
        #Core Layers
        (5010, 5014),# Activation
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (5014, "en", 'Activation', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String),)

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        #Activation
        (5114, 'INPUT', '', 1, 'ONE', 5014, 'input data'),
        (5214, 'OUTPUT', '', 1, 'ONE', 5014, 'output data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        #Activation
        (5114, 1),
        (5214, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        #Activation
        (5114, "en", 'input data', 'Input data'),
        (5214, "en", 'output data', 'Output data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        #Activation
        (5131, 1, 1, 'execution'), #activation
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        #Activation - activation
        (5131, 'en', 'Execution'),
        (5131, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (5014, 41),  #appearance

        #Activation - activation
        (5014, 5131),  # own execution form
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field():
    tb = table(
        'operation_form_field',
        column('id', Integer),
        column('name', String),
        column('type', String),
        column('required', Integer),
        column('order', Integer),
        column('default', Text),
        column('suggested_widget', String),
        column('values_url', String),
        column('values', String),
        column('scope', String),
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [

        #Activation - activation
        (5131, 'activation', 'TEXT', 1, 1, 'linear', 'dropdown', None,
         json.dumps([
             {"key": "elu", "value": "elu"},
             {"key": "exponential", "value": "exponential"},
             {"key": "hard_sigmoid", "value": "hard_sigmoid"},
             {"key": "linear", "value": "linear"},
             {"key": "relu", "value": "relu"},
             {"key": "selu", "value": "selu"},
             {"key": "sigmoid", "value": "sigmoid"},
             {"key": "softmax", "value": "softmax"},
             {"key": "softplus", "value": "softplus"},
             {"key": "softsign", "value": "softsign"},
             {"key": "tanh", "value": "tanh"}
         ]),
         'EXECUTION', 5131),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [

        #Activation - activation
        (5131, 'en', 'Activation function', 'Activation function to use. '
                                            'If you do not specify anything, '
                                            'no activation is applied (ie. \"linear\" '
                                            'activation: a(x) = x).'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 5014'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id = 5014'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 5014'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 5014'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 5014 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 5114 AND 5214'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 5114 AND 5214'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 5114 AND 5214'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 5131'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id = 5131'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 5131'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id = 5131'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5014'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET foreign_key_checks = 0;')
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
        connection.execute('SET foreign_key_checks = 1;')
    except:
        session.rollback()
        raise
    session.commit()

