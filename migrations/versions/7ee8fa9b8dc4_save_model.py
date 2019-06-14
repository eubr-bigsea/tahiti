# -*- coding: utf-8 -*-
"""save_model and voting classifier

Revision ID: 7ee8fa9b8dc4
Revises: 0228939b09d1
Create Date: 2017-06-19 12:10:52.849002

"""
import json

from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.sql import table, column, text
import collections

# revision identifiers, used by Alembic.
revision = '7ee8fa9b8dc4'
down_revision = '0228939b09d1'
branch_labels = None
depends_on = None

SAVE_MODEL_ID = 39
SAVE_MODEL_FORM_ID = 100

VOTING_CLASS_ID = 84
VOTING_CLASS_FORM_ID = 101


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (VOTING_CLASS_ID, 'voting-classifier', 1, 'TRANSFORMATION',
         'fa-hand-peace-o'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (VOTING_CLASS_ID, 'en', 'Voting classifier', 'Voting classifier'),
        (VOTING_CLASS_ID, 'pt', 'Classificador por votos',
         'Classificador por votos'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        (VOTING_CLASS_ID, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (SAVE_MODEL_FORM_ID, 1, 1, 'execution'),
        (VOTING_CLASS_FORM_ID, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (SAVE_MODEL_ID, SAVE_MODEL_FORM_ID),
        (VOTING_CLASS_ID, VOTING_CLASS_FORM_ID),
        (VOTING_CLASS_ID, 41),
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
        (SAVE_MODEL_FORM_ID, 'en', 'Execution'),
        (SAVE_MODEL_FORM_ID, 'pt', 'Execução'),

        (VOTING_CLASS_FORM_ID, 'en', 'Execution'),
        (VOTING_CLASS_FORM_ID, 'pt', 'Execução'),
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

    columns = [c.name for c in tb.columns]

    options = [{"key": "BEST", "value": "Save best model"},
               {"key": "ALL",
                "value": "Save all (names will be suffixed with model rank)"},
               ]

    data = [
        (233, 'storage', 'INTEGER', 1, 1, None, 'lookup',
         '{{LIMONERO_URL}}/models', None, 'EXECUTION', SAVE_MODEL_FORM_ID),

        (234, 'name', 'TEXT', 1, 2, None, 'text',
         None, None, 'EXECUTION', SAVE_MODEL_FORM_ID),

        (235, 'save_criteria', 'TEXT', 1, 3, 'BEST', 'dropdown',
         None, json.dumps(options), 'EXECUTION', SAVE_MODEL_FORM_ID),

        (236, 'weights', 'TEXT', 0, 3, None, 'text',
         None, None, 'EXECUTION', VOTING_CLASS_FORM_ID),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
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

    op.execute("UPDATE operation_port SET multiplicity = 'MANY' "
               "WHERE id = 83")


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

        (236, 'en', 'Weights (comma-separated, '
                    'if empty, all estimators will have same weight)',
         'Weights (if empty, all estimators will have same weight, otherwise, '
         'implies "soft" voting)'),
        (236, 'pt', 'Pesos (separados por vírgula, '
                    'se vazio, os estimadores terão o mesmo peso)',
         'Pesos (se vazio, os estimadores terão o mesmo peso).'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (VOTING_CLASS_ID, 1),
        (VOTING_CLASS_ID, 8),
        (VOTING_CLASS_ID, 18),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


#
def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (184, 'OUTPUT', None, VOTING_CLASS_ID, 1, 'MANY', 'output data'),
        (185, 'INPUT', None, VOTING_CLASS_ID, 2, 'MANY', 'models'),
        (186, 'INPUT', None, VOTING_CLASS_ID, 1, 'ONE', 'input data')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (184, 'en', 'output data', 'Output data'),
        (184, 'pt', 'dados de saída', 'Dados de saída'),
        (185, 'en', 'models', 'Input models'),
        (185, 'pt', 'models', 'Modelos de entrada'),
        (186, 'en', 'input data', 'Input data'),
        (186, 'pt', 'dados de entrada', 'Dados de entrada'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    data = [
        (184, 1),
        (185, 2),
        (185, 7),
        (186, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = {}'.format(VOTING_CLASS_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(VOTING_CLASS_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id = {}'.format(VOTING_CLASS_ID)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation WHERE operation_id = {}'.format(
         VOTING_CLASS_ID)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in (184, 185, 186)"),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in (184, 185, 186)"),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in (184, 185, 186)"),

    (_fix_port_interface, undo_fix_port_interface),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({0}, {1})'.format(
         SAVE_MODEL_FORM_ID, VOTING_CLASS_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0}, {1})'.format(SAVE_MODEL_ID, VOTING_CLASS_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({0}, {1})'.format(
         SAVE_MODEL_FORM_ID, VOTING_CLASS_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({0}, {1})'.format(
         SAVE_MODEL_FORM_ID, VOTING_CLASS_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({0}, {1}))'.format(SAVE_MODEL_FORM_ID,
                                              VOTING_CLASS_FORM_ID)),
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
            if isinstance(cmd[1], collections.Callable):
                cmd[1]()
            else:
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
