# -*- coding: utf-8 -*-}
"""refactoring ml operations

Revision ID: d653bb706444
Revises: 7ee8fa9b8dc4
Create Date: 2017-06-20 12:03:14.342069

"""
import json

from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.sql import table, column, text
import collections

# revision identifiers, used by Alembic.
revision = 'd653bb706444'
down_revision = '7ee8fa9b8dc4'
branch_labels = None
depends_on = None

OPERATION_ID = 39
FORM_ID = 100
FORM_ID_2 = 52


def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = [c.name for c in tb.columns]
    data = [
        (18, 'pt', 'Classificação'),
        (19, 'pt', 'Agrupamento'),
        (20, 'pt', 'Recomendação'),
        (21, 'pt', 'Regressão'),
        (22, 'pt', 'Associativa'),
        (23, 'pt', 'Extração de features'),
        (24, 'pt', 'Afinação (tunning)'),
        (25, 'pt', 'Avaliação'),
        (26, 'pt', 'Modelos'),
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

    options = [{"key": "OVERWRITE", "value": "Overwrite"},
               {"key": "ERROR", "value": "Raise error"},
               ]

    data = [
        (237, 'write_mode', 'TEXT', 1, 3, 'ERROR', 'dropdown',
         None, json.dumps(options), 'EXECUTION', FORM_ID),
        (238, 'prediction', 'TEXT', 1, 1, 'prediction', 'text',
         None, None, 'EXECUTION', FORM_ID_2),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _undo_insert_operation_form_field():
    op.execute(text('DELETE FROM operation_form_field WHERE id IN (237, 238)'))


all_commands = [

    # Update missing translation
    (_insert_operation_category_translation,
     "DELETE FROM operation_category_translation WHERE locale = 'pt' AND "
     "id BETWEEN 18 AND 26"),
    # Disable score model operation
    ('UPDATE operation SET enabled = 0 WHERE id IN (14, 22, 2, 54) ',
     'UPDATE operation SET enabled = 1 WHERE id IN (14, 22, 2, 54) '),

    ("UPDATE operation_form_field SET values_url = '{{LIMONERO_URL}}/storages' "
     "WHERE id IN (233) ",
     "UPDATE operation_form_field SET values_url = '{{LIMONERO_URL}}/models' "
     "WHERE id IN (233) "),

    # Change metric port from evaluate model to 'evaluated model'
    ("UPDATE operation_port SET slug = 'evaluated model' WHERE id = 39",
     "UPDATE operation_port SET slug = 'metric' WHERE id = 39"),

    ("UPDATE operation_port_translation SET name = 'evaluated model', "
     "description = 'Evaluated model' WHERE id = 39 and locale = 'en'",
     "UPDATE operation_port_translation SET name = 'metric', "
     "description ='Metric used for evaluation' "
     "WHERE id = 39 and locale = 'en'"),

    ("UPDATE operation_port_translation SET name = 'modelo avaliado', "
     "description = 'Modelo avaliado' WHERE id = 39 and locale = 'pt'",
     "UPDATE operation_port_translation SET name = 'metric', "
     "description ='Métrica usada para a avaliação' "
     "WHERE id = 39 and locale = 'pt'"),

    # Associate port interface
    ("UPDATE operation_port_interface_operation_port "
     "SET operation_port_interface_id = 7 "
     "WHERE operation_port_interface_id = 9 AND operation_port_id = 39",
     "UPDATE operation_port_interface_operation_port "
     "SET operation_port_interface_id = 9 "
     "WHERE operation_port_interface_id = 7 AND operation_port_id = 39",
     ),

    # Change evaluation port from CrossValidationOperation to 'best model'
    ("UPDATE operation_port SET slug = 'best model' WHERE id = 98",
     "UPDATE operation_port SET slug = 'evaluation' WHERE id = 98"),

    ("UPDATE operation_port_translation SET name = 'best model', "
     "description = 'Best model generated' WHERE id = 98 and locale = 'en'",
     "UPDATE operation_port_translation SET name = 'evaluation', "
     "description ='Evaluation' "
     "WHERE id = 98 and locale = 'en'"),

    ("UPDATE operation_port_translation SET name = 'modelo avaliado', "
     "description = 'Melhor modelo' WHERE id = 98 and locale = 'pt'",
     "UPDATE operation_port_translation SET name = 'metric', "
     "description ='Avaliação' WHERE id = 98 and locale = 'pt'"),

    # Associate port interface
    ("UPDATE operation_port_interface_operation_port "
     "SET operation_port_interface_id = 7 "
     "WHERE operation_port_interface_id = 9 AND operation_port_id = 98",
     "UPDATE operation_port_interface_operation_port "
     "SET operation_port_interface_id = 9 "
     "WHERE operation_port_interface_id = 7 AND operation_port_id = 98",
     ),

    # Reuse existing interface, currently not being used
    ("UPDATE operation_port_interface_translation "
     "SET name = 'ModelWithEvaluation' WHERE id = 7",
     "UPDATE operation_port_interface_translation "
     "SET name = 'IFold' WHERE id = 7"),

    # Associate new interface to SaveModel operation's models port
    ("INSERT INTO operation_port_interface_operation_port "
     "VALUES(83, 7)",
     'DELETE FROM operation_port_interface_operation_port '
     '  WHERE operation_port_id = 83 AND operation_port_interface_id = 7'),

    # Associate appearance form to Save Model
    ("INSERT INTO  operation_operation_form VALUES(39, 41)",
     'DELETE FROM operation_operation_form'
     '  WHERE operation_id = 39 AND operation_form_id = 41'),

    # Save Model now have a parameter write_mode
    (_insert_operation_form_field, _undo_insert_operation_form_field),

    ("INSERT INTO operation_form_field_translation "
     "VALUES(237, 'en', 'Action if model exists', 'Action if model exists')",
     "DELETE FROM operation_form_field_translation "
     "WHERE id = 237 AND locale='en'"),

    ("INSERT INTO operation_form_field_translation "
     "VALUES(237, 'pt', 'Ação caso modelo já exista', "
     "'Ação caso modelo já exista')",
     "DELETE FROM operation_form_field_translation "
     "WHERE id = 237 AND locale='pt'"),

    ("INSERT INTO operation_form_field_translation "
     "VALUES(238, 'en', 'Prediction attribute name (new)', "
     "'Prediction attribute name (new)')",
     "DELETE FROM operation_form_field_translation "
     "WHERE id = 238 AND locale='en'"),

    ("INSERT INTO operation_form_field_translation "
     "VALUES(238, 'pt', 'Atributo com a predição (novo)', "
     "'Atributo com a predição (novo)')",
     "DELETE FROM operation_form_field_translation "
     "WHERE id = 238 AND locale='pt'"),

    # Adjust Apply Model interfaces
    ("DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_interface_id = 6 AND `operation_port_id` = 93;",
     "INSERT INTO operation_port_interface_operation_port VALUES (93, 6)"),

    ("INSERT INTO operation_port_interface_operation_port VALUES (93, 2)",
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_interface_id = 2 AND `operation_port_id` = 93;"),

    ("INSERT INTO operation_port_interface_operation_port VALUES (93, 18)",
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_interface_id = 18 AND `operation_port_id` = 93;"),
    ("UPDATE operation_form_field SET `default` = 'ALL' WHERE id = 235",
     "UPDATE operation_form_field SET `default` = 'BEST' WHERE id = 235"),

    ("INSERT operation_category_operation(operation_id, operation_category_id) "
     "  VALUES (39, 8);",
     "DELETE FROM operation_category_operation "
     "WHERE operation_id = 39 AND operation_category_id = 8"),

    ("INSERT operation_category_operation(operation_id, operation_category_id) "
     "  VALUES (39, 26);",
     "DELETE FROM operation_category_operation "
     "WHERE operation_id = 39 AND operation_category_id = 26"),
]


def upgrade():
    last = ''
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in all_commands:
            assert isinstance(cmd, tuple)
            last = cmd[0]
            if isinstance(cmd[0], collections.Callable):
                cmd[0]()
            else:
                op.execute(text(cmd[0]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        print('-' * 20)
        print('Last', last)
        print('-' * 20)
        raise


def downgrade():
    last = ''
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in reversed(all_commands):
            last = cmd[1]
            if isinstance(cmd[1], collections.Callable):
                cmd[1]()
            else:
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        print('-' * 20)
        print('Last', last)
        print('-' * 20)
        raise
