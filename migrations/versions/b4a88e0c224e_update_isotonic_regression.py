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



all_commands = [
    ("""UPDATE operation_form_field SET enable_conditions = 'this.perform_cross_validation.internalValue === "1"' 
     WHERE id = 487""",
     """UPDATE operation_form_field SET enable_conditions = 'this.perform_cross_validation.internalValue === "1"' 
     WHERE id = 487"""),
    ("""UPDATE operation_form_field SET enable_conditions = 'this.perform_cross_validation.internalValue === "1"' 
     WHERE id = 488""",
     """UPDATE operation_form_field SET enable_conditions = 'this.perform_cross_validation.internalValue === "1"'
     WHERE id = 488"""),
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

