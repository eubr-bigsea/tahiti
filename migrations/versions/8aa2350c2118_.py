# coding=utf-8
"""empty message

Revision ID: 8aa2350c2118
Revises: 06a74bba9db8
Create Date: 2017-09-28 13:33:13.361476

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '8aa2350c2118'
down_revision = '06a74bba9db8'
branch_labels = None
depends_on = None


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

    columns = [c.name for c in tb.columns]

    data = [
        [366, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector',
         None, None, 'EXECUTION', 33],
        [367, 'value', 'TEXT', 1, 1, None, 'text', None, None,
         'EXECUTION', 33],
        [368, 'replacement', 'TEXT', 1, 2, None, 'text', None, None,
         'EXECUTION', 33],
    ]
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
        [366, 'en', 'Attributes',
         'Attributes in which the operation of replacement will be applied.'],
        [366, 'pt', 'Atributos',
         'Atributos onde a operação de substituição será aplicada.'],
        [367, 'en', 'Value to be replaced', 'Value to be replaced.'],
        [367, 'pt', 'Valor a ser substituído', 'Valor a ser substituído.'],
        [368, 'en', 'Replacement',
         'Replacement for the value.'],
        [368, 'pt', 'Substituir por', 'Valor usado para substituir.'],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     """DELETE FROM operation_form_field
        WHERE (form_id BETWEEN 33 AND 33)"""),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE (form_id BETWEEN 33 AND 33))'),
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
