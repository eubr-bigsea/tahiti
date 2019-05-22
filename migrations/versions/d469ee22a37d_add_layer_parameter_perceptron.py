# coding=utf-8
"""add_layer_parameter_perceptron

Revision ID: d469ee22a37d
Revises: e9fd11c0952a
Create Date: 2019-02-06 10:17:09.302118

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'd469ee22a37d'
down_revision = 'e9fd11c0952a'
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
        # Dense - units
        (476, 'layers', 'TEXT', 1, 1, '2,2,2', 'text', None, None,
         'EXECUTION', 68),
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

    columns = ('id', 'locale', 'label', 'help')
    data = [
        # Dense - kernel_constraint
        (476, 'en', 'Layers (inform sizes separated by commas)',
         'Sizes of layers from input layer to output layer '
         'E.g., "780, 100, 10" (without quotes) means 780 inputs, one hidden '
         'layer with 100 neurons and output layer of 10 neurons.'),

        # Dense - bias_constraint
        (476, 'pt', 'Camadas (informe os tamanhos separados por vírgula)',
         'Tamanho das camadas da camada de  entrada para a camada de saída.'
         'Ex.: "780, 100, 10" (sem aspas) significa 780 entradas, uma camada '
         'oculta com 100 neurônios e uma camada de saída com 10 neurônios.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 476 AND 476'),
    (_insert_operation_form_field_translation,
     '''DELETE FROM operation_form_field_translation
     WHERE id BETWEEN 476 AND 476'''),
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
