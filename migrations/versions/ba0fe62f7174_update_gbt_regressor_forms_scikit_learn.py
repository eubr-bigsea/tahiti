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
        (4357, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4006, None),
        (4358, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 4006, None),
        (4359, 'prediction', 'TEXT', 0, 3, 'prediction', 'text', None, None, 'EXECUTION', 4006, None),
        (4360, 'validation_fraction', 'FLOAT', 0, 6, 0.1, 'decimal', None, None, 'EXECUTION', 4006, enabled_condition2),
        (4361, 'max_depth', 'INTEGER', 0, 8, 3, 'integer', None, None, 'EXECUTION', 4006, None),
        (4362, 'n_iter_no_change', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 4006, None),
        (4363, 'tol', 'DECIMAL', 0, 12, 1e-4, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4364, 'criterion', 'TEXT', 0, 13, 'friedman_mse', 'dropdown', None,
         json.dumps([
             {"key": "friedman_mse", "value": "Mean squared error with improvement score by Friedman"},
             {"key": "mse", "value": "Mean squared error"},
             {"key": "mae", "value": "Mean absolute error"},
         ]),
         'EXECUTION', 4006, None),
        (4365, 'loss', 'TEXT', 0, 13, 'ls', 'dropdown', None,
         json.dumps([
             {"key": "ls", "value": "Least squares regression"},
             {"key": "lad", "value": "Least absolute deviation"},
             {"key": "huber", "value": "Combination of the two above"},
             {"key": "quantile", "value": "Quantile regression"},
         ]),
         'EXECUTION', 4006, None),
        (4366, 'subsample', 'DECIMAL', 0, 14, 1.0, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4367, 'alpha', 'DECIMAL', 0, 15, 0.9, 'decimal', None, None, 'EXECUTION', 4006, enabled_condition),
        (4368, 'min_weight_fraction_leaf', 'DECIMAL', 0, 16, 0, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4369, 'max_leaf_nodes', 'INTEGER', 0, 17, None, 'integer', None, None, 'EXECUTION', 4006, None),
        (4370, 'min_impurity_decrease', 'DECIMAL', 0, 18, 0, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4371, 'max_features', 'TEXT', 0, 22, None, 'dropdown', None,
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
        (4357, 'en', 'Features', 'Features.'),
        (4357, 'pt', 'Atributo(s) previsor(es)', 'Atributo(s) previsor(es).'),

        (4358, 'en', 'Label attribute', 'Label attribute.'),
        (4358, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo.'),

        (4359, 'en', 'Prediction attribute (new)', 'Prediction attribute (new).'),
        (4359, 'pt', 'Atributo com a predição (novo)', 'Atributo usado para predição (novo).'),

        (4360, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4360, 'pt', 'Fração de validação', 'A proporção de dados de treinamento a serem retirados como validação'
                                            ' definida para parada antecipada.'),

        (4361, 'en', 'Maximum depth', 'Maximum depth of the individual regression estimators. The maximum depth limits'
                                      ' the number of nodes in the tree. Tune this parameter for best performance; the'
                                      ' best value depends on the interaction of the input variables.'),
        (4361, 'pt', 'Profundidade máxima', 'Profundidade máxima na árvore.'),

        (4362, 'en', 'Early stopping', 'Used to decide if early stopping will be used to terminate training when'
                                       ' validation score is not improving.'),
        (4362, 'pt', 'Parada antecipada', 'Usada para decidir se a parada antecipada vai ser usada para terminar treino'
                                          ' quando a pontuação de validação não está melhorando.'),

        (4363, 'en', 'Tolerance', 'Tolerance for the early stopping.'),
        (4363, 'pt', 'Tolerância', 'Tolerância para a parada antecipada.'),

        (4364, 'en', 'Criterion', 'The function to measure the quality of a split..'),
        (4364, 'pt', 'Critério', 'A função para medir a qualidade de um split..'),

        (4365, 'en', 'Loss', 'Loss function to be optimized.'),
        (4365, 'pt', 'Perda', 'Função de perda a ser otimizada.'),

        (4366, 'en', 'Subsample', 'The fraction of samples to be used for fitting the individual base learners.'),
        (4366, 'pt', 'Subamostra', 'A fração de amostras para serem usadas para fazer o fitting em learners de base'
                                   ' individual.'),

        (4367, 'en', 'Alpha', 'The alpha-quantile of the huber loss function and the quantiles loss function.'),
        (4367, 'pt', 'Alfa', 'O alfa-quantil da função huber loss e a função de perda de quantis.'),

        (4368, 'en', 'Min. weight fraction leaf', 'The minimum weighted fraction of the sum total of weights (of all'
                                                  ' the input samples) required to be at a leaf node..'),
        (4368, 'pt', 'Fração ponderada mínima', 'A fração ponderada mínima da soma total de pesos (de todas as amostras'
                                                ' de entrada) necessária para estar em um nó folha.'),

        (4369, 'en', 'Max. leaf nodes', 'Grow trees with max_leaf_nodes in best-first fashion.'),
        (4369, 'pt', 'Max. nós folha', 'Cresça árvores com max_leaf_nodes da melhor maneira possível.'),

        (4370, 'en', 'Min. impurity decrease', 'A node will be split if this split induces a decrease of the impurity'
                                               ' greater than or equal to this value.'),
        (4370, 'pt', 'Redução mínima da impureza', 'Um nó será dividido se essa divisão induzir uma redução da impureza'
                                                   ' maior ou igual a esse valor.'),

        (4371, 'en', 'Max. features', 'The number of features to consider when looking for the best split.'),
        (4371, 'pt', 'Número máximo de atributos', 'Número de atributos a serem considerados ao procurar a melhor '
                                                   'divisão.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4357 AND 4374'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4357 AND 4374'),
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