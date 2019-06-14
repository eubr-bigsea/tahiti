# -*- coding: utf-8 -*-
"""Creates Meta-operation.

Revision ID: 55605557d9cc
Revises: 8a4558f255a4
Create Date: 2019-03-14 10:11:56.933470

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '55605557d9cc'
down_revision = '54dff15ea3f9'
branch_labels = None
depends_on = None

SPARK_PLATAFORM_ID = 1
OPHIDIA_PLATAFORM_ID = 2
COMPSS_PLATAFORM_ID = 3
SCIKIT_LEARN_PLATAFORM_ID = 4
KERAS_PLATAFORM_ID = 5

META_OPERATION_ID = 125
META_OPERATION_FORM_ID = 136


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer), )

    columns = ('id', 'slug', 'enabled', 'type', 'icon')
    data = [
        (META_OPERATION_ID, "meta-operation", 0, 'ACTION', ''),
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
        (META_OPERATION_ID, "en", 'Meta-operation',
         'Meta-operation is an operation that contain subworkflows, '
         'i.e. in the workflow they look like a single operation, '
         'although they can contain many operations and even more meta-operations.'),
        (META_OPERATION_ID, "pt", 'Meta-operação',
         'A meta-operação é uma operação que contém subfluxos, ou seja, '
         'no fluxo de trabalho eles se parecem com uma única operação, embora '
         'possam conter muitas operações e também outras meta-operações.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    data = [
        (META_OPERATION_ID, SPARK_PLATAFORM_ID),
        (META_OPERATION_ID, OPHIDIA_PLATAFORM_ID),
        (META_OPERATION_ID, COMPSS_PLATAFORM_ID),
        (META_OPERATION_ID, SCIKIT_LEARN_PLATAFORM_ID),
        (META_OPERATION_ID, KERAS_PLATAFORM_ID),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category():
    tb = table(
        'operation_category',
        column('id', Integer),
        column('type', String),
        column('order', Integer),
        column('default_order', Integer))

    columns = ('id', 'type', 'order', 'default_order')
    data = [
        (43, 'group', 0, 8),
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
        (43, META_OPERATION_ID),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (43, 'en', 'Meta-operation'),
        (43, 'pt', 'Meta-operação'),
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
        (META_OPERATION_FORM_ID, 1, 1, 'execution'),
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
        (META_OPERATION_FORM_ID, 'en', 'Execution'),
        (META_OPERATION_FORM_ID, 'pt', 'Execução'),
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
        (META_OPERATION_ID, 41),
        (META_OPERATION_ID, META_OPERATION_FORM_ID),
        (META_OPERATION_ID, 110),
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

        (502, 'quantity_input_ports', 'INTEGER', 1, 1, 2, 'text', None, None,
         'EXECUTION', META_OPERATION_FORM_ID),
        (503, 'quantity_output_ports', 'INTEGER', 1, 2, 2, 'text', None, None,
         'EXECUTION', META_OPERATION_FORM_ID),
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

        (502, 'en', 'Input ports',
         'Number of input ports for the meta-operation [0:N].'),
        (502, 'pt', 'Portas de entrada',
         'Número de portas de entrada para a meta-operação [0:N].'),

        (503, 'en', 'Output ports',
         'Number of output ports for the meta-operation [0:N].'),
        (503, 'pt', 'Portas de saída',
         'Número de portas de saída para a meta-operação [0:N].'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation,
     'DELETE FROM operation WHERE id = {}'.format(META_OPERATION_ID)),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(
         META_OPERATION_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = {}'.format(
         META_OPERATION_ID)),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE ID = 43'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = {}'.format(
         META_OPERATION_ID)),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id = 43'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = {}'.format(META_OPERATION_FORM_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = {}'.format(
         META_OPERATION_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = {}'.format(
         META_OPERATION_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 502 and 503'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 502 and 503'),

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
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()
