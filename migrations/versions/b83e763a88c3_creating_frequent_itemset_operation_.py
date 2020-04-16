"""creating frequent itemset operation sklearn

Revision ID: b83e763a88c3
Revises: 1c3a04ef970d
Create Date: 2020-04-14 11:36:27.963701

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
revision = 'b83e763a88c3'
down_revision = '1c3a04ef970d'
branch_labels = None
depends_on = None

SCIKIT_LEARN_PLATAFORM_ID = 4
ID_OPERATION = 4048

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
        (3, SCIKIT_LEARN_PLATAFORM_ID)
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
        (ID_OPERATION, "frequent-item-set-model", 1, 'TRANSFORMATION', ''),
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
        (ID_OPERATION, "pt", 'Mineração de itemsets frequentes', 'Identifica conjuntos de itens frequentes em transações'),
        (ID_OPERATION, "en", 'Frequent itemsets mining', 'Identifies frequent itemsets in transactions')
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
        (ID_OPERATION, 4047),  # own execution form
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
        (4047, 1, 1, 'execution'), #data_format
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
        (4047, 'en', 'Execution'),
        (4047, 'pt', 'Execução'),
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
        (4376, 'min_support', 'DECIMAL', 1, 1, None, 'decimal', None, None, 'EXECUTION', 4047, None),
        (4378, 'min_confidence', 'DECIMAL', 0, 3, 0.9, 'decimal', None, None, 'EXECUTION', 4047, None),
        (4377, 'attrtibute', 'TEXT', 0, 2, None, 'attribute-selector', None,
	 json.dumps([
            {"key": "multiple", "value": "false"}
        ]), 'EXECUTION', 4047, None)
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
        (4376, 'en', 'Min. support', 'The minimum support for an itemset to be identified as frequent. For example, if an item appears 3 out of 5 transactions, it has a support of 3/5=0.6.'),
        (4376, 'pt', 'Suporte mínimo', 'Suporte mínimo'),

        (4378, 'en', 'Min. confidence (for rules generation)', 'Min. confidence (for rules generation).'),
        (4378, 'pt', 'Confiança mínima (para geração das regras)', 'Confiança mínima (para geração das regras).'),

        (4377, 'en', 'Attribute with transactions (empty = first attribute)', 'Attribute with transactions (empty = first attribute).'),
        (4377, 'pt', 'Atributo com transações (vazio = primeiro atributo)', 'Atributo com transações (vazio = primeiro atributo).')

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
        (4105, 'OUTPUT', '', 1, 'MANY', ID_OPERATION, 'output data'),
        (4106, 'INPUT', '', 1, 'ONE', ID_OPERATION, 'input data'),
        (4107, 'OUTPUT', '', 2, 'MANY', ID_OPERATION, 'rules output')	
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
        (4105, 1),
        (4106, 1),
        (4107, 1)	
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
        (4107, "en", 'rules output', 'Rules output'),
        (4107, "pt", 'saída das regras', 'Saída das regras'),	
        (4106, "en", 'input data', 'Input data'),
        (4106, "pt", 'dados de entrada', 'Dados de entrada'),
        (4105, "en", 'output data', 'Output data'),
        (4105, "pt", 'dados de saída', 'Dados de saída')
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
     'DELETE FROM operation_form WHERE id=4047'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4376 AND 4378'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id=4047'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4376 AND 4378'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = {}'.format(ID_OPERATION)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 4105 AND 4107'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 4105 AND 4107'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 4105 AND 4107'),

    ('DELETE FROM operation_platform where operation_id=3 and platform_id={}'.format(SCIKIT_LEARN_PLATAFORM_ID),
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
