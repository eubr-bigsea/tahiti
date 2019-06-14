# coding=utf-8
"""refactoring_sklearn
Revision ID: 50e0ae9aa406f
Revises: fef08022f308
Create Date: 2019-01-23 14:55:47.471104
"""
import itertools

from alembic import context
from alembic import op
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '50e0ae9aa406f'
down_revision = '13dcbb138118'
branch_labels = None
depends_on = None

SKLEARN_PLATFORM = 4

OPERATIONS_CLASSIFIER = ",".join(
    ["4021", "4022", "4023", "4024", "4025", "4031", "4032", "4034", '4036'])
OPERATIONS_REGRESSOR = ",".join(
    ["4026", "4027", "4028", "4029", "4030", "4035"])
OPERATIONS_CLUSTERING = ",".join(["4033"])

ALL_OPERATIONS = OPERATIONS_CLASSIFIER + "," + \
                 OPERATIONS_CLUSTERING + "," + OPERATIONS_REGRESSOR


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (4021, 'logistic-regression-model', 1, 'TRANSFORMATION',
         'fa-exchange-alt'),
        (4022, 'random-forest-classifier-model', 1, 'TRANSFORMATION',
         'fa-random'),
        (4023, 'gbt-classifier-model', 1, 'TRANSFORMATION', 'fa-tree'),
        (4024, 'decision-tree-classifier-model', 1, 'TRANSFORMATION',
         'fa-arrow-right'),
        (4025, 'perceptron-classifier-model', 1, 'TRANSFORMATION',
         'fa-angle-double-down'),
        (4026, 'gbt-regressor-model', 1, 'TRANSFORMATION', 'fa-id-card'),
        (4027, 'linear-regression-model', 1, 'TRANSFORMATION', 'fa-chart-line'),
        (4028, 'random-forest-regressor-model', 1, 'TRANSFORMATION',
         'fa-laptop'),
        (4029, 'sgd-regressor-model', 1, 'TRANSFORMATION', 'fa-id-card'),
        (4030, 'huber-regressor-model', 1, 'TRANSFORMATION', 'fa-laptop'),
        (4031, 'svm-classification-model', 1, 'TRANSFORMATION', 'fa-tag'),
        (4032, 'naive-bayes-classifier-model', 1, 'TRANSFORMATION', 'fa-tag'),
        (4033, 'k-means-clustering-model', 1, 'TRANSFORMATION', 'fa-braille'),
        (4034, 'mlp-classifier-model', 1, 'TRANSFORMATION', 'fa-code-branch'),
        (4035, 'mlp-regressor-model', 1, 'TRANSFORMATION', 'fa-code-branch'),
        (4036, 'knn-classifier-model', 1, 'TRANSFORMATION', 'fa-braille'),
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
    columns = [c.name for c in tb.columns]
    data = [
        (4021, 'en', 'Logistic regression Classifier',
         'Performs logistic regression.'),
        (4021, 'pt', 'Classificador Regressão Logistica',
         'Classificador por Regressão Logistica.'),
        (4022, 'en', 'Random forest classifier', 'Random forest classifier.'),
        (4022, 'pt', 'Classificador random forest',
         'Classificador random forest.'),
        (4023, 'en', 'GBT Classifier',
         'Gradient-Boosted Trees (GBTs) learning algorithm for classification. It supports binary labels, as well as both continuous and categorical features.'),
        (4023, 'pt', 'Classificador GBT',
         'Algoritmo de aprendizado para classificação Gradient-Boosted Trees (GBTs). Suporta rótulos binários e features contínuas e categóricas.'),
        (4024, 'en', 'Decision tree classifier',
         'Decision tree learning algorithm for classification. It supports both binary and multiclass labels, as well as both continuous and categorical features.'),
        (4024, 'pt', 'Classif. Árv. Decisão',
         'Classificador baseado em árvores de decisão. Suporta tanto rótulos binários quanto multiclasses e features contínuas e categóricas.'),
        (4025, 'en', 'Perceptron Classifier',
         'Classifier trainer based on the Multilayer Perceptron.'),
        (4025, 'pt', 'Classificador Perceptron',
         'Classificador baseado no Perceptron de Multicamadas.'),
        (4026, 'en', 'Gradient Boosting Regressor',
         'Gradient Boosting for regression'),
        (4026, 'pt', 'Regressor Gradient Boosting',
         'Regressão por Gradient Boosting'),
        (4027, 'en', 'Linear Regression',
         'Linear regression with combined L1 and L2 priors as regularizer (ElasticNet).'),
        (4027, 'pt', 'Regressão Linear',
         'Regressão linear com combinações de regularizadores L1 e L2 (ElasticNet).'),
        (4028, 'en', 'Random Forest Regressor', 'A random forest regressor.'),
        (4028, 'pt', 'Regressão por Random Forest',
         'Um regressor por random forest.'),
        (4029, 'en', 'SGD Regressor',
         'Linear model fitted by minimizing a regularized empirical loss with Stochastic Gradient Descent.'),
        (4029, 'pt', 'Regressor SGD',
         'Modelo linear ajustado por minimização com o gradiente descendente estocástico.'),
        (4030, 'en', 'Huber Regressor',
         'Linear regression model that is robust to outliers.'),
        (4030, 'pt', 'Regressor Hube ',
         'Modelo de regressão linear que é robusto para outliers.'),
        (4031, 'en', 'SVM Classification', 'Uses a SVM Classifier.'),
        (4031, 'pt', 'Classificador SVM', 'Usa um classificador SVM.'),
        (
        4032, 'en', 'Naive-Bayes Classifier', 'Uses a Naive-Bayes Classifier.'),
        (4032, 'pt', 'Classificador Naive-Bayes',
         'Usa um classificador Naive-Bayes.'),
        (4033, 'en', 'K-Means Clustering',
         'Uses K-Means algorithm for clustering.'),
        (4033, 'pt', 'Agrupamento K-Means',
         'Usa o algoritmo K-Means para agrupamento.'),
        (4034, 'en', 'Multi-layer Perceptron classifier',
         'Multi-layer Perceptron classifier.'),
        (4034, 'pt', 'Classificador Perceptron multicamadas',
         'Classificador Perceptron multicamadas.'),
        (4035, 'en', 'Multi-layer Perceptron Regressor',
         'Multi-layer Perceptron Regressor.'),
        (4035, 'pt', 'Regressor Perceptron multicamadas',
         'Regressor Perceptron multicamadas.'),
        (4036, 'en', 'KNN Classification', 'Uses a KNN Classifier'),
        (4036, 'pt', 'Classificador KNN', 'Usa um classificador KNN'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        (i, SKLEARN_PLATFORM) for i in range(4021, 4037)
        ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

    data = [
        (2, SKLEARN_PLATFORM),
        (112, SKLEARN_PLATFORM),
        (119, SKLEARN_PLATFORM),
        (120, SKLEARN_PLATFORM),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (4030, "INPUT", None, 1, "ONE", 4021, "train input data"),
        (4031, "OUTPUT", None, 2, "MANY", 4021, "model"),
        (4032, "OUTPUT", None, 1, "MANY", 4021, "output data"),
        (4033, "INPUT", None, 1, "ONE", 4022, "train input data"),
        (4034, "OUTPUT", None, 2, "MANY", 4022, "model"),
        (4035, "OUTPUT", None, 1, "MANY", 4022, "output data"),
        (4036, "INPUT", None, 1, "ONE", 4023, "train input data"),
        (4037, "OUTPUT", None, 2, "MANY", 4023, "model"),
        (4038, "OUTPUT", None, 1, "MANY", 4023, "output data"),
        (4039, "INPUT", None, 1, "ONE", 4024, "train input data"),
        (4040, "OUTPUT", None, 2, "MANY", 4024, "model"),
        (4041, "OUTPUT", None, 1, "MANY", 4024, "output data"),
        (4042, "INPUT", None, 1, "ONE", 4025, "train input data"),
        (4043, "OUTPUT", None, 2, "MANY", 4025, "model"),
        (4044, "OUTPUT", None, 1, "MANY", 4025, "output data"),
        (4045, "INPUT", None, 1, "ONE", 4026, "train input data"),
        (4046, "OUTPUT", None, 2, "MANY", 4026, "model"),
        (4047, "OUTPUT", None, 1, "MANY", 4026, "output data"),
        (4048, "INPUT", None, 1, "ONE", 4027, "train input data"),
        (4049, "OUTPUT", None, 2, "MANY", 4027, "model"),
        (4050, "OUTPUT", None, 1, "MANY", 4027, "output data"),
        (4051, "INPUT", None, 1, "ONE", 4028, "train input data"),
        (4052, "OUTPUT", None, 2, "MANY", 4028, "model"),
        (4053, "OUTPUT", None, 1, "MANY", 4028, "output data"),
        (4054, "INPUT", None, 1, "ONE", 4029, "train input data"),
        (4055, "OUTPUT", None, 2, "MANY", 4029, "model"),
        (4056, "OUTPUT", None, 1, "MANY", 4029, "output data"),
        (4057, "INPUT", None, 1, "ONE", 4030, "train input data"),
        (4058, "OUTPUT", None, 2, "MANY", 4030, "model"),
        (4059, "OUTPUT", None, 1, "MANY", 4030, "output data"),
        (4060, "INPUT", None, 1, "ONE", 4031, "train input data"),
        (4061, "OUTPUT", None, 2, "MANY", 4031, "model"),
        (4062, "OUTPUT", None, 1, "MANY", 4031, "output data"),
        (4063, "INPUT", None, 1, "ONE", 4032, "train input data"),
        (4064, "OUTPUT", None, 2, "MANY", 4032, "model"),
        (4065, "OUTPUT", None, 1, "MANY", 4032, "output data"),
        (4066, "INPUT", None, 1, "ONE", 4033, "train input data"),
        (4067, "OUTPUT", None, 2, "MANY", 4033, "model"),
        (4068, "OUTPUT", None, 1, "MANY", 4033, "output data"),
        (4069, "INPUT", None, 1, "ONE", 4034, "train input data"),
        (4070, "OUTPUT", None, 2, "MANY", 4034, "model"),
        (4071, "OUTPUT", None, 1, "MANY", 4034, "output data"),
        (4072, "INPUT", None, 1, "ONE", 4035, "train input data"),
        (4073, "OUTPUT", None, 2, "MANY", 4035, "model"),
        (4074, "OUTPUT", None, 1, "MANY", 4035, "output data"),
        (4075, "INPUT", None, 1, "ONE", 4036, "train input data"),
        (4076, "OUTPUT", None, 2, "MANY", 4036, "model"),
        (4077, "OUTPUT", None, 1, "MANY", 4036, "output data"),
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

    columns = [c.name for c in tb.columns]
    data = [
        (4030, "en", "train input data", "Train input data"),
        (4031, "en", "model", "Output model"),
        (4032, "en", "output data", "Output data"),
        (4033, "en", "train input data", "Train input data"),
        (4034, "en", "model", "Output model"),
        (4035, "en", "output data", "Output data"),
        (4036, "en", "train input data", "Train input data"),
        (4037, "en", "model", "Output model"),
        (4038, "en", "output data", "Output data"),
        (4039, "en", "train input data", "Train input data"),
        (4040, "en", "model", "Output model"),
        (4041, "en", "output data", "Output data"),
        (4042, "en", "train input data", "Train input data"),
        (4043, "en", "model", "Output model"),
        (4044, "en", "output data", "Output data"),
        (4045, "en", "train input data", "Train input data"),
        (4046, "en", "model", "Output model"),
        (4047, "en", "output data", "Output data"),
        (4048, "en", "train input data", "Train input data"),
        (4049, "en", "model", "Output model"),
        (4050, "en", "output data", "Output data"),
        (4051, "en", "train input data", "Train input data"),
        (4052, "en", "model", "Output model"),
        (4053, "en", "output data", "Output data"),
        (4054, "en", "train input data", "Train input data"),
        (4055, "en", "model", "Output model"),
        (4056, "en", "output data", "Output data"),
        (4057, "en", "train input data", "Train input data"),
        (4058, "en", "model", "Output model"),
        (4059, "en", "output data", "Output data"),
        (4060, "en", "train input data", "Train input data"),
        (4061, "en", "model", "Output model"),
        (4062, "en", "output data", "Output data"),
        (4063, "en", "train input data", "Train input data"),
        (4064, "en", "model", "Output model"),
        (4065, "en", "output data", "Output data"),
        (4066, "en", "train input data", "Train input data"),
        (4067, "en", "model", "Output model"),
        (4068, "en", "output data", "Output data"),
        (4069, "en", "train input data", "Train input data"),
        (4070, "en", "model", "Output model"),
        (4071, "en", "output data", "Output data"),
        (4072, "en", "train input data", "Train input data"),
        (4073, "en", "model", "Output model"),
        (4074, "en", "output data", "Output data"),
        (4075, "en", "train input data", "Train input data"),
        (4076, "en", "model", "Output model"),
        (4077, "en", "output data", "Output data"),

        (4030, "pt", "entrada do treino", "Train input data"),
        (4031, "pt", "modelo", "Output model"),
        (4032, "pt", "dados de saída", "Dados de saída"),
        (4033, "pt", "entrada do treino", "Train input data"),
        (4034, "pt", "modelo", "Output model"),
        (4035, "pt", "dados de saída", "Dados de saída"),
        (4036, "pt", "entrada do treino", "Train input data"),
        (4037, "pt", "modelo", "Output model"),
        (4038, "pt", "dados de saída", "Dados de saída"),
        (4039, "pt", "entrada do treino", "Train input data"),
        (4040, "pt", "modelo", "Output model"),
        (4041, "pt", "dados de saída", "Dados de saída"),
        (4042, "pt", "entrada do treino", "Train input data"),
        (4043, "pt", "modelo", "Output model"),
        (4044, "pt", "dados de saída", "Dados de saída"),
        (4045, "pt", "entrada do treino", "Train input data"),
        (4046, "pt", "modelo", "Output model"),
        (4047, "pt", "dados de saída", "Dados de saída"),
        (4048, "pt", "entrada do treino", "Train input data"),
        (4049, "pt", "modelo", "Output model"),
        (4050, "pt", "dados de saída", "Dados de saída"),
        (4051, "pt", "entrada do treino", "Train input data"),
        (4052, "pt", "modelo", "Output model"),
        (4053, "pt", "dados de saída", "Dados de saída"),
        (4054, "pt", "entrada do treino", "Train input data"),
        (4055, "pt", "modelo", "Output model"),
        (4056, "pt", "dados de saída", "Dados de saída"),
        (4057, "pt", "entrada do treino", "Train input data"),
        (4058, "pt", "modelo", "Output model"),
        (4059, "pt", "dados de saída", "Dados de saída"),
        (4060, "pt", "entrada do treino", "Train input data"),
        (4061, "pt", "modelo", "Output model"),
        (4062, "pt", "dados de saída", "Dados de saída"),
        (4063, "pt", "entrada do treino", "Train input data"),
        (4064, "pt", "modelo", "Output model"),
        (4065, "pt", "dados de saída", "Dados de saída"),
        (4066, "pt", "entrada do treino", "Train input data"),
        (4067, "pt", "modelo", "Output model"),
        (4068, "pt", "dados de saída", "Dados de saída"),
        (4069, "pt", "entrada do treino", "Train input data"),
        (4070, "pt", "modelo", "Output model"),
        (4071, "pt", "dados de saída", "Dados de saída"),
        (4072, "pt", "entrada do treino", "Train input data"),
        (4073, "pt", "modelo", "Output model"),
        (4074, "pt", "dados de saída", "Dados de saída"),
        (4075, "pt", "entrada do treino", "Train input data"),
        (4076, "pt", "modelo", "Output model"),
        (4077, "pt", "dados de saída", "Dados de saída"),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    models_ports = set(range(4031, 4077, 3))
    data_ports = set(range(4030, 4078, 1)) - models_ports
    data = sorted(list(itertools.product(data_ports, [1])) + list(
        itertools.product(models_ports, [2])), key=lambda x: x[0])

    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]

    # Classification
    data = itertools.product([int(x) for x in OPERATIONS_CLASSIFIER.split(',')],
                             [4001, 4, 18, 8])

    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)

    # Regression
    data = itertools.product([int(x) for x in OPERATIONS_REGRESSOR.split(',')],
                             [4001, 21, 8])
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)

    # Clustering
    data = itertools.product([int(x) for x in OPERATIONS_CLUSTERING.split(',')],
                             [4001, 19, 8])

    rows = [dict(list(zip(columns, cat))) for cat in data]
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
        (4021, 1, 1, 'execution'),
        (4022, 1, 1, 'execution'),
        (4023, 1, 1, 'execution'),

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
        (4021, 'en', 'Execution'),
        (4021, 'pt', 'Execução'),
        (4022, 'en', 'Execution'),
        (4022, 'pt', 'Execução'),
        (4023, 'en', 'Execution'),
        (4023, 'pt', 'Execução'),
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

        # Classifier
        [4021, 39],
        [4021, 40],
        [4021, 41],
        [4021, 110],
        [4021, 4021],
        [4021, 4001],

        [4022, 39],
        [4022, 40],
        [4022, 41],
        [4022, 110],
        [4022, 4021],
        [4022, 4002],

        [4023, 39],
        [4023, 40],
        [4023, 41],
        [4023, 110],
        [4023, 4021],
        [4023, 4003],

        [4024, 39],
        [4024, 40],
        [4024, 41],
        [4024, 110],
        [4024, 4021],
        [4024, 4004],

        [4025, 39],
        [4025, 40],
        [4025, 41],
        [4025, 110],
        [4025, 4021],
        [4025, 4005],

        [4031, 39],
        [4031, 40],
        [4031, 41],
        [4031, 110],
        [4031, 4021],
        [4031, 4011],

        [4032, 39],
        [4032, 40],
        [4032, 41],
        [4032, 110],
        [4032, 4021],
        [4032, 4012],

        [4034, 39],
        [4034, 40],
        [4034, 41],
        [4034, 110],
        [4034, 4021],
        [4034, 4019],

        [4036, 39],
        [4036, 40],
        [4036, 41],
        [4036, 110],
        [4036, 3005],
        [4036, 4021],

        # Regressor
        [4026, 41],
        [4026, 110],
        [4026, 4022],
        [4026, 4006],

        [4027, 41],
        [4027, 110],
        [4027, 4022],
        [4027, 4007],

        [4028, 41],
        [4028, 110],
        [4028, 4022],
        [4028, 4008],

        [4029, 41],
        [4029, 110],
        [4029, 4022],
        [4029, 4009],

        [4030, 41],
        [4030, 110],
        [4030, 4022],
        [4030, 4010],

        [4035, 41],
        [4035, 110],
        [4035, 4022],
        [4035, 4020],

        # Clustering
        [4033, 41],
        [4033, 110],
        [4033, 4023],
        [4033, 4013],

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
        column('default', String),
        column('suggested_widget', String),
        column('values_url', String),
        column('values', String),
        column('scope', String),
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')
    data = [

        (4105, 'features', 'TEXT', '1', '1', None, 'attribute-selector', None,
         None, 'EXECUTION', 4021, None),
        (4106, 'label', 'TEXT', '1', '2', None, 'attribute-selector', None,
         '{"multiple": false}', 'EXECUTION', 4021, None),
        (4107, 'prediction', 'TEXT', '0', '3', None, 'text', None, None,
         'EXECUTION', 4021, None),
        (4108, 'features', 'TEXT', '1', '1', None, 'attribute-selector', None,
         None, 'EXECUTION', 4022, None),
        (4109, 'label', 'TEXT', '1', '2', None, 'attribute-selector', None,
         '{"multiple": false}', 'EXECUTION', 4022, None),
        (4110, 'prediction', 'TEXT', '0', '3', None, 'text', None, None,
         'EXECUTION', 4022, None),
        (4111, 'features', 'TEXT', '1', '1', None, 'attribute-selector', None,
         None, 'EXECUTION', 4023, None),
        (4112, 'prediction', 'TEXT', '0', '2', None,
         'text', None, None, 'EXECUTION', 4023, None),
        (477, 'topic_indices', 'TEXT', 1, 2, None, 'attribute-selector', None,
         None, 'EXECUTION', 2, None),
        (478, 'topic_terms', 'TEXT', 1, 3, None, 'attribute-selector', None,
         None, 'EXECUTION', 2, None),

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
        (4105, 'en', 'Features attribute', 'Features attribute'),
        (4105, 'pt', 'Atributo com features', 'Atributo com features'),
        (4106, 'en', 'Label attribute', 'Label attribute'),
        (4106, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo'),
        (
        4107, 'en', 'Prediction attribute (new)', 'Prediction attribute (new)'),
        (4107, 'pt', 'Atributo usado para predição (novo)',
         'Atributo usado para predição (novo)'),

        (4108, 'en', 'Features attribute', 'Features attribute'),
        (4108, 'pt', 'Atributo com features', 'Atributo com features'),
        (4109, 'en', 'Label attribute', 'Label attribute'),
        (4109, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo'),
        (
        4110, 'en', 'Prediction attribute (new)', 'Prediction attribute (new)'),
        (4110, 'pt', 'Atributo usado para predição (novo)',
         'Atributo usado para predição (novo)'),

        (4111, 'en', 'Features attribute', 'Features attribute'),
        (4111, 'pt', 'Atributo com features', 'Atributo com features'),
        (
        4112, 'en', 'Prediction attribute (new)', 'Prediction attribute (new)'),
        (4112, 'pt', 'Atributo usado para predição (novo)',
         'Atributo usado para predição (novo)'),

        (477, 'en', 'Topic Indices field', 'Topic Indices field'),
        (477, 'pt', 'Atributo do Indices de tópicos',
         'Atributo do Indices de tópicos'),
        (478, 'en', 'Topic Terms alias', 'Topic Terms alias'),
        (478, 'pt', 'Coluna para o termos do tópico',
         'Coluna para o termos do tópico'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({})'.format(ALL_OPERATIONS)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({})'.format(
         ALL_OPERATIONS)),

    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = {} AND operation_id IN ({})'.format(SKLEARN_PLATFORM,
                                                              ALL_OPERATIONS)),

    ('DELETE FROM operation_platform '
     'WHERE platform_id = 4 AND operation_id IN (74,3005,3015,3016,3018, 56, 48, 10)',

     'DELETE FROM operation_platform '
     'WHERE platform_id = 4 AND operation_id IN (112, 119, 120, 2);'
     'INSERT INTO operation_platform (`operation_id`,`platform_id`) '
     'VALUES (74, 4), (3005, 4), (3015,4), (3016,4), (3018, 4), (56, 4), (48, 4), (10, 4);'
     ),

    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({})'.format(ALL_OPERATIONS)),

    (_insert_operation_port,
     "DELETE FROM operation_port WHERE operation_id in ({})".format(
         ALL_OPERATIONS)),

    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in "
     "(SELECT id FROM operation_port WHERE operation_id IN ({}))".format(
         ALL_OPERATIONS)),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in ("
     "SELECT id FROM operation_port WHERE operation_id IN ({}))".format(
         ALL_OPERATIONS)),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 4021 AND 4023'),

    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({})'.format(ALL_OPERATIONS)),

    (_insert_operation_form_translation,
     "DELETE FROM operation_form_translation WHERE id BETWEEN 4021 AND 4023"),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4105 AND 4112;'
     'DELETE FROM operation_form_field WHERE id BETWEEN 477 AND 478;'),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4105 AND 4112;'
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 477 AND 478;'),

    # DROP AND JOIN
    ("""
        DELETE FROM operation_category_operation WHERE operation_id IN (3014, 3030);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`) 
     VALUES (3014, 7),(3014, 31),(3014, 3001),(3030, 7),(3030, 31),(3030, 3001);
     """,
     """ 
        DELETE FROM operation_category_operation WHERE operation_id IN (3014, 3030);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`) 
     VALUES (3014, 7),(3014, 3001),(3030, 7),(3030, 3001);
     """),
    # STBSCAN AND READSHAPEFILE
    ("""
        DELETE FROM operation_category_operation WHERE operation_id IN (3021, 3031);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`)
     VALUES (3021, 41), (3021, 42),(3021,  3001),(3031, 41), (3031, 42),(3031, 3001);
     """,
     """
        DELETE FROM operation_category_operation WHERE operation_id IN (3021, 3031);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`)
     VALUES (3021, 17), (3021,  3001), (3031, 17), (3031, 3001);
     
     """),
    # execute sql query
    ("""
     UPDATE operation_category_operation SET `operation_category_id` = 41
     WHERE `operation_id` = 4018 AND `operation_category_id` = 7; 
     """,
     """
     UPDATE operation_category_operation SET `operation_category_id` = 7
     WHERE `operation_id` = 4018 AND `operation_category_id` = 41; 
     """
     ),
    # Convert words to vector
    ("""
        DELETE FROM operation_category_operation WHERE operation_id IN (4016);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`) 
     VALUES (4016, 32), (4016, 37), (4016, 4001);
     """,
     """ 
        DELETE FROM operation_category_operation WHERE operation_id IN (4016);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`) 
     VALUES (4016, 16), (4016, 4001);
     
     """),
    # quantile discreter
    ("""
        DELETE FROM operation_category_operation WHERE operation_id IN (4014);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`) 
     VALUES (4014, 32), (4014, 35), (4014, 4001);
     """,
     """
       DELETE FROM operation_category_operation WHERE operation_id IN (4014);
       INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`)
    VALUES (4014, 8), (4014, 23),(4014, 4001);
    """),
    # load-model and save-model
    ("""
        DELETE FROM operation_category_operation WHERE operation_id IN (3026, 3027);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`) 
     VALUES (3026, 6), (3026, 3001), (3027, 6), (3027, 3001);
     """,
     """
       DELETE FROM operation_category_operation WHERE operation_id IN (3026, 3027);
       INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`)
    VALUES (3026, 8), (3026, 26), (3026, 3001), (3027, 8), (3027, 26),(3027, 3001);
    """),
    # evaluate model
    ("""
        DELETE FROM operation_category_operation WHERE operation_id IN (4017);
        INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`) 
     VALUES (4017, 40), (4017, 4001);
     """,
     """
       DELETE FROM operation_category_operation WHERE operation_id IN (4017);
       INSERT INTO operation_category_operation (`operation_id`, `operation_category_id`)
    VALUES (4017, 8), (4017, 26), (4017, 4001);
    """),

    # disabling ml
    ("""
        UPDATE operation SET `enabled` = 0
        WHERE id in (4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4019,4020);

     """,
     """
        UPDATE operation SET `enabled` = 1
        WHERE id in (4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4019,4020);

     """),
    ("""
        UPDATE operation_form_field SET `values` = 
        '[{"key": \"auto\", \"value\": \"auto\"}, {\"key\": \"sqrt\", \"value\": \"sqrt\"}, 
          {\"key\": \"log2\", \"value\": \"log2\"}]' WHERE id = 4040;
        UPDATE operation_form_field SET `default` = 'auto' WHERE id = 4040;
     """,
     "SELECT 1"),
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