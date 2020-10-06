""" Adjusts sept 2020  

Revision ID: 6a299689ea75
Revises: 86699b2e6672
Create Date: 2020-09-02 15:26:43.422785

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import sqlalchemy as sa
import json

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a299689ea75'
down_revision = '86699b2e6672'
branch_labels = None
depends_on = None


BASE_FORM_ID = 152
BASE_FORM_FIELD_ID = 578

BASE_PORT_ID = 324
DATA_SOURCE = 139

ALL_OPS = [DATA_SOURCE]

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
            (DATA_SOURCE, 'data-source', 1, 'SHORTCUT', ' ', None),
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
        (DATA_SOURCE, 'en', 'Data source', 'Reads a data source.'),
        (DATA_SOURCE, 'pt', 'Fonte de dados', 'Lê uma fonte de dados.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [(op_id, 1) for op_id in ALL_OPS]
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
        # new_id += 1
        # rows.append([new_id, 'INPUT', None, op_id, 1, 'ONE', 'input data'])

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
        # new_id += 1
        # data.append([new_id, 'en', 'input data', 'Input data'])
        # data.append([new_id, 'pt', 'dados de entrada', 'Dados de entrada'])

    
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
        # new_id += 1
        # data.append([new_id, 1])

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
        data.append([op_id, 1])
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
        column('form_id', Integer), 
        column('editable', Integer), 
        )

    JOIN_TYPES = [
            {"en": "Inner join", "key": "inner", "value": "Inner join", "pt": "Inner join"}, 
            {"en": "Left outer join", "key": "left_outer", "value": "Left outer join", "pt": "Left outer join"}, 
            {"en": "Right outer join", "key": "right_outer", "value": "Right outer join", "pt": "Right outer join"}
    ]
    data = [
        # DATA SOURCE
        [BASE_FORM_ID + 1, 'data_source', 'INTEGER', 1, 0, None, 'lookup', 
            '`${LIMONERO_URL}/datasources?uiw=1&simple=true&list=true&enabled=1`', None, 'EXECUTION', None, 
            BASE_FORM_ID + 1, 0],

        # [571, 'join', 'TEXT', 0, 2, None, 'join-editor', None, None, 'EXECUTION', None, 
        #     BASE_FORM_ID + 1],
        # [572, 'join_type', 'TEXT', 0, 3, 'inner', 'dropdown', None, json.dumps(JOIN_TYPES), 'EXECUTION', None, 
        #     BASE_FORM_ID + 1],
        # [573, 'left_alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', None, 
        #     BASE_FORM_ID + 1],
        # [574, 'right_alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', None, 
        #     BASE_FORM_ID + 1],
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
        # Data Source
        [BASE_FORM_ID  + 1, 'en', 'Data source', 'Data source.'],
        [BASE_FORM_ID  + 1, 'pt', 'Fonte de dados', 'Fonte de dados.']
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [

     (
         "ALTER TABLE operation MODIFY COLUMN `type` enum('ACTION','SHUFFLE','TRANSFORMATION','VISUALIZATION', 'SHORTCUT') COLLATE utf8_unicode_ci NOT NULL",
         "ALTER TABLE operation MODIFY COLUMN `type` enum('ACTION','SHUFFLE','TRANSFORMATION','VISUALIZATION') COLLATE utf8_unicode_ci NOT NULL"
     ),
    (
          "ALTER TABLE operation_form_field ADD COLUMN editable TINYINT(1) NOT NULL DEFAULT 1",
          "ALTER TABLE operation_form_field DROP COLUMN editable",
     ),
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN {s} AND {e}'.format(s=DATA_SOURCE, e=DATA_SOURCE)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {s} AND {e}'.format(s=DATA_SOURCE, e=DATA_SOURCE)),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {e}'.format(s=DATA_SOURCE, e=DATA_SOURCE)),

    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE operation_id BETWEEN {s} AND {e})'.format(s=DATA_SOURCE, e=DATA_SOURCE)),

    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {e})'.format(s=DATA_SOURCE, e=DATA_SOURCE)),


    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {s} AND {e}'.format(s=DATA_SOURCE, e=DATA_SOURCE)),

    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN {s} AND {e}'.format(s=DATA_SOURCE, e=DATA_SOURCE)),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {s} AND {e}'.format(
         s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {e} '.format(
                                           s=DATA_SOURCE, e=DATA_SOURCE)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {s} AND {e}'.format(
         s=BASE_FORM_ID + 1 , e=BASE_FORM_ID + 1 + len(ALL_OPS))),

     (_insert_operation_form_field, """DELETE FROM operation_form_field 
          WHERE form_id BETWEEN {s} AND {e} """.format(
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
