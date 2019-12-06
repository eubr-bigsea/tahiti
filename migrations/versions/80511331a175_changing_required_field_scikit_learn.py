# -*- coding: utf-8 -*-

"""Changing required field (scikit_learn).

Revision ID: 80511331a175
Revises: 1c688e5c61f3
Create Date: 2019-12-06 08:06:19.386743

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
revision = '80511331a175'
down_revision = '1c688e5c61f3'
branch_labels = None
depends_on = None


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (4038, 41), #appearance
        (4037, 41), #appearance
        (4041, 41), #appearance
        (112, 41), #appearance
        (4027, 41), #appearance
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `required` = '0' 
        WHERE id IN (4045, 4046, 4208, 4211, 4212, 4214, 4215, 4216, 4217)""",
     """UPDATE operation_form_field SET `required` = '1' 
        WHERE id IN (4045, 4046, 4208, 4211, 4212, 4214, 4215, 4216, 4217)"""),

    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id IN (4038, 4037, 4041, 112, 4027)  '
     'AND operation_form_id = 41'),

    ("""UPDATE operation_form_field SET `required` = '0' WHERE id = 4149""",
     """UPDATE operation_form_field SET `required` = '1' WHERE id = 4149"""),

    ("""UPDATE operation_form_field SET `order` = '2' WHERE id = 4122""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4122"""),

    ("""UPDATE operation_form_field SET `order` = '3' WHERE id = 4149""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4149"""),

    ("""UPDATE operation_form_field SET `order` = '4' WHERE id = 4126""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4126"""),

    ("""UPDATE operation_form_field SET `order` = '5' WHERE id = 4123""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4123"""),

    ("""UPDATE operation_form_field SET `order` = '6' WHERE id = 4124""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4124"""),

    ("""UPDATE operation_form_field SET `order` = '7' WHERE id = 4125""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4125"""),

    ("""UPDATE operation_form_field SET `order` = '2' WHERE id = 4113""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4113"""),

    ("""UPDATE operation_form_field SET `order` = '3' WHERE id = 4114""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4114"""),

    ("""UPDATE operation_form_field SET `order` = '5' WHERE id = 4115""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4115"""),

    ("""UPDATE operation_form_field SET `order` = '6' WHERE id = 4116""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4116"""),

    ("""UPDATE operation_form_field SET `order` = '7' WHERE id = 4117""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4117"""),

    ("""UPDATE operation_form_field SET `order` = '8' WHERE id = 4118""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4118"""),

    ("""UPDATE operation_form_field SET `order` = '9' WHERE id = 4119""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4119"""),

    ("""UPDATE operation_form_field SET `order` = '10' WHERE id = 4120""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4120"""),

    ("""UPDATE operation_form_field SET `order` = '11' WHERE id = 4121""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4121"""),

    ("""UPDATE operation_form_field SET `order` = '2' WHERE id = 4145""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4145"""),

    ("""UPDATE operation_form_field SET `order` = '3' WHERE id = 4141""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4141"""),

    ("""UPDATE operation_form_field SET `order` = '4' WHERE id = 4142""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4142"""),

    ("""UPDATE operation_form_field SET `order` = '5' WHERE id = 4143""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4143"""),

    ("""UPDATE operation_form_field SET `order` = '6' WHERE id = 4146""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4146"""),

    ("""UPDATE operation_form_field SET `order` = '7' WHERE id = 4147""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4147"""),
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