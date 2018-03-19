# coding: utf-8
"""window_operation

Revision ID: 47830b97d8d8
Revises: abc9192ljsj3
Create Date: 2018-03-18 11:18:44.840187
"""
import json

from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '47830b97d8d8'
down_revision = 'abc9192ljsj3'
branch_labels = None
depends_on = None

WINDOW_TRANSFORMATION_ID = 99
WINDOW_TRANSFORMATION_FORM_ID = 125

APPEARANCE_FORM_ID = 41
RESULTS_FORM_ID = 110


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (WINDOW_TRANSFORMATION_ID, 'window-transformation', 1,
         'TRANSFORMATION', 'fa-picture-o'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        (WINDOW_TRANSFORMATION_ID, 'en', 'Window transformation',
         'Window transformation'),
        (WINDOW_TRANSFORMATION_ID, 'pt', 'Transformação em janela',
         'Transformação em janela'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        (WINDOW_TRANSFORMATION_ID, 1),
    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        (WINDOW_TRANSFORMATION_FORM_ID, 1, 1, 'execution'),
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
        (WINDOW_TRANSFORMATION_ID, WINDOW_TRANSFORMATION_FORM_ID),
        (WINDOW_TRANSFORMATION_ID, APPEARANCE_FORM_ID),
        (WINDOW_TRANSFORMATION_ID, RESULTS_FORM_ID),
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
        (WINDOW_TRANSFORMATION_FORM_ID, 'en', 'Execution'),
        (WINDOW_TRANSFORMATION_FORM_ID, 'pt', 'Execução'),
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

    order_opts = {
        "functions": [
            {"key": "asc", "value": "Ascending", "help": "Ascending order"},
            {"key": "desc", "value": "Descending",
             "help": "Descending order"}
        ],
        "options": {
            "title": "Sort operation",
            "description": "Sort a data source by a set of attributes",
            "show_alias": False
        }
    }
    data = [
        (453, 'partition_attribute', 'TEXT', 1, 0, None, 'attribute-selector',
         None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        (454, 'order_by', 'TEXT', 0, 1, None, 'attribute-function',
         None, json.dumps(order_opts), 'EXECUTION',
         WINDOW_TRANSFORMATION_FORM_ID),
        (443, 'rows_from', 'TEXT', 0, 2, None, 'integer',
         None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        (444, 'rows_to', 'TEXT', 0, 3, None, 'integer',
         None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        (445, 'range_from', 'TEXT', 0, 4, None, 'text',
         None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        (446, 'range_to', 'TEXT', 0, 5, None, 'text',
         None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        (447, 'expressions', 'TEXT', 1, 6, None, 'expression',
         None, json.dumps({'multiple': True, "alias": True}), 'EXECUTION',
         WINDOW_TRANSFORMATION_FORM_ID),
        # (448, 'alias_1', 'TEXT', 0, 7, None, 'text',
        #  None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        # (449, 'expression_2', 'TEXT', 0, 8, None, 'expression',
        #  None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        # (450, 'alias_2', 'TEXT', 0, 9, None, 'text',
        #  None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        # (451, 'expression_3', 'TEXT', 0, 10, None, 'expression',
        #  None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),
        # (452, 'alias_3', 'TEXT', 0, 11, None, 'text',
        #  None, None, 'EXECUTION', WINDOW_TRANSFORMATION_FORM_ID),

    ]
    rows = [dict(zip(columns, row)) for row in data]
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
        (453, 'en', 'Partition attribute',
         'Attribute used to partition data in windows.'),
        (453, 'pt', 'Atributo de partição',
         'Atributo usado para particionar os dados nas janelas.'),

        (454, 'en', 'Order by attribute(s)',
         'Attribute(s) used to order rows in windows.'),
        (454, 'pt', 'Atributo(s) para ordenação',
         'Atributo(s) usado(s) para ordenar os dados nas janelas.'),

        (443, 'en', 'Rows before current (empty = unbounded)',
         'How many rows before current row will be used. Empty means all '
         'previous rows are used.'),
        (443, 'pt', 'Registros antes do atual (vazio = ilimitado)',
         'Quantos registros antes do registro atual serão suados. Vazio '
         'significa que todos os anteriores são usados.'),

        (444, 'en', 'Rows after current (empty = unbounded)',
         'How many rows after current row will be used. Empty means all '
         'following rows are used.'),
        (444, 'pt', 'Registros após o atual (vazio = ilimitado)',
         'Quantos registros após o registro atual serão suados. Vazio '
         'significa que todos os posteriores são usados.'),

        (445, 'en',
         'Inicial partition attribute value (included, empty = ignored)',
         'Initial value for partition attribute. Values smaller than this will '
         'be discarded.'),
        (445, 'pt',
         'Valor inicial para o atributo de partição (incluído, vazio=ignorado)',
         'Valor inicial para o atributo de partição. Valores menores que este '
         'serão ignorados.'),

        (446, 'en',
         'Final partition attribute value (included, empty = ignored)',
         'Final value for partition attribute. Values greater than this will '
         'be discarded.'),
        (446, 'pt',
         'Valor final para o atributo de partição (incluído, vazio=ignorado)',
         'Valor final para o atributo de partição. Valores maiores que este '
         'serão ignorados.'),

        (447, 'en', 'Expressions for new attributes',
         'Expressions will generate new attributes in resulting data.'),
        (447, 'pt', 'Expressões para novos atributos',
         'Expressões gerarão novos atributos no resultado.'),

        # (448, 'en', 'Alias 1', 'Name for attribute generated by expression 1.'),
        # (448, 'pt', 'Nome 1', 'Nome para o atributo gerado pela expressão 1.'),
        #
        # (449, 'en', 'Expression 2',
        #  'Expression 2 will generate a new attribute in resulting data.'),
        # (449, 'pt', 'Expressão 2',
        #  'Expressão 2 gerará um novo atributo no resultado.'),
        #
        # (450, 'en', 'Alias 2', 'Name for attribute generated by expression 2.'),
        # (450, 'pt', 'Nome 2', 'Nome para o atributo gerado pela expressão 2.'),
        #
        # (451, 'en', 'Expression 3',
        #  'Expression 3 will generate a new attribute in resulting data.'),
        # (451, 'pt', 'Expressão 3',
        #  'Expressão 3 gerará um novo atributo no resultado.'),
        #
        # (452, 'en', 'Alias 3', 'Name for attribute generated by expression 3.'),
        # (452, 'pt', 'Nome 3', 'Nome para o atributo gerado pela expressão 3.'),

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (WINDOW_TRANSFORMATION_ID, 2),
        (WINDOW_TRANSFORMATION_ID, 7),
    ]
    rows = [dict(zip(columns, cat)) for cat in data]

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
        (227, 'OUTPUT', None, WINDOW_TRANSFORMATION_ID, 1, 'MANY',
         'output data'),
        (228, 'INPUT', None, WINDOW_TRANSFORMATION_ID, 1, 'ONE',
         'input data'),
    ]
    rows = [dict(zip(columns, row)) for row in data]

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
        (227, 'en', 'output data', 'Output data'),
        (227, 'pt', 'dados de saída', 'Dados de saída'),
        (228, 'en', 'input data', 'Input data'),
        (228, 'pt', 'dados de entrada', 'Dados de entrada'),

    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    data = [
        (227, 1),
        (228, 1),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({})'.format(
         WINDOW_TRANSFORMATION_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({})'.format(
         WINDOW_TRANSFORMATION_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({})'.format(
         WINDOW_TRANSFORMATION_ID)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({})'.format(WINDOW_TRANSFORMATION_ID)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in (227, 228)"),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in "
     "(227, 228)"),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in (227, 228)"),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({})'.format(
         WINDOW_TRANSFORMATION_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({})'.format(WINDOW_TRANSFORMATION_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({})'.format(
         WINDOW_TRANSFORMATION_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({})'.format(
         WINDOW_TRANSFORMATION_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({}))'.format(
         WINDOW_TRANSFORMATION_FORM_ID)),
    (
        '''INSERT INTO
        operation_script(id, `type`, enabled, body, operation_id)
        VALUES (48, 'JS_CLIENT', '1',
        'onlyField(task, "x_attribute", true);', {})'''.format(
            WINDOW_TRANSFORMATION_ID),
        '''DELETE FROM operation_script WHERE id = 48'''
    ),

    ("""
        UPDATE operation_form_field SET
        `values` = '{"multiple": false}'
        WHERE id IN (99, 100, 106, 117, 131, 154, 155, 167, 179, 180, 181, 186,
        200, 228, 243, 263, 279, 290, 291, 304, 305, 311, 312, 313, 314, 333,
        334, 335, 336, 338, 339, 348, 352, 356, 359, 374, 478, 421, 424, 435,
        436, 437, 438, 439, 440, 453);
    """,
     """
        UPDATE operation_form_field SET
        `values` = NULL
        WHERE id IN (99, 100, 106, 117, 131, 154, 155, 167, 179, 180, 181, 186,
        200, 228, 243, 263, 279, 290, 291, 304, 305, 311, 312, 313, 314, 333,
        334, 335, 336, 338, 339, 348, 352, 356, 359, 374, 478, 421, 424, 435,
        436, 437, 438, 439, 440, 453);
    """,
     )
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
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
            if isinstance(cmd[1], (unicode, str)):
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
