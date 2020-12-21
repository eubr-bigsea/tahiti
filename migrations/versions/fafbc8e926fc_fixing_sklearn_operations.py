"""Fixing sklearn operations.

Revision ID: fafbc8e926fc
Revises: faf6f1c74416
Create Date: 2020-12-21 15:58:29.018770

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
revision = 'fafbc8e926fc'
down_revision = 'faf6f1c74416'
branch_labels = None
depends_on = None

all_commands = [
    ("""DELETE FROM operation_form_field_translation WHERE id = 3014""",
     """
     INSERT INTO operation_form_field ("id","locale","label","help") VALUES
    ("3014","en","k neighbors","It's is a positive integer typically small 
    which represents a number of neighbors to be used in the classification."),
    ("3014","pt","k vizinhos","Número inteiro positivo geralmente pequeno que 
    representa a quantidade de vizinhos para a classificação."),
     """),
    ("""DELETE FROM operation_form_field WHERE id = 3014""",
     """
     INSERT INTO operation_form_field ("id","name","type","required","order",
     "default","suggested_widget","values_url","values","scope","form_id",
     "enable_conditions","editable") VALUES (3014,"k","INTEGER",1,1,5,
     "integer",NULL,NULL,"EXECUTION",3005,NULL,1)
     """),
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