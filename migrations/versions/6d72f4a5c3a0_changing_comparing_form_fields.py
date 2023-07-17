"""Changing comparing form fields.

Revision ID: 6d72f4a5c3a0
Revises: 446e73d62c97
Create Date: 2021-04-29 15:48:09.360086

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
revision = '6d72f4a5c3a0'
down_revision = '446e73d62c97'
branch_labels = None
depends_on = None


COMPARING_ID = 4052
COMPARING_FORM_ID = 4053


all_commands = [
    ("""UPDATE operation_form_field SET `suggested_widget` = 'expression' WHERE id = 4396""",
     """UPDATE operation_form_field SET `suggested_widget` = 'attribute-selector' WHERE id = 4396"""),

    ("""UPDATE operation_form_field SET `values` = '{"alias": false}' WHERE id = 4396""",
     """UPDATE operation_form_field SET `values` = NULL WHERE id = 4396"""),

    ("""UPDATE operation_form_field SET `name` = 'expression' WHERE id = 4396""",
     """UPDATE operation_form_field SET `name` = 'attributes' WHERE id = 4396"""),

    ("""UPDATE operation_form_field_translation SET `label` = 'Filter expression (advanced)' WHERE id = 4396 AND `locale` LIKE 'en'""",
     """UPDATE operation_form_field_translation SET `label` = 'Attributes' WHERE id = 4396 AND `locale` LIKE 'en'"""),

    ("""UPDATE operation_form_field_translation SET `label` = 'Expressão para filtro (avançado)' WHERE id = 4396 AND `locale` LIKE 'pt'""",
     """UPDATE operation_form_field_translation SET `label` = 'Atributos' WHERE id = 4396 AND `locale` LIKE 'pt'"""),

    ("""UPDATE operation_form_field SET `required` = 0 WHERE id IN (4397, 4398)""",
     """UPDATE operation_form_field SET `required` = 1 WHERE id IN (4397, 4398)"""),
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
