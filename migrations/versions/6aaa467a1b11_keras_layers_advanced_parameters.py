# -*- coding: utf-8 -*-
"""Keras layers advanced parameters

Revision ID: 6aaa467a1b11
Revises: f4e270f5197b
Create Date: 2019-08-12 14:18:13.974533

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json


# revision identifiers, used by Alembic.
revision = '6aaa467a1b11'
down_revision = 'f4e270f5197b'
branch_labels = None
depends_on = None

ENABLED_CONDITION = 'this.advanced_options.internalValue === "1"'


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
        column('form_id', Integer),
        column('enable_conditions', String)
    )

    dense_form = 5100
    dropout_form = 5120
    input_form = 5175
    lambda_form = 5136

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')

    data = [
        (5562, 'advanced_options', 'INTEGER', 0, 1, 0, 'checkbox', None, None,
         'EXECUTION', dense_form, None),
        (5563, 'advanced_options', 'INTEGER', 0, 1, 0, 'checkbox', None, None,
         'EXECUTION', dropout_form, None),
        (5564, 'advanced_options', 'INTEGER', 0, 1, 0, 'checkbox', None, None,
         'EXECUTION', input_form, None),
        (5565, 'advanced_options', 'INTEGER', 0, 1, 0, 'checkbox', None, None,
         'EXECUTION', lambda_form, None),
        ]
    rows = [dict(zip(columns, row)) for row in data]
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
        (5562, 'en', 'Advanced options', 'Enable advanced options.'),
        (5562, 'pt', 'Opções avançadas', 'Habilita as opções avançadas.'),
        (5563, 'en', 'Advanced options', 'Enable advanced options.'),
        (5563, 'pt', 'Opções avançadas', 'Habilita as opções avançadas.'),
        (5564, 'en', 'Advanced options', 'Enable advanced options.'),
        (5564, 'pt', 'Opções avançadas', 'Habilita as opções avançadas.'),
        (5565, 'en', 'Advanced options', 'Enable advanced options.'),
        (5565, 'pt', 'Opções avançadas', 'Habilita as opções avançadas.'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("UPDATE operation_form_field SET `form_id`=5100 WHERE `id` BETWEEN 5100 AND 5109",
     ""),
    ("DELETE FROM operation_operation_form WHERE operation_form_id BETWEEN 5101 AND 5109",
     ""),

    ("UPDATE operation_form_field SET `form_id`=5120 WHERE `id` BETWEEN 5120 AND 5122",
     ""),
    ("DELETE FROM operation_operation_form WHERE operation_form_id BETWEEN 5121 AND 5122",
     ""),

    ("UPDATE operation_form_field SET `form_id`=5136 WHERE `id` IN (5136, 5137, 5138, 5418)",
     ""),
    ("DELETE FROM operation_operation_form WHERE operation_form_id BETWEEN 5137 AND 5138",
     ""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 5562 AND 5565'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 5562 AND 5565'),
    ('''UPDATE operation_form_field SET `enable_conditions`= '{}' WHERE `id` BETWEEN 5101 and 5109'''.format(ENABLED_CONDITION),
     'UPDATE operation_form_field SET `enable_conditions`= NULL WHERE `id` BETWEEN 5101 and 5109'),
    ('''UPDATE operation_form_field SET `enable_conditions`= '{}' WHERE `id` BETWEEN 5121 and 5122'''.format(ENABLED_CONDITION),
     'UPDATE operation_form_field SET `enable_conditions`= NULL WHERE `id` BETWEEN 5121 and 5122'),
    ('''UPDATE operation_form_field SET `enable_conditions`= '{}' WHERE `id` BETWEEN 5420 and 5422'''.format(ENABLED_CONDITION),
     'UPDATE operation_form_field SET `enable_conditions`= NULL WHERE `id` BETWEEN 5420 and 5422'),
    ('''UPDATE operation_form_field SET `enable_conditions`= '{}' WHERE `id` IN (5137, 5138, 5418)'''.format(ENABLED_CONDITION),
     'UPDATE operation_form_field SET `enable_conditions`= NULL WHERE `id` IN (5137, 5138, 5418)'),

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if cmd[0]:
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
            if cmd[1]:
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


