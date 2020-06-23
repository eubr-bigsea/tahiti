"""sliding_window

Revision ID: aa8beb5ca6ac
Revises: 953911f74e49
Create Date: 2020-04-30 16:38:10.738802

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
from migrations.utils import TablesV1 as T1

revision = 'aa8beb5ca6ac'
down_revision = '953911f74e49'
branch_labels = None
depends_on = None

SLIDING = 127
PORT_RANGE = [302, 303]
FORM_ID = 138
FORM_FIELD_RANGE = [515, 518]


def _insert_operation():
    T1.execute(T1.OPERATION, rows=[
        T1.operation(SLIDING, 'sliding-window', 1, 'TRANSFORMATION', 'fa-window-close-o')
    ])


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (SLIDING, 'en', 'Sliding window',
         'Sliding window over vector.'),
        (SLIDING, 'pt', 'Janela deslizante',
         'Janela deslizante sobre vetor.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [
        (SLIDING, 1),
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
        (302, 'INPUT', None, SLIDING, 1, 'ONE', 'input data'),
        (303, 'OUTPUT', None, SLIDING, 1, 'MANY', 'output data'),
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
        (302, 'en', 'input data', 'Input data'),
        (302, 'pt', 'dados de entrada', 'Dados de entrada'),

        (303, 'en', 'output data', 'Output data'),
        (303, 'pt', 'dados de saída', 'Dados de saída'),

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
        (302, 1),
        (303, 1),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _insert_operation_script():
    tb = table(
        'operation_script',
        column('id', Integer),
        column('type', String),
        column('enabled', Integer),
        column('body', String),
        column('operation_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        [70, 'JS_CLIENT', 1,
         "repeatFromAlias(task, 'alias', 'window_size');", SLIDING],
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
        (SLIDING, 1),
        (SLIDING, 7),
        (SLIDING, 29),
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
        (FORM_ID, 1, 1, 'execution'),
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
        (SLIDING, FORM_ID),
        (SLIDING, 110),  # reports
        (SLIDING, 41),  # appearance
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
        (FORM_ID, 'en', 'Execution'),
        (FORM_ID, 'pt', 'Execução'),
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
        [515, 'attribute', 'TEXT', 1, 1, None,
         'attribute-selector', None, None, 'EXECUTION', FORM_ID],
        [516, 'window_size', 'INTEGER', 0, 2, '10', 'integer', None, None,
         'EXECUTION', FORM_ID],
        [517, 'window_gap', 'INTEGER', 0, 3, 1, 'integer', None, None,
         'EXECUTION', FORM_ID],
        [518, 'alias', 'TEXT', 0, 4, 'attr_', 'text', None, None,
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
        [515, 'en',
         'Attribute',
         'Attribute used as a vector for the sliding window.'],
        [515, 'pt', 'Atributo',
         'Atributo usado como vetor para a janela deslizante.'],
        [516, 'en',
         'Window size',
         'Window size (>=0).'],
        [516, 'pt', 'Tamanho da janela',
         'Tamanho da janela (>=0).'],
        [517, 'en', 'Gap', 'Gap (> 0) defines the next start of window.'],
        [517, 'pt', 'Deslocamento (lacuna)',
         'Deslocamento (>0) determina o próximo início da janela.'],
        [518, 'en', 'Name prefix for new attributes', 'Name for new attributes (optional).'],
        [518, 'pt', 'Prefixo para nome dos atributos',
         'Prefixo usado para formar o nome dos novos atributos.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN {s} AND {s}'.format(s=SLIDING)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {s} AND {s}'.format(s=SLIDING)),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE (operation_id BETWEEN {s} AND {s})'.format(s=SLIDING)),

    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN {s} AND {s}))'.format(s=SLIDING)),
    (_insert_operation_script,
     'DELETE FROM operation_script WHERE operation_id BETWEEN {s} AND {s}'.format(s=SLIDING),
     ),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {s})'.format(s=SLIDING)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {s} AND {s}'.format(s=SLIDING)),

    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN {s} AND {s}'.format(s=SLIDING)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {f} AND {f}'.format(f=FORM_ID)),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {s}'.format(s=SLIDING)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {f} AND {f}'.format(f=FORM_ID)),

    (_insert_operation_form_field, """DELETE FROM operation_form_field
         WHERE form_id BETWEEN {f} AND {f}""".format(f=FORM_ID)),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (' +
     'SELECT id FROM operation_form_field WHERE form_id BETWEEN {f} AND {f})'.format(f=FORM_ID)),
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
