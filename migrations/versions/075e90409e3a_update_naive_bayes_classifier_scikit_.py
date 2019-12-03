# -*- coding: utf-8 -*-

"""Update Naive-Bayes classifier (scikit_learn).

Revision ID: 075e90409e3a
Revises: f744c0dbb4a1
Create Date: 2019-12-03 10:01:23.865437

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
revision = '075e90409e3a'
down_revision = 'f744c0dbb4a1'
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
        (4032, 41),  #appearance
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

    enable_condition = 'this.type.internalValue === "Bernoulli"'
    enable_condition2 = 'this.type.internalValue === "Multinomial" || this.type.internalValue === "Bernoulli"'
    enable_condition3 = 'this.type.internalValue === "Gaussian"'

    data = [
        #Flatten - data_format
        (4262, 'piors', 'TEXT', 0, 4, None, 'text', None,  None, 'EXECUTION', 4012, enable_condition3),
        (4263, 'var_smoothing', 'DECIMAL', 0, 5, 1e-9, 'decimal', None,  None, 'EXECUTION', 4012, enable_condition3),
        (4264, 'fit_prior', 'INTEGER', 0, 6, 1, 'integer', None,  None, 'EXECUTION', 4012, enable_condition2),
        (4265, 'binarize', 'DECIMAL', 0, 7, 0, 'decimal', None,  None, 'EXECUTION', 4012, enable_condition),
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
        (4262, 'en', 'Piors', 'Prior probabilities of the classes.'),
        (4262, 'pt', 'Anteriores', 'Probabilidades anteriores das classes.'),

        (4263, 'en', 'Variance', 'Portion of the largest variance of all features that is added to variances for'
                                 ' calculation stability.'),
        (4263, 'pt', 'Variação', 'Parte da maior variação de todos os recursos adicionados às variações de'
                                 ' estabilidade de cálculo.'),

        (4264, 'en', 'Class prior probabilities', 'Whether to learn class prior probabilities or not.'),
        (4264, 'pt', 'Probabilidades anteriores da classe', 'Se deve aprender as probabilidades anteriores da aula ou'
                                                            ' não.'),

        (4265, 'en', 'Binarize', 'Threshold for binarizing (mapping to booleans) of sample features.'),
        (4265, 'pt', 'Binarização', 'Limite para binarização (mapeamento para booleanos) de recursos de amostra.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4061""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4061"""),

    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.type.internalValue === "Multinomial" || 
        this.type.internalValue === "Bernoulli"' WHERE id = 4061""",
     """UPDATE operation_form_field SET `enable_conditions` = 'None' WHERE id = 4061"""),

    ("""UPDATE operation_form_field SET `enable_conditions` = 'this.type.internalValue === "Multinomial" || 
        this.type.internalValue === "Bernoulli"' WHERE id = 4062""",
     """UPDATE operation_form_field SET `enable_conditions` = 'None' WHERE id = 4062"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4262 AND 4265'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4262 AND 4265'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4032 AND operation_form_id = 41'),
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