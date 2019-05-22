# -*- coding: utf-8 -*-
"""Update the operation Convert Categorical to Numeric and create a new operation Vector Indexer.

Revision ID: 8a4558f255a4
Revises: 2232f498d42e
Create Date: 2019-02-26 11:12:07.685379

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '8a4558f255a4'
down_revision = '5bfa53aaa86d'
branch_labels = None
depends_on = None

SPARK_PLATAFORM_ID = 1


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer), )

    columns = ('id', 'slug', 'enabled', 'type', 'icon')
    data = [
        (122, "vector-indexer", 1, 'ACTION', ''),
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
        (32, 122),
        (33, 122),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    data = [
        (122, SPARK_PLATAFORM_ID),  # Vector indexer

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
        (122, "en", 'Vector indexer',
         'Indexing categorical features represented in a Vector.'),
        (122, "pt", 'Indexador de vetor',
         'Indexa categorical features representadas por um vetor.'),
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
        column('slug', String), )

    columns = (
        'id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        (292, 'INPUT', '', 1, 'ONE', 122, 'input data'),
        (293, 'OUTPUT', '', 1, 'MANY', 122, 'output data'),
        (294, 'OUTPUT', '', 2, 'MANY', 122, 'indexer models'),
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
        (292, 1),
        (293, 1),
        (294, 4),
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
        (
            292, "en", 'input data',
            'Data set with feature columns to be indexed'),
        (292, "pt", 'dados de entrada',
         'Conjunto de dados com atributos a serem indexados'),
        (293, "en", 'output data', 'Output data with new indexed column'),
        (
            293, "pt", 'dados de saída',
            'Dados de saída com nova coluna indexada'),
        (294, "en", 'model', 'Indexer model generated'),
        (294, "pt", 'modelo', 'Modelo de indexação gerado'),
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
        (131, 1, 1, 'execution'),
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
        (131, 'en', 'Execution'),
        (131, 'pt', 'Execução'),
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
        (122, 41),
        (122, 131),
        (122, 110),  # results
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
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [

        (484, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 131),
        (485, 'alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION',
         131),
        (486, 'max_categories', 'INTEGER', 0, 3, '20', 'integer',
         None, None, 'EXECUTION', 131),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_downgrade_operation_form_field():
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
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [

        (94, "indexer_type", "TEXT", 1, 2, None, "dropdown", None,
         '[{"en": "String", "key": "string", "value": "String", "pt": "String"}, '
         '{"en": "Vector", "key": "vector", "value": "Vector", "pt": "Vetor"}]',
         "EXECUTION", 50),
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

        (484, 'en', 'Attributes', 'Attributes (features) to be indexed'),
        (484, 'pt', 'Atributos', 'Atributos (features) a ser indexados'),
        (485, 'en', 'Name for new indexed attribute(s)',
         'Name for new indexed attribute(s)'),
        (485, 'pt', 'Nome para novo(s) atributo(s) indexado(s)',
         'Nome para novo(s) atributo(s) indexado(s)'),
        (486, 'en', 'Max categories (threshold)',
         'Threshold for the number of values a categorical feature can take '
         '(>= 2). If a feature is found to have > maxCategories values, '
         'then it is declared continuous.'),
        (486, 'pt', 'Quantidade máxima de categorias',
         'Limite para a quantidade de valores que feature categórica pode ter '
         '(>= 2). Se uma feature tem mais categorias que esse valor, '
         'ela é declarada contínua.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id = 122'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id = 122'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id = 122'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id = 122 AND platform_id = {}'.format(
         SPARK_PLATAFORM_ID)),
    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 292 AND 294'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 292 AND 294'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 292 AND 294'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 131 AND 131'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 131 AND 131'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 122'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 484 and 486'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 484 '
     'and 486'),

    ('UPDATE operation_port_translation '
     'SET name = "models" '
     'WHERE id = 89 AND locale = "en"',
     'UPDATE operation_port_translation '
     'SET name = "indexer models" '
     'WHERE id = 89 AND locale = "en"'),
    ('UPDATE operation_port_translation '
     'SET name = "modelos" '
     'WHERE id = 89 AND locale = "pt"',
     'UPDATE operation_port_translation '
     'SET name = "modelos do indexador" '
     'WHERE id = 89 AND locale = "pt"'),
    ('UPDATE operation_port '
     'SET slug = "models" '
     'WHERE id = 89 AND operation_id = 40',
     'UPDATE operation_port '
     'SET slug = "indexer models" '
     'WHERE id = 89 AND operation_id = 40'),
    ('UPDATE operation_form_field '
     'SET form_id = 130 '
     'WHERE id = 96',
     'UPDATE operation_form_field '
     'SET form_id = 50 '
     'WHERE id = 96'),
    ('UPDATE operation_form_field_translation '
     'SET label = "Max. categories", help = "Max. categories" '
     'WHERE id = 96 AND locale = "en"',
     'UPDATE operation_form_field_translation '
     'SET label = "Max. categories (vector only)", help = "Max. categories (vector only)" '
     'WHERE id = 96 AND locale = "en"'),
    ('UPDATE operation_form_field_translation '
     'SET label = "Máx. categorias", help = "Máx. categorias" '
     'WHERE id = 96 AND locale = "pt"',
     'UPDATE operation_form_field_translation '
     'SET label = "Máx. categorias (vetor apenas)", help = "Máx. categorias (vetor apenas)" '
     'WHERE id = 96 AND locale = "pt"'),

    ('DELETE FROM operation_form_field_translation '
     'WHERE id = 94 AND locale = "en"',
     'INSERT INTO operation_form_field_translation '
     '(`id`, `locale`, `label`, `help`) VALUES (94, "en", "Indexer type", "Indexer type")'),

    ('DELETE FROM operation_form_field_translation '
     'WHERE id = 94 AND locale = "pt"',
     'INSERT INTO operation_form_field_translation '
     '(`id`, `locale`, `label`, `help`) VALUES (94, "pt", "Tipo de indexador", "Tipo de indexador")'),

    ('DELETE FROM operation_form_field '
     'WHERE id = 94 AND form_id = 50',
     _insert_downgrade_operation_form_field),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    connection.execute('SET FOREIGN_KEY_CHECKS=0;')
    try:
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    session.commit()
