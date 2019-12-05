"""Add fields on SVM Classifier at scikit learn.

Revision ID: 4c1ebd8863a8
Revises: ba0fe62f7174
Create Date: 2019-11-04 16:20:48.481455

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json

# revision identifiers, used by Alembic.
revision = '4c1ebd8863a8'
down_revision = 'ba0fe62f7174'
branch_labels = None
depends_on = None

SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4031

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

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
	
    data = [
        (4178, 'gamma', 'DECIMAL', 0, 7, 'auto', 'decimal', None, None, 'EXECUTION', 4011, None),
        (4179, 'coef0', 'DECIMAL', 0, 8, 0.0, 'decimal', None, None, 'EXECUTION', 4011, None),
        (4180, 'shrinking', 'INTEGER', 0, 9, 1, 'checkbox', None, None, 'EXECUTION', 4011, None),
        (4181, 'probability', 'INTEGER', 0, 10, 0, 'checkbox', None, None, 'EXECUTION', 4011, None),
        (4182, 'cache_size', 'DECIMAL', 0, 11, 200, 'decimal', None, None, 'EXECUTION', 4011, None),
        (4183, 'decision_function_shape', 'TEXT', 0, 12, 'ovr', 'dropdown', None,
         json.dumps([
             {'key': 'ovr', 'value': 'ovr'},
             {'key': 'ovo', 'value': 'ovo'}
         ]),
         'EXECUTION', 4011, None)
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
        (4178, 'en', 'Kernel coefficient.', 'Kernel coefficient for "rbf", "poly" and "sigmoid".'),
        (4178, 'pt', 'Coeficiente do kernel.', 'Coeficiente do kernel para as métricas "rbf", "poly" e "sigmoid.'),

        (4179, 'en', 'Independent term in kernel function.', 'Independent term in kernel function. It is only significant in "poly" and "sigmoid".'),
        (4179, 'pt', 'Termo independente da função do kernel.', 'Termp independente da função do kernel. É significativo apenas nas métricas "poly" e "sigmoid".'),

        (4180, 'en', 'Use the shrinking heuristic.', 'Whether to use the shrinking heuristic.'),
        (4180, 'pt', 'Usar a heurística shrinking.', 'Necessidade de usar a heurística shrinking'),

        (4181, 'en', 'Enable probability estimates.', 'Whether to enable probability estimates.'),
        (4181, 'pt', 'Habilitar estimativas probailísticas.', 'Habilitar estimativas probailísticas.'),

        (4182, 'en', 'Size of the kernel cache (in MB).', 'Specify the size of the kernel cache (in MB).'),
        (4182, 'pt', 'Tamanho do cache em MB.', 'Especificação do tamanho do cache em MB.'),

        (4183, 'en', 'Return decision.', 'Return (one-vs-rest) "ovr" or (one-vs-one) "ovo" decision funcion.'),
        (4183, 'pt', 'Decisão de retorno.' , 'Decisão de retorno "ovr" (one-vs-rest : um por todos) ou "ovo" (one-vs-one: um por um).')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4178 AND 4183'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4178 AND 4183')

]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
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
