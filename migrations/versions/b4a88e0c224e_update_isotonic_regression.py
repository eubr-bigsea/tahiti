# -*- coding: utf-8 -*-

"""Update isotonic regression

Revision ID: b4a88e0c224e
Revises: 3e10f106043c
Create Date: 2019-10-14 17:13:12.586484

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
revision = 'b4a88e0c224e'
down_revision = '3e10f106043c'
branch_labels = None
depends_on = None

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
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    data = [
        #Flatten - data_format
        (245, 'y_min', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION', 103, None),
        (248, 'y_max', 'FLOAT', 0, 3, None, 'decimal', None, None, 'EXECUTION', 103, None),
        (487, 'out_of_bounds', 'TEXT', 0, 3, "nan", 'dropdown', None,
         json.dumps([
             {"key": "nan", "value": "nan"},
             {"key": "clip", "value": "clip"},
             {"key": "raise", "value": "raise"}
         ]),
         'EXECUTION', 103, None),
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
        #Flatten - data_format
        (245, 'en', 'Y min', 'Y min.'),
        (245, 'pt', 'Y min', 'Y min.'),

        (248, 'en', 'Y max', 'Y max.'),
        (248, 'pt', 'Y max', 'Y max.'),

        (487, 'en', 'Out of bounds', 'Out of bounds.'),
        (487, 'pt', 'Out of bounds', 'Out of bounds.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (245, 248, 487)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (245, 248, 487)'),
    ("""UPDATE operation_form_field SET `default` = 'prediction' WHERE id = 244""",
     """UPDATE operation_form_field SET `default` = 'None' WHERE id = 244"""),
]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
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

