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
from sqlalchemy.sql import table, column, text

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
        (4015, 'agglomerative-clustering', 1, 'TRANSFORMATION',
         'fa-ruler-horizontal'),
        (4016, 'word-to-vector', 1, 'TRANSFORMATION', 'fa-list-ol'),
        (4017, 'evaluate-model', 1, 'TRANSFORMATION', 'fa-check'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
            'operation_platform',
            column('operation_id', Integer),
            column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (4015, 4),
        (3015, 4),  # regression-model (compss)
        (3018, 4),  # classification-model (compss)
        (4016, 4),
        (4017, 4),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
            'operation_category_operation',
            column('operation_id', Integer),
            column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        (4015, 8),
        (4015, 19),  # clustering
        (4015, 4001),

        (4016, 16),  # textoperaitons
        (4016, 4001),

        (4017, 8),
        (4017, 26),  # evaluate-model
        (4017, 4001),

    ]

    rows = [dict(list(zip(columns, row))) for row in data]
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
        (4016, 1, 1, 'execution'),
        (4017, 1, 1, 'execution'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
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
        (4016, 'en', 'Execution'),
        (4016, 'pt', 'Execução'),
        (4017, 'en', 'Execution'),
        (4017, 'pt', 'Execução'),
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
        (4015, 41),  # appearance
        (4015, 110),  # results
        (4015, 4015),  # own execution form

        (4016, 41),  # appearance
        (4016, 110),  # results
        (4016, 4016),  # own execution form

        (4017, 41),  # appearance
        (4017, 110),  # results
        (4017, 4017),  # own execution form
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

    columns = ('id', 'locale', 'name', 'description')
    data = [

        (4015, 'en', 'Agglomerative Clustering',
         'Recursively merges the pair of clusters that minimally increases a '
         'given linkage distance.'),
        (4015, 'pt', 'Agrupamento Aglomerativo',
         'Recursivamente mescla o par de clusters que aumenta minimamente uma '
         'dada distância de ligamento.'),

        (4016, 'en', 'Convert words to vector', 'Convert words to vector.'),
        (4016, 'pt', 'Converter palavras em vetor',
         'Converter palavras em vetor.'),

        (4017, 'en', 'Evaluate model', 'Evaluates a machine learning model'),
        (4017, 'pt', 'Avaliar modelo',
         'Avalia um modelo de aprendizado de máquina'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
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

        (4017, 'INPUT', None, 4015, 1, 'ONE', 'input data'),
        (4018, 'OUTPUT', None, 4015, 1, 'MANY', 'output data'),

        (3069, 'OUTPUT', None, 3016, 2, 'MANY', 'cluster centroids'),

        (4019, 'INPUT', None, 4016, 1, 'ONE', 'input data'),
        (4020, 'OUTPUT', None, 4016, 1, 'MANY', 'vocabulary'),
        (4021, 'OUTPUT', None, 4016, 2, 'MANY', 'output data'),
        (4022, 'OUTPUT', None, 4016, 3, 'MANY', 'vector-model'),

        (4023, 'INPUT', None, 4017, 1, 'ONE', 'input data'),
        (4024, 'INPUT', None, 4017, 2, 'ONE', 'model'),

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

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (4017, 'en', 'input data', 'Input data'),
        (4017, 'pt', 'dados de entrada', 'Dados de entrada'),
        (4018, 'en', 'output data', 'Output data'),
        (4018, 'pt', 'dados de saída', 'Dados de saída'),
        (3069, 'en', 'cluster centroids', 'Cluster centroids'),
        (3069, 'pt', 'centroids do agrupamento', 'Centroids do agrupamento'),
        (4019, 'en', 'input data', 'Input data'),
        (4019, 'pt', 'dados de entrada', 'Dados de entrada'),
        (4020, 'en', 'vocabulary', 'Vocabulary produced'),
        (4020, 'pt', 'vocabulário', 'Vocabulário gerado'),
        (4021, 'en', 'output data', 'Output data'),
        (4021, 'pt', 'dados de saída', 'Dados de saída'),
        (4022, 'en', 'vector model', 'Vector model'),
        (4022, 'pt', 'modelo de vetores', 'Modelo de vetores'),

        (4023, 'en', 'input data', 'Input data to be used during evaluation'),
        (4023, 'pt', 'dados de entrada',
         'Input data to be used during evaluation'),
        (4024, 'en', 'model', 'Model to be evaluated'),
        (4024, 'pt', 'modelo', 'Model to be evaluated'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
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

        (4019, 1),
        (4020, 13),  # vocabulary
        (4021, 1),
        (4022, 20),  # model

        (4023, 1),
        (4024, 2),
        (4024, 4),
        (4024, 14),
        (4024, 15),
        (4024, 18),
        (4024, 20),

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

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        # agglomerative-clustering
        (4075, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         '{"multiple": false}', 'EXECUTION', 4015),
        (4076, 'alias', 'TEXT', 0, 2, 'clusters', 'text', None, None,
         'EXECUTION', 4015),
        (4077, 'number_of_clusters', 'INTEGER', 0, 3, 2, 'integer', None, None,
         'EXECUTION', 4015),
        (4078, 'linkage', 'TEXT', 0, 4, 'euclidean', 'dropdown', None,
         '[{"key": \"ward\", \"value\": \"ward\"}, '
         '{\"key\": \"complete\", \"value\": \"complete\"}, '
         '{\"key\": \"average\", \"value\": \"average\"}]', 'EXECUTION', 4015),
        (4079, 'affinity', 'TEXT', 0, 5, 'ward', 'dropdown', None,
         '[{"key": \"euclidean\", \"value\": \"euclidean\"}, '
         '{\"key\": \"l1\", \"value\": \"l1\"}, '
         '{\"key\": \"l2\", \"value\": \"l2\"}, '
         '{\"key\": \"manhattan\", \"value\": \"manhattan\"}, '
         '{\"key\": \"cosine\", \"value\": \"cosine\"}]', 'EXECUTION', 4015),

        # words-to-Vector
        (4080, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         '{"multiple": false}', 'EXECUTION', 4016),
        (4081, 'alias', 'TEXT', 0, 2, 'wordsvector', 'text', None, None,
         'EXECUTION', 4016),
        (4082, 'type', 'TEXT', 1, 3, 'count', 'dropdown', None,
         '[{"en": "Count term frequency", "value": "Count term frequency", '
         '"key": "count", "pt": "Contar a frequencia do termo"}, '
         '{"en": "Term Frequency Inverse Document Frequency (TF-IDF)", '
         '"value": "tf-idf", "key": "TF-IDF", "pt": "TF-IDF"}, '
         '{"en": "Use word2vec algorithm", "value": "Use Word2vec algorithm", '
         '"key": "word2vec", "pt": "Usar o algoritmo Word2vec"}, '
         '{"en": "Map the sequence of terms to their TF using hashing trick", '
         '"value": "Map the sequence of terms to their TF using hashing '
         'trick", '
         '"key": "hashing_tf", "pt": "Mapear a sequencia de termos para TF ('
         'frequencia do termo) usando hashing"}]',
         'EXECUTION', 4016),
        (4083, 'vocab_size', 'INTEGER', 0, 4, None, 'integer', None, None,
         'EXECUTION', 4016),
        (4084, 'minimum_df', 'INTEGER', 0, 5, None, 'integer', None, None,
         'EXECUTION', 4016),

        # evaluate-model
        (4085, 'prediction_attribute', 'TEXT', 1, 1, None, 'attribute-selector',
         None, '{"multiple": false}', 'EXECUTION', 4017),
        (4086, 'label_attribute', 'TEXT', 0, 2, None, 'attribute-selector',
         None, '{"multiple": false}', 'EXECUTION', 4017),
        (4087, 'model_type', 'TEXT', 1, 4, None, 'dropdown', None,
         '[{"en": "Clustering model", "value": "Clustering model", "key": '
         '"clustering", "pt": "Model de agrupamento"}, '
         '{"en": "Classifier model", "value": "Classifier mode", "key": '
         '"classification", "pt": "Modelo de classificação"}, '
         '{"en": "Regressor model", "value": "Regressor model", "key": '
         '"regression", "pt": "Modelo de regressão"}]',
         'EXECUTION', 4017),
        (4088, 'feature', 'TEXT', 0, 3, None, 'attribute-selector', None,
         '{"multiple": false}', 'EXECUTION', 4017),

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
        # agglomerative-clustering
        (4075, 'en', 'Feature', 'Column name to be clusterized.'),
        (4076, 'en', 'Alias', 'Alias to the new feature'),
        (4077, 'en', 'Number of Clusters', 'The number of clusters to find.'),
        (4078, 'en', 'Linkage',
         'The linkage criterion determines which distance to use between sets '
         'of observation.'),
        (4079, 'en', 'Affinity', 'Metric used to compute the linkage.'),
        (4075, 'pt', 'Feature', 'Nome da coluna para ser agrupada.'),
        (4076, 'pt', 'Alias', 'Nome para a nova coluna.'),
        (4077, 'pt', 'Número de Clusters',
         'O número de clusters para serem encontrados.'),
        (4078, 'pt', 'Ligação',
         'O critério de ligação determina qual distância usar entre conjuntos '
         'de observação.'),
        (4079, 'pt', 'Afinidade', 'Métrica usada para calcular a ligação.'),

        # wordsvector
        (4080, 'en', 'Attribute', 'Field with the words to converter.'),
        (4081, 'en', 'Alias', 'New column name.'),
        (4082, 'en', 'Type', 'Type of conversor.'),
        (4083, 'en', 'Vocabulary size',
         'If there are more unique words than this, then prune the infrequent '
         'ones.'),
        (4084, 'en', 'Minimum frequency in docs (DF)',
         'Ignores all words with total frequency lower than this.'),
        (4080, 'pt', 'Attributo',
         'Campo com as palavras para serem convertidas.'),
        (4081, 'pt', 'Alias', 'Nova coluna.'),
        (4082, 'pt', 'Tipo', 'Tipo do conversor.'),
        (4083, 'pt', 'Tamanho do Vocabulario',
         'Se houver mais palavras únicas do que isso, podar as menos '
         'frequentes.'),
        (4084, 'pt', 'Frequência mínima nos documentos (DF)',
         'Ignora todas as palavras com frequência total inferior a esta.'),

        # evaluate-model
        (4085, 'en', 'Prediction attribute', 'Prediction attribute.'),
        (4085, 'pt', 'Atributo usado para predição',
         'Atributo usado para predição.'),
        (4086, 'en', 'Label attribute (if classification or regression)',
         'Label attribute (only if is classification or regression model).'),
        (4086, 'pt',
         'Atributo usado como label (se é classificação ou regressão)',
         'Atributo usado como label (apenas se é modelo de classificação ou '
         'regressão)'),
        (4087, 'en', 'Model Type', 'Type of model to be evaluated.'),
        (4087, 'pt', 'Tipo do modelo',
         'Tipo do modelo para ser avaliado.'),
        (4088, 'en', 'Feature attribute (if clustering)',
         'Feature attribute (only if is clustering model).'),
        (4088, 'pt', 'Atributo de features',
         'Atributo usado como features (apenas se é modelo de agrupamento).'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 4015 AND 4017'),
    (_insert_new_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id BETWEEN 4015 AND 4017;'
     'DELETE FROM operation_platform WHERE operation_id = 3018 AND '
     'platform_id = 4;'
     'DELETE FROM operation_platform WHERE operation_id = 3015 AND '
     'platform_id = 4;'
     ),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN '
     '4015 AND 4017'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 4015 AND 4017'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 4015 AND 4017'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id BETWEEN 4015 '
     'AND 4017'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 4015 AND 4017'),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4017 AND 4024 OR id = 3069'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4017 AND 4024 '
     'OR id = 3069'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE '
     'operation_port_id BETWEEN 4017 AND 4024 OR operation_port_id = 3069'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4075 AND 4088'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4075 AND '
     '4088'),
    ("""
    DELETE FROM operation_platform WHERE operation_id = 1  AND platform_id = 4;
    DELETE FROM operation_platform WHERE operation_id = 73 AND platform_id = 4;
    DELETE FROM operation_platform WHERE operation_id = 52 AND platform_id = 4;
    DELETE FROM operation_operation_form
    WHERE operation_id BETWEEN 4001 AND 4005 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3005 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3007 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3009 AND operation_form_id = 110;
    DELETE FROM operation_operation_form
    WHERE operation_id = 3013 AND operation_form_id = 110;
    
    UPDATE operation_form_field_translation
    SET label='Treat these values as NULL (comma-separated)', 
    help='These values will be considered as NULL when parsing the file. Separe items by comma (,).'
    WHERE id=3005 AND locale='en';
    """,
     """
     INSERT INTO operation_platform (operation_id, platform_id)
     VALUES (1, 4), (73, 4), (52, 4);
     INSERT INTO operation_operation_form (operation_id, operation_form_id)
     VALUES (3005, 110), (3007, 110), (3009, 110), (3013, 110),
            (4001, 110), (4002, 110), (4003, 110), (4004, 110), (4005, 110);
     """),

]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                cmds = cmd[0].split(';')
                for new_cmd in cmds:
                    if new_cmd.strip():
                        connection.execute(new_cmd)
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
                cmds = cmd[1].split(';')
                for new_cmd in cmds:
                    if new_cmd.strip():
                        connection.execute(new_cmd)
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()