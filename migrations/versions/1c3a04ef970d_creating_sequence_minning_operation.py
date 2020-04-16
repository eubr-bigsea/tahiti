"""creating sequence minning operation

Revision ID: 1c3a04ef970d
Revises: 953911f74e49
Create Date: 2020-04-02 18:25:24.451967

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
revision = '1c3a04ef970d'
down_revision = '953911f74e49'
branch_labels = None
depends_on = None

SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4047

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

def _reinsert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')

    data = [
        (86, SCIKIT_LEARN_PLATAFORM_ID)
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
        (ID_OPERATION, "sequence-mining-model", 1, 'TRANSFORMATION', ''),
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
        (1, ID_OPERATION),
        (8, ID_OPERATION),
        (22, ID_OPERATION)
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
        (ID_OPERATION, "pt", 'Mineração de sequências', 'Mineração de sequências'),
        (ID_OPERATION, "en", 'Sequence mining', 'Sequence mining')
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
        (ID_OPERATION, 4046),  # own execution form
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
        column('category', String))

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        #Flatten
        (4046, 1, 1, 'execution'), #data_format
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
        (4046, 'en', 'Execution'),
        (4046, 'pt', 'Execução'),
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
        (4373, 'min_support', 'DECIMAL', 1, 1, 0.1, 'decimal', None, None, 'EXECUTION', 4046, None),
        (4374, 'max_pattern_length', 'INTEGER', 1, 2, 10, 'integer', None, None, 'EXECUTION', 4046, None),
        (4375, 'attrtibute', 'TEXT', 0, 3, None, 'attribute-selector', None,
	 json.dumps([
            {"key": "multiple", "value": "false"}
        ]), 'EXECUTION', 4046, None)
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
        (4373, 'en', 'Min. support', 'Min. support'),
        (4373, 'pt', 'Suporte mínimo', 'Suporte mínimo'),

        (4374, 'en', 'Max. sequence length', 'Max. sequence length'),
        (4374, 'pt', 'Tamanho máx. da sequência', 'Tamanho máx. da sequência'),

        (4375, 'en', 'Attribute with transactions (empty = first attribute)', 'Attribute with transactions (empty = first attribute)'),
        (4375, 'pt', 'Atributo com transações (vazio = primeiro atributo)', 'Atributo com transações (vazio = primeiro atributo)')

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
        (4103, 'INPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
        (4104, 'OUTPUT', '', 1, 'MANY', ID_OPERATION, 'output data')
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
        (4103, 1),
        (4104, 1)
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
        (4103, "en", 'input data', 'Input data'),
        (4103, "pt", 'dados de entrada', 'Dados de entrada'),
        (4104, "en", 'output data', 'Output data'),
        (4104, "pt", 'dados de saída', 'Dados de saída')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = {}'.format(ID_OPERATION)),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = {}'.format(ID_OPERATION)),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id IN ({})'.format(ID_OPERATION)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = {} AND platform_id = {}'.format(ID_OPERATION, SCIKIT_LEARN_PLATAFORM_ID)),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id=4046'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4373 AND 4375'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4046'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4373 AND 4375'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = {}'.format(ID_OPERATION)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4103 AND 4104'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4103 AND 4104'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4103 AND 4104'),

    ('DELETE FROM operation_platform where operation_id=86 and platform_id={}'.format(SCIKIT_LEARN_PLATAFORM_ID),
    _reinsert_operation_platform)

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
