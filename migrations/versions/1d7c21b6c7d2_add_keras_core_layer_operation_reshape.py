# -*- coding: utf-8 -*-
"""Add Keras Core Layer Operation Reshape

Revision ID: 1d7c21b6c7d2
Revises: 4a4b7df125b7
Create Date: 2018-11-01 10:26:22.659859

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '1d7c21b6c7d2'
down_revision = '4a4b7df125b7'
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
        (5015, KERAS_PLATAFORM_ID),# Reshape

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
        (5015, "reshape", 1, 'ACTION', ''),
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
        (5015, "subgroup", 8, 8),# Reshape
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
        (5010, 5015),# Reshape
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
        (5015, "en", 'Reshape', ''),
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
        #Reshape
        (5115, 'INPUT', '', 1, 'ONE', 5015, 'input data'),
        (5215, 'OUTPUT', '', 1, 'ONE', 5015, 'output data'),
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
        #Reshape
        (5115, 1),
        (5215, 1),
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
        #Reshape
        (5115, "en", 'input data', 'Input data'),
        (5215, "en", 'output data', 'Output data'),
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
        #Reshape - target_shape
        (5132, 1, 1, 'execution'),
        #Reshape - input_shape
        #(5133, 1, 1, 'execution'),
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
        #Reshape - target_shape
        (5132, 'en', 'Execution'),
        (5132, 'pt', 'Execução'),
        #Reshape - input_shape
        #(5133, 'en', 'Execution'),
        #(5133, 'pt', 'Execução'),
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
        (5015, 41),  #appearance

        #Reshape - target_shape
        (5015, 5132),  # own execution form
        #Reshape - input_shape
        #(5015, 5133),  # own execution form
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

        #Reshape - target_shape
        (5132, 'target_shape', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION', 5132),
        #Reshape - input_shape
        #(5133, 'input_shape', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 5133),
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

        #Reshape - target_shape
        (5132, 'en', 'Target shape', 'Tuple of integers. Does not include the batch axis. Ex.: (6,2)'),
        #Reshape - input_shape
        #(5133, 'en', 'input_shape', 'Arbitrary, although all dimensions in the input shaped must be fixed. '
        #                            'Use the keyword argument input_shape (tuple of integers, does not '
        #                            'include the batch axis) when using this layer as the first '
        #                            'layer in a model. Ex.: (12,)'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 5015'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id = 5015'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 5015'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 5015'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 5015 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id IN (5115, 5215)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (5115, 5215)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN (5115, 5215)'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN (5132, 5133)'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (5132, 5133)'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id IN (5132, 5133)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (5132, 5133)'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5015'),
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
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()

