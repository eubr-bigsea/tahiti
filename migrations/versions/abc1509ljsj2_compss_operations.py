# -*- coding: utf-8 -*-

"""Adding COMPSs Operations

Revision ID: abc1509ljsjf
Revises: 42d80390b2db
Create Date: 2017-09-08 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = 'abc1509ljsj2'
down_revision = '42d80390b2db'
branch_labels = None
depends_on = None



def _update_platform():
    op.execute(text('UPDATE platform SET enabled = 1 WHERE id = 3'))
    #op.execute(text('UPDATE platform SET icon = "" WHERE id = 3'))

    op.execute(text("""
		UPDATE platform_translation
		SET description = 'COMPSs 2.1 Bougainvillea - Execution platform'
		WHERE id = 3 and locale = 'en'
		"""))

    op.execute(text("""
		UPDATE platform_translation
		SET description = 'COMPSs 2.1 Bougainvillea - Plataforma de execução'
		WHERE id = 3 and locale = 'pt'
		"""))

def _add_operations_platform_from_spark():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [

		(3, 3), #'frequent-item-set'
        (5, 3), #'filter-selection'
        (6, 3), #'projection'
		(7, 3), #'tranformation'

        (12, 3),#'add-rows'
        (13, 3),#'set-intersection'
		(15, 3),#'aggregation'
        (16, 3),#'join'
        (17, 3),#'split'
		(21, 3),#'clean-missing'
        (23, 3),#'remove-duplicated-rows'
        (24, 3),#'add-columns'
        (25, 3),#'comment'
        (28, 3),#'sample'
		(32, 3),#'sort'
        (37, 3),#'difference'
		(41, 3),#'feature-assembler'

		(49, 3),#'tokenizer'
		(50, 3),#'remove-stop-words'
		(53, 3),#'read-shapefile'
		(55, 3),#'within'
		(85, 3),#'association-rules'
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)

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
        (3001, 'data-reader', 1,  	'TRANSFORMATION', 'fa-database'),
        (3002, 'data-writer', 1,  	'ACTION', 'fa-save'),
		(3003, 'balance-data', 1, 	'TRANSFORMATION', 'fa-balance-scale' ),
		(3004, 'word-to-vector', 1, 'TRANSFORMATION', 'fa-long-arrow-right'),
        (3005, 'knn-classifier', 1, 'TRANSFORMATION', 'fa-braille'),
        (3006, 'svm-classification', 1, 'TRANSFORMATION', 'fa-tag'),
		(3007, 'linear-regression', 1, 'TRANSFORMATION', 'fa-line-chart'),
		(3008, 'logistic-regression', 1, 'TRANSFORMATION', 'fa-exchange'),
		(3009, 'k-means-clustering', 1, 'TRANSFORMATION', 'fa-braille'),
		(3010, 'evaluate-model', 1, 'TRANSFORMATION', 'fa-check'),
		(3011, 'replace-value', 1, 'TRANSFORMATION', 'fa-eraser'),
		(3012, 'feature-indexer', 1, 'TRANSFORMATION', 'fa-list-ol'),
		(3013, 'naive-bayes-classifier', 1, 'TRANSFORMATION', 'fa-tag'),
		(3014, 'drop', 1, 'TRANSFORMATION', 'fa-binoculars'),
		(3015, 'regression-model', 1, 'TRANSFORMATION', 'fa-shield'),
		(3016, 'clustering-model', 1, 'TRANSFORMATION', 'fa-users'),
		(3017, 'page-rank', 1, 'TRANSFORMATION', 'fa-share-alt'),
		(3018, 'classification-model', 1, 'TRANSFORMATION', 'fa-dashboard'),
		(3019, 'apply-model', 1, 'TRANSFORMATION', 'fa-lightbulb-o'),
		(3020, 'dbscan-clustering',1,'TRANSFORMATION','fa-dot-circle-o'),
		(3021, 'stdbscan',1,'TRANSFORMATION','fa-dot-circle-o'),
		(3022, 'normalize',1,'TRANSFORMATION','fa-text-height'),
		(3023, 'change-attribute', 1, 'TRANSFORMATION', 'fa-edit'),

    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category():
    # Tive que adicionar nova categoria, para pertencer as operacoes do COMPSs
    tb = table('operation_category',
                            column("id", Integer),
                            column("type", String),
                            )
    columns = ['id', 'type']
    data = [
        (3001, 'technology'),
		(3002, 'group'), 	#Graph

    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category_translation():

    tb = table('operation_category_translation',
                            column("id", Integer),
                            column("locale", String),
                            column('name', String),
                            )
    columns = ['id', 'locale', 'name']
    data = [
        (3001, 'en', 'COMPSs'),
        (3001, 'pt', 'COMPSs'),
		(3002, 'en', 'Graph'),
		(3002, 'pt', 'Grafo'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


# -----------------------------------------------------------------------------

def _insert_new_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
		(3001, 3),#data-reader
        (3002, 3),#data-writer
		(3003, 3),#balance-data
		(3004, 3),#word-to-vector
        (3005, 3),#knn-classifier
        (3006, 3),#svm-classification
		(3007, 3),#linear-regression
		(3008, 3),#logistic-regression
		(3009, 3),#k-means
		(3010, 3),#evaluation-model
		(3011, 3),#replace-value
		(3012, 3),#feature-indexer'
		(3013, 3),#naive-bayes-classifier
		(3014, 3),#drop
		(3015, 3),#regression-model
		(3016, 3),#clustering-model
		(3017, 3),#page-rank
		(3018, 3),#classification-model
		(3019, 3),#apply-model
		(3020, 3),#dbscan-clustering
		(3021, 3),#stdbscan
		(3022, 3),#normalize
		(3023, 3),#change-attribute
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
			(3001, 3),#data-reader
			(3001, 3001),#data-reader
        	(3001, 6),#data-reader

			(3002, 6),#data-writer
			(3002, 3001),#data-writer

			(3003, 10),#balance-data
			(3003, 3001),#balance-data

			(3004, 12),#word-to-vector
			(3004, 3001),

			(3005, 8),#knn-classifier
	        (3005, 18),#knn-classifier
			(3005, 3001),

			(3006,  8),#svm-classification
	        (3006, 18),#svm-classification
			(3006, 3001),

			(3007, 8),#linear-regression
			(3007, 21),#linear-regression
			(3007, 3001),

			(3008, 8),#logistic-regression
			(3008, 18),#logistic-regression
			(3008, 3001),

			(3009, 8),#k-means
			(3009, 19),#k-means
			(3009, 3001),

			#evaluation-model
			(3010, 8),
			(3010, 26),
			(3010, 3001),

			(3011, 7),#replace-value
			(3011, 3001),

			(3012, 8),#feature-indexer'
			(3012, 23),#feature-indexer'
			(3012, 3001),

			(3013, 8),#svm-classification
			(3013, 18),#svm-classification
			(3013, 3001),#svm-classification

			(3014, 7),	 #drop
			(3014, 3001), #drop

			(3015, 8),#regression-model
			(3015, 21),#regression-model
			(3015, 3001),#regression-model

			(3016, 8),#clustering-model
			(3016, 19),#clustering-model
			(3016, 3001),#clustering-model

			(3017,3002), #page-rank
			(3017,3001), #page-rank

			(3018, 8),#classification-model
			(3018, 18),#classification-model
			(3018, 3001),#classification-model

			#apply-model
			(3019, 8),
			(3019, 26),
			(3019, 3001),

			#dbscan-clustering
			(3020, 8),
			(3020, 19),
			(3020, 3001),

			#stdbscan
			(3021, 17),
			(3021, 3001),

			#normalize
			(3022, 7),
			(3022, 3001),

			#change-attribute
			(3023, 10),
			(3023, 3001),
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
        (3001, 1, 1, 'execution'),#data-reader
		(3002, 1, 1, 'execution'),#data-writer
		(3003, 1, 1, 'execution'),#balance-data
		(3004, 1, 1, 'execution'),#word-to-vector
		(3005, 1, 1, 'execution'),#knn-classifier
		(3006, 1, 1, 'execution'),#svm-classification
		(3007, 1, 1, 'execution'),#linear-regression
		(3008, 1, 1, 'execution'),#logistic-regression
		(3009, 1, 1, 'execution'),#k-means
		(3010, 1, 1, 'execution'),#evaluation-model
		(3011, 1, 1, 'execution'),#replace-value
		(3012, 1, 1, 'execution'),#feature-indexer'
		(3013, 1, 1, 'execution'),#naive-bayes-classifier
		(3014, 1, 1, 'execution'),#drop
		(3015, 1, 1, 'execution'),#regression-model
		(3016, 1, 1, 'execution'),#clustering-model
		(3017, 1, 1, 'execution'),#page-rank
		(3018, 1, 1, 'execution'),#classification-model
		(3019, 1, 1, 'execution'),#apply-model
		(3020, 1, 1, 'execution'),#dbscan-clustering
		(3021, 1, 1, 'execution'),#stdbscan
		(3022, 1, 1, 'execution'),#normalize
		(3023, 1, 1, 'execution'),#change-attribute
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
        (3001, 'en', 'Execution'),
        (3001, 'pt', 'Execução'),
        (3002, 'en', 'Execution'),
        (3002, 'pt', 'Execução'),
		(3003, 'en', 'Execution'),
        (3003, 'pt', 'Execução'),
		(3004, 'en', 'Execution'),
        (3004, 'pt', 'Execução'),
		(3005, 'en', 'Execution'),
        (3005, 'pt', 'Execução'),
		(3006, 'en', 'Execution'),
        (3006, 'pt', 'Execução'),
		(3007, 'en', 'Execution'),
        (3007, 'pt', 'Execução'),
		(3008, 'en', 'Execution'),
        (3008, 'pt', 'Execução'),
		(3009, 'en', 'Execution'),
        (3009, 'pt', 'Execução'),
		(3010, 'en', 'Execution'),
        (3010, 'pt', 'Execução'),
		(3011, 'en', 'Execution'),
        (3011, 'pt', 'Execução'),
		(3012, 'en', 'Execution'),
        (3012, 'pt', 'Execução'),
		(3013, 'en', 'Execution'),
        (3013, 'pt', 'Execução'),
		(3014, 'en', 'Execution'),
        (3014, 'pt', 'Execução'),
		(3015, 'en', 'Execution'),
        (3015, 'pt', 'Execução'),
		(3016, 'en', 'Execution'),
        (3016, 'pt', 'Execução'),
		(3017, 'en', 'Execution'),
		(3017, 'pt', 'Execução'),
		(3018, 'en', 'Execution'),
		(3018, 'pt', 'Execução'),
		(3019, 'en', 'Execution'),
		(3019, 'pt', 'Execução'),
		(3020, 'en', 'Execution'),
		(3020, 'pt', 'Execução'),
		(3021, 'en', 'Execution'),
		(3021, 'pt', 'Execução'),
		(3022, 'en', 'Execution'),
		(3022, 'pt', 'Execução'),
		(3023, 'en', 'Execution'),
		(3023, 'pt', 'Execução'),
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
		(3001, 39),#data-reader
		(3001, 40),
		(3001, 41),
		(3001, 43),
		(3001, 110),
		(3001,3001),
		(3002, 39),#data-writer
		(3002, 40),
		(3002, 41),
		(3002, 43),
		(3002, 110),
		(3002,3002),
		(3003, 39),#balance-data
		(3003, 40),
		(3003, 41),
		(3003, 43),
		(3003, 110),
		(3003,3003),
		(3004, 39),#word-to-vector
		(3004, 40),
		(3004, 41),
		(3004, 43),
		(3004, 110),
		(3004,3004),
		(3005, 39),#knn-classifier
		(3005, 40),
		(3005, 41),
		(3005, 43),
		(3005, 110),
		(3005,3005),
		(3006, 39),#svm-classification
		(3006, 40),
		(3006, 41),
		(3006, 43),
		(3006, 110),
		(3006,3006),
		(3007, 39),#linear-regression
		(3007, 40),
		(3007, 41),
		(3007, 43),
		(3007, 110),
		(3007,3007),
		(3008, 39),#logistic-regression
		(3008, 40),
		(3008, 41),
		(3008, 43),
		(3008, 110),
		(3008,3008),
		(3009, 39),#k-means
		(3009, 40),
		(3009, 41),
		(3009, 43),
		(3009, 110),
		(3009,3009),
		(3010, 39),#evaluation-model
		(3010, 40),
		(3010, 41),
		(3010, 43),
		(3010, 110),
		(3010,3010),
		(3011, 39),#replace-value
		(3011, 40),
		(3011, 41),
		(3011, 43),
		(3011, 110),
		(3011,3011),
		(3012, 39),#feature-indexer'
		(3012, 40),
		(3012, 41),
		(3012, 43),
		(3012, 110),
		(3012,3012),
		(3013, 39),#naive-bayes-classifier
		(3013, 40),
		(3013, 41),
		(3013, 43),
		(3013, 110),
		(3013,3013),
		(3014, 39),#drop
		(3014, 40),
		(3014, 41),
		(3014, 43),
		(3014, 110),
		(3014,3014),
		(3015, 39),#regression-model
		(3015, 40),
		(3015, 41),
		(3015, 43),
		(3015, 110),
		(3015, 3015),
		(3016, 39),#clustering-model
		(3016, 40),
		(3016, 41),
		(3016, 43),
		(3016, 110),
		(3016, 3016),
		(3017, 39),#page-rank
		(3017, 40),
		(3017, 41),
		(3017, 43),
		(3017, 110),
		(3017, 3017),
		(3018, 39),#classification-model
		(3018, 40),
		(3018, 41),
		(3018, 43),
		(3018, 110),
		(3018, 3018),
		(3019, 39),#apply-model
		(3019, 40),
		(3019, 41),
		(3019, 43),
		(3019, 110),
		(3019, 3019),

		(3020, 39),#dbscan-clustering
		(3020, 40),
		(3020, 41),
		(3020, 43),
		(3020, 110),
		(3020, 3020),

		(3021, 39),#stdbscan
		(3021, 40),
		(3021, 41),
		(3021, 43),
		(3021, 110),
		(3021, 3021),

		(3022, 39),#normalize
		(3022, 40),
		(3022, 41),
		(3022, 43),
		(3022, 110),
		(3022, 3022),

		(3023, 39),#change-attribute
		(3023, 40),
		(3023, 41),
		(3023, 43),
		(3023, 110),
		(3023,3023),
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
        (3001, 'en', 'Data reader', 'Reads data from a data set'),
        (3001, 'pt', 'Leitor de dados', 'Lê dados de uma fonte de dados'),

        (3002, 'en', 'Data writer', 'Writes a new data set'),
        (3002, 'pt', 'Escritor de dados', 'Escreve uma nova fonte de dados'),

		(3003, 'en', 'Workload balancer', 'Balances the workload between the resources'),
        (3003, 'pt', 'Balanceador de carga', 'Balancea a carga de trabalho entre os recursos'),

		(3004, 'en', 'Convert words to vector', 'Convert words to vector'),
        (3004, 'pt', 'Converter palavras em vetor', 'Converter palavras em vetor'),

        (3005, 'en', 'KNN Classification', 'Uses a KNN Classifier'),
        (3005, 'pt', 'Classificador KNN', 'Usa um classificador KNN'),

        (3006, 'en', 'SVM Classification', 'Uses a SVM Classifier'),
        (3006, 'pt', 'Classificador SVM', 'Usa um classificador SVM'),

		(3007, 'en', 'Linear regression', 'Applies a linear regression algorithm'),
        (3007, 'pt', 'Regressão linear', 'Aplica a regressão linear'),

		(3008, 'en', 'Logistic regression', 'Performs logistic regression'),
        (3008, 'pt', 'Regressão logística', 'Realiza regressão logística'),

		(3009, 'en', 'K-Means Clustering', 'Uses K-Means algorithm for clustering'),
        (3009, 'pt', 'Agrupamento K-Means', 'Usa o algoritmo K-Means para agrupamento'),

		(3010, 'en', 'Evaluate model', 'Evaluates a machine learning model'),
        (3010, 'pt', 'Avaliar modelo', 'Avalia um modelo de aprendizado de máquina'),

		(3011, 'en', 'Replace value', 'Replaces column value by another'),
        (3011, 'pt', 'Substituir valor', 'Substitui o valor da coluna por outro valor'),

		(3012, 'en', 'Feature indexer', 'Indexes a feature by encoding a string column as a column containing indexes for labels (String type) or by encoding a Vector column as a column containing indexes for these vectors.'),
        (3012, 'pt', 'Indexador feature', 'Indexa uma feature codificando o texto da coluna como uma coluna contendo os índices para os rótulos ou codificando uma coluna do tipo Vector como uma coluna de índices para esses vetores'),

		(3013, 'en', 'Naive Bayes classifier', 'Naive Bayes Classifiers'),
        (3013, 'pt', 'Classificador Naive Bayes', 'Usa um classificador Naive Bayes'),

		(3014, 'en', 'Drop', 'Remove a selected column'),
        (3014, 'pt', 'Remover Coluna', 'Remove as colunas selecionadas'),

		(3015, 'en', 'Regression Model', 'Regression Model'),
		(3015, 'pt', 'Modelo de Regressão', 'Modelo de Regressão'),

		(3016, 'en', 'Clustering Model', 'Clustering Model'),
		(3016, 'pt', 'Modelo de Agrupamento', 'Modelo de Agrupamento'),

		(3017, 'en', 'PageRank', 'Applies a PageRank algorithm'),
		(3017, 'pt', 'PageRank', 'Aplica o algoritmo PageRank'),

		(3018, 'en', 'Classification Model', 'Classification Model'),
		(3018, 'pt', 'Modelo de Classificação', 'Modelo de Classificação'),

		(3019, 'en', 'Apply model', 'Apply a machine learning model to data'),
		(3019, 'pt', 'Aplicar modelo', 'Aplica um modelo de aprendizado de máquina aos dados'),

		(3020, 'en', 'DBSCAN Clustering', 'Uses DBSCAN algorithm for clustering'),
        (3020, 'pt', 'Agrupamento DBSCAN', 'Usa o algoritmo DBSCAN para agrupamento'),

		(3021, 'en', 'ST-DBSCAN', 'Uses ST-DBSCAN algorithm for clustering spartial-temporal data'),
        (3021, 'pt', 'ST-DBSCAN', 'Usa o algoritmo ST-DBSCAN para agrupamento de dados espacias-temporais'),

		(3022, 'en', 'Normalize Data', 'Normalize the selected columns'),
        (3022, 'pt', 'Normalizar Dados',  'Normaliza as colunas selecionadas'),

		(3023, 'en', 'Change attributes', 'Change metadata information associated to attributes'),
		(3023, 'pt', 'Modificar atributos', 'Altera metadados associados a um ou mais atributos'),

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
        (3001, 'OUTPUT', None, 3001, 1, 'MANY','output data'),#data-reader

        (3002, 'INPUT', None, 3002, 1, 'ONE', 'input data'),#data-writer

        (3003, 'INPUT', None, 3003, 1, 'ONE', 'input data'),#balance-data
		(3004, 'OUTPUT', None, 3003, 1, 'MANY', 'output data'),#balance-data

		(3005, 'INPUT', None, 3004, 1, 'ONE','input data'),#word-to-vector
		(3006, 'OUTPUT', None, 3004, 1, 'MANY','output data'),#word-to-vector
		(3007, 'OUTPUT', None, 3004, 1, 'MANY','vocabulary'),#word-to-vector

		(3008, 'OUTPUT', None, 3005, 1, 'MANY', 'algorithm'),#knn-classifier

		(3009, 'OUTPUT', None, 3006, 1, 'MANY', 'algorithm'),#svm-classification

		(3010, 'OUTPUT', None, 3007, 1, 'MANY', 'algorithm'),#linear-regression

		(3011, 'OUTPUT', None, 3008, 1, 'MANY', 'algorithm'),#logistic-regression

		(3012, 'OUTPUT', None, 3009, 1, 'ONE', 'algorithm'),#k-means

		(3013, 'INPUT',  None, 3010,1, 'ONE', 'input data'),	#evaluation-model
		(3014, 'INPUT',  None, 3010,1, 'ONE', 'model'),			#evaluation-model
		(3015, 'OUTPUT', None, 3010,1, 'MANY', 'evaluated model'),	#evaluation-model
		(3016, 'OUTPUT', None, 3010,1, 'MANY', 'evaluator'),	#evaluation-model

		(3017, 'INPUT',  None, 3011,1, 'ONE', 'input data'),#replace-value
		(3018, 'OUTPUT', None, 3011,1, 'MANY', 'output data'),#replace-value

		(3019, 'INPUT', None, 3012, 1, 'ONE', 'input data'),	#feature-indexer'
		(3020, 'OUTPUT', None, 3012, 1, 'MANY', 'output data'),	#feature-indexer'

		(3021, 'OUTPUT', None, 3013, 1, 'MANY', 'algorithm'), #naive-bayes-classifier

		(3022, 'INPUT',  None, 3014,1, 'ONE', 'input data'),#drop
		(3023, 'OUTPUT', None, 3014,1, 'MANY', 'output data'),#drop

		(3024, 'INPUT',  None, 3015, 1, 'ONE',  'train input data'),#regression-model
		(3025, 'INPUT',  None, 3015, 2, 'ONE',  'algorithm'),		#regression-model
		(3026, 'OUTPUT', None, 3015, 2, 'MANY', 'model'),			#regression-model
		(3032, 'OUTPUT', None, 3015, 1, 'MANY', 'output data'),		#regression-model

		(3027, 'INPUT',  None, 3016, 1, 'ONE',  'train input data'),#clustering-model
		(3028, 'INPUT',  None, 3016, 2, 'ONE',  'algorithm'),		#clustering-model
		(3029, 'OUTPUT', None, 3016, 2, 'MANY', 'model'),			#clustering-model
		(3033, 'OUTPUT', None, 3016, 1, 'MANY', 'output data'),		#clustering-model

		(3030, 'INPUT',  None, 3017, 1, 'ONE', 'input data'),#page-rank
		(3031, 'OUTPUT', None, 3017, 1, 'MANY', 'output data'),#page-rank

		(3034, 'INPUT',  None, 3018, 1, 'ONE',  'train input data'),#classification-model
		(3035, 'INPUT',  None, 3018, 2, 'ONE',  'algorithm'),		#classification-model
		(3036, 'OUTPUT', None, 3018, 2, 'MANY', 'model'),			#classification-model
		(3037, 'OUTPUT', None, 3018, 1, 'MANY', 'output data'),		#classification-model

		#apply-model
		(3038, 'INPUT',  None, 3019, 1,'ONE', 'input data'),
		(3039, 'INPUT',  None, 3019, 2,'ONE', 'model'),
		(3040, 'OUTPUT', None, 3019, 1, 'MANY', 'output data'),

		#dbscan-clustering
		(3041, 'OUTPUT', None, 3020, 1, 'ONE', 'algorithm'),

		#stdbscan
		(3042, 'INPUT',  None, 3021,1, 'ONE',   'input data'),
		(3043, 'OUTPUT', None, 3021,1, 'MANY', 'output data'),

		#normalize
		(3044, 'INPUT',  None, 3022,1, 'ONE', 'input data'),
		(3045, 'OUTPUT', None, 3022,1, 'MANY', 'output data'),

		#change-attribute
		(3046, 'INPUT', None, 3023, 1, 'ONE', 'input data'),
		(3047, 'OUTPUT', None, 3023, 1, 'MANY', 'output data'),


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
			(3001, 'en','output data', 'Read data'),#data-reader
			(3001, 'pt','dados de saída', 'Lê dados'),#data-reader

	        (3002, 'en', 'input data','Write data'),#data-writer
			(3002, 'pt', 'dados de entrada','Escrita de dados'),#data-writer

	        (3003, 'en', 'input data', 'Input Data'),#balance-data
			(3003, 'pt', 'dados de entrada', "Dados de entrada"),#balance-data
			(3004, 'en', 'output data', "Output Data"),#balance-data
			(3004, 'pt', 'dados de saída','Dados de saída'),#balance-data

			(3005, 'en','input data', 'Input Data'),#word-to-vector
			(3005, 'pt', 'dados de entrada', "Dados de entrada"),#word-to-vector
			(3006, 'en','output data',"Output Data"),#word-to-vector
			(3006, 'pt', 'dados de saída','Dados de saída'),#word-to-vector
			(3007, 'en','vocabulary', 'Vocabulary'),#word-to-vector
			(3007, 'pt','vocabulário', 'Vocabulário'),#word-to-vector

			(3008, 'en', 'algorithm', 'Untrained classification model'),#knn-classifier
			(3008, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),#knn-classifier

			(3009, 'en', 'algorithm', 'Untrained classification model'),#svm-classification
			(3009, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),#svm-classification

			(3010, 'en', 'algorithm', 'Regression model'),#linear-regression
			(3010, 'pt', 'algoritmo', 'Modelo de regressão'),#linear-regression

			(3011, 'en', 'algorithm', 'Untrained classification model'),#logistic-regression
			(3011, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),#logistic-regression

			(3012, 'en', 'algorithm', 'Clustering model'),#k-means
			(3012, 'pt', 'algoritmo', 'Modelo de agrupamento'),#k-means

			(3013, 'en', 'input data', 'Input Data'),#evaluation-model
			(3013, 'pt', 'dados de entrada', "Dados de entrada"),#evaluation-model
			(3014, 'en', 'model','Model'),#evaluation-model
			(3014, 'pt', 'modelo', 'Modelo'),#evaluation-model
			(3015, 'en', 'evaluated model','Evaluated model'),#evaluation-model
			(3015, 'pt', 'modelo avaliado','Modelo avaliado'),#evaluation-model
			(3016, 'en', 'evaluator',"Evaluator"),#evaluation-mo
			(3016, 'pt', 'avaliador','Avaliador'),#evaluation-mo

			(3017, 'en', 'input data', 'Input Data'),#replace-value
			(3017, 'pt', 'dados de entrada', "Dados de entrada"),#replace-value
			(3018, 'en', 'output data','Output Data'),#replace-value
			(3018, 'pt', 'dados de saída','Dados de saída'),#replace-value

			(3019, 'en', 'input data', 'Input Data'),	#feature-indexer'
			(3019, 'pt', 'dados de entrada', "Dados de entrada"),	#feature-indexer'
			(3020, 'en', 'output data', 'Output Data'),	#feature-indexer'
			(3020, 'pt', 'dados de saída', 'Dados de saída'),	#feature-indexer'

			(3021, 'en', 'algorithm', 'Untrained classification model'), #naive-bayes-classifier
			(3021, 'pt', 'algoritmo', 'Modelo de classificação não treinado'), #naive-bayes-classifier

			(3022, 'en', 'input data', 'Input Data'),#drop
			(3023, 'en', 'output data','Output Data'),#drop
			(3022, 'pt', 'dados de entrada', "Dados de entrada"),#drop
			(3023, 'pt', 'dados de saída','Dados de saída'),#drop

			(3024, 'en', 'train input data', 'Train input data'), #regression-model
			(3024, 'pt', 'dados de treino de entrada', 'Dados de treino de entrada'), #regression-model
			(3025, 'en', 'algorithm', 'Algorithm'), #regression-model
			(3025, 'pt', 'algoritmo', 'Algoritmo'), #regression-model
			(3026, 'en', 'model', 'Model'), 		#regression-model
			(3026, 'pt', 'modelo', 'Modelo'), 		#regression-model
			(3032, 'en', 'output data', 'Output Data'),	#regression-model
			(3032, 'pt', 'dados de saída', 'Dados de saída'), #regression-model

			(3027, 'en', 'train input data', 'Train input data'), #clustering-model
			(3027, 'pt', 'dados de treino de entrada', 'Dados de treino de entrada'), #clustering-model
			(3028, 'en', 'algorithm', 'Algorithm'),#clustering-model
			(3028, 'pt', 'algoritmo', 'Algoritmo'),#clustering-model
			(3029, 'en', 'model', 'Model'),#clustering-model
			(3029, 'pt', 'modelo', 'Modelo'),#clustering-model
			(3033, 'en', 'output data', 'Output Data'),	#clustering-model
			(3033, 'pt', 'dados de saída', 'Dados de saída'),#clustering-model

			(3030, 'en', 'input data', 'Input Data'),				#page-rank
			(3030, 'pt', 'dados de entrada', "Dados de entrada"), 	#page-rank
			(3031, 'en', 'output data', 'Output Data'),				#page-rank
			(3031, 'pt', 'dados de saída', 'Dados de saída'), 		#page-rank

			#classification-model
			(3034, 'en', 'train input data', 'Train input data'),
			(3034, 'pt', 'dados de treino de entrada', 'Dados de treino de entrada'),
			(3035, 'en', 'algorithm', 'Algorithm'),
			(3035, 'pt', 'algoritmo', 'Algoritmo'),
			(3036, 'en', 'model', 'Model'),
			(3036, 'pt', 'modelo', 'Modelo'),
			(3037, 'en', 'output data', 'Output Data'),
			(3037, 'pt', 'dados de saída', 'Dados de saída'),

			#apply-model
			(3038, 'en', 'input data', 'Input data'),
			(3038, 'pt', 'dados de entrada', 'Dados de entrada'),
			(3039, 'en', 'model', 'Model'),
			(3039, 'pt', 'modelo', 'Modelo'),
			(3040, 'en', 'output data', 'Output Data'),
			(3040, 'pt', 'dados de saída', 'Dados de saída'),

			#dbscan-clustering
			(3041, 'en', 'algorithm', 'Clustering model'),
			(3041, 'pt', 'algoritmo', 'Modelo de agrupamento'),

			#stdbscan
			(3042, 'en', 'input data', 'Input Data'),
			(3042, 'pt', 'dados de entrada', "Dados de entrada"),
			(3043, 'en', 'output data', "Output Data"),
			(3043, 'pt', 'dados de saída','Dados de saída'),

			#normalize
			(3044, 'en', 'input data', 'Input Data'),
			(3044, 'pt', 'dados de entrada', "Dados de entrada"),
			(3045, 'en', 'output data', 'Output Data'),
			(3045, 'pt', 'dados de saída', 'Dados de saída'),

			#change-attribute
			(3046, 'en', 'input data', 'Input Data'),
			(3046, 'pt', 'dados de entrada', "Dados de entrada"),
			(3047, 'en', 'output data', "Output Data"),
			(3047, 'pt', 'dados de saída','Dados de saída'),
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
        		(3001, 1),#data-reader
				(3002, 1),#data-writer
				(3003, 1),#balance-data
				(3004, 1),#balance-data
				(3005, 1),#word-to-vector
				(3006, 1),#word-to-vector
				(3007, 1),#word-to-vector
				(3008, 5),#knn-classifier
				(3009, 5),#svm-classification
				(3010, 17),#linear-regression
				(3011, 5),#logistic-regression
				(3012, 11),#k-means
				(3013, 1),#evaluation-model
				(3014, 2),#evaluation-model
				(3014, 18),#evaluation-model
				(3015, 7),#evaluation-model
				(3016, 10),#evaluation-model
				(3017, 1),#replace-value
				(3018, 1),#replace-value
				(3019, 1),#feature-indexer'
				(3020, 1),#feature-indexer'
				(3021, 5),#naive-bayes-classifier
				(3022, 1),#drop
				(3023, 1),#drop

				(3024, 1),#regression-model
				(3024, 6),#regression-model -- MachineLearningModel
				(3025, 17),#regression-model --> IRegressionAlgorithm
				(3026, 18),#regression-model --> model
				(3032, 1),#regression-model

				(3027, 1),#clustering-model
				(3028, 11),#clustering-model
				(3029, 18),#clustering-model --> model
				(3033, 1),#clustering-model

				#page-rank
				(3030, 1),
				(3031, 1),

				#classification-model
				(3034, 1),
				(3035, 5),
				(3036, 18),
				(3037, 1),

				#apply-model
				(3038,1),
				(3039,18),
				(3040,1),

				#dbscan-clustering
				(3041, 11),

				#stdbscan
				(3042, 1),
				(3043, 1),

				#normalize
				(3044, 1),
				(3045, 1),

				#change-attribute
				(3046, 1),
				(3047, 1),


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
		#data-reader
        (3001, 'data_source','TEXT', 1, 0, None, 'text', None, None, 'EXECUTION',3001),
        (3002, 'header', 'INTEGER', 0, 2, 1, 'checkbox', None, None,'EXECUTION', 3001),
        (3003, 'separator', 'TEXT', 1, 3, ',', 'text', None, None, 'EXECUTION',  3001),
        (3004, 'infer_schema', 'TEXT', 0, 4, 'FROM_LIMONERO', 'dropdown', None,
         '[\r\n  {"key": "FROM_VALUES", "value": "From data"},\r\n  '
         '{"key": "NO", "value": "Do not infer"}\r\n]',
         'EXECUTION', 3001),
        (3005, 'None_values', 'TEXT', 0, 3, None, 'textarea', None, None,'EXECUTION', 3001),

		#data-writer
		(3049, 'name', 'TEXT', '1', '1', None, 'text', None, None, 'EXECUTION', 3002),
		(3050, 'path', 'TEXT', '1', '2', None, 'text', None, None, 'EXECUTION', 3002),
		(3051, 'format', 'TEXT', '1', '4', None, 'dropdown', None,
		'[\r\n  { \"key\": \"CSV\", \"value\": \"CSV data file\" \r\n  },\r\n  '
		'{ \"key\": \"JSON\", \"value\": \"JSON data file\" \r\n  }]', 'EXECUTION', 3002),
		(3052, 'tags', 'TEXT', '0', '5', None, 'tag', None, None, 'EXECUTION', 3002),
		(3053, 'mode', 'INTEGER', '0', '6', None, 'dropdown', None,
		'[{ \"key\": \"append\", \"value\": \"Append data to the existing file\" },\r\n '
		'{\"key\": \"error\", \"value\": \"Do not overwrite, raise error\" },\r\n'
		'{\"key\": \"ignore\", \"value\": \"Ignore if file exists\" },\r\n '
		'{\"key\": \"overwrite\", \"value\": \"Overwrite if file exists\" }\r\n]', 'EXECUTION',  3002),
		(3054, 'header', 'INTEGER', '0', '7', None, 'checkbox', None, None, 'EXECUTION', 3002),

		#word-to-vector
		(3006, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector', None, None, 'EXECUTION', 3004),
		(3007, 'alias', 'TEXT', 	 1, 1, None, 'text', None, None, 'EXECUTION', 3004),
		(3008, 'type', 'TEXT', 		 1, 2, 'count', 'dropdown', None,
		'[\r\n  {\r\n  "key": "count", "value": \"Count term frequency\" \r\n},\r\n  '
		'{\r\n    \"key\": \"BoW\", \"value\": \"Use Bag of Words\" \r\n  }\r\n]', 'EXECUTION', 3004),
		(3009, 'vocab_size', 'INTEGER', 0, 3, None, 'integer', None, None, 'EXECUTION', 3004),
		(3010, 'minimum_df', 'INTEGER', 0, 4, None, 'integer', None, None, 'EXECUTION', 3004),
		(3011, 'minimum_tf', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 3004),

		#knn-classifier
        (3014, 'k', 'INTEGER', 1, 1, 1, 'integer', None, None, 'EXECUTION', 3005),

		#svm-classification
        (3017, 'coef_lambda', 'FLOAT', 		0, 1, 0.0001, 'decimal', None, None, 'EXECUTION', 3006),
        (3018, 'coef_lr', 'FLOAT', 			0, 2, 0.01, 'decimal', None, None, 'EXECUTION', 3006),
        (3019, 'coef_threshold', 'FLOAT', 	0, 3, 0.01, 'decimal', None, None, 'EXECUTION', 3006),
        (3020, 'max_iter', 'INTEGER', 		0, 4, 1000, 'integer', None, None, 'EXECUTION', 3006),

		#linear-regression
		(3032, 'alpha', 'FLOAT', 		0, 1, 0.001, 'decimal', None, None, 'EXECUTION', 3007),
		(3033, 'max_iter', 'INTEGER', 	0, 2, 100, 'integer', None, None, 'EXECUTION', 3007),

		#logistic-regression
		(3034, 'coef_alpha', 'FLOAT', 		0, 1, 0.001, 'decimal', None, None, 'EXECUTION', 3008),
		(3035, 'max_iter', 'INTEGER', 		0, 4, 100, 'integer', None, None, 'EXECUTION', 3008),
		(3036, 'coef_threshold', 'FLOAT', 	0, 3, 0.003, 'decimal', None, None, 'EXECUTION', 3008),
		(3037, 'coef_lr', 'FLOAT', 			0, 2, 0.01, 'decimal', None, None, 'EXECUTION', 3008),

		#k-means
		(3038, 'number_of_clusters', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION',  3009),
		(3039, 'init_mode', 'TEXT', 			1, 2, 'k-means||', 'dropdown', None,
        '[\r\n	{\"key\": \"k-means||\", \"value\": \"kmeans|| (kmeans++ variant)\"},\r\n	'
        '{\"key\": \"random\", \"value\": \"random\"}\r\n]', 'EXECUTION', 3009),
		(3040, 'max_iterations', 'INTEGER', 1, 3, None, 'integer', None, None, 'EXECUTION', 3009),
		(3041, 'tolerance', 'FLOAT', 		0, 4, 0.0001, 'decimal', None, None, 'EXECUTION', 3009),

		#evaluation-model
        (3042, 'metric', 'TEXT', 1, 3, None, 'dropdown', None,
        '[\r\n {  \"key\": \"f1\", \"value\": \" Precision, Recall and F1 (F-mesure)\" },\r\n '
        '{    \"key\": \"accuracy\", \"value\": \"Accuracy\"  },\r\n  '
        '{    \"key\": \"rmse\", \"value\": \"Root mean squared error  (Regression only)\" },\r\n '
        '{    \"mse\": \"mse\", \"value\": \"Mean squared error (Regression only)\"  },\r\n '
        '{    \"key\": \"mae\", \"value\": \"Mean absolute error  (Regression only)\"  }\r\n]', 'EXECUTION', 3010),
        (3043, 'label_attribute', 'TEXT',      1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3010),
        (3044, 'prediction_attribute', 'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 3010),

		#replace-value
		(3026, 'attributes', 'TEXT', '1', '0', None, 'attribute-selector', None, None, 'EXECUTION', 3011),
        (3045, 'mode', 'TEXT', 		 '1', '1', None, 'dropdown', None,
        '[{\"key\": \"regex\", \"value\": \"Replace by regex expression (only to string)\"},'
        ' {\"key\": \"value\", \"value\": \"Replace by value\"}]', 'EXECUTION', 3011),
        (3046, 'regex', 'TEXT', 	'0', '2', None, 'text', None, None, 'EXECUTION', 3011),
        (3047, 'old_value', 'TEXT', '0', '3', None, 'text', None, None, 'EXECUTION', 3011),
        (3048, 'new_value', 'TEXT', '1', '4', None, 'text', None, None, 'EXECUTION', 3011),

		#feature-indexer'
		(3027, 'attributes', 'TEXT', 	1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3012),
		(3028, 'indexer_type', 'TEXT', 	1, 3, None, 'dropdown', None,'[\r\n  {"key": "string", "value": "String"}\r\n]', 'EXECUTION', 3012),
		(3029, 'alias', 'TEXT', 		1, 2, None, 'text', None, None, 'EXECUTION', 3012),

		#naive-bayes-classifier
		#nothing

		#drop
		(3055, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3014),

		#regression-model
		(3056, 'features', 'TEXT', 	 1, 1, None, 'attribute-selector', None, None, 'EXECUTION',3015),
		(3057, 'label', 'TEXT', 	 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 3015),
		(3058, 'prediction', 'TEXT', 0, 3, 'prediction', 'text', None, None, 'EXECUTION', 3015),

		#clustering-model
		(3059, 'features', 'TEXT',   1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3016),
		(3060, 'prediction', 'TEXT', 0, 2, 'prediction', 'text', None, None, 'EXECUTION', 3016),

		#pagerank
		(3061, 'outlink',         'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3017),
		(3062, 'inlink',          'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 3017),
		(3063, 'maxIters',     'INTEGER', 0, 3, 100, 'integer', None, None, 'EXECUTION', 3017),
		(3064, 'damping_factor', 'FLOAT', 0, 4, 0.85, 'decimal', None, None, 'EXECUTION', 3017),

		#classification-model
		(3065, 'features', 'TEXT', 	1, 0, None, 'attribute-selector', None, None, 'EXECUTION',3018),
		(3066, 'label', 'TEXT',   	1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3018),
		(3067, 'prediction', 'TEXT',0, 2, 'prediction', 'text', None, None, 'EXECUTION', 3018),

		#apply-model
		(3068, 'features', 'TEXT', 	 1, 1, None, 'attribute-selector', None, None, 'EXECUTION',3019),
		(3069, 'prediction', 'TEXT', 0, 2, 'prediction', 'text', None, None, 'EXECUTION', 3019),

		#dbscan-clustering
		(3070, 'eps', 		   'FLOAT',	0, 1, 0.5, 'decimal', None, None, 'EXECUTION', 3020),
		(3071, 'min_sample', 'INTEGER', 0, 2, 10,  'integer', None, None, 'EXECUTION', 3020),

		#stdbscan
		(3072, 'LAT', 		'TEXT', 1, 0, None, 'attribute-selector', None, None, 'EXECUTION', 3021),
		(3073, 'LON', 		'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3021),
		(3074, 'DATETIME', 	'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 3021),
		(3075, 'thresold_spartial',	   'FLOAT',	0, 3, 500, 'decimal', None, None, 'EXECUTION', 3021),
		(3076, 'thresold_temporal',	   'FLOAT',	0, 4, 60,  'decimal', None, None, 'EXECUTION', 3021),
		(3077, 'min_sample', 		 'INTEGER', 0, 5, 10,  'integer', None, None, 'EXECUTION', 3021),

		#normalize
		(3078, 'attributes', 'TEXT',1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3022),
        (3079, 'alias', 'TEXT', 	1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 3022),
		(3080, 'mode',  'TEXT', 	1, 3, 'range', 'dropdown', None,
		'[{\"key\": \"range\", \"value\": \"Range Normalization\"},\r\n  '
        ' {\"key\": \"standard\", \"value\": \"Standard Score Normalization\"}\r\n  ]', 'EXECUTION', 3022),

		#change-attribute
		(3081, 'attributes', 'TEXT', 	1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 3023),
		(3082, 'new_name', 'TEXT', 		0, 2, None, 'text', None, None, 'EXECUTION', 3023),
		(3083, 'new_data_type', 'TEXT', 0, 3, None, 'dropdown', None,
								 '[\r\n{\"key\": \"keep\", \"value\": \"Do not change\"},\r\n '
								 '{\"key\": \"integer\", \"value\": \"Integer\"},\r\n'
								 '{\"key\": \"string\", \"value\": \"String\"},\r\n '
								 '{\"key\": \"double\", \"value\": \"Double\"},\r\n '
								 '{\"key\": \"Date\", \"value\": \"Date\"},\r\n '
								 '{\"key\": \"Date/time\", \"value\": \"Date/time\"}]', 'EXECUTION', 3023),



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
		#data-reader
        (3001, 'en', 'Data source', 'Data source to be used as input.'),
        (3001, 'pt', 'Fonte de Dados', 'Fonte de dados para ser usado como entrada.'),
        (3002, 'en', 'Use first line as header', 'Does file first line contain header information about attributes?'),
        (3002, 'pt', 'Usar primeira linha como header', 'A primeira linha contêm informação sobre os campos?'),
        (3003, 'en', 'Attribute separator','Character used as attribute separator'),
        (3003, 'pt', 'Atributo separador','Caractere usado como atributo separador'),
        (3004, 'en', 'Infer data source schema',  'Infer data source schema from attribute\'s values.'),
        (3004, 'pt', 'Infer data source schema',   'Infer data source schema from attribute\'s values.'),
        (3005, 'en', 'Treat these values as None (comma-separated)',
         'These values will be considered as None when parsing the file. '
         'Separe items by comma (,).'),
        (3005, 'pt', 'Tratar esses valores como nulos (separe por vírgula)',
         'Esses valores serão considerados como nulos quando o arquivo '
         'estiver sendo lido. Separe os valores por vírgula (,).'),

		 #data-writer
		(3049, 'en', 'Data source name', 'Data source name'),
 		(3050, 'en', 'Data source path (relative to storage)', 'Path for data source'),
 		(3051, 'en', 'Output format', 'Output format used to write data'),
 		(3052, 'en', 'Tags', 'Tags'),
 		(3053, 'en', 'Overwrite mode', 'Action in case of trying to write over an existing file'),
 		(3054, 'en', 'Save header', 'Save header information if format is CSV'),
		(3049, 'pt', 'Data source name', 'Data source name'),
 		(3050, 'pt', 'Data source path (relative to storage)', 'Path for data source'),
 		(3051, 'pt','Formato de saída','Formato de saída usado para a escrita do dado.'),
 		(3052, 'pt', 'Tags', 'Tags'),
 		(3053, 'pt', 'Modo sobrescrever', 'Ação em caso de tentar escrever sobre um arquivo já existente'),
 		(3054, 'pt','Salvar header', 'Salva o cabeçalho se o formato for CSV'),

         #word-to-vector
         (3006, 'en', 'Attributes', 'Attributes'),
         (3006, 'pt', 'Attributos', 'Colunas para serem consideradas'),
         (3007, 'en', 'Alias', 'Name of the new column'),
         (3007, 'pt', 'Alias', 'Nome para a nova coluna criada'),
         (3008, 'en', 'Type', 'Type'),
         (3008, 'pt', 'Tipo', 'Tipo'),
         (3009,'pt', 'Tamanho do vocabulário', 'Tamanho do vocabulário'),
         (3009,'en', 'Vocabulary size', 'Vocabulary size'),
         (3010,'pt', 'Frequência mínima de documentos (DF)','Frequência mínima de documentos (DF)'),
         (3010,'en', 'Minimum frequency in docs (DF)', 'Minimum frequency in docs (DF)'),
         (3011,'en', 'Minimum term frequency (TF)', 'Minimum term frequency (TF)'),
         (3011,'pt', 'Frequência mínima do termo (TF)', 'Frequência mínima do termo (TF)'),

		 #knn-classifier
        (3014,'pt','k vizinhos','Número inteiro positivo geralmente pequeno '
        'que representa a quantidade de vizinhos para a classificação.'),
        (3014,'en','k neighbors','It\'s is a positive integer typically small '
        'which represents a number of neighbors to be used in the classification.'),

		#svm-classification
        (3017,'pt','Parâmetro de Regularização','Valores entre zero e infinito.'),
        (3017,'en','Regularization  parameter','Values between zero and infinity.'),
        (3018,'pt','Taxa de aprendizado','Valores entre zero e um.'),
        (3018,'en','Learning rate parameter','Values between zero and one'),
        (3019,'pt','Tolerância',"Tolerância para o critério de parada."),
        (3019,'en','Tolerance','Tolerance for stopping criterion'),
        (3020,'pt','Max iterações','Número máximo de iterações'),
        (3020,'en','Max iterations','Number of maximum iterations'),

        #linear-regression
        (3032, 'en', 'Learning rate parameter','Values between zero and one'),
		(3032, 'pt', 'Taxa de aprendizado','Valores entre zero e um.'),
        (3033, 'en', 'Max iterations','Number of maximum iterations'),
		(3033, 'pt', 'Max iterações','Número máximo de iterações'),

        #logistic-regression
        (3034, 'en', 'Learning rate parameter','Values between zero and one'),
		(3034, 'pt', 'Taxa de aprendizado','Valores entre zero e um.'),
        (3035, 'en', 'Max iterations','Number of maximum iterations'),
		(3035, 'pt', 'Max iterações','Número máximo de iterações'),
        (3036, 'pt', 'Tolerância',"Tolerância para o critério de parada."),
        (3036, 'en', 'Tolerance','Tolerance for stopping criterion'),
        (3037, 'pt', 'Parâmetro de Regularização','Valores entre zero e infinito.'),
        (3037, 'en', 'Regularization  parameter','Values between zero and infinity.'),

        #k-means
        (3038, 'en', 'Number of clusters (K)', 'Number of clusters (K)'),
        (3038, 'pt', 'Quantidade de agrupamentos (K)', 'Quantidade de agrupamentos (K)'),
        (3039, 'en', 'Init mode', 'How to generate initial centroids'),
        (3039, 'pt', 'Geração dos centroids iniciais', 'Geração dos centroids iniciais'),
        (3040, 'en', 'Max iterations', 'Max iterations'),
        (3040, 'pt', 'Número máx. de iterações', 'Número máx. de iterações'),
        (3041, 'en', 'Tolerance', 'Convergency tolerance for the within-cluster sums of point-to-centroid distances.'),
        (3041, 'pt', 'Tolerância', 'Tolerância de convergência para as somas das distâncias intra-cluster do ponto ao centroide.'),

        #evaluation-model
		(3042, 'en', 'Metric to evaluation', 'Metric to evaluation'),
		(3042, 'pt', 'Métrica de avaliação', 'Métrica de avaliação'),
		(3043, 'en', 'Label attribute', 'Label attribute'),
		(3043, 'pt', 'Label dos atributos', 'Label dos atributos'),
		(3044, 'en', 'Prediction attribute', 'Prediction attribute'),
		(3044, 'pt', 'Atributos', 'Atributos'),

        #replace-value
		(3026, 'en', 'Features', 'Feature'),
		(3026, 'pt', 'Atributos', 'Atributos'),
		(3045, 'en','Replacer type', 'Replacer type'),
		(3045, 'pt','Tipo de substituição', 'Tipo de substituição'),
		(3046, 'en','Regex expression (if choosed)', 'Regex expression'),
		(3046, 'pt','Expressão Regex (se escolhida)', 'Expressão Regex'),
		(3047, 'en','Old values (if choosed)', 'Old values'),
		(3047, 'pt','Valores antigos (se escolhida)', 'Valores antigos'),
		(3048, 'en','New values', 'New values'),
		(3048, 'pt','Novos valores', 'Novos valores'),

        #feature-indexer'
		(3027,'en','Attributes', 'Attributes (features) to be indexed'),
		(3027,'pt','Atributos', 'Atributos (features) a ser indexados'),
		(3028,'en','Indexer type', 'Indexer type'),
		(3028,'pt','Tipo de indexador', 'Tipo de indexador'),
		(3029,'en','Name for new indexed attribute(s)', 'Name for new indexed attribute(s)'),
		(3029,'pt','Nome para novo(s) atributo(s) indexado(s)', 'Nome para novo(s) atributo(s) indexado(s)'),

		#drop
		(3055, 'en', 'Attributes','Attributes to be deleted'),
		(3055, 'pt', 'Atributos', 'Atributos para serem removidos'),

		#regression-model
		(3056, 'en', 'Features', 'Feature'),
		(3056, 'pt', 'Atributos', 'Atributos'),
		(3057, 'en', 'Label attribute', 'Label attribute'),
		(3057, 'pt', 'Label dos atributos', 'Label dos atributos'),
		(3058, 'en', 'Prediction attribute', 'Prediction attribute'),
		(3058, 'pt', 'Atributo para predição', 'Atributo para predição'),

		#clustering-model
		(3059, 'en', 'Features', 'Feature'),
		(3059, 'pt', 'Atributos', 'Atributos'),
		(3060, 'en', 'Prediction attribute', 'Prediction attribute'),
		(3060, 'pt', 'Atributo para predição', 'Atributo para predição'),

		#page-rank
		(3061, 'en','Out-links attribute','Out-links attribute'),
		(3061, 'pt','Atributo do vértice saída','Atributo do vértice saída'),
		(3062, 'en','In-links attribute','In-links attribute'),
		(3062, 'pt','Atributo do vértice entrada','Atributo do vértice entrada'),
		(3063, 'en', 'Max iterations', 'Max iterations'),
        (3063, 'pt', 'Número máx. de iterações', 'Número máx. de iterações'),
		(3064, 'en','Damping Factor', 'Damping Factor'),
		(3064, 'pt','Fator de Amortecimento', 'Fator de Amortecimento'),

		#classification-model
		(3065, 'en', 'Features', 'Feature'),
		(3065, 'pt', 'Atributos', 'Atributos'),
		(3066, 'en', 'Label attribute', 'Label attribute'),
		(3066, 'pt', 'Label dos atributos', 'Label dos atributos'),
		(3067, 'en', 'Prediction attribute', 'Prediction attribute'),
		(3067, 'pt', 'Atributo para predição', 'Atributo para predição'),

		#apply-model
		(3068, 'en', 'Features', 'Feature'),
		(3068, 'pt', 'Atributos', 'Atributos'),
		(3069, 'en', 'Prediction attribute', 'Prediction attribute'),
		(3069, 'pt', 'Atributo para predição', 'Atributo para predição'),

		#dbscan-clustering
		(3070,'en','Eps','The maximum distance between two samples for them to be considered as in the same neighborhood.'),
		(3070,'pt','Eps','A distânca máxima entre dois pontos para serem considerados do mesmo grupo.'),
		(3071,'en','Minimum sample', 'The number of samples in a neighborhood for a point to be considered as a core point.'),
		(3071,'pt','Número minimo da vizinhança', 'O número de pontos vizinhos para ser considerado um ponto central.'),

		#stdbscan
		(3072, 'en', 'Latitude Column', 'Latitude Column'),
		(3072, 'pt', 'Coluna da Latitude', 'Coluna da Latitude'),
		(3073, 'en', 'Longitude Column', 'Longitude Column'),
		(3073, 'pt', 'Coluna da Longitude', 'Coluna da Longitude'),
		(3074, 'en', 'Datetime Column', 'Datetime Column'),
		(3074, 'pt', 'Coluna do Datetime', 'Coluna do Datetime'),
		(3075, 'en', 'Spartial distance thresold (in meters)','The maximum distance between two samples for them to be considered as in the same neighborhood.'),
		(3075, 'pt', 'Distância espacial máxima (em metros)','A distânca máxima entre dois pontos para serem considerados do mesmo grupo.'),
		(3076, 'en', 'Temporal Distance thresold (in seconds)','The maximum distance between two samples for them to be considered as in the same neighborhood.'),
		(3076, 'pt', 'Intervalo de tempo máximo (em segundos)','A distânca máxima entre dois pontos para serem considerados do mesmo grupo.'),
		(3077, 'en', 'Minimum sample', 'The number of samples in a neighborhood for a point to be considered as a core point.'),
		(3077, 'pt', 'Número minimo da vizinhança', 'O número de pontos vizinhos para ser considerado um ponto central.'),

		#normalize
		(3078, 'en', 'Attributes', 'Attributes'),
		(3078, 'pt', 'Attributos', 'Colunas para serem consideradas'),
		(3079, 'en', 'Alias', 'Name of the new column'),
		(3079, 'pt', 'Alias', 'Nome para a nova coluna criada'),
		(3080, 'en', 'Normalization Type',   'Type of Normalization to perform.'),
		(3080, 'pt', 'Tipo de Normalização', 'Tipo de Normalização para ser feita.'),

		#change-attribute
		(3081, 'en', 'Attribute(s)', 'Select one or more attributes.'),
		(3081, 'pt', 'Atributo(s)', 'Selecione um ou mais atributos.'),
		(3082, 'en', 'New name', 'New name. If used with multiple attributes, a numerical suffix will be used to distinguish them. For example, name1, name2, ...\r\nYou can use the variable ${attribute_name} to rename attributes by adding a prefix or a suffix to the original name.'),
		(3082, 'pt', 'Novo nome', 'Novo nome. Se usado com vários atributos, o nome será o sufixo.'),
		(3083, 'en', 'New data type', 'New data type. A conversion is not performed and if you incorrectly change this information, the workflow may not work.'),
		(3083, 'pt', 'Novo tipo de dados', 'Novo tipo dos dados. Nenhuma conversão é realizada.'),



	]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)





all_commands = [
    (_update_platform,					 	'UPDATE platform SET enabled = 0 WHERE id = 3' ),
	(_add_operations_platform_from_spark, 	'DELETE FROM operation_platform WHERE platform_id = 3'),
	(_insert_operation_category,				'DELETE FROM operation_category WHERE id > 3000' ),
	(_insert_operation_category_translation,	'DELETE FROM operation_category_translation WHERE id > 3000' ),
	(_insert_operation, 						'DELETE FROM operation WHERE id > 3000'),
	(_insert_new_operation_platform,  	  	'DELETE FROM operation_platform WHERE platform_id = 3' ),
	(_insert_operation_category_operation, 	'DELETE FROM operation_category_operation WHERE operation_id > 3000'),
	(_insert_operation_form, 			'DELETE FROM operation_form WHERE id > 3000'),
	(_insert_operation_form_translation, 'DELETE FROM operation_form_translation WHERE id > 3000'),
	(_insert_operation_operation_form, 	'DELETE FROM operation_operation_form WHERE operation_id > 3000'),
	(_insert_operation_translation, 		'DELETE FROM operation_translation WHERE id > 3000'),
	(_insert_operation_port, 			'DELETE FROM operation_port WHERE id > 3000' ),
	(_insert_operation_port_translation, 'DELETE FROM operation_port_translation WHERE id > 3000' ),
	(_insert_operation_port_interface_operation_port, 'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id > 3000'),
	(_insert_operation_form_field, 					 'DELETE FROM operation_form_field WHERE id > 3000'),
	(_insert_operation_form_field_translation,		 'DELETE FROM operation_form_field_translation WHERE id > 3000' ),
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
