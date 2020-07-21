"""updating sliding window

Revision ID: 05985c3f83ca
Revises: 95394e5f8107
Create Date: 2020-06-25 10:21:42.423298

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '05985c3f83ca'
down_revision = '95394e5f8107'
branch_labels = None
depends_on = None

FORM_ID = 138


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
        [519, 'window_gap', 'INTEGER', 0, 4, 1, 'integer', None, None,
         'EXECUTION', FORM_ID],
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
        [519, 'pt', 'Tamanho da Janela de Previsão',
         'Define o tamanho da janela (> 0) entre os dados de treinamento'
         ' e a variável a ser predita.'],
        [519, 'en', 'Forecast Window',
         'Defines the size of the window (> 0) between the training data '
         'and the variable to be predicted.'],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ('UPDATE operation_form_field_translation '
     'SET label = "Deslocamento (tamanho do passo)" '
     'WHERE id = 517 and locale = "pt"', "SELECT 1"),
    ('UPDATE operation_form_field SET name = "window_pass" WHERE id = 517',
     'UPDATE operation_form_field SET name = "window_gap" WHERE id = 517'),
    ('UPDATE operation_form_field SET `order`=5 WHERE id=518',
     'UPDATE operation_form_field SET `order`=4 WHERE id=518'),
    (_insert_operation_form_field,
     "DELETE from operation_form_field WHERE id = 519"),
    (_insert_operation_form_field_translation,
     "DELETE from operation_form_field_translation WHERE id = 519"),

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
