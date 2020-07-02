"""disassemble vectors

Revision ID: aea8dea22277
Revises: 05985c3f83ca
Create Date: 2020-06-26 10:31:42.967078

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
from migrations.utils import TablesV1 as T1

revision = 'aea8dea22277'
down_revision = '05985c3f83ca'
branch_labels = None
depends_on = None

SUMMARY_FORM_ID = 99
SUMMARY_FIELD_ID = 520

DISASSEMBLER_ID = 128
DISASSEMBLER_FORM = 139


def _insert_operation():
    T1.execute(T1.OPERATION, rows=[
        T1.operation(DISASSEMBLER_ID, 'feature-disassembler', 1,
                     'TRANSFORMATION', 'fa-truck')
    ])


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (DISASSEMBLER_ID, 'en', 'Feature Disassembler',
         'It takes a Vector data type column, and creates a new column '
         'for each item in the Vector.'),
        (DISASSEMBLER_ID, 'pt', 'Separador de Atributos',
         'Operação que transforma uma coluna de tipo de dados Vector em '
         'uma nova coluna para cada item no Vector.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [
        (DISASSEMBLER_ID, 1),
    ]
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

    rows = [
        (304, 'INPUT', None, DISASSEMBLER_ID, 1, 'ONE', 'input data'),
        (305, 'OUTPUT', None, DISASSEMBLER_ID, 1, 'MANY', 'output data'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (304, 'en', 'input data', 'Input data'),
        (304, 'pt', 'dados de entrada', 'Dados de entrada'),

        (305, 'en', 'output data', 'Output data'),
        (305, 'pt', 'dados de saída', 'Dados de saída'),

    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (304, 1),
        (305, 1),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (DISASSEMBLER_ID, 1),
        (DISASSEMBLER_ID, 32),
        (DISASSEMBLER_ID, 23),
    ]
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
    data = [
        (DISASSEMBLER_FORM, 1, 1, 'execution'),
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
        (DISASSEMBLER_ID, DISASSEMBLER_FORM),
        (DISASSEMBLER_ID, 110),  # reports
        (DISASSEMBLER_ID, 41),  # appearance
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
        (DISASSEMBLER_FORM, 'en', 'Execution'),
        (DISASSEMBLER_FORM, 'pt', 'Execução'),
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

    data = [
        [SUMMARY_FIELD_ID, 'correlation', "INTEGER", 0, 3, None, "checkbox",
         None, None, "EXECUTION", SUMMARY_FORM_ID],
        [SUMMARY_FIELD_ID+1, 'feature', 'TEXT', 1, 1, None,
         'attribute-selector', None, None, 'EXECUTION', DISASSEMBLER_FORM],
        [SUMMARY_FIELD_ID+2, 'top_n', 'INTEGER', 0, 2, 0, 'integer', None, None,
         'EXECUTION', DISASSEMBLER_FORM],
        [SUMMARY_FIELD_ID+3, 'alias', 'TEXT', 0, 3, 'vector_', 'text', None,
         None, 'EXECUTION', DISASSEMBLER_FORM],

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
        [SUMMARY_FIELD_ID, 'en', 'Correlation',
         'Calculate the correlation between each pair of columns.'],
        [SUMMARY_FIELD_ID, 'pt', 'Correlação',
         'Calcular a correlação entre cada par de colunas.'],

        [SUMMARY_FIELD_ID+1,  'en',
         'Attribute',
         'Attribute to extract the features.'],
        [SUMMARY_FIELD_ID+1, 'pt', 'Atributo',
         'Coluna utilizada para extrair o vetor de atributos'],
        [SUMMARY_FIELD_ID+2, 'en', 'Top N',
         'Top n (> 0) restricts to first n index in vector.'],
        [SUMMARY_FIELD_ID+2, 'pt', 'Top N',
         'Top n (> 0) restringe a extração dos primeiros n índices do vetor.'],

        [SUMMARY_FIELD_ID+3, 'en', 'Name prefix for new attributes',
         'Name for new attributes (optional).'],
        [SUMMARY_FIELD_ID+3, 'pt', 'Prefixo para nome dos atributos',
         'Prefixo usado para formar o nome dos novos atributos.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN {s} AND {s}'.format(s=DISASSEMBLER_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {s} AND {s}'.format(s=DISASSEMBLER_ID)),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE (operation_id BETWEEN {s} AND {s})'.format(s=DISASSEMBLER_ID)),

    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN {s} AND {s}))'.format(s=DISASSEMBLER_ID)),

    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {s})'.format(s=DISASSEMBLER_ID)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {s} AND {s}'.format(s=DISASSEMBLER_ID)),

    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN {s} AND {s}'.format(s=DISASSEMBLER_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {f} AND {f}'.format(f=DISASSEMBLER_FORM)),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {s}'.format(s=DISASSEMBLER_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {f} AND {f}'.format(f=DISASSEMBLER_FORM)),

    (_insert_operation_form_field, """DELETE FROM operation_form_field
         WHERE id BETWEEN {} AND {}""".format(SUMMARY_FIELD_ID, SUMMARY_FIELD_ID+3)),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN {} AND {}'
     .format(SUMMARY_FIELD_ID, SUMMARY_FIELD_ID+3)),
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
