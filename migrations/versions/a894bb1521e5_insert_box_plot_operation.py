# -*- coding: utf-8 -*-

"""Insert Box Plot operation.

Revision ID: a894bb1521e5
Revises: 89965c2cd39b
Create Date: 2019-09-13 17:24:05.560237

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
revision = 'a894bb1521e5'
down_revision = '89965c2cd39b'
branch_labels = None
depends_on = None


SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4040


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
        (ID_OPERATION, "box-plot", 1, 'ACTION', ''),
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
        (15, 4040),
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
        (ID_OPERATION, "pt", 'Box Plot', 'Diagrama de caixa, diagrama de extremos e quartis, boxplot ou box plot é uma'
                                         ' ferramenta gráfica para representar a variação de dados observados de uma '
                                         'variável numérica por meio de quartis.'),
        (ID_OPERATION, "en", 'Box Plot', '')
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
        (ID_OPERATION, 4027),  # own execution form
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
        (4027, 1, 1, 'execution'), #data_format
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
        (4027, 'en', 'Execution'),
        (4027, 'pt', 'Execução'),
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
        (4135, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 4027, None),
        (4136, 'entry', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4027, None),
        (4137, 'x_axis', 'TEXT', 0, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4027, None),
        (4138, 'discrepancy', 'INTEGER', 0, 1, 0, 'checkbox', None, None, 'EXECUTION', 4027, None),
        (4139, 'x', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 4027, None),
        (4140, 'y', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', 4027, None),
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
        (4135, 'en', 'Title', 'Title for the graphic.'),
        (4135, 'pt', 'Título', 'Título para o gŕafico.'),

        (4136, 'en', 'Entry attributes', 'Attributes used to calculate the quartiles and to generate the box plot.'),
        (4136, 'pt', 'Atributo(s) de entrada', 'Atributos usados para calcular os quartis e gerar o box plot.'),

        (4137, 'en', 'Attribute used to group (x-axis)', 'The entry data will be grouped by this attribute and the '
                                                         'quartiles will be calculated for each group. Each group will'
                                                         ' be a box on the X axis.'),
        (4137, 'pt', 'Atributo usado para agrupar (x-axis)', 'Os dados de entrada serão agrupados por este atributo e'
                                                             ' os quartis serão calculados para cada grupo. Cada grupo'
                                                             ' será uma caixa no eixo X.'),

        (4138, 'en', 'Display discrepancy', 'Display discrepancy (outliers).'),
        (4138, 'pt', 'Exibir discrepantes', 'Exibir discrepantes (outliers).'),

        (4139, 'en', 'Title for the X axis', 'Title for the X axis.'),
        (4139, 'pt', 'Título para o eixo X', 'Título para o eixo X.'),

        (4140, 'en', 'Title for the Y axis', 'Title for the Y axis.'),
        (4140, 'pt', 'Título para o eixo Y', 'Título para o eixo Y.'),

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
        (4086, 'INPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
        (4087, 'OUTPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
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
        (4086, 1),
        (4087, 1),

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
        (4086, "en", 'input data', 'Input data'),
        (4086, "pt", 'dados de entrada', 'Dados de entrada'),
        (4087, "en", 'visualization', 'Visualization'),
        (4087, "pt", 'visualização', 'Visualização'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 4040'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(ID_OPERATION)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id IN (4040)'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4040 AND platform_id = {}'.format(SCIKIT_LEARN_PLATAFORM_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4027'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4135 AND 4140'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4027'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4135 AND 4140'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4040'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4086 AND 4087'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4086 AND 4087'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4086 AND 4087'),

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