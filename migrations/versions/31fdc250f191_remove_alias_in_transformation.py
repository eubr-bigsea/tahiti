# coding=utf-8
"""remove_alias_in_transformation

Revision ID: 31fdc250f191
Revises: 47830b97d8d8
Create Date: 2018-04-11 15:08:22.254171

"""
import json

import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '31fdc250f191'
down_revision = '47830b97d8d8'
branch_labels = None
depends_on = None

ALIAS_ATTRIBUTE_ID = 89
ADVANCED_EXPRESSION_ATTRIBUTE_ID = 2


def _add_columns():
    op.add_column('task', sa.Column(
        'enabled', sa.Boolean(), nullable=False,
        server_default=sa.schema.DefaultClause("1")))


def _remove_columns():
    op.drop_column('task', 'enabled')


def _do_insert_operation_form_field(data):
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
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _re_insert_operation_form_field():
    _do_insert_operation_form_field([
        (ALIAS_ATTRIBUTE_ID, 'alias', 'TEXT', 1, 0, None, 'text',
         None, None, 'EXECUTION', 7),
    ])


def _do_insert_operation_form_field_translation(data):
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _re_insert_operation_form_field_translation():
    _do_insert_operation_form_field_translation([
        (ALIAS_ATTRIBUTE_ID, 'en', 'Name for transformed attribute',
         'Name for transformed attribute.'),
        (ALIAS_ATTRIBUTE_ID, 'pt', 'Nome do atributo transformado',
         'Escolha um ou mais atributos. Esses atributos serão selecionados '
         'para a saída da fonte de dados.'),
    ])


def _insert_operation_form_field():
    params = {"alias": False}
    _do_insert_operation_form_field([
        (ADVANCED_EXPRESSION_ATTRIBUTE_ID, 'expression',
         'TEXT', 1, 0, None, 'expression',
         None, json.dumps(params), 'EXECUTION', 5),
    ])


def _insert_operation_form_field_translation():
    _do_insert_operation_form_field_translation([
        (ADVANCED_EXPRESSION_ATTRIBUTE_ID, 'en', 'Filter expression (advanced)',
         'Filter expression (advanced).'),
        (ADVANCED_EXPRESSION_ATTRIBUTE_ID, 'pt', 'Expressão para filtro (avançado).',
         'Permite especificar uma expressão para filtrar os dados.'),
    ])


all_commands = [
    (_add_columns, _remove_columns),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN ({})'.format(
         ADVANCED_EXPRESSION_ATTRIBUTE_ID),
     ),

    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN ({})'.format(
         ADVANCED_EXPRESSION_ATTRIBUTE_ID),
     ),

    ('DELETE FROM operation_form_field_translation WHERE id IN ({})'.format(
        ALIAS_ATTRIBUTE_ID),
     _re_insert_operation_form_field_translation),

    ('DELETE FROM operation_form_field WHERE id IN ({})'.format(
        ALIAS_ATTRIBUTE_ID),
     _re_insert_operation_form_field,),

    ("UPDATE operation_form_field SET `values` ='' WHERE id = 88",
     "UPDATE operation_form_field SET `values` ='' WHERE id = 88",)
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
    connection.execute('SET foreign_key_checks = 0;')

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
    connection.execute('SET foreign_key_checks = 1;')
    session.commit()
