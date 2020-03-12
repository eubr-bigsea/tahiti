# -*- coding: utf-8 -*-

"""Update Agglomerative Clustering Operation (scikit_learn).

Revision ID: f3d65f1a5878
Revises: 6c6668dd3682
Create Date: 2020-01-31 09:07:43.509424

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json


# revision identifiers, used by Alembic.
revision = 'f3d65f1a5878'
down_revision = '6c6668dd3682'
branch_labels = None
depends_on = None


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String),)

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        #Reshape
        (4096, 'OUTPUT', '', 2, 'MANY', 4015, 'model'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        #Reshape
        (4096, 2),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        #Reshape
        (4096, "en", 'model', 'Model'),
        (4096, "pt", 'modelo', 'Modelo'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (4015, 41),  #appearance
        (4015, 4015),  # own execution form
        (4015, 110)
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
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    enable_condition = 'this.algorithm.internalValue === "ball_tree" or this.algorithm.internalValue === "kd_tree"'
    data = [
        #Flatten - data_format
        (4337, 'memory', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION', 4015, None),
        (4338, 'connectivity', 'TEXT', 0, 7, None, 'text', None, None, 'EXECUTION', 4015, None),
        (4339, 'compute_full_tree', 'TEXT', 0, 8, 'auto', 'dropdown', None,
         json.dumps([
             {'key': 'auto', 'value': 'auto'},
             {'key': 'true', 'value': 'true'},
             {'key': 'false', 'value': 'false'},
         ]),
         'EXECUTION', 4015, None),
        (4340, 'distance_threshold', 'DECIMAL', 0, 9, None, 'decimal', None, None, 'EXECUTION', 4015, None),

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

    columns = ('id', 'locale', 'label', 'help')
    data = [
        #Flatten - data_format
        (4337, 'en', 'Memory', 'Used to cache the output of the computation of the tree.'),
        (4337, 'pt', 'Memória', 'Usado para armazenar em cache a saída do cálculo da árvore.'),

        (4338, 'en', 'Connectivity', 'Connectivity matrix.'),
        (4338, 'pt', 'Conectividade', 'Matriz de conectividade.'),

        (4339, 'en', 'Compute full tree', 'Stop early the construction of the tree at number of clusters.'),
        (4339, 'pt', 'Calcular árvore completa', 'Pare cedo a construção da árvore em número de clusters.'),

        (4340, 'en', 'Distance threshold', 'The linkage distance threshold above which, clusters will not be merged.'),
        (4340, 'pt', 'Limiar de distância', 'O limite da distância de ligação acima do qual os clusters não serão '
                                            'mesclados.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `default` = 'euclidean' WHERE id = 4079""",
     """UPDATE operation_form_field SET `default` = 'ward' WHERE id = 4079"""),
    (
    """UPDATE operation_form_field SET `default` = 'ward' WHERE id = 4078""",
    """UPDATE operation_form_field SET `default` = 'euclidean' WHERE id = 4078"""),

    ("""UPDATE operation_form_field_translation SET `label` = 'Atributo(s) previsor(es)' WHERE id = 4075 
    AND `locale` LIKE '%%pt%%'""",
     """UPDATE operation_form_field_translation SET `label` = 'Atributo(s) previsor(es)' WHERE id = 4075 
    AND `locale` LIKE '%%pt%%'"""),

    ("""UPDATE operation_form_field_translation SET `label` = 'Atrbuto com a predição (novo)' WHERE id = 4076 
    AND `locale` LIKE '%%pt%%'""",
     """UPDATE operation_form_field_translation SET `label` = 'Atrbuto com a predição (novo)' WHERE id = 4076 
    AND `locale` LIKE '%%pt%%'"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4337 AND 4340'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4337 AND 4340'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4015'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id = 4096'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id = 4096'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id = 4096'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
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
