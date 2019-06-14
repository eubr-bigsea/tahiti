# -*- coding: utf-8 -*-
"""frequent items operations

Revision ID: 146dc5127e5e
Revises: 70078039a87a
Create Date: 2017-07-20 11:06:20.366248

"""

from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.sql import table, column, text
import collections

# revision identifiers, used by Alembic.
revision = '146dc5127e5e'
down_revision = '70078039a87a'
branch_labels = None
depends_on = None

ASSOCIATION_RULES_ID = 85
ASSOCIATION_RULES_FORM_ID = 108

SEQUENCE_MINING_ID = 86
SEQUENCE_MINING_FORM_ID = 109


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (ASSOCIATION_RULES_ID, 'association-rules', 1, 'TRANSFORMATION',
         'fa-long-arrow-right'),
        (SEQUENCE_MINING_ID, 'sequence-mining', 1, 'TRANSFORMATION',
         'fa-diamond'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )
    columns = [c.name for c in tb.columns]
    data = [
        (ASSOCIATION_RULES_ID, 'en', 'Association rules', 'Association rules'),
        (ASSOCIATION_RULES_ID, 'pt', 'Regras de associação',
         'Regras de associação'),
        (SEQUENCE_MINING_ID, 'en', 'Sequence mining', 'Sequence mining'),
        (SEQUENCE_MINING_ID, 'pt', 'Mineração de sequências',
         'Mineração de sequências'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        (ASSOCIATION_RULES_ID, 1),
        (SEQUENCE_MINING_ID, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (ASSOCIATION_RULES_FORM_ID, 1, 1, 'execution'),
        (SEQUENCE_MINING_FORM_ID, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (ASSOCIATION_RULES_ID, ASSOCIATION_RULES_FORM_ID),
        (ASSOCIATION_RULES_ID, 41),
        (SEQUENCE_MINING_ID, SEQUENCE_MINING_FORM_ID),
        (SEQUENCE_MINING_ID, 41),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String)
    )

    columns = [c.name for c in tb.columns]
    data = [
        (ASSOCIATION_RULES_FORM_ID, 'en', 'Execution'),
        (ASSOCIATION_RULES_FORM_ID, 'pt', 'Execução'),

        (SEQUENCE_MINING_FORM_ID, 'en', 'Execution'),
        (SEQUENCE_MINING_FORM_ID, 'pt', 'Execução'),
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

    columns = [c.name for c in tb.columns]

    data = [
        (286, 'confidence', 'DECIMAL', 1, 1, '0.9', 'decimal',
         None, None, 'EXECUTION', ASSOCIATION_RULES_FORM_ID),
        (287, 'rules_count', 'INTEGER', 1, 2, '200', 'integer',
         None, None, 'EXECUTION', ASSOCIATION_RULES_FORM_ID),

        (288, 'min_support', 'INTEGER', 1, 1, '0.1', 'integer',
         None, None, 'EXECUTION', SEQUENCE_MINING_FORM_ID),
        (289, 'max_pattern_length', 'INTEGER', 1, 2, '10', 'integer',
         None, None, 'EXECUTION', SEQUENCE_MINING_FORM_ID),

        (290, 'attribute', 'TEXT', 0, 3, None, 'attribute-selector', None, None,
         'EXECUTION', ASSOCIATION_RULES_FORM_ID),
        (291, 'attribute', 'TEXT', 0, 3, None, 'attribute-selector', None, None,
         'EXECUTION', SEQUENCE_MINING_FORM_ID)

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

    columns = [c.name for c in tb.columns]
    data = [
        (286, 'en', 'Min. confidence', 'Min. confidence'),
        (286, 'pt', 'Confiança mímina', 'Confiança mímina'),

        (287, 'en', 'Number of rules to generate',
         'Number of rules to generate'),
        (287, 'pt', 'Quantidade de regras a serem geradas',
         'Quantidade de regras a serem geradas'),

        (288, 'en', 'Min. support', 'Min. support'),
        (288, 'pt', 'Suporte mínimo', 'Suporte mínimo'),

        (289, 'en', 'Max. sequence length', 'Max. sequence length'),
        (289, 'pt', 'Tamanho máx. da sequência', 'Tamanho máx. da sequência'),

        (290, 'en', 'Attribute with transactions (empty = first attribute)',
         ' Attribute with transactions (empty = first attribute)'),

        (290, 'pt', 'Atributo com transações (vazio = primeiro atributo)',
         'Atributo com transações (vazio = primeiro atributo)'),

        (291, 'en', 'Attribute with transactions (empty = first attribute)',
         ' Attribute with transactions (empty = first attribute)'),

        (291, 'pt', 'Atributo com transações (vazio = primeiro atributo)',
         'Atributo com transações (vazio = primeiro atributo)'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (ASSOCIATION_RULES_ID, 1),
        (ASSOCIATION_RULES_ID, 8),
        (ASSOCIATION_RULES_ID, 22),

        (SEQUENCE_MINING_ID, 1),
        (SEQUENCE_MINING_ID, 8),
        (SEQUENCE_MINING_ID, 22),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


#
def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (187, 'OUTPUT', None, ASSOCIATION_RULES_ID, 1, 'MANY', 'output data'),
        (188, 'INPUT', None, ASSOCIATION_RULES_ID, 1, 'ONE', 'input data'),
        (189, 'OUTPUT', None, SEQUENCE_MINING_ID, 1, 'MANY', 'output data'),
        (190, 'INPUT', None, SEQUENCE_MINING_ID, 1, 'ONE', 'input data')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (187, 'en', 'output data', 'Output data'),
        (187, 'pt', 'dados de saída', 'Dados de saída'),
        (188, 'en', 'input data', 'Input data'),
        (188, 'pt', 'dados de entrada', 'Dados de entrada'),

        (189, 'en', 'output data', 'Output data'),
        (189, 'pt', 'dados de saída', 'Dados de saída'),
        (190, 'en', 'input data', 'Input data'),
        (190, 'pt', 'dados de entrada', 'Dados de entrada'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = [c.name for c in tb.columns]
    data = [
        (187, 1),
        (188, 1),
        (189, 1),
        (190, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id IN ({}, {})'.format(
         ASSOCIATION_RULES_ID, SEQUENCE_MINING_ID)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id IN ({}, {})'.format(
         ASSOCIATION_RULES_ID, SEQUENCE_MINING_ID)),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE platform_id = 1 AND operation_id IN ({}, {})'.format(
         ASSOCIATION_RULES_ID, SEQUENCE_MINING_ID)),
    (_insert_operation_category_operation,
     'DELETE from operation_category_operation '
     'WHERE operation_id IN ({}, {})'.format(ASSOCIATION_RULES_ID,
                                             SEQUENCE_MINING_ID)),
    (_insert_operation_port,
     "DELETE FROM operation_port WHERE id in (187, 188, 189, 190)"),
    (_insert_operation_port_translation,
     "DELETE FROM operation_port_translation WHERE id in (187, 188, 189, 190)"),

    (_insert_operation_port_interface_operation_port,
     "DELETE FROM operation_port_interface_operation_port "
     "WHERE operation_port_id in (187, 188, 189, 190)"),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN ({0}, {1})'.format(
         ASSOCIATION_RULES_FORM_ID, SEQUENCE_MINING_FORM_ID)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0}, {1})'.format(ASSOCIATION_RULES_ID,
                                               SEQUENCE_MINING_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation  WHERE id IN ({0}, {1})'.format(
         ASSOCIATION_RULES_FORM_ID, SEQUENCE_MINING_FORM_ID)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id IN ({0}, {1})'.format(
         ASSOCIATION_RULES_FORM_ID, SEQUENCE_MINING_FORM_ID)),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ({0}, {1}))'.format(ASSOCIATION_RULES_FORM_ID,
                                              SEQUENCE_MINING_FORM_ID)),
]


def upgrade():
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in all_commands:
            cmd[0]()
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise


def downgrade():
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], collections.Callable):
                cmd[1]()
            else:
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
