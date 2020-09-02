"""fixing vector disasemble

Revision ID: ed920c727112
Revises: 0206bdda81bc
Create Date: 2020-07-28 17:26:21.719685

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = 'ed920c727112'
down_revision = '0206bdda81bc'
branch_labels = None
depends_on = None


def _insert_operation_script():
    tb = table(
        'operation_script',
        column('id', Integer),
        column('type', String),
        column('enabled', Integer),
        column('body', String),
        column('operation_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        [71, 'JS_CLIENT', 1,
         "repeatFromAlias(task, 'alias', 'top_n');", 128],
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field set `required`=1 WHERE id = 522""",
     """UPDATE operation_form_field set `required`=0 WHERE id = 522"""),
    ("""UPDATE operation_form_field set `default`=1 WHERE id = 522""",
     """UPDATE operation_form_field set `default`=0 WHERE id = 522"""),
    (_insert_operation_script,
     'DELETE FROM operation_script WHERE operation_id = 128')
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()
    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                if cmd[0] != '':
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
                if cmd[1] != '':
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
