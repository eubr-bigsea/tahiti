# -*- coding: utf-8 -*-

"""Update Perceptron classifier (scikit_learn).

Revision ID: 5d65ae2809bd
Revises: 075e90409e3a
Create Date: 2019-12-03 11:07:49.689505

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
revision = '5d65ae2809bd'
down_revision = '075e90409e3a'
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
        (4025, 41),  #appearance
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

    enable_condition = 'this.early_stopping.internalValue === "1"'

    data = [
        #Flatten - data_format
        (4266, 'fit_intercept', 'INTEGER', 0, 7, 1, 'integer', None,  None, 'EXECUTION', 4005, None),
        (4267, 'verbose', 'INTEGER', 0, 8, 0, 'integer', None,  None, 'EXECUTION', 4005, None),
        (4268, 'eta0', 'DECIMAL', 0, 9, 1, 'decimal', None,  None, 'EXECUTION', 4005, None),
        (4269, 'n_jobs', 'INTEGER', 0, 10, None, 'integer', None,  None, 'EXECUTION', 4005, None),
        (4270, 'early_stopping', 'INTEGER', 0, 11, 0, 'integer', None,  None, 'EXECUTION', 4005, None),
        (4271, 'validation_fraction', 'DECIMAL', 0, 12, 0.1, 'decimal', None,  None, 'EXECUTION', 4005,
         enable_condition),
        (4272, 'n_iter_no_change', 'INTEGER', 0, 13, 5, 'integer', None,  None, 'EXECUTION', 4005, None),
        (4273, 'class_weight', 'TEXT', 0, 14, None, 'text', None,  None, 'EXECUTION', 4005, None),
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
        (4266, 'en', 'Fit intercept', 'Whether the intercept should be estimated or not.'),
        (4266, 'pt', 'Fit interceptação', 'Se a interceptação deve ser estimada ou não.'),

        (4267, 'en', 'Verbose', 'The verbosity level.'),
        (4267, 'pt', 'Verbosidade', 'O nível de verbosidade.'),

        (4268, 'en', 'Eta', 'Constant by which the updates are multiplied.'),
        (4268, 'pt', 'Eta', 'Constante pela qual as atualizações são multiplicadas.'),

        (4269, 'en', 'Number of jobs', 'The number of CPUs to use to do the OVA (One Versus All, for multi-class'
                                       ' problems) computation.'),
        (4269, 'pt', 'Número de jobs', 'O número de CPUs a serem usadas para calcular o OVA (One Versus All, para'
                                       ' problemas de várias classes).'),

        (4270, 'en', 'Early stopping', 'Whether to use early stopping to terminate training when validation score is'
                                       ' not improving.'),
        (4270, 'pt', 'Parada antecipada', 'Se a parada antecipada deve ser usada para encerrar o treinamento quando a'
                                          ' pontuação de validação não está melhorando.'),

        (4271, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4271, 'pt', 'Fração de validação', 'A proporção de dados de treinamento a serem retirados como validação'
                                            ' definida para parada antecipada.'),

        (4272, 'en', 'Number of iterations with no change', 'Number of iterations with no improvement to wait before'
                                                            ' early stopping.'),
        (4272, 'pt', 'Número de iterações sem melhoria', 'Número de iterações sem melhoria a aguardar antes da parada'
                                                         ' precoce.'),

        (4273, 'en', 'Class weight', 'Preset for the class_weight fit parameter (dictionary).'),
        (4273, 'pt', 'Peso da classe', 'Predefinição para o parâmetro de ajuste class_weight (dicionário).'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4022 OR id = 4024""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4022 OR id = 4024"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4266 AND 4273'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4266 AND 4273'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4025 AND operation_form_id = 41'),
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
