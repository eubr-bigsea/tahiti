# -*- coding: utf-8 -*-
"""Add Keras Core Layer Operation Lambda

Revision ID: 76f8084a5aee
Revises: 1ff9d4d725e5
Create Date: 2018-11-05 12:00:28.217290

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '76f8084a5aee'
down_revision = '1ff9d4d725e5'
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
        (5018, KERAS_PLATAFORM_ID),#Lambda

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
        (5018, "lambda", 1, 'ACTION', ''),
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
        # Lambda
        (5018, "subgroup", 9, 9 ),
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
        # Core Layers - Lambda
        (5010, 5018),
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
        (5018, "en", 'Lambda', ''),
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
        # Lambda
        (5118, 'INPUT', '', 1, 'ONE', 5018, 'input data'),
        (5218, 'OUTPUT', '', 1, 'ONE', 5018, 'output data'),
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
        # Lambda
        (5118, 1),
        (5218, 1),
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
        # Lambda
        (5118, "en", 'input data', 'Input data'),
        (5218, "en", 'output data', 'Output data'),
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
        # Lambda - function
        (5136, 1, 1, 'execution'),
        # Lambda - mask
        (5137, 1, 1, 'execution'),
        # Lambda - arguments
        (5138, 1, 1, 'execution'),
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
        #Lambda - function
        (5136, 'en', 'Execution'),
        (5136, 'pt', 'Execução'),
        #Lambda - mask
        (5137, 'en', 'Execution'),
        (5137, 'pt', 'Execução'),
        #Lambda - arguments
        (5138, 'en', 'Execution'),
        (5138, 'pt', 'Execução'),
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
        (5018, 41),#appearance
        #Lambda - function
        (5018, 5136),
        #Lambda - mask
        (5018, 5137),
        #Lambda - arguments
        (5018, 5138),
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

        # Lambda - function
        (5136, 'function', 'TEXT', 1, 1, None, 'code', None, '{"language": "python"}', 'EXECUTION', 5136),
        # Lambda - mask
        (5137, 'mask', 'DECIMAL', 0, 4, None, 'decimal', None, None, 'EXECUTION', 5137),
        # Lambda - arguments
        (5138, 'arguments', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 5138),
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

        # Lambda - function
        (5136, 'en', 'Function', 'The function to be evaluated. Takes input tensor as first argument.'),
        # Lambda - mask
        (5137, 'en', 'Mask', 'Masks a sequence by using a mask value to skip timesteps.'
                             'For each timestep in the input tensor (dimension #1 in the tensor), '
                             'if all values in the input tensor at that timestep are equal to '
                             'mask_value, then the timestep will be masked (skipped) in all '
                             'downstream layers (as long as they support masking).'
                             'If any downstream layer does not support masking yet '
                             'receives such an input mask, an exception will be raised.'),
        # Lambda - arguments
        (5138, 'en', 'Arguments', 'Optional dictionary of keyword arguments to be passed to the function.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 5018'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id = 5018'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 5018'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 5018'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 5018 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id IN (5118, 5218)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (5118, 5218)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN (5118, 5218)'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5136 AND 5138'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5136 AND 5138'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5136 AND 5138'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5136 AND 5138'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5018'),
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

