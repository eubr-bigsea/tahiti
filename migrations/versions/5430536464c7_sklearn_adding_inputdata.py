# -*- coding: utf-8 -*-

"""Sklearn operations

Revision ID: 5430536464c7
Revises: 4b5b8e3470af
Create Date: 2018-09-03 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = '5430536464c7'
down_revision = '4b5b8e3470af'
branch_labels = None
depends_on = None


def _insert_operation():
    tb = table('operation',
                            column("id", Integer),
                            column("slug", String),
                            column('enabled', Integer),
                            column('type', String),
                            column('icon', String),
                            )
    columns = ['id', 'slug', 'enabled', 'type', 'icon']
    data = [
    (4015, 'agglomerative-clustering', 1, 'TRANSFORMATION', 'fa-ruler-horizontal'),

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (4015, 4),
        (3015, 4), #regression-model (compss)
        (3018, 4), #classification-model (compss)

    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        (4015, 8),
        (4015, 19),  #clustering
        (4015, 4001),

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (4015, 1, 1, 'execution'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)

def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (4015, 'en', 'Execution'),
        (4015, 'pt', 'Execução'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (4015, 41), # appearance
        (4015, 110), #results
        (4015, 4015), # own execution form
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

    columns = ('id', 'locale', 'name', 'description')
    data = [

        (4015, 'en', 'Agglomerative Clustering', 'Recursively merges the pair of clusters that minimally increases a given linkage distance.'),
        (4015, 'pt', 'Agrupamento Aglomerativo', 'Recursivamente mescla o par de clusters que aumenta minimamente uma dada distância de ligamento.'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
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
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [

        (4017,	'INPUT',  None, 4015, 1,'ONE','input data'),
        (4018,	'OUTPUT', None, 4015, 1,'MANY','output data'),
        (3069,	'OUTPUT', None, 3016, 2,'MANY','cluster centroids'),

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

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (4017,'en', 'input data', 'Input data'),
        (4017,'pt', 'dados de entrada', 'Dados de entrada'),
        (4018,'en', 'output data', 'Output data'),
        (4018,'pt', 'dados de saída', 'Dados de saída'),
        (3069,'en', 'cluster centroids', 'Cluster centroids'),
        (3069,'pt', 'centroids do agrupamento', 'Centroids do agrupamento')

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [

        (4017, 1),  # data
        (4018, 1),  # data
        (3069, 1),

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

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        # agglomerative-clustering
        (4075, 'attributes', 'TEXT',   1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4015),
        (4076, 'alias','TEXT', 0, 2, 'clusters','text',None,None,'EXECUTION', 4015),
        (4077, 'number_of_clusters', 'INTEGER', 0, 3, 2, 'integer', None, None, 'EXECUTION', 4015),
        (4078, 'linkage', 'TEXT', 0, 4, 'euclidean', 'dropdown', None,
		'[{"key": \"euclidean\", \"value\": \"euclidean\"}, '
		'{\"key\": \"l1\", \"value\": \"l1\"}, '
        '{\"key\": \"l2\", \"value\": \"l2\"}, '
        '{\"key\": \"manhattan\", \"value\": \"manhattan\"}, '
        '{\"key\": \"cosine\", \"value\": \"cosine\"}]', 'EXECUTION', 4015),
        (4079, 'affinity', 'TEXT', 0, 5, 'ward', 'dropdown', None,
		'[{"key": \"ward\", \"value\": \"ward\"}, '
		'{\"key\": \"complete\", \"value\": \"complete\"}, '
        '{\"key\": \"average\", \"value\": \"average\"}]', 'EXECUTION', 4015),


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

    columns = ('id', 'locale', 'label', 'help')
    data = [
        # agglomerative-clustering
        (4075, 'en', 'Feature', 'Column name to be clusterized.'),
        (4076, 'en', 'Alias', 'Alias to the new feature'),
        (4077, 'en', 'Number of Clusters', 'The number of clusters to find.'),
        (4078, 'en', 'Linkage', 'The linkage criterion determines which distance to use between sets of observation.'),
        (4079, 'en', 'Affinity', 'Metric used to compute the linkage.'),
        (4075, 'pt', 'Feature', 'Nome da coluna para ser agrupada.'),
        (4076, 'pt', 'Alias', 'Nome para a nova coluna.'),
        (4077, 'pt', 'Número de Clusters', 'O número de clusters para serem encontrados.'),
        (4078, 'pt', 'Ligação', 'O critério de ligação determina qual distância usar entre conjuntos de observação.'),
        (4079, 'pt', 'Afinidade', 'Métrica usada para calcular a ligação.'),



	]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)



all_commands = [

	(_insert_operation, 'DELETE FROM operation WHERE id >= 4015'),
	(_insert_new_operation_platform,
        'DELETE FROM operation_platform WHERE operation_id >= 4015;'
        'DELETE FROM operation_platform WHERE operation_id = 3018 AND platform_id = 4;'
        'DELETE FROM operation_platform WHERE operation_id = 3015 AND platform_id = 4;' ),
	(_insert_operation_category_operation, 'DELETE FROM operation_category_operation WHERE operation_id >= 4015'),
	(_insert_operation_form, 'DELETE FROM operation_form WHERE id >= 4015'),
	(_insert_operation_form_translation, 'DELETE FROM operation_form_translation WHERE id >= 4015'),
	(_insert_operation_operation_form, 'DELETE FROM operation_operation_form WHERE operation_id >= 4015'),
	(_insert_operation_translation, 'DELETE FROM operation_translation WHERE id >= 4015'),
	(_insert_operation_port, 'DELETE FROM operation_port WHERE id >= 4017 OR id = 3069' ),
	(_insert_operation_port_translation, 'DELETE FROM operation_port_translation WHERE id >= 4017 OR id = 3069' ),
	(_insert_operation_port_interface_operation_port,
        'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id >= 4017 OR operation_port_id = 3069'),
	(_insert_operation_form_field, 'DELETE FROM operation_form_field WHERE id >= 4075'),
	(_insert_operation_form_field_translation, 'DELETE FROM operation_form_field_translation WHERE id >= 4075' ),
    ("""
    DELETE FROM operation_platform WHERE operation_id = 1  AND platform_id = 4;
    DELETE FROM operation_platform WHERE operation_id = 73 AND platform_id = 4;
    DELETE FROM operation_operation_form
    WHERE operation_id >= 4001 AND operation_id <= 4005 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3005 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3007 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3009 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3013 AND operation_form_id = 110;
    """,
    """
    INSERT INTO operation_platform (operation_id, platform_id)
    VALUES (1, 4), (73, 4);
    INSERT INTO operation_operation_form (operation_id, operation_form_id)
    VALUES (3005, 110), (3007, 110), (3009, 110), (3013, 110),
           (4001, 110), (4002, 110), (4003, 110), (4004, 110), (4005, 110);
    """)

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
