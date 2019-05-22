"""fix_form_fields

Revision ID: 790ae4e8f5d6
Revises: 31fdc250f191
Create Date: 2018-04-17 14:49:15.288466

"""

from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '790ae4e8f5d6'
down_revision = 'db303e910542'
branch_labels = None
depends_on = None

all_commands = [
    ("""
        UPDATE operation_form_field SET
        `values_url`='`${LIMONERO_URL}/datasources?format=SHAPEFILE&simple=true&list=true&enabled=1`'
        WHERE id = 133
        """,
     """
        UPDATE operation_form_field SET
        `values_url` ='`${LIMONERO_URL}/datasources?format=SHAPEFILE'
        WHERE id = 133
    """,),
    ("""
    INSERT IGNORE INTO
        operation_operation_form(operation_id, operation_form_id)
        VALUES (96, 110);
    """,
     """
     DELETE FROM operation_operation_form WHERE operation_form_id = 110 AND
        operation_id = 96
     """),
    ("""
    INSERT IGNORE INTO
        operation_operation_form(operation_id, operation_form_id)
        VALUES (2, 110);
    """,
     """
     DELETE FROM operation_operation_form WHERE operation_form_id = 110 AND
        operation_id = 2
     """),

    ("DELETE FROM operation_form_field_translation WHERE id = 153",
     "SELECT 1"),
    ("DELETE FROM operation_form_field WHERE id = 153", 'SELECT 1'),
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
    connection.execute('SET foreign_key_checks = 0;')

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
    connection.execute('SET foreign_key_checks = 1;')
    session.commit()
