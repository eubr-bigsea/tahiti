# -*- coding: utf-8 -*-
"""Add Keras - Loss Functions

Revision ID: ec9191676104
Revises: 5cd95feb3808
Create Date: 2018-10-05 15:01:43.236452

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = 'ec9191676104'
down_revision = '5cd95feb3808'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (5060, "en", 'Functions'),
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
        (5061, KERAS_PLATAFORM_ID),#loss functions
        (5062, KERAS_PLATAFORM_ID),#optimizer functions
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
        (5060, "group", 6, 6),
        (5061, "subgroup", 1, 1),
        (5062, "subgroup", 2, 2),
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
        (5061, "loss", 1, 'ACTION', ''),
        (5062, "optimizer", 1, 'ACTION', ''),
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
        #Loss Functions
        (5060, 5061),
        (5060, 5062),
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
        (5061, "en", "Loss", ''),
        (5062, "en", "Optimizer", ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5061 AND 5062'),

    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id BETWEEN 5060 AND 5062'),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5061 AND 5062'),

    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5061 AND 5062'),

    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id = 5060'),

    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id BETWEEN 5061 AND 5062 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),
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

