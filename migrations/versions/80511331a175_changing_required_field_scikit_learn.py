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

all_commands = [
    ("""UPDATE operation_form_field SET `required` = '0' 
        WHERE id IN (4045, 4046, 4208, 4211, 4212, 4214, 4215, 4216, 4217)""",
     """UPDATE operation_form_field SET `required` = '1' 
        WHERE id IN (4045, 4046, 4208, 4211, 4212, 4214, 4215, 4216, 4217)"""),
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