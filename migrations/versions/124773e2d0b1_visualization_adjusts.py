""" visualization_adjusts  

Revision ID: 124773e2d0b1
Revises: 253949e0710b
Create Date: 2020-07-07 21:54:15.862262

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import sqlalchemy as sa
import json

# revision identifiers, used by Alembic.
revision = '124773e2d0b1'
down_revision = '253949e0710b'
branch_labels = None
depends_on = None

FORM_ID = 141
FORM_FIELD_RANGE = [524, 525]


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (FORM_ID, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String)
    )

    columns = [c.name for c in tb.columns]
    data = [
        (FORM_ID, 'en', 'Execution'),
        (FORM_ID, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


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
        [527, 'grid_coordinates', 'TEXT', 0, 20, None,
         'grid-coordinates', None, None, 'EXECUTION', FORM_ID],
        [528, 'command', 'TEXT', 0, 22, None,
         'code', None, json.dumps({"language": "javascript"}), 'EXECUTION', FORM_ID],
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
        [527, 'en', 'Grid coordinates', 'If generating dashboards, where to include the visualization. Grid has 12 columns and unlimited number of rows.'],
        [527, 'pt', 'Coordenadas da grade', 'Se a visualização é usada em um dashboard, em qual coordenada da grade ela deve ser incluída. A grade tem 12 colunas e um número ilimitado de linhas.'],
        [528, 'en', 'Command executed on click', 'Command executed if user clicks a point in the visualization.'],
        [528, 'pt', 'Comando executado no clique', 'Comando executado se o usuário clica um ponto na visualização.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {f} AND {f}'.format(f=FORM_ID)),

    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {f} AND {f}'.format(f=FORM_ID)),

    (_insert_operation_form_field, """DELETE FROM operation_form_field
         WHERE form_id BETWEEN {f} AND {f}""".format(f=FORM_ID)),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (' +
     'SELECT id FROM operation_form_field WHERE form_id BETWEEN {f} AND {f})'.format(f=FORM_ID)),
    ( """
        INSERT INTO operation_operation_form VALUES
        (35, {f}),
        (68, {f}),
        (69, {f}),
        (60, {f}),
        (70, {f}),
        (71, {f}),
        (72, {f}),
        (80, {f}),
        (81, {f}),
        (87, {f}),
        (88, {f}),
        (89, {f}),
        (123, {f}),
        (123, {f})
        """.format(f=FORM_ID), 
     'DELETE FROM operation_operation_form WHERE operation_form_id = {}'.format(FORM_ID)
     )
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
