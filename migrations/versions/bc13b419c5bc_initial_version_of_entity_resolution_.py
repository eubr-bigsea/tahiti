"""Initial version of entity resolution operations

Revision ID: bc13b419c5bc
Revises: a73c21a49894
Create Date: 2021-03-18 15:57:57.978549

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
revision = 'bc13b419c5bc'
down_revision = 'a73c21a49894'
branch_labels = None
depends_on = None

OPERATION_ID = 4003
SCIKIT_LEARN_PLATAFORM_ID = 4

def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')

    data = [
        (OPERATION_ID, SCIKIT_LEARN_PLATAFORM_ID)
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
        (OPERATION_ID, "group", 0, 0),
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
        (OPERATION_ID, "pt", 'Resolução de entidades'),
        (OPERATION_ID, "en", 'Entity resolution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id = {}'.format(OPERATION_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = {}'.format(OPERATION_ID)),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id = {}'.format(OPERATION_ID)),
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
