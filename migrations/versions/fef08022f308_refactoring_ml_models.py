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
down_revision = '1d36e073f89d'
branch_labels = None
depends_on = None

OPERATIONS = ",".join(["104", "105", "106", "107", "108", "109", "110", "111"])


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
    ]
    rows = [dict(zip(columns, row)) for row in data]
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
    ]
    rows = [dict(zip(columns, row)) for row in data]
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

    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    models_ports = set(range(240, 262, 3))
    data_ports = set(range(239, 263, 1)) - models_ports
    data = sorted(list(itertools.product(data_ports, [1])) + list(
        itertools.product(models_ports, [2])), key=lambda x: x[0])

    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = itertools.product([int(x) for x in OPERATIONS.split(',')],
                             [1, 4, 18, 8])
    rows = [dict(zip(columns, cat)) for cat in data]

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
        [104, 43],
        [104, 64],
        [105, 1],
        [105, 9],
        [105, 39],
        [105, 40],
        [105, 41],
        [105, 43],
        [106, 1],
        [106, 34],
        [106, 39],
        [106, 40],
        [106, 41],
        [106, 43],
        [107, 1],
        [107, 41],
        [107, 39],
        [107, 43],
        [107, 40],
        [107, 65],
        [108, 1],
        [108, 41],
        [108, 39],
        [108, 43],
        [108, 40],
        [108, 67],
        [109, 1],
        [109, 41],
        [109, 39],
        [109, 43],
        [109, 40],
        [109, 66],
        [110, 1],
        [110, 41],
        [110, 39],
        [110, 43],
        [110, 40],
        [110, 68],
        [111, 1],
        [111, 119],
        [111, 110],
        [111, 41]
    ]
    rows = [dict(zip(columns, row)) for row in data]

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
    connection.execute('SET foreign_key_checks = 0;')

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
    connection.execute('SET foreign_key_checks = 1;')
    session.commit()
