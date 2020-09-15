"""Adding Kmodes in Spark platform

Revision ID: 86699b2e6672
Revises: b7442131c810
Create Date: 2020-09-09 14:44:51.915594

"""

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import json
# revision identifiers, used by Alembic.
from migrations.utils import TablesV1 as T1


# revision identifiers, used by Alembic.
revision = '86699b2e6672'
down_revision = 'b7442131c810'
branch_labels = None
depends_on = None


OFFSET_OP = 138
OFFSET_FORM = 152
OFFSET_PORT = 322
OFFSET_FIELD = 575


def _insert_operation():
    T1.execute(T1.OPERATION, rows=[
        T1.operation(OFFSET_OP, 'k-modes-clustering-model', 1, 'TRANSFORMATION',
                     'fa-braille')
    ])


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (OFFSET_OP, 'en', 'K-Modes Clustering',
         'Uses a distributed version of K-Modes algorithm '
         '(Ensemble-based incremental distributed K-Modes) for clustering'),
        (OFFSET_OP, 'pt', 'Agrupamento por K-Modes',
         'Usa uma versão distribuída do algoritmo K-Modes '
         '(Ensemble-based incremental distributed K-Modes) para agrupamento'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [
        (OFFSET_OP, 1),
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
        (OFFSET_PORT, 'INPUT', None, OFFSET_OP, 1, 'ONE', 'train input data'),
        (OFFSET_PORT+1, 'OUTPUT', None, OFFSET_OP, 2, 'MANY', 'model'),
        (OFFSET_PORT+2, 'OUTPUT', None, OFFSET_OP, 1, 'MANY', 'output data'),
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
        (OFFSET_PORT, 'en', 'train input data', 'Train input data'),
        (OFFSET_PORT, 'pt', 'entrada do treino', 'Train input data'),

        (OFFSET_PORT+1, 'en', 'model', 'Output model'),
        (OFFSET_PORT+1, 'pt', 'modelo', 'Output model'),

        (OFFSET_PORT+2, 'en', 'output data', 'Output data'),
        (OFFSET_PORT+2, 'pt', 'dados de saída', 'Dados de saída'),

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
        (OFFSET_PORT, 1),
        (OFFSET_PORT + 1, 2),
        (OFFSET_PORT + 2, 1),
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
        (OFFSET_OP, 1),
        (OFFSET_OP, 19),
        (OFFSET_OP, 8),
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
        (OFFSET_FORM, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [(OFFSET_OP, i) for i in (10, 41, 110, OFFSET_FORM)]
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
        (OFFSET_FORM, 'en', 'Execution'),
        (OFFSET_FORM, 'pt', 'Execução'),
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

        [OFFSET_FIELD, 'number_of_clusters', "INTEGER", 1, 3, None,
         "integer", None, None, "EXECUTION", OFFSET_FORM],
        [OFFSET_FIELD + 1, 'max_iterations', 'INTEGER', 1, 4, 10, 'integer',
         None, None,  'EXECUTION', OFFSET_FORM],
        [OFFSET_FIELD + 2, "similarity", "TEXT", 0, 5, "hamming", "dropdown",
         None,
        json.dumps([
             {'key': 'frequency', 'value': 'Frequency-based dissimilarity'},
             {'key': 'hamming', 'value': 'Hamming distance'},
             {'key': 'all_frequency', 'value':
                 'All Frequency-based dissimilarity for modes.'},
         ]), "EXECUTION", OFFSET_FORM, None],
        [OFFSET_FIELD + 3, "metamodessimilarity", "TEXT", 0, 6, "hamming",
         "dropdown", None,
         json.dumps([
             {'key': 'frequency', 'value': 'Frequency-based dissimilarity'},
             {'key': 'hamming', 'value': 'Hamming distance'},
             {'key': 'all_frequency', 'value':
                 'All Frequency-based dissimilarity for modes.'},
         ]), "EXECUTION", OFFSET_FORM, None]

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
        [OFFSET_FIELD, "en", "Number of clusters (K)",
         "Number of clusters (K)"],
        [OFFSET_FIELD, "pt",
            "Quantidade de agrupamentos (K)", "Quantidade de agrupamentos (K)"],

        [OFFSET_FIELD + 1, "en", "Max iterations", "Max iterations"],
        [OFFSET_FIELD + 1, "pt", "Número máx. de iterações",
         "Número máx. de iterações"],

        [OFFSET_FIELD + 2, "en", "Dissimilarity function", "Distance function"],
        [OFFSET_FIELD + 2, "pt", "Função de dissimilaridade",
         "Função de dissimilaridade"],

        [OFFSET_FIELD + 3, "en", "Dissimilarity function for Metamodes",
         "Distance function for Metamodes"],
        [OFFSET_FIELD + 3, "pt", "Função de dissimilaridade para os Metamodes",
         "Função de dissimilaridade para os metamodes"],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN {s} AND {s}'.format(s=OFFSET_OP)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {s} AND {s}'.format(
             s=OFFSET_OP)),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE (operation_id BETWEEN {s} AND {s})'.format(s=OFFSET_OP)),

    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN {s} AND {s}))'.format(s=OFFSET_OP)),

    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {s})'.format(s=OFFSET_OP)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {s} AND {s}'.format(s=OFFSET_OP)),

    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id BETWEEN {s} AND {s}'
     .format(s=OFFSET_OP)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {f} AND {f}'
     .format(f=OFFSET_FORM)),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {s}'
     .format(s=OFFSET_OP)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {f} AND {f}'
     .format(f=OFFSET_FORM)),

    (_insert_operation_form_field, """DELETE FROM operation_form_field
         WHERE id BETWEEN {} AND {}""".format(OFFSET_FIELD, OFFSET_FIELD+3)),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN {} AND {}'
     .format(OFFSET_FIELD, OFFSET_FIELD+3)),
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
