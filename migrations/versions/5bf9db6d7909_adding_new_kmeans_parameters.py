"""adding new kmeans parameters

Revision ID: 5bf9db6d7909
Revises: a13c4b5cc25f
Create Date: 2020-10-15 10:01:50.734058

"""
from alembic import context, op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import json

# revision identifiers, used by Alembic.
revision = '5bf9db6d7909'
down_revision = 'a13c4b5cc25f'
branch_labels = None
depends_on = None

OFFSET_FIELD = 582
FORM_KMEANS = 27
FORM_KMODES = 152


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
            column('form_id', Integer),
            column('enable_conditions', String),
    )
    data = [
        [OFFSET_FIELD, 'distance', 'TEXT', 0, 9, 'euclidean',
         "dropdown", None,  json.dumps([
                   {'key': 'euclidean', 'value': 'Euclidean'},
                   {'key': 'cosine', 'value': 'Cosine'},
               ]), "EXECUTION", FORM_KMEANS, None],

        [OFFSET_FIELD+1, 'fragmentation', 'INTEGER', 0, 9, None, 'checkbox',
         None, None, 'EXECUTION', FORM_KMODES, None],
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
        [OFFSET_FIELD, "en", "Distance Measure", "The distance measure"],
        [OFFSET_FIELD, "pt", "Medida de distância", "A medida de distância"],

        [OFFSET_FIELD+1, "en", "Reduce fragmentation",
         "If enabled, it will reduce the parallelization in favor of the "
         "ability to handle small databases."],
        [OFFSET_FIELD+1, "pt", "Reduzir a fragmentação",
         "Se ativado, irá reduzir a paralelização em favor da capacidade de "
         "lidar com pequenas bases"],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation_form_field, """DELETE FROM operation_form_field
         WHERE id BETWEEN {} AND {}""".format(OFFSET_FIELD, OFFSET_FIELD+1)),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN {} AND {}'
     .format(OFFSET_FIELD, OFFSET_FIELD+1)),
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
