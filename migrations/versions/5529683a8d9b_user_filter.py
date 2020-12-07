""" user filter  

Revision ID: 5529683a8d9b
Revises: ed920c727112
Create Date: 2020-06-18 20:06:05.438946

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5529683a8d9b'
down_revision = 'ed920c727112'
branch_labels = None
depends_on = None

USER_FILTER = 129
PORT_RANGE = [306, 307]
FORM_ID = 140
FORM_FIELD_RANGE = [524, 526]


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
            (USER_FILTER, 'user-filter', 1, 'TRANSFORMATION', 'fa-window-close-o', 'double-layout'),
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
        (USER_FILTER, 'en', 'User filter',
         'Allows users to provide filters values before the execution.'),
        (USER_FILTER, 'pt', 'Filtro do usuário',
         'Permite que os usuários especifiquem filtros antes da execução.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [
        (USER_FILTER, 1),
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
        (306, 'INPUT', None, USER_FILTER, 1, 'ONE', 'input data'),
        (307, 'OUTPUT', None, USER_FILTER, 1, 'MANY', 'output data'),
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
        (306, 'en', 'input data', 'Input data'),
        (306, 'pt', 'dados de entrada', 'Dados de entrada'),

        (307, 'en', 'output data', 'Output data'),
        (307, 'pt', 'dados de saída', 'Dados de saída'),

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
        (306, 1),
        (307, 1),
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
        [72, 'JS_CLIENT', 1,
         "copyInput(task);", USER_FILTER],
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
        (USER_FILTER, 1),
        (USER_FILTER, 41),
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
        (USER_FILTER, FORM_ID),
        (USER_FILTER, 110),  # reports
        (USER_FILTER, 41),  # appearance
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
        [524, 'filters', 'TEXT', 1, 1, None,
         'filter', None, None, 'EXECUTION', FORM_ID],
        [525, 'ignore', 'INTEGER', 0, 2, None,
         'checkbox', None, None, 'EXECUTION', FORM_ID],
        [526, 'use_advanced_editor', 'INTEGER', 0, 3, None,
         'checkbox', None, None, 'EXECUTION', FORM_ID],
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
        [524, 'en', 'Filters', 'Filters to be applied to the input.'],
        [524, 'pt', 'Filtros', 'Filtros a serem aplicados à entrada.'],
        [525, 'en', 'Ignore in design', 'In design/editing mode, filters are ignored.'],
        [525, 'pt', 'Ignore ao executar em ambiente de edição', 
            'Filtros são ignorados durante a edição do workflow.'],
        [526, 'en', 'User can use advanced query editor', 'Users can define custom filters using an advanced query editor.'],
        [526, 'pt', 'Disponibilizar editor de consulta', 'Usuários podem editar os filtros usando um editor avançado de consultas.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN {s} AND {s}'.format(s=USER_FILTER)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {s} AND {s}'.format(s=USER_FILTER)),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE (operation_id BETWEEN {s} AND {s})'.format(s=USER_FILTER)),

    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN {s} AND {s}))'.format(s=USER_FILTER)),
    (_insert_operation_script,
     'DELETE FROM operation_script WHERE operation_id BETWEEN {s} AND {s}'.format(s=USER_FILTER),
     ),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {s})'.format(s=USER_FILTER)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {s} AND {s}'.format(s=USER_FILTER)),

    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN {s} AND {s}'.format(s=USER_FILTER)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {f} AND {f}'.format(f=FORM_ID)),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {s}'.format(s=USER_FILTER)),
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
        op.add_column('workflow', sa.Column('publishing_status', sa.Enum('DISABLED', 'EDITING', 'PUBLISHED', name='PublishingStatusEnumType'), nullable=True))
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
        op.drop_column('workflow', 'publishing_status')
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
