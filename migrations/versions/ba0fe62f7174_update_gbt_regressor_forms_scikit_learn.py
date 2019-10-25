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
        (4026, 4022),
        (4026, 4006),  # own execution form
        (4026, 110)
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form(): #ok
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

    enabled_condition = 'this.loss.internalValue === "huber"' or 'this.loss.internalValue === "quantile"'
    enabled_condition2 = 'this.n_iter_no_change.internalValue !== "None"'

    data = [
        #Flatten - data_format
        (4160, 'loss', 'TEXT', 0, 7, 'ls', 'dropdown', None,
         json.dumps([
             {"key": "ls", "value": "Least squares regression"},
             {"key": "lad", "value": "Least absolute deviation"},
             {"key": "huber", "value": "Combination of the two above"},
             {"key": "quantile", "value": "Quantile regression"},
         ]),
         'EXECUTION', 4006, None),
        (4161, 'subsample', 'FLOAT', 0, 8, 1.0, 'decimal', None, None, 'EXECUTION', 4006, None),
        (4162, 'alpha', 'FLOAT', 0, 9, 0.9, 'attribute-selector', None, None, 'EXECUTION', 4006, enabled_condition),
        (4163, 'presort', 'TEXT', 0, 10, None, 'text', None, None, 'EXECUTION', 4006, None), #falta
        (4164, 'validation_fraction', 'FLOAT', 0, 11, 0.1, 'decimal', None, None, 'EXECUTION', 4006, enabled_condition2),
        (4165, 'n_iter_no_change', 'INTEGER', 0, 12, None, 'int', None, None, 'EXECUTION', 4006, None),
        (4166, 'tol', 'FLOAT', 0, 13, 1e-4, 'decimal', None, None, 'EXECUTION', 4006, None),
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
        (4160, 'en', 'Loss', 'Loss function to be optimized.'),
        (4160, 'pt', 'Perda', 'Função de perda a ser otimizada.'),

        (4161, 'en', 'Subsample', 'The fraction of samples to be used for fitting the individual base learners.'),
        (4161, 'pt', 'Subamostra', 'A fração de amostras para serem usadas para fazer o fitting em learners de base'
                                   ' individual.'),

        (4162, 'en', 'Alpha', 'The alpha-quantile of the huber loss function and the quantiles loss function.'),
        (4162, 'pt', 'Alfa', 'O alfa-quantil da função huber loss e a função de perda de quantis.'),

        (4163, 'en', 'Presort', 'Wheter to presort the data to speed up the finding of best splits in fitting.'),
        (4163, 'pt', 'Pré-ordenar', 'Se deve pré-ordenar os dados para acelerar a busca das melhores divisões no'
                                    ' ajuste.'),

        (4164, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4164, 'pt', 'Fração de validação', 'A proporção de dados de treinamento a serem retirados como validação'
                                            ' definida para parada antecipada.'),

        (4165, 'en', 'Early stopping', 'Used to decide if early stopping will be used to terminate training when'
                                       ' validation score is not improving.'),
        (4165, 'pt', 'Parada antecipada', 'Usada para decidir se a parada antecipada vai ser usada para terminar treino'
                                          ' quando a pontuação de validação não está melhorando.'),

        (4166, 'en', 'Tolerance', 'Tolerance for the early stopping.'),
        (4166, 'pt', 'Tolerância', 'Tolerância para a parada antecipada.'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4160 AND 41466'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4160 AND 4166'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4026 AND operation_form_id = 4006'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id = 4026'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id = 4026'),

    ('DELETE FROM operation_form_field_translation WHERE id = 4032',
     'DELETE FROM operation_form_field_translation WHERE id = 4032'),
    ('DELETE FROM operation_form_field WHERE id = 4032',
     'DELETE FROM operation_form_field WHERE id = 4032'),
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