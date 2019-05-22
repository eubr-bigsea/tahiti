# coding=utf-8
"""load_model_op

Revision ID: 6da9e093897c
Revises: bd294c13637b
Create Date: 2017-09-18 16:20:14.029058

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '6da9e093897c'
down_revision = 'bd294c13637b'
branch_labels = None
depends_on = None


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

    all_ops = [
        (45, 'INPUT', None, 22, 2, 'ONE', 'input data'),
        (47, 'INPUT', None, 22, 1, 'ONE', 'model'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    all_ops = [
        (45, 'en', 'input data', 'Input data'),
        (45, 'pt', 'dados de entrada', 'Dados de entrada'),

        (47, 'en', 'model', 'Model'),
        (47, 'pt', 'modelo', 'Modelo'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (45, 1),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

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
    data = [
        [361, 'model', 'TEXT', 1, 1, None, 'lookup',
         '`${LIMONERO_URL}/models?simple=true&list=true&enabled=1`', None,
         'EXECUTION', 21],
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

    columns = [c.name for c in tb.columns]
    data = [
        [361, 'en', 'Model', 'Model to be loaded (previously saved).'],
        [361, 'pt', 'Modelo', 'Modelo anteriormente salvo a ser carregado'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation SET slug = 'load-model', icon = 'fa-cloud-download',
        enabled = 1 WHERE id = 22""",
     """UPDATE operation SET slug = 'score-model', icon = 'fa-bullseye',
        enabled = 0 WHERE id = 22"""),

    ("""UPDATE operation_translation SET name = 'Carregar modelo',
        description = 'Carrega um modelo (Spark) salvo anteriormente.'
        WHERE id = 22 AND locale = 'pt' """,
     """UPDATE operation_translation SET name = 'Modelo de pontuação',
        description = 'Modelo de pontuação'
        WHERE id = 22 and locale = 'pt' """),

    ("""UPDATE operation_translation SET name = 'Load model',
        description = 'Loads a previously saved model (Spark)'
        WHERE id = 22 and locale = 'en' """,
     """UPDATE operation_translation SET name = 'Score model',
        description = 'Scores a machine learning model'
        WHERE id = 22 AND locale = 'en' """
     ),

    (
        'DELETE FROM operation_port_translation WHERE id IN (45, 47)',
        _insert_operation_port_translation,
    ),

    (
        'DELETE FROM operation_port_interface_operation_port '
        'WHERE operation_port_id IN (45, 47)',
        _insert_operation_port_interface_operation_port,
    ),

    (
        "UPDATE operation_port SET slug = 'model' WHERE id = 46",
        "UPDATE operation_port SET slug = 'output result' WHERE id = 46",
    ),

    (
        '''
          INSERT INTO operation_port_interface_operation_port
            (operation_port_interface_id, operation_port_id)
          VALUES (2, 46), (4, 46), (14, 46), (15, 46), (18, 46), (20, 46)''',
        '''DELETE FROM operation_port_interface_operation_port
        WHERE operation_port_id = 46
            AND operation_port_interface_id IN (2, 4, 14, 15, 18, 20)
        '''
    ),
    (
        ["""UPDATE operation_port_translation SET name = 'model',
            description = 'Loaded model' WHERE id = 46 AND locale = 'en' """,
         """UPDATE operation_port_translation SET name = 'modelo',
             description = 'Modelo carregado'
             WHERE id = 46 AND locale = 'pt' """, ],

        ["""UPDATE operation_port_translation SET name = 'output result',
            description = 'Output result'
            WHERE id = 46 AND locale = 'en' """,
         """UPDATE operation_port_translation SET name = 'resultado de saída',
             description = 'Saída de resultado'
             WHERE id = 46 AND locale = 'pt' """, ]
    ),

    (
        'DELETE FROM operation_port WHERE id IN (45, 47)',
        _insert_operation_port,
    ),

    (
        '''INSERT INTO operation_category_operation
           (operation_id, operation_category_id) VALUES(22, 1)''',
        'DELETE FROM operation_category_operation '
        'WHERE operation_id = 22 AND operation_category_id = 1'
    ),

    (_insert_operation_form_field,
     """DELETE FROM operation_form_field WHERE form_id = 21"""),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id = 21)'),
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
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
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
