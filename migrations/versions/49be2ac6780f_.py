"""empty message

Revision ID: 49be2ac6780f
Revises: d5967e62d5c4
Create Date: 2018-07-25 14:17:04.132217

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = '49be2ac6780f'
down_revision = 'd5967e62d5c4'
branch_labels = None
depends_on = None

all_commands = [
    ("""
    INSERT operation_port_interface_operation_port VALUES (37, 14), (37, 20), (37, 4)
    """,
    """
    DELETE FROM operation_port_interface_operation_port
    WHERE operation_port_id = 37 AND operation_port_interface_id IN (14, 20, 4)
    """),
    ("UPDATE `operation_port_interface` SET color = '#ff7700' WHERE id = 4;",
     "UPDATE `operation_port_interface` SET color = '#FFDC00' WHERE id = 4;")
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
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
            if isinstance(cmd[1], str):
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
