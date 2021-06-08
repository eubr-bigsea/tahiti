""" Add Cast operation  

Revision ID: ea5b31a667ff
Revises: faf6f1c74416
Create Date: 2021-02-22 19:49:56.634787

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import sqlalchemy as sa
import json


# revision identifiers, used by Alembic.
revision = 'ea5b31a667ff'
down_revision = 'faf6f1c74416'
branch_labels = None
depends_on = None

CAST_OP_ID = 140
ALL_OPS = [CAST_OP_ID]
BASE_PORT_ID = 325
BASE_FORM_ID = 153
BASE_FORM_FIELD_ID = 584

def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', String),
        column('type', String), 
        column('icon', String), 
        column('css_class', String), 
        )

    rows = [
            (CAST_OP_ID, 'cast', 1, 'TRANSFORMATION', ' ', None),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)

def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (CAST_OP_ID, 'en', 'Change data types',
         'Allow to change attribute type (casting).'),
        (CAST_OP_ID, 'pt', 'Alterar tipos de dados',
         'Permite alterar o tipo de um ou mais atributos.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [(CAST_OP_ID, 1), (CAST_OP_ID, 4)]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String))

    new_id = BASE_PORT_ID
    rows = []
    for op_id in ALL_OPS:
        new_id += 1
        rows.append([new_id, 'OUTPUT', None, op_id, 1, 'MANY', 'output data'])
        new_id += 1
        rows.append([new_id, 'INPUT', None, op_id, 1, 'ONE', 'input data'])

    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]
    op.bulk_insert(tb, rows)
    
def _insert_operation_port_translation():    

    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )
    new_id = BASE_PORT_ID
    data = []
    for op_id in ALL_OPS:
        new_id += 1
        data.append([new_id, 'en', 'output data', 'Output data'])
        data.append([new_id, 'pt', 'dados de saída', 'Dados de saída'])
        new_id += 1
        data.append([new_id, 'en', 'input data', 'Input data'])
        data.append([new_id, 'pt', 'dados de entrada', 'Dados de entrada'])

    
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    
    base_id_port = BASE_PORT_ID
    new_id = base_id_port

    data = []
    for op_id in ALL_OPS:
        new_id += 1
        data.append([new_id, 1])
        new_id += 1
        data.append([new_id, 1])

    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = []
    for op_id in ALL_OPS:
        data.append([op_id, 7])
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]

    form_id = BASE_FORM_ID + 1
    data = []
    for op_id in ALL_OPS:
        data.append([form_id, 1, 1, 'execution'])
        form_id += 1

    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]

    form_id = BASE_FORM_ID + 1
    data = []
    for op_id in ALL_OPS:
        data.append([op_id, 41]) # appearance
        data.append([op_id, 110]) # result/reports
        data.append([op_id, form_id])
        form_id += 1
    
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

    form_id = BASE_FORM_ID + 1
    data = []
    for op_id in ALL_OPS:
        data.append([form_id, 'en', 'Execution'])
        data.append([form_id, 'pt', 'Execução'])
        form_id += 1

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
        column('enable_conditions', String),
        column('form_id', Integer), )

    types = [
            {"en": "Array", "value": "Array", "key": "Array", "pt": "Array"},
            {"en": "Boolean", "value": "Boolean", "key": "Boolean", "pt": "Booleano (lógico)"},
            {"en": "Date", "value": "Date", "key": "Date", "pt": "Data"},
            {"en": "Decimal", "value": "Decimal", "key": "Decimal", "pt": "Decimal"},
            {"en": "Integer", "value": "Integer", "key": "Integer", "pt": "Inteiro"},
            {"en": "JSON", "value": "JSON", "key": "JSON", "pt": "JSON"},
            {"en": "Time", "value": "Time", "key": "Time", "pt": "Hora"},
    ]
    errors = [
        {"en": "Coerce value (invalid become null)", "value": "coerce", "key": "coerce", "pt": "Forçar conversão (inválidos viram nulo)"},
        {"en": "Fail", "value": "raise", "key": "raise", "pt": "Falhar"},
        {"en": "Ignore value (may cause errors)", "value": "ignore", "key": "ignore", "pt": "Ignorar valor (pode causar erros)"},
    ]

    data = [
        # CAST_OP_ID
        [585, 'attributes', 'TEXT', 0, 0, None, 'cast', None, json.dumps(types), 'EXECUTION', None, 
            BASE_FORM_ID + 1],
        [586, 'errors', 'TEXT', 0, 0, None, 'dropdown', None, json.dumps(errors), 'EXECUTION', None, 
            BASE_FORM_ID + 1],
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
        # Indicator
        [585, 'en', 'Attributes', 'Attributes to change their types.'],
        [585, 'pt', 'Atributos', 'Atributos que terão o seu tipo alterado.'],
        [586, 'en', 'Action if error', 'Action to be taken in case of error.'],
        [586, 'pt', 'Ação em caso de erro', 'Ação a ser tomada em caso de erro.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN {s} AND {e}'.format(s=CAST_OP_ID, e=CAST_OP_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {s} AND {e}'.format(s=CAST_OP_ID, e=CAST_OP_ID)),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {e}'.format(s=CAST_OP_ID, e=CAST_OP_ID)),

    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE operation_id BETWEEN {s} AND {e})'.format(s=CAST_OP_ID, e=CAST_OP_ID)),

    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {e})'.format(s=CAST_OP_ID, e=CAST_OP_ID)),


    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {s} AND {e}'.format(s=CAST_OP_ID, e=CAST_OP_ID)),

    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN {s} AND {e}'.format(s=CAST_OP_ID, e=CAST_OP_ID)),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {s} AND {e}'.format(
         s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {e} '.format(
                                           s=CAST_OP_ID, e=CAST_OP_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {s} AND {e} '.format(
         s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

     (_insert_operation_form_field, """DELETE FROM operation_form_field 
          WHERE form_id BETWEEN {s} AND {e}""".format(
              s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),
 
     (_insert_operation_form_field_translation,
      'DELETE FROM operation_form_field_translation WHERE id IN (' +
      'SELECT id FROM operation_form_field WHERE form_id BETWEEN {s} AND {e})'.format(
          s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

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
