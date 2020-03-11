# -*- coding: utf-8 -*-

"""Update Clustering Operations (scikit_learn).

Revision ID: 9bb45622ba10
Revises: 80e8e1eab0ba
Create Date: 2020-02-06 14:40:26.462399

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
revision = '9bb45622ba10'
down_revision = '80e8e1eab0ba'
branch_labels = None
depends_on = None


all_commands = [
    ("""UPDATE operation_form_field SET `form_id` =  4030 WHERE id IN (4303, 4304, 4305, 4309, 4312, 4313) """,
     """UPDATE operation_form_field SET `form_id` = 4013  WHERE id IN (4303, 4304, 4305, 4309, 4312, 4313) """),

    ("""UPDATE operation_form_field SET `form_id` =  4030 WHERE id IN (4322, 4323, 4324, 4325) """,
     """UPDATE operation_form_field SET `form_id` = 4031  WHERE id IN (4322, 4323, 4324, 4325) """),

    ("""UPDATE operation_form_field SET `form_id` =  4030 WHERE id IN (4332, 4333, 4334, 4335, 4336) """,
     """UPDATE operation_form_field SET `form_id` = 4032  WHERE id IN (4332, 4333, 4334, 4335, 4336) """),

    ("""UPDATE operation_form_field SET `form_id` =  4030 WHERE id IN (4337, 4338, 4339, 4340) """,
     """UPDATE operation_form_field SET `form_id` = 4015  WHERE id IN (4337, 4338, 4339, 4340) """),

    ('DELETE FROM operation_port_translation WHERE id IN (4096, 4095)',
     'DELETE FROM operation_port_translation WHERE id IN (4096, 4095)'),

    ('DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (4096, 4095)',
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id IN (4096, 4095)'),

    ('DELETE FROM operation_port WHERE id IN (4096, 4095)',
     'DELETE FROM operation_port WHERE id IN (4096, 4095)'),

    ("""UPDATE operation_form_field SET `default` = 'clusters' WHERE id IN (4112, 4315, 4328)""",
     """UPDATE operation_form_field SET `default` = 'prediction' WHERE id IN (4112, 4315, 4328)"""),
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
