# -*- coding: utf-8 -*-

"""Fixing scikit_learn Huber regressor.

Revision ID: f2c2be48125d
Revises: ba0fe62f7174
Create Date: 2019-11-05 15:12:11.502286

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
revision = 'f2c2be48125d'
down_revision = '4c1ebd8863a8'
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
        (4030, 41),  #appearance
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

    data = [
        #Flatten - data_format
        (4185, 'warm_start', 'INTEGER', 0, 8, 0, 'checkbox', None, None, 'EXECUTION', 4010, None),
        (4186, 'fit_intercept', 'INTEGER', 0, 9, 1, 'checkbox', None, None, 'EXECUTION', 4010, None),
        (4187, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4010, None),
        (4188, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None, 'EXECUTION', 4010, None),
        (4189, 'prediction', 'TEXT', 0, 3, 'prediction', 'text', None, None, 'EXECUTION', 4010, None),
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
        (4185, 'en', 'Warm start', 'This is useful if the stored attributes of a previously used model has to be '
                                   'reused. If set to False, then the coefficients will be rewritten for every call to'
                                   ' fit.'),
        (4185, 'pt', 'Warm start', 'Isso é útil se os atributos armazenados de um modelo usado anteriormente tiverem'
                                   ' que ser reutilizados. Se definido como Falso, os coeficientes serão reescritos'
                                   ' para cada chamada ao fit.'),

        (4186, 'en', 'Fit the intercept', 'Whether or not to fit the intercept. This can be set to False if the data is'
                                          ' already centered around the origin.'),
        (4186, 'pt', 'Fit interceptação', 'Se deve ou não caber na interceptação. Isso pode ser definido como False se'
                                          ' os dados já estiverem centralizados em torno da origem.'),

        (4187, 'en', 'Features', 'Features.'),
        (4187, 'pt', 'Atributo(s) previsor(es)', 'Atributo(s) previsor(es).'),

        (4188, 'en', 'Label attribute', 'Label attribute.'),
        (4188, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo.'),

        (4189, 'en', 'Prediction attribute (new)', 'Prediction attribute (new).'),
        (4189, 'pt', 'Atributo com a predição (novo)', 'Atributo usado para predição (novo).'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_translation SET `name` = 'Regressor Huber' WHERE id = 4030 AND `locale` = 'pt'""",
     """UPDATE operation_translation SET `name` = 'Regressor Hube' WHERE id = 4030 AND `locale` = 'pt'"""),

    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4050 OR id = 4052 OR id = 4053""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4050 OR id = 4052 OR id = 4053"""),

    ("""UPDATE operation_form_field SET `order` = '5' WHERE id = 4050""",
     """UPDATE operation_form_field SET `order` = '1' WHERE id = 4050"""),

    ("""UPDATE operation_form_field SET `order` = '6' WHERE id = 4051""",
     """UPDATE operation_form_field SET `order` = '2' WHERE id = 4051"""),

    ("""UPDATE operation_form_field SET `order` = '7' WHERE id = 4052""",
     """UPDATE operation_form_field SET `order` = '3' WHERE id = 4052"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4185 AND 4189'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4185 AND 4189'),

    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4030 AND operation_form_id = 41'),
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
