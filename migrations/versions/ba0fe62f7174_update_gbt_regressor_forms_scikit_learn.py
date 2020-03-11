# -*- coding: utf-8 -*-

"""Update GBT regressor forms (scikit_learn).

Revision ID: ba0fe62f7174
Revises: 02edf9a6f289
Create Date: 2019-10-25 15:04:52.352433

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
revision = 'ba0fe62f7174'
down_revision = '02edf9a6f289'
branch_labels = None
depends_on = None


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (4026, 41),  #appearance
        (4026, 4006),  # own execution form
        (4026, 110)
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
        #Flatten
        (4026, 1, 1, 'execution'), #data_format
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
        #Flatten - data_format
        (4026, 'en', 'Execution'),
        (4026, 'pt', 'Execução'),
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

    enabled_condition = 'this.loss.internalValue === "huber" || this.loss.internalValue === "quantile"'
    enabled_condition2 = 'this.n_iter_no_change.internalValue !== "0"'

    data = [
        #Flatten - data_format
        (4027, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4006, None),
        (4028, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 4006, None),
        (4029, 'prediction', 'TEXT', 0, 3, 'prediction', 'text', None, None, 'EXECUTION', 4006, None),
        (4030, 'presort', 'INTEGER', 0, 4, 0, 'checkbox', None, None, 'EXECUTION', 4006, None),
        (4031, 'validation_fraction', 'FLOAT', 0, 6, 0.1, 'decimal', None, None, 'EXECUTION', 4006, enabled_condition2),
        (4160, 'learning_rate', 'DECIMAL', 0, 6, 0.1, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4161, 'n_estimators', 'INTEGER', 0, 7, 100, 'integer', None, None, 'EXECUTION', 4006, None),
        (4162, 'max_depth', 'INTEGER', 0, 8, 3, 'integer', None, None, 'EXECUTION', 4006, None),
        (4163, 'min_samples_split', 'INTEGER', 0, 9, 2, 'integer', None, None, 'EXECUTION', 4006, None),
        (4164, 'min_samples_leaf', 'INTEGER', 0, 10, 1, 'integer', None, None, 'EXECUTION', 4006, None),
        (4165, 'n_iter_no_change', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 4006, None),
        (4166, 'tol', 'DECIMAL', 0, 12, 1e-4, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4167, 'criterion', 'TEXT', 0, 13, 'friedman_mse', 'dropdown', None,
         json.dumps([
             {"key": "friedman_mse", "value": "Mean squared error with improvement score by Friedman"},
             {"key": "mse", "value": "Mean squared error"},
             {"key": "mae", "value": "Mean absolute error"},
         ]),
         'EXECUTION', 4006, None),
        (4168, 'loss', 'TEXT', 0, 13, 'ls', 'dropdown', None,
         json.dumps([
             {"key": "ls", "value": "Least squares regression"},
             {"key": "lad", "value": "Least absolute deviation"},
             {"key": "huber", "value": "Combination of the two above"},
             {"key": "quantile", "value": "Quantile regression"},
         ]),
         'EXECUTION', 4006, None),
        (4169, 'subsample', 'DECIMAL', 0, 14, 1.0, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4170, 'alpha', 'DECIMAL', 0, 15, 0.9, 'decimal', None, None, 'EXECUTION', 4006, enabled_condition),
        (4171, 'min_weight_fraction_leaf', 'DECIMAL', 0, 16, 0, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4172, 'max_leaf_nodes', 'INTEGER', 0, 17, None, 'integer', None, None, 'EXECUTION', 4006, None),
        (4173, 'min_impurity_decrease', 'DECIMAL', 0, 18, 0, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4174, 'random_state', 'INTEGER', 0, 19, None, 'integer', None, None, 'EXECUTION', 4006, None),
        (4175, 'verbose', 'INTEGER', 0, 20, 0, 'integer', None, None, 'EXECUTION', 4006, None),
        (4176, 'warm_start', 'INTEGER', 0, 21, 0, 'checkbox', None, None, 'EXECUTION', 4006, None),
        (4177, 'max_features', 'TEXT', 0, 22, None, 'dropdown', None,
         json.dumps([
             {"key": "auto", "value": "auto"},
             {"key": "sqrt", "value": "sqrt"},
             {"key": "log2", "value": "log2"},
         ]),
         'EXECUTION', 4006, None),
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
        (4027, 'en', 'Features', 'Features.'),
        (4027, 'pt', 'Atributo(s) previsor(es)', 'Atributo(s) previsor(es).'),

        (4028, 'en', 'Label attribute', 'Label attribute.'),
        (4028, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo.'),

        (4029, 'en', 'Prediction attribute (new)', 'Prediction attribute (new).'),
        (4029, 'pt', 'Atributo com a predição (novo)', 'Atributo usado para predição (novo).'),

        (4030, 'en', 'Presort', 'Wheter to presort the data to speed up the finding of best splits in fitting.'),
        (4030, 'pt', 'Pré-ordenar', 'Se deve pré-ordenar os dados para acelerar a busca das melhores divisões no'
                                    ' ajuste.'),

        (4031, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4031, 'pt', 'Fração de validação', 'A proporção de dados de treinamento a serem retirados como validação'
                                            ' definida para parada antecipada.'),

        (4160, 'en', 'Learning rate', 'Learning rate shrinks the contribution of each tree by learning_rate. There is a'
                                      ' trade-off between learning rate and number of estimators.'),
        (4160, 'pt', 'Taxa de aprendizado', 'A taxa de aprendizado reduz a contribuição de cada árvore. Existe um'
                                            ' trade-off entre taxa de aprendizado e número de árvores.'),

        (4161, 'en', 'Number of estimators', 'The number of boosting stages to perform. Gradient boosting is fairly'
                                             ' robust to over-fitting so a large number usually results in better'
                                             ' performance.'),
        (4161, 'pt', 'Número de árvores', 'Número de árvores na floresta.'),

        (4162, 'en', 'Maximum depth', 'Maximum depth of the individual regression estimators. The maximum depth limits'
                                      ' the number of nodes in the tree. Tune this parameter for best performance; the'
                                      ' best value depends on the interaction of the input variables.'),
        (4162, 'pt', 'Profundidade máxima', 'Profundidade máxima na árvore.'),

        (4163, 'en', 'Minimun samples split', 'The minimum number of samples required to split an internal node.'),
        (4163, 'pt', 'Nó interno mínimo', 'Porcentagem do número mínimo de amostras necessárias para dividir um nó'
                                          ' interno.'),

        (4164, 'en', 'Minimum samples leaf', 'The minimum number of samples required to be at a leaf node.'),
        (4164, 'pt', 'Nó de folha mínima', 'Porcentagem do número mínimo de amostras necessárias para estar em um nó'
                                           ' folha.'),

        (4165, 'en', 'Early stopping', 'Used to decide if early stopping will be used to terminate training when'
                                       ' validation score is not improving.'),
        (4165, 'pt', 'Parada antecipada', 'Usada para decidir se a parada antecipada vai ser usada para terminar treino'
                                          ' quando a pontuação de validação não está melhorando.'),

        (4166, 'en', 'Tolerance', 'Tolerance for the early stopping.'),
        (4166, 'pt', 'Tolerância', 'Tolerância para a parada antecipada.'),

        (4167, 'en', 'Criterion', 'The function to measure the quality of a split..'),
        (4167, 'pt', 'Critério', 'A função para medir a qualidade de um split..'),

        (4168, 'en', 'Loss', 'Loss function to be optimized.'),
        (4168, 'pt', 'Perda', 'Função de perda a ser otimizada.'),

        (4169, 'en', 'Subsample', 'The fraction of samples to be used for fitting the individual base learners.'),
        (4169, 'pt', 'Subamostra', 'A fração de amostras para serem usadas para fazer o fitting em learners de base'
                                   ' individual.'),

        (4170, 'en', 'Alpha', 'The alpha-quantile of the huber loss function and the quantiles loss function.'),
        (4170, 'pt', 'Alfa', 'O alfa-quantil da função huber loss e a função de perda de quantis.'),

        (4171, 'en', 'Min. weight fraction leaf', 'The minimum weighted fraction of the sum total of weights (of all'
                                                  ' the input samples) required to be at a leaf node..'),
        (4171, 'pt', 'Fração ponderada mínima', 'A fração ponderada mínima da soma total de pesos (de todas as amostras'
                                                ' de entrada) necessária para estar em um nó folha.'),

        (4172, 'en', 'Max. leaf nodes', 'Grow trees with max_leaf_nodes in best-first fashion.'),
        (4172, 'pt', 'Max. nós folha', 'Cresça árvores com max_leaf_nodes da melhor maneira possível.'),

        (4173, 'en', 'Min. impurity decrease', 'A node will be split if this split induces a decrease of the impurity'
                                               ' greater than or equal to this value.'),
        (4173, 'pt', 'Redução mínima da impureza', 'Um nó será dividido se essa divisão induzir uma redução da impureza'
                                                   ' maior ou igual a esse valor.'),

        (4174, 'en', 'Random state', 'Is the seed used by the random number generator.'),
        (4174, 'pt', 'Estado aleatório', 'É a semente usada pelo gerador de números aleatórios.'),

        (4175, 'en', 'Verbose', 'Controls the verbosity when fitting and predicting..'),
        (4175, 'pt', 'Verbose', 'Controla a verbosidade ao ajustar e prever.'),

        (4176, 'en', 'Warm start', 'When set to True, reuse the solution of the previous call to fit and add more'
                                   ' estimators to the ensemble, otherwise, just fit a whole new forest..'),
        (4176, 'pt', 'Warm start', 'Quando definido como verdadeiro, reutilize a solução da chamada anterior para'
                                   ' ajustar e adicione mais estimadores ao conjunto; caso contrário, ajuste apenas uma'
                                   ' floresta totalmente nova.'),

        (4177, 'en', 'Max. features', 'The number of features to consider when looking for the best split.'),
        (4177, 'pt', 'Número máximo de atributos', 'Número de atributos a serem considerados ao procurar a melhor '
                                                   'divisão.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4160 AND 4178 OR id BETWEEN 4027 AND 4031'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4160 AND 4178 OR id BETWEEN 4027 AND 4031'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4026'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 4026'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 4026'),
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