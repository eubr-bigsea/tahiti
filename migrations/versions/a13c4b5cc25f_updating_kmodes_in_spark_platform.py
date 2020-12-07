"""Updating Kmodes in Spark platform


Revision ID: a13c4b5cc25f
Revises: 6a299689ea75
Create Date: 2020-09-21 09:05:00.976893

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = 'a13c4b5cc25f'
down_revision = '6a299689ea75'
branch_labels = None
depends_on = None

OFFSET_FIELD = 579
OFFSET_FORM = 152
FORM_KMEANS = 27


def _insert_operation_form_field():
    tb = table(
        'operation_form_field',
        column('id', Integer),
        column('name', String),
        column('type', String),
        column('required', Integer),
        column('order', Integer),
        column('default', Text),
        column('suggested_widget', String),
        column('values_url', String),
        column('values', String),
        column('scope', String),
        column('form_id', Integer), )

    data = [

        [OFFSET_FIELD, 'max_local_iterations', 'INTEGER', 0, 7, 10, 'integer',
         None, None,  'EXECUTION', OFFSET_FORM],
        [OFFSET_FIELD+1, 'seed', 'INTEGER', 0, 8, None, 'integer',
         None, None, 'EXECUTION', OFFSET_FORM],
        [OFFSET_FIELD + 2, 'seed', 'INTEGER', 0, 8, None, 'integer',
         None, None, 'EXECUTION', FORM_KMEANS],

    ]
    columns = [c.name for c in tb.columns]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        [OFFSET_FIELD, "en", "Max iterations in Metamodes generation",
         "Maximum iterations in second step (Metamodes generation)"],
        [OFFSET_FIELD, "pt", "Número máx. de iterações na geração de Metamodes",
         "Número máximo de iterações na segunda etapa (geração de Metamodes)"],

        [OFFSET_FIELD + 1, "en", "Seed", "Seed"],
        [OFFSET_FIELD + 1, "pt", "Semente", "Semente aleatória"],

        [OFFSET_FIELD + 2, "en", "Seed", "Seed"],
        [OFFSET_FIELD + 2, "pt", "Semente", "Semente aleatória"],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation_form_field, """DELETE FROM operation_form_field
         WHERE id BETWEEN {} AND {}""".format(OFFSET_FIELD, OFFSET_FIELD+2)),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN {} AND {}'
     .format(OFFSET_FIELD, OFFSET_FIELD+2)),
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
