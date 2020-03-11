# -*- coding: utf-8 -*-

"""Insert operation K Fold

Revision ID: 93084d865c9e
Revises: a894bb1521e5
Create Date: 2019-09-16 16:41:53.717489

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
revision = '93084d865c9e'
down_revision = 'a894bb1521e5'
branch_labels = None
depends_on = None


SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4041


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
        (ID_OPERATION, "k-fold", 1, 'ACTION', ''),
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
        (32, 4041),
        (38, 4041),
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
        (ID_OPERATION, "pt", 'Divisão dos dados em K partições', 'Esta operação realiza a divisão do conjunto de dados'
                                                                 ' em k partições ou grupos de tamanho aproximadamente'
                                                                 ' igual'),
        (ID_OPERATION, "en", 'Split data into K Fold', 'This operation involves dividing the dataset into k folds or '
                                                       'partitions of approximately equal size')
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
        (ID_OPERATION, 4028),  # own execution form
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
        (4028, 1, 1, 'execution'), #data_format
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
        (4028, 'en', 'Execution'),
        (4028, 'pt', 'Execução'),
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

    enable_condition = 'this.shuffle.internalValue === "1"'
    enable_condition2 = 'this.stratified.internalValue === "1"'

    data = [
        #Flatten - data_format
        (4141, 'n_splits', 'INTEGER', 1, 1, 3, 'integer', None, None, 'EXECUTION', 4028, None), #Changed in version
        # 0.20: n_splits default value will change from 3 to 5 in v0.22.
        (4142, 'shuffle', 'INTEGER', 0, 1, 0, 'checkbox', None, None, 'EXECUTION', 4028, None),
        (4143, 'random_state', 'INTEGER', 0, 1, 1000, 'integer', None, None, 'EXECUTION', 4028, enable_condition),
        (4144, 'label', 'TEXT', 1, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4028, None),
        (4145, 'attribute', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION', 4028, None),
        (4146, 'stratified', 'TEXT', 0, 1, 0, 'checkbox', None, None, 'EXECUTION', 4028, None),
        (4147, 'column', 'TEXT', 0, 1, None, 'attribute-selector', None, None, 'EXECUTION', 4028, enable_condition2),
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
        (4141, 'en', 'Number of folds', 'Number of folds.'),
        (4141, 'pt', 'Número de partições', 'Número de partições.'),

        (4142, 'en', 'Embaralhar', 'Whether to shuffle the data before splitting into batches.'),
        (4142, 'pt', 'Shuffle', 'Se deve embaralhar os dados antes de dividir em lotes.'),

        (4143, 'en', 'Seed', 'Seed used by the random number generator.'),
        (4143, 'pt', 'Semente', 'Semente usada pelo gerador de números aleatórios.'),

        (4144, 'en', 'Label', 'Label.'),
        (4144, 'pt', 'Atributo usado como rótulo (label)', 'Atributo usado como rótulo (label).'),

        (4145, 'en', 'New attribute name', 'Name of the new attribute that indicates what fold the object belongs to.'),
        (4145, 'pt', 'Nome do novo atributo', 'Nome do novo atributo que indica a que partição o objeto pertence.'),

        (4146, 'en', 'Stratified K Fold', 'Stratified K-Folds cross-validator.'),
        (4146, 'pt', 'K Fold estratificado', 'Validação cruzada com K Fold estratificado.'),

        (4147, 'en', 'Database column', 'Database column that will be used in the K Fold.'),
        (4147, 'pt', 'Coluna da base de dados', 'Coluna da base de dados que será utilizada pra realizar o K Fold.'),

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
        (4088, 'INPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
        (4089, 'OUTPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
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
        (4088, 1),
        (4089, 1),

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
        (4088, "en", 'input data', 'Input data'),
        (4088, "pt", 'dados de entrada', 'Dados de entrada'),
        (4089, "en", 'output data', 'Output data'),
        (4089, "pt", 'dados de saída', 'Dados de saída'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 4041'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(ID_OPERATION)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id IN (4041)'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 4041 AND platform_id = {}'.format(SCIKIT_LEARN_PLATAFORM_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4028'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4141 AND 4147'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4028'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4141 AND 4147'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4041'),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4088 AND 4089'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4088 AND 4089'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4088 AND 4089'),

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
