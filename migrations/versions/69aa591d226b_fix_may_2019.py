# coding=utf-8
"""fix_may_2019

Revision ID: 69aa591d226b
Revises: f39f7e2623e3
Create Date: 2019-04-29 08:32:43.723078

"""
import json

import pymysql
from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '69aa591d226b'
down_revision = 'f39f7e2623e3'
branch_labels = None
depends_on = None

all_commands = [
    (
        """INSERT IGNORE INTO operation_form_field_translation
            (id, locale, label, `help`) VALUES
            (125, 'pt', 'Frequência mínima nos documentos (DF)',
                'Frequência mínima nos documentos (DF)')
        """, ''
    ),
    (
        """
        UPDATE operation_form_field_translation
        SET label = 'Atributo de saída', `HELP` = 'Atributo de saída'
        WHERE id = 422 AND locale = 'pt'
        """
        , ''

    )
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()
    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
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
            if isinstance(cmd[1], (unicode, str)):
                if cmd[1]:
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
