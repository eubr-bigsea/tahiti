# coding=utf-8
"""refactoring_ml_models

Revision ID: fef08022f308
Revises: 1d36e073f89d
Create Date: 2018-12-07 10:51:47.471104

"""
import itertools

from alembic import context
from alembic import op
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'fef08022f308'
down_revision = 'b76fe74daeb6'
branch_labels = None
depends_on = None

OPERATIONS = ",".join(["104", "105", "106", "107", "108", "109", "110", "111",
                       "112", "113", "114", "115", "116", "117", "118", "119",
                       "120"])


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (104, "naive-bayes-classifier-model", "1", "TRANSFORMATION", "fa-tag"),
        (105, "svm-classification-model", "1", "TRANSFORMATION", "fa-tag"),
        (106, "logistic-regression-classifier-model", "1", "TRANSFORMATION",
         "fa-exchange-alt"),
        (107, "random-forest-classifier-model", "1", "TRANSFORMATION",
         "fa-random"),
        (108, "gbt-classifier-model", "1", "TRANSFORMATION", "fa-tree"),
        (109, "decision-tree-classifier-model", "1", "TRANSFORMATION",
         "fa-arrow-right"),
        (110, "perceptron-classifier-model", "1", "TRANSFORMATION",
         "fa-angle-double-down"),
        (111, "one-vs-rest-classifier-model", "1", "TRANSFORMATION",
         "fa-window-close"),

        # Regression
        (112, "isotonic-regression-model", 1, "TRANSFORMATION",
         "fa-battery-quarter"),
        (113, "aft-survival-regression-model", 1, "TRANSFORMATION", "fa-fire"),
        (114, "gbt-regressor-model", 1, "TRANSFORMATION", "fa-id-card"),
        (115, "random-forest-regressor-model", 1, "TRANSFORMATION",
         "fa-laptop"),
        (116, "generalized-linear-regressor-model", 1, "TRANSFORMATION",
         "fa-plus-square"),
        (117, "linear-regression-model", 1, "TRANSFORMATION", "fa-chart-line"),

        # Clustering
        (118, "k-means-clustering-model", 1, "TRANSFORMATION", "fa-lemon"),
        (119, "lda-clustering-model", 1, "TRANSFORMATION", "fa-file-alt"),
        (120, "gaussian-mixture-clustering-model", 1, "TRANSFORMATION",
         "fa-bullseye"),
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
        (104, "en", "Naive Bayes classifier",
         "Naive Bayes Classifiers. It supports both Multinomial and Bernoulli NB. Multinomial NB can handle finitely supported discrete data. For example\, by converting documents into TF-IDF vectors\, it can be "),
        (105, "en", "SVM Classification", "Uses a SVM Classifier"),
        (106, "en", "Logistic regression", "Performs logistic regression"),
        (107, "en", "Random forest classifier", "Random forest classifier"),
        (108, "en", "GBT Classifier",
         "Gradient-Boosted Trees (GBTs) learning algorithm for classification. It supports binary labels\, as well as both continuous and categorical features. "),
        (109, "en", "Decision tree classifier",
         "Decision tree learning algorithm for classification. It supports both binary and multiclass labels\, as well as both continuous and categorical features."),
        (110, "en", "Perceptron Classifier",
         "Classifier trainer based on the Multilayer Perceptron. Each layer has sigmoid activation function\, output layer has softmax. Number of inputs has to be equal to the size of feature vectors. Number of "),
        (111, "en", "One vs. rest classifier",
         "Reduction of multiclass classification to binary classification."),

        (104, "pt", "Classificador Naive Bayes", "Usa um classificador"),
        (105, "pt", "Classificador SVM", "Usa um classificador SVM"),
        (106, "pt", "Regressão logística", "Realiza regressão logística"),
        (107, "pt", "Classificador random forest",
         "Classificador random forest"),
        (108, "pt", "Classificador GBT",
         "Algoritmo de aprendizado para classificação Gradient-Boosted Trees (GBTs). Suporta rótulos binários e features contínuas e categóricas."),
        (109, "pt", "Classif. Árv. Decisão",
         "Classificador baseado em árvores de decisão. Suporta tanto rótulos binários quanto multiclasses e features contínuas e categóricas."),
        (110, "pt", "Classificador Perceptron",
         "Classifier trainer based on the Multilayer Perceptron. Each layer has sigmoid activation function\, output layer has softmax. Number of inputs has to be equal to the size of feature vectors. Number of "),
        (111, "pt", "Classificador 1 vs. resto",
         "Redução da classificação multiclasse para a classificação binária."),

        # Regression
        (112, "en", "Isotonic Regression", "Isotonic Regression"),
        (113, "en", "AFT Survival Regression",
         "Accelerated Failure Time (AFT) Model Survival Regression"),
        (114, "en", "GBT Regressor",
         "Gradient-Boosted Trees (GBTs) learning algorithm for regression. It supports both continuous and categorical featur"),
        (115, "en", "Random Forest Regressor",
         "Random Forest learning algorithm for regression. It supports both continuous and categorical features."),
        (116, "en", "Generalized Linear Regressor",
         "Generalized Linear Regressor"),
        (117, "en", "Linear regression",
         "Applies a linear regression algorithm"),

        (112, "pt", "Regressão Isotônica", "Regressão Isotônica"),
        (113, "pt", "Regressão AFT Survival",
         "Accelerated Failure Time (AFT) Model Survival Regression"),
        (114, "pt", "Regressor GBT",
         "Gradient-Boosted Trees (GBTs) learning algorithm for regression. It supports both continuous and categorical feature"),
        (115, "pt", "Regressor Random Forest",
         "Random Forest learning algorithm for regression. It supports both continuous and categorical features."),
        (116, "pt", "Regressor Linear Generalizado",
         "Regressor Linear Generalizado"),
        (117, "pt", "Regressão linear", "Aplica a regressão linear"),

        # Clustering
        (118, "en", "K-Means Clustering",
         "Uses K-Means algorithm for clustering"),
        (119, "en", "LDA Clustering", "LDA Clustering"),
        (120, "en", "Gaussian Mix. Clustering", "Gaussian Mix. Clustering"),

        (118, "pt", "Agrupamento K-Means",
         "Usa o algoritmo K-Means para agrupamento"),
        (119, "pt", "Agrupamento LDA", "Agrupamento LDA"),
        (120, "pt", "Agrupamento Gaussian Mix.", "Agrupamento Gaussian Mix."),

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
        (104, 1),
        (105, 1),
        (106, 1),
        (107, 1),
        (108, 1),
        (109, 1),
        (110, 1),
        (111, 1),

        (112, 1),
        (113, 1),
        (114, 1),
        (115, 1),
        (116, 1),
        (117, 1),

        (118, 1),
        (119, 1),
        (120, 1),
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
        (239, "INPUT", None, 1, "ONE", 104, "train input data"),
        (240, "OUTPUT", None, 2, "MANY", 104, "model"),
        (241, "OUTPUT", None, 1, "MANY", 104, "output data"),
        (242, "INPUT", None, 1, "ONE", 105, "train input data"),
        (243, "OUTPUT", None, 2, "MANY", 105, "model"),
        (244, "OUTPUT", None, 1, "MANY", 105, "output data"),
        (245, "INPUT", None, 1, "ONE", 106, "train input data"),
        (246, "OUTPUT", None, 2, "MANY", 106, "model"),
        (247, "OUTPUT", None, 1, "MANY", 106, "output data"),
        (248, "INPUT", None, 1, "ONE", 107, "train input data"),
        (249, "OUTPUT", None, 2, "MANY", 107, "model"),
        (250, "OUTPUT", None, 1, "MANY", 107, "output data"),
        (251, "INPUT", None, 1, "ONE", 108, "train input data"),
        (252, "OUTPUT", None, 2, "MANY", 108, "model"),
        (253, "OUTPUT", None, 1, "MANY", 108, "output data"),
        (254, "INPUT", None, 1, "ONE", 109, "train input data"),
        (255, "OUTPUT", None, 2, "MANY", 109, "model"),
        (256, "OUTPUT", None, 1, "MANY", 109, "output data"),
        (257, "INPUT", None, 1, "ONE", 110, "train input data"),
        (258, "OUTPUT", None, 2, "MANY", 110, "model"),
        (259, "OUTPUT", None, 1, "MANY", 110, "output data"),
        (260, "INPUT", None, 1, "ONE", 111, "train input data"),
        (261, "OUTPUT", None, 2, "MANY", 111, "model"),
        (262, "OUTPUT", None, 1, "MANY", 111, "output data"),

        (263, "INPUT", None, 1, "ONE", 112, "train input data"),
        (264, "OUTPUT", None, 2, "MANY", 112, "model"),
        (265, "OUTPUT", None, 1, "MANY", 112, "output data"),
        (266, "INPUT", None, 1, "ONE", 113, "train input data"),
        (267, "OUTPUT", None, 2, "MANY", 113, "model"),
        (268, "OUTPUT", None, 1, "MANY", 113, "output data"),
        (269, "INPUT", None, 1, "ONE", 114, "train input data"),
        (270, "OUTPUT", None, 2, "MANY", 114, "model"),
        (271, "OUTPUT", None, 1, "MANY", 114, "output data"),
        (272, "INPUT", None, 1, "ONE", 115, "train input data"),
        (273, "OUTPUT", None, 2, "MANY", 115, "model"),
        (274, "OUTPUT", None, 1, "MANY", 115, "output data"),
        (275, "INPUT", None, 1, "ONE", 116, "train input data"),
        (276, "OUTPUT", None, 2, "MANY", 116, "model"),
        (277, "OUTPUT", None, 1, "MANY", 116, "output data"),
        (278, "INPUT", None, 1, "ONE", 117, "train input data"),
        (279, "OUTPUT", None, 2, "MANY", 117, "model"),
        (280, "OUTPUT", None, 1, "MANY", 117, "output data"),

        (281, "INPUT", None, 1, "ONE", 118, "train input data"),
        (282, "OUTPUT", None, 2, "MANY", 118, "model"),
        (283, "OUTPUT", None, 1, "MANY", 118, "output data"),
        (284, "INPUT", None, 1, "ONE", 119, "train input data"),
        (285, "OUTPUT", None, 2, "MANY", 119, "model"),
        (286, "OUTPUT", None, 1, "MANY", 119, "output data"),
        (287, "INPUT", None, 1, "ONE", 120, "train input data"),
        (288, "OUTPUT", None, 2, "MANY", 120, "model"),
        (289, "OUTPUT", None, 1, "MANY", 120, "output data"),

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
        (239, "en", "train input data", "Train input data"),
        (240, "en", "model", "Output model"),
        (241, "en", "output data", "Output data"),
        (242, "en", "train input data", "Train input data"),
        (243, "en", "model", "Output model"),
        (244, "en", "output data", "Output data"),
        (245, "en", "train input data", "Train input data"),
        (246, "en", "model", "Output model"),
        (247, "en", "output data", "Output data"),
        (248, "en", "train input data", "Train input data"),
        (249, "en", "model", "Output model"),
        (250, "en", "output data", "Output data"),
        (251, "en", "train input data", "Train input data"),
        (252, "en", "model", "Output model"),
        (253, "en", "output data", "Output data"),
        (254, "en", "train input data", "Train input data"),
        (255, "en", "model", "Output model"),
        (256, "en", "output data", "Output data"),
        (257, "en", "train input data", "Train input data"),
        (258, "en", "model", "Output model"),
        (259, "en", "output data", "Output data"),
        (260, "en", "train input data", "Train input data"),
        (261, "en", "model", "Output model"),
        (262, "en", "output data", "Output data"),

        (239, "pt", "entrada do treino", "Train input data"),
        (240, "pt", "modelo", "Output model"),
        (241, "pt", "dados de saída", "Dados de saída"),
        (242, "pt", "entrada do treino", "Train input data"),
        (243, "pt", "modelo", "Output model"),
        (244, "pt", "dados de saída", "Dados de saída"),
        (245, "pt", "entrada do treino", "Train input data"),
        (246, "pt", "modelo", "Output model"),
        (247, "pt", "dados de saída", "Dados de saída"),
        (248, "pt", "entrada do treino", "Train input data"),
        (249, "pt", "modelo", "Output model"),
        (250, "pt", "dados de saída", "Dados de saída"),
        (251, "pt", "entrada do treino", "Train input data"),
        (252, "pt", "modelo", "Output model"),
        (253, "pt", "dados de saída", "Dados de saída"),
        (254, "pt", "entrada do treino", "Train input data"),
        (255, "pt", "modelo", "Output model"),
        (256, "pt", "dados de saída", "Dados de saída"),
        (257, "pt", "entrada do treino", "Train input data"),
        (258, "pt", "modelo", "Output model"),
        (259, "pt", "dados de saída", "Dados de saída"),
        (260, "pt", "entrada do treino", "Train input data"),
        (261, "pt", "modelo", "Output model"),
        (262, "pt", "dados de saída", "Dados de saída"),

        (263, "en", "train input data", "Train input data"),
        (264, "en", "model", "Output model"),
        (265, "en", "output data", "Output data"),
        (266, "en", "train input data", "Train input data"),
        (267, "en", "model", "Output model"),
        (268, "en", "output data", "Output data"),
        (269, "en", "train input data", "Train input data"),
        (270, "en", "model", "Output model"),
        (271, "en", "output data", "Output data"),
        (272, "en", "train input data", "Train input data"),
        (273, "en", "model", "Output model"),
        (274, "en", "output data", "Output data"),
        (275, "en", "train input data", "Train input data"),
        (276, "en", "model", "Output model"),
        (277, "en", "output data", "Output data"),
        (278, "en", "train input data", "Train input data"),
        (279, "en", "model", "Output model"),
        (280, "en", "output data", "Output data"),

        (263, "pt", "entrada do treino", "Train input data"),
        (264, "pt", "modelo", "Output model"),
        (265, "pt", "dados de saída", "Dados de saída"),
        (266, "pt", "entrada do treino", "Train input data"),
        (267, "pt", "modelo", "Output model"),
        (268, "pt", "dados de saída", "Dados de saída"),
        (269, "pt", "entrada do treino", "Train input data"),
        (270, "pt", "modelo", "Output model"),
        (271, "pt", "dados de saída", "Dados de saída"),
        (272, "pt", "entrada do treino", "Train input data"),
        (273, "pt", "modelo", "Output model"),
        (274, "pt", "dados de saída", "Dados de saída"),
        (275, "pt", "entrada do treino", "Train input data"),
        (276, "pt", "modelo", "Output model"),
        (277, "pt", "dados de saída", "Dados de saída"),
        (278, "pt", "entrada do treino", "Train input data"),
        (279, "pt", "modelo", "Output model"),
        (280, "pt", "dados de saída", "Dados de saída"),

        (281, "en", "train input data", "Train input data"),
        (282, "en", "model", "Output model"),
        (283, "en", "output data", "Output data"),
        (284, "en", "train input data", "Train input data"),
        (285, "en", "model", "Output model"),
        (286, "en", "output data", "Output data"),
        (287, "en", "train input data", "Train input data"),
        (288, "en", "model", "Output model"),
        (289, "en", "output data", "Output data"),

        (281, "pt", "entrada do treino", "Train input data"),
        (282, "pt", "modelo", "Output model"),
        (283, "pt", "dados de saída", "Dados de saída"),
        (284, "pt", "entrada do treino", "Train input data"),
        (285, "pt", "modelo", "Output model"),
        (286, "pt", "dados de saída", "Dados de saída"),
        (287, "pt", "entrada do treino", "Train input data"),
        (288, "pt", "modelo", "Output model"),
        (289, "pt", "dados de saída", "Dados de saída"),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    models_ports = set(range(240, 289, 3))
    data_ports = set(range(239, 290, 1)) - models_ports
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
    data = itertools.product([int(x) for x in OPERATIONS.split(',')
                              if int(x) <= 111],
                             [1, 4, 18, 8])

    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)

    # Regression
    data = itertools.product([int(x) for x in OPERATIONS.split(',')
                              if 118 > int(x) > 111],
                             [1, 21, 8])
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)

    # Clustering
    data = itertools.product([int(x) for x in OPERATIONS.split(',')
                              if (121 > int(x) > 117) and (int(x) != 119)],
                             [1, 19, 8])

    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)

    data = [(119, 32), (119, 37),]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        [104, 1],
        [104, 39],
        [104, 40],
        [104, 41],
        [104, 110],
        [104, 64],
        [105, 1],
        [105, 9],
        [105, 39],
        [105, 40],
        [105, 41],
        [105, 110],
        [106, 1],
        [106, 34],
        [106, 39],
        [106, 40],
        [106, 41],
        [106, 110],
        [107, 1],
        [107, 41],
        [107, 39],
        [107, 110],
        [107, 40],
        [107, 65],
        [108, 1],
        [108, 41],
        [108, 39],
        [108, 110],
        [108, 40],
        [108, 67],
        [109, 1],
        [109, 41],
        [109, 39],
        [109, 110],
        [109, 40],
        [109, 66],
        [110, 1],
        [110, 41],
        [110, 39],
        [110, 110],
        [110, 40],
        [110, 68],
        [111, 1],
        [111, 119],
        [111, 110],
        [111, 41],

        [112, 102],
        [112, 103],
        [112, 41],
        [112, 110],
        [113, 102],
        [113, 104],
        [113, 41],
        [113, 110],
        [114, 102],
        [114, 105],
        [114, 41],
        [114, 110],
        [115, 106],
        [115, 41],
        [115, 110],
        [115, 102],
        [116, 107],
        [116, 41],
        [116, 110],
        [116, 102],

        [117, 8],
        [117, 41],
        [117, 110],
        [117, 102],

        [118, 27],
        [118, 10],
        [118, 41],
        [118, 110],
        [119, 41],
        [119, 10],
        [119, 110],
        [119, 58],
        [120, 41],
        [120, 10],
        [120, 110],
        [120, 71],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [

    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({})'.format(
         OPERATIONS)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({})'.format(
         OPERATIONS)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({})'.format(
         OPERATIONS)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({})'.format(OPERATIONS)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE operation_id in ({})".format(
         OPERATIONS)),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in "
     "(SELECT id FROM operation_port WHERE operation_id IN ({}))".format(
         OPERATIONS)),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in ("
     "SELECT id FROM operation_port WHERE operation_id IN ({}))".format(
         OPERATIONS)),

    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({})'.format(OPERATIONS)),

    ("""UPDATE operation_form SET category = 'execution'
        WHERE id IN (9,34,64,65,66,67,68,119)""",
     """UPDATE operation_form SET category = 'paramgrid'
        WHERE id IN (9,34,64,65,66,67,68,119)"""),

    ("""UPDATE operation_form_translation SET NAME = 'Execution'
        WHERE id IN (9,34,64,65,66,67,68,119) AND locale = 'en';""",
     """UPDATE operation_form_translation SET NAME = 'Param grid'
        WHERE id IN (9,34,64,65,66,67,68,119) AND locale = 'en';"""),

    ("""UPDATE operation_form_translation SET NAME = 'Execução'
        WHERE id IN (9,34,64,65,66,67,68,119) AND locale = 'pt';""",
     """UPDATE operation_form_translation SET NAME = 'Grade de parâmetros'
        WHERE id IN (9,34,64,65,66,67,68,119) AND locale = 'pt';"""),

    ("UPDATE operation_form SET `order` = 0 WHERE id IN (10, 1, 102)",
     "UPDATE operation_form SET `order` = 1 WHERE id IN (10, 1, 102)"),

    ('UPDATE operation_translation '
     'SET name = "Naïve Bayes" '
     'WHERE id = 104 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Naïve Bayes Classifier" '
     'WHERE id = 104 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Naïve Bayes" '
     'WHERE id = 104 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador Naive Bayes" '
     'WHERE id = 104 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Support Vector Machines (SVM)" '
     'WHERE id = 105 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "SVM Classification" '
     'WHERE id = 105 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Support Vector Machines (SVM)" '
     'WHERE id = 105 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador SVM" '
     'WHERE id = 105 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Logistic regression" '
     'WHERE id = 106 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Logistic regression" '
     'WHERE id = 106 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão logística" '
     'WHERE id = 106 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressão logística" '
     'WHERE id = 106 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Random forest" '
     'WHERE id = 107 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Random forest classifier" '
     'WHERE id = 107 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Random forest" '
     'WHERE id = 107 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador random forest" '
     'WHERE id = 107 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Gradient Boosted Tree" '
     'WHERE id = 108 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "GBT Classifier" '
     'WHERE id = 108 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gradient Boosted Tree" '
     'WHERE id = 108 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador GBT" '
     'WHERE id = 108 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Decision Tree" '
     'WHERE id = 109 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Decision tree classifier" '
     'WHERE id = 109 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Árvore de Decisão" '
     'WHERE id = 109 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classif. Árv. Decisão" '
     'WHERE id = 109 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Multi-layer Perceptron" '
     'WHERE id = 110 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Perceptron Classifier" '
     'WHERE id = 110 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Perceptron multicamadas" '
     'WHERE id = 110 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador Perceptron" '
     'WHERE id = 110 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "One vs. rest classifier" '
     'WHERE id = 111 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "One vs. rest classifier" '
     'WHERE id = 111 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Classificador 1 vs. resto" '
     'WHERE id = 111 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador 1 vs. resto" '
     'WHERE id = 111 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Isotonic Regression" '
     'WHERE id = 112 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Isotonic Regression" '
     'WHERE id = 112 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão Isotônica" '
     'WHERE id = 112 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressão Isotônica" '
     'WHERE id = 112 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "AFT Survival Regression" '
     'WHERE id = 113 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "AFT Survival Regression" '
     'WHERE id = 113 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão AFT Survival" '
     'WHERE id = 113 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressão AFT Survival" '
     'WHERE id = 113 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Gradient Boosted Tree Regressor" '
     'WHERE id = 114 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "GBT Regressor" '
     'WHERE id = 114 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gradient Boosted Tree Regressor" '
     'WHERE id = 114 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressor GBT" '
     'WHERE id = 114 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Random Forest Regressor" '
     'WHERE id = 115 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Random Forest Regressor" '
     'WHERE id = 115 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Random Forest Regressor" '
     'WHERE id = 115 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressor Random Forest" '
     'WHERE id = 115 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Generalized Linear Regression" '
     'WHERE id = 116 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Generalized Linear Regressor" '
     'WHERE id = 116 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão Linear generalizada" '
     'WHERE id = 116 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressor Linear Generalizado" '
     'WHERE id = 116 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Linear regression" '
     'WHERE id = 117 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Linear regression" '
     'WHERE id = 117 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão linear" '
     'WHERE id = 117 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressão linear" '
     'WHERE id = 117 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "K-Means" '
     'WHERE id = 118 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "K-Means Clustering" '
     'WHERE id = 118 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "K-Means" '
     'WHERE id = 118 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Agrupamento K-Means" '
     'WHERE id = 118 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Latent Dirichlet Allocation (LDA)" '
     'WHERE id = 119 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "LDA Clustering" '
     'WHERE id = 119 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Latent Dirichlet Allocation (LDA)" '
     'WHERE id = 119 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Agrupamento LDA" '
     'WHERE id = 119 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Gaussian Mixture" '
     'WHERE id = 120 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Gaussian Mix. Clustering" '
     'WHERE id = 120 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Mistura de Gaussianas" '
     'WHERE id = 120 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Agrupamento Gaussian Mix." '
     'WHERE id = 120 AND locale = "pt"'),
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
    connection.execute('SET foreign_key_checks = 0;')

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
    connection.execute('SET foreign_key_checks = 1;')
    session.commit()
