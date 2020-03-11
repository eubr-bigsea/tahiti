# -*- coding: utf-8 -*-

"""Deleting form fields (scikit_learn).

Revision ID: 9307a4e438de
Revises: 5d65ae2809bd
Create Date: 2019-12-04 11:46:20.567816

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
revision = '9307a4e438de'
down_revision = '5d65ae2809bd'
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
        #Flatten
        (4030, 0, 1, 'execution'), #data_format
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
        #Flatten - data_format
        (4030, 'en', 'Trash'),
        (4030, 'pt', 'Lixo'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4158""",
     """UPDATE operation_form_field SET `form_id` = '4022' WHERE id = 4158"""),

    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4176""",
     """UPDATE operation_form_field SET `form_id` = '4006' WHERE id = 4176"""),

    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4185""",
     """UPDATE operation_form_field SET `form_id` = '4010' WHERE id = 4185"""),

    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4199""",
     """UPDATE operation_form_field SET `form_id` = '4020' WHERE id = 4199"""),

    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4210""",
     """UPDATE operation_form_field SET `form_id` = '4009' WHERE id = 4210"""),

    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4235""",
     """UPDATE operation_form_field SET `form_id` = '4001' WHERE id = 4235"""),

    ("""UPDATE operation_form_field SET `form_id` = '4030' WHERE id = 4249""",
     """UPDATE operation_form_field SET `form_id` = '4003' WHERE id = 4249"""),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4030'),

    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4030'),
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
