# -*- coding: utf-8 -*-
"""Add Keras Core Layer Operation ActivityRegularization

Revision ID: 3f13fb8ef399
Revises: 76f8084a5aee
Create Date: 2018-11-05 15:30:44.151542

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '3f13fb8ef399'
down_revision = '76f8084a5aee'
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
        # ActivityRegularization
        (5019, KERAS_PLATAFORM_ID),

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
        # ActivityRegularization
        (5019, "activityRegularization", 1, 'ACTION', ''),
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
        # ActivityRegularization
        (5019, "subgroup", 9, 9),
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
        # Core Layers - ActivityRegularization
        (5010, 5019),
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
        (5019, "en", 'ActivityRegularization', 'Layer that applies an update to the cost '
                                               'function based input activity.'),
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
        # ActivityRegularization
        (5119, 'INPUT', '', 1, 'ONE', 5019, 'input data'),
        (5219, 'OUTPUT', '', 1, 'ONE', 5019, 'output data'),
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
        # ActivityRegularization
        (5119, 1),
        (5219, 1),
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
        # ActivityRegularization
        (5119, "en", 'input data', 'Input data'),
        (5219, "en", 'output data', 'Output data'),
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
        # ActivityRegularization - L1
        (5139, 1, 1, 'execution'),
        # ActivityRegularization - L2
        (5140, 1, 1, 'execution'),
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
        # ActivityRegularization - L1
        (5139, 'en', 'Execution'),
        (5139, 'pt', 'Execução'),
        # ActivityRegularization - L2
        (5140, 'en', 'Execution'),
        (5140, 'pt', 'Execução'),
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
        (5019, 41),#appearance
        # ActivityRegularization - L1
        (5019, 5139),
        # ActivityRegularization - L2
        (5019, 5140),
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

        # ActivityRegularization - L1
        (5139, 'l1', 'DECIMAL', 1, 1, 0.0, 'decimal', None, None, 'EXECUTION', 5139),
        # ActivityRegularization - L2
        (5140, 'l2', 'DECIMAL', 1, 2, 0.0, 'decimal', None, None, 'EXECUTION', 5140),
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

        # ActivityRegularization - L1
        (5139, 'en', 'L1', ' L1 regularization factor (positive float).'),
        # ActivityRegularization - L2
        (5140, 'en', 'L2', 'L2 regularization factor (positive float).'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 5019'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id = 5019'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 5019'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 5019'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 5019 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id IN (5119, 5219)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (5119, 5219)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN (5119, 5219)'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5139 AND 5140'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5139 AND 5140'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5139 AND 5140'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5139 AND 5140'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5019'),
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

