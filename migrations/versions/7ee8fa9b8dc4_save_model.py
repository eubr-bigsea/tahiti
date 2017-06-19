# -*- coding: utf-8 -*-
"""save_model

Revision ID: 7ee8fa9b8dc4
Revises: 0228939b09d1
Create Date: 2017-06-19 12:10:52.849002

"""
import json

from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '7ee8fa9b8dc4'
down_revision = '0228939b09d1'
branch_labels = None
depends_on = None

OPERATION_ID = 39
FORM_ID = 100


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
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (OPERATION_ID, FORM_ID),
    ]
    rows = [dict(zip(columns, row)) for row in data]

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
    rows = [dict(zip(columns, row)) for row in data]

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

    columns = [c.name for c in tb.columns]

    options = [{"key": "BEST", "value": "Save best model"},
               {"key": "WORST", "value": "Save worst model"},
               {"key": "ALL",
                "value": "Save all (names will be suffixed with model rank)"},
               ]

    data = [
        (233, 'storage', 'INTEGER', 1, 1, None, 'lookup',
         '{{LIMONERO_URL}}/models', None, 'EXECUTION', FORM_ID),

        (234, 'name', 'TEXT', 1, 2, None, 'text',
         None, None, 'EXECUTION', FORM_ID),

        (235, 'save_criteria', 'TEXT', 1, 3, 'BEST', 'dropdown',
         None, json.dumps(options), 'EXECUTION', FORM_ID),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _fix_port_interface():
    op.execute('DELETE FROM operation_port_interface_operation_port WHERE '
               'operation_port_id = 83 AND operation_port_interface_id = 5')
    op.execute(
        'DELETE FROM operation_port_interface_operation_port WHERE '
        'operation_port_id = 100 AND operation_port_interface_id IN (2, 19)')
    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(100, 8)')

    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(100, 2)')
    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(100, 18)')

    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(83, 2)')
    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(83, 18)')
    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(100, 2)')
    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(100, 18)')

    op.execute("UPDATE operation_port_interface_translation "
               "SET name = 'IListOfMachineLearningModels' WHERE id = 8")

    op.execute("UPDATE operation_port SET multiplicity = 'MANY' WHERE id = 83")


def undo_fix_port_interface():
    op.execute(
        'DELETE FROM operation_port_interface_operation_port WHERE '
        'operation_port_id = 100 AND operation_port_interface_id IN (8)')

    op.execute(
        'DELETE FROM operation_port_interface_operation_port WHERE '
        'operation_port_id = 83 AND operation_port_interface_id IN (2, 18)')

    op.execute(
        'DELETE FROM operation_port_interface_operation_port WHERE '
        'operation_port_id = 100 AND operation_port_interface_id IN (2, 18)')

    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(83, 5)')
    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(100, 2)')
    op.execute('INSERT INTO operation_port_interface_operation_port '
               'VALUES(100, 19)')
    op.execute("UPDATE operation_port_interface_translation "
               "SET name = 'IListOfClassificationModels' WHERE id = 8")
    op.execute("UPDATE operation_port SET multiplicity = 'ONE' WHERE id = 83")


def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (233, 'en', 'Storage', 'Storage'),
        (233, 'pt', 'Armazenamento', 'Armazenamento'),

        (234, 'en', 'Model name', 'Model name'),
        (234, 'pt', 'Nome do modelo', 'Nome do modelo'),

        (235, 'en', 'Which model to save? (required if many models)',
         'Which model to save.'),
        (235, 'pt', 'Qual modelo salvar? (obrigatório se vários modelos)',
         'Qual modelo salvar.'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_fix_port_interface, undo_fix_port_interface),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {0} AND {0}'.format(FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id BETWEEN {0} AND {0}'.format(OPERATION_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation '
     '  WHERE id BETWEEN {0} AND {0}'.format(FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field '
     'WHERE form_id BETWEEN {0} AND {0}'.format(FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id BETWEEN {0} AND {0})'.format(FORM_ID)),
]


def upgrade():
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in all_commands:
            cmd[0]()
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise


def downgrade():
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in reversed(all_commands):
            if callable(cmd[1]):
                cmd[1]()
            else:
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
