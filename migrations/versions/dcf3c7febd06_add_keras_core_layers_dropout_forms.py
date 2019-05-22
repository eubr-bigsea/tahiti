# -*- coding: utf-8 -*-
"""Add Keras - Core Layers - Dropout forms

Revision ID: dcf3c7febd06
Revises: cbcb14e49217
Create Date: 2018-10-05 10:56:42.397869

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = 'dcf3c7febd06'
down_revision = 'cbcb14e49217'
branch_labels = None
depends_on = None


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        #Dropout
        (5120, 1, 1, 'execution'), #rate
        (5121, 1, 1, 'execution'), #noise_shape
        (5122, 1, 1, 'execution'), #seed
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
        #Dropout - rate
        (5120, 'en', 'Execution'),
        (5120, 'pt', 'Execução'),

        #Dropout - noise_shape
        (5121, 'en', 'Execution'),
        (5121, 'pt', 'Execução'),

        #Dropout - seed
        (5122, 'en', 'Execution'),
        (5122, 'pt', 'Execução'),
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
        (5012, 41),  #appearance

        #Dropout - rate
        (5012, 5120),  # own execution form

        #Dropout - noise_shape
        (5012, 5121),  # own execution form

        #Dropout - seed
        (5012, 5122),  # own execution form
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
        #Dropout - rate
        (5120, 'rate', 'FLOAT', 1, 1, 0.3, 'decimal', None, None, 'EXECUTION', 5120),

        #Dropout - noise_shape
        (5121, 'noise_shape', 'INTEGER', 0, 2, None, 'integer', None, None, 'EXECUTION', 5121),

        #Dropout - seed
        (5122, 'seed', 'INTEGER', 0, 3, None, 'integer', None, None, 'EXECUTION', 5122),
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
        #Dense - rate
        (5120, 'en', 'Fraction to drop', ' Float between 0 and 1. Fraction of the input units to drop.'),

        #Dense - noise_shape
        (5121, 'en', 'Noise shape', '1D integer tensor representing the shape of the binary dropout mask '
                                    'that will be multiplied with the input. For instance, if your inputs '
                                    'have shape (batch_size, timesteps, features) and you want the dropout '
                                    'mask to be the same for all timesteps, you can use '
                                    'noise_shape=(batch_size, 1, features).'),

        #Dense - seed
        (5122, 'en', 'Seed', 'A Python integer to use as random seed.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5120 AND 5122'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5120 AND 5122'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5120 AND 5122'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5120 AND 5122'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 5012'),
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
