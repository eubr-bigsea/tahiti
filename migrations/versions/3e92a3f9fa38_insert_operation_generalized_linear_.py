# -*- coding: utf-8 -*-

"""Insert operation Generalized Linear Regression

Revision ID: 3e92a3f9fa38
Revises: b819b756d9f9
Create Date: 2019-09-09 14:42:02.221461

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
revision = '3e92a3f9fa38'
down_revision = 'b819b756d9f9'
branch_labels = None
depends_on = None


SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4038


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')

    data = [
        (ID_OPERATION, SCIKIT_LEARN_PLATAFORM_ID)
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer),)

    columns = ('id', 'slug', 'enabled', 'type', 'icon')

    data = [
        (ID_OPERATION, "generalized-linear-regression", 1, 'ACTION', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_category_id', 'operation_id')
    data = [
        #Core Layers
        (8, 4038),
        (21, 4038)
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (ID_OPERATION, "pt", 'Regressão Linear Generalizada', ''),
        (ID_OPERATION, "en", 'Generalized Linear Regression', 'Generalized Linear Regression fits a linear model with '
                                                              'coefficients  to minimize the residual sum of squares '
                                                              'between the observed targets in the dataset, and the '
                                                              'targets predicted by the linear approximation.')
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
        (ID_OPERATION, 41),  #appearance
        (ID_OPERATION, 4025),  # own execution form
        (ID_OPERATION, 110)
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
        (4025, 1, 1, 'execution'), #data_format
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
        (4025, 'en', 'Execution'),
        (4025, 'pt', 'Execução'),
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
    enable_condition = 'this.fit_intercept.internalValue === "1"'
    data = [
        #Flatten - data_format
        (4122, 'label', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4025, None),
        (4123, 'fit_intercept', 'INTEGER', 0, 1, 1, 'checkbox', None, None, 'EXECUTION', 4025, None),
        (4124, 'normalize', 'INTEGER', 0, 1, 0, 'checkbox', None, None, 'EXECUTION', 4025, enable_condition),
        (4125, 'copy_X', 'INTEGER', 0, 1, 1, 'checkbox', None, None, 'EXECUTION', 4025, None),
        (4126, 'n_jobs', 'INTEGER', 0, 1, None, 'integer', None, None, 'EXECUTION', 4025, None),
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
        (4122, 'en', 'Label', 'Label.'),
        (4122, 'pt', 'Atributo usado como rótulo (label)', 'Atributo usado como rótulo (label).'),

        (4123, 'en', 'Intercept', 'Whether to calculate the intercept for this model.'),
        (4123, 'pt', 'Interceptar', 'Se deve calcular a interceptação para este modelo.'),

        (4124, 'en', 'Normalize', 'Used to normalized the regressors before regression.'),
        (4124, 'pt', 'Normalizar', 'Usado para normalizar os regressores antes da regressão.'),

        (4125, 'en', 'Copy', 'If True, X will be copied; else, it may be overwritten.'),
        (4125, 'pt', 'Copiar', 'Se verdadeiro, X vai ser copiado; senão, pode ser sobrescrito.'),

        (4126, 'en', 'Number of jobs', 'The number of jobs to use for the computation.'),
        (4126, 'pt', 'Número de jobs', 'O número de jobs usados para a computação.'),

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
        column('slug', String),)

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        #Reshape
        (4080, 'INPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
        (4081, 'OUTPUT', '', 1, 'ONE', ID_OPERATION, 'output data'),
        (4082, 'OUTPUT', '', 2, 'MANY', ID_OPERATION, 'output model'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        #Reshape
        (4080, 1),
        (4081, 1),
        (4082, 2),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        #Reshape
        (4080, "en", 'input data', 'Input data'),
        (4080, "pt", 'dados de entrada', 'Dados de entrada'),
        (4081, "en", 'output data', 'Output data'),
        (4081, "pt", 'dados de saída', 'Dados de saída'),
        (4082, "en", 'model', 'Model'),
        (4082, "pt", 'Modelo', 'Modelo'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 4038'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(ID_OPERATION)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id IN (4038)'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4038 AND platform_id = {}'.format(SCIKIT_LEARN_PLATAFORM_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4025'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4122 AND 4126'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4025'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4122 AND 4126'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4038'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4080 AND 4082'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4080 AND 4082'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4080 AND 4082'),

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