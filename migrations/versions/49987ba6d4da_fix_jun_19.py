# coding=utf-8
"""fix_jun_19

Revision ID: 49987ba6d4da
Revises: a569f5a6c2d8
Create Date: 2019-07-03 11:15:41.884077

"""
from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '49987ba6d4da'
down_revision = 'a569f5a6c2d8'
branch_labels = None
depends_on = None

all_commands = [
    (""" ALTER TABLE operation CHANGE `cssClass` `css_class` VARCHAR(200);""",
     """ ALTER TABLE operation CHANGE `css_class` `cssClass` VARCHAR(200);"""),

    (""" UPDATE platform SET enabled = 0 WHERE id = 2""",
     """ UPDATE platform SET enabled = 1 WHERE id = 2""")
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
