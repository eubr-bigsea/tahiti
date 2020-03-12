# -*- coding: utf-8 -*-

"""Update random forest regressor form fields (scikit_learn).

Revision ID: 02edf9a6f289
Revises: 3e10f106043c
Create Date: 2019-10-24 14:07:25.529478

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
revision = '02edf9a6f289'
down_revision = '3e10f106043c'
branch_labels = None
depends_on = None


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

    data = [
        #Flatten - data_format
        (4150, 'min_weight_fraction_leaf', 'FLOAT', 0, 4, 0, 'decimal', None, None, 'EXECUTION', 4022, None),
        (4151, 'max_leaf_nodes', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 4022, None),
        (4152, 'min_impurity_decrease', 'FLOAT', 0, 6, 0, 'decimal', None, None, 'EXECUTION', 4022, None),
        (4153, 'bootstrap', 'INTEGER', 0, 7, 1, 'checkbox', None, None, 'EXECUTION', 4022, None),
        (4154, 'oob_score', 'INTEGER', 0, 8, 0, 'checkbox', None, None, 'EXECUTION', 4022, None),
        (4155, 'n_jobs', 'INTEGER', 0, 9, 0, 'integer', None, None, 'EXECUTION', 4022, None),
        (4156, 'random_state', 'INTEGER', 0, 10, None, 'integer', None, None, 'EXECUTION', 4022, None),
        (4157, 'verbose', 'INTEGER', 0, 11, 0, 'integer', None, None, 'EXECUTION', 4022, None),
        (4158, 'warm_start', 'INTEGER', 0, 12, 0, 'checkbox', None, None, 'EXECUTION', 4022, None),
        (4159, 'criterion', 'TEXT', 0, 13, "mse", 'dropdown', None,
         json.dumps([
             {"key": "mse", "value": "Mean squared error"},
             {"key": "mae", "value": "Mean absolute error"}
         ]),
         'EXECUTION', 4022, None),
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
        (4150, 'en', 'Minimum weighted fraction', 'The minimum weighted fraction of the sum total of weights (of all'
                                                  ' the input samples) required to be at a leaf node.'),
        (4150, 'pt', 'Fração ponderada mínima', 'A fração ponderada mínima da soma total de pesos (de todas as amostras'
                                                ' de entrada) necessária para estar em um nó folha.'),
        (4151, 'en', 'Max. leaf nodes', 'Grow trees with max_leaf_nodes in best-first fashion.'),
        (4151, 'pt', 'Max. nós folha', 'Cresça árvores com max_leaf_nodes da melhor maneira possível.'),
        (4152, 'en', 'Min. impurity decrease', 'A node will be split if this split induces a decrease of the impurity'
                                               ' greater than or equal to this value.'),
        (4152, 'pt', 'Redução mínima da impureza', 'Um nó será dividido se essa divisão induzir uma redução da'
                                                   ' impureza maior ou igual a esse valor.'),
        (4153, 'en', 'Bootstrap', 'Whether bootstrap samples are used when building trees.'),
        (4153, 'pt', 'Amostras de autoinicialização', 'Se as amostras de autoinicialização são usadas na construção de'
                                                      ' árvores.'),
        (4154, 'en', 'Out-of-bag samples', 'Whether to use out-of-bag samples to estimate the R² on unseen data.'),
        (4154, 'pt', 'Amostras prontas', 'Se é necessário usar amostras prontas para estimar o R² em dados não'
                                         ' vistos.'),
        (4155, 'en', 'Number of jobs', 'The number of jobs to run in parallel for both fit and predict.'),
        (4155, 'pt', 'Números de jobs', 'O número de jobs a serem executados em paralelo para o fit e o predict'),
        (4156, 'en', 'Random state', 'Is the seed used by the random number generator.'),
        (4156, 'pt', 'Estado aleatório', 'É a semente usada pelo gerador de números aleatórios.'),
        (4157, 'en', 'Verbose', 'Controls the verbosity when fitting and predicting.'),
        (4157, 'pt', 'Verbose', 'Controla a verbosidade ao ajustar e prever.'),
        (4158, 'en', 'Warm start', 'When set to True, reuse the solution of the previous call to fit and add more'
                                   ' estimators to the ensemble, otherwise, just fit a whole new forest.'),
        (4158, 'pt', 'Warm start', 'Quando definido como verdadeiro, reutilize a solução da chamada anterior para'
                                   ' ajustar e adicione mais estimadores ao conjunto; caso contrário, ajuste apenas uma'
                                   ' floresta totalmente nova.'),
        (4159, 'en', 'Criterion', 'The function to measure the quality of a split.'),
        (4159, 'pt', 'Critério', 'A função para medir a qualidade de um split.'),
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
        (4028, 41),  #appearance
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4150 AND 4159'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4150 AND 41459'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_form_id = 41'),
    ("""UPDATE operation_form_field SET `default` = '100' WHERE id = 4039""",
     """UPDATE operation_form_field SET `default` = '10' WHERE id = 4039"""),
    ("""UPDATE operation_form_field SET `default` = 'prediction' WHERE id = 4110""",
     """UPDATE operation_form_field SET `default` = NULL WHERE id = 4110"""),
    ("""UPDATE operation_form_field SET `default` = NULL WHERE id = 4041""",
     """UPDATE operation_form_field SET `default` = '3' WHERE id = 4041"""),
    ('DELETE FROM operation_form_field_translation WHERE id = 4044',
     'DELETE FROM operation_form_field_translation WHERE id = 4044'),
    ('DELETE FROM operation_form_field WHERE id = 4044',
     'DELETE FROM operation_form_field WHERE id = 4044'),
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