# -*- coding: utf-8 -*-
"""empty message

Revision ID: b2b823fe47b1
Revises: 74349d2f1936
Create Date: 2017-06-02 17:25:45.929892

"""
from alembic import op
import sqlalchemy as sa

from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = 'b2b823fe47b1'
down_revision = '74349d2f1936'
branch_labels = None
depends_on = None


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (99, 1, 1, 'execution'),
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
        (81, 99),
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
        (99, 'en', 'Execution'),
        (99, 'pt', 'Execução'),
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
        (231, 'title', 'TEXT', 1, 1,
         '', 'text', None, None, 'EXECUTION', 99),

        (232, 'attributes', 'TEXT', 1, 2,
         '', 'attribute-selector', None, None,
         'EXECUTION', 99),
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
        (231, 'en', 'Title', 'Title'),
        (231, 'pt', 'Título', 'Título'),

        (232, 'en', 'Attributes (empty=all)', 'Attributes'),
        (232, 'pt', 'Atributos (vazio=todos)', 'Atributos'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 99 AND 99'),
    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN 81 AND 81 '
                                       'AND operation_form_id <> 41 '),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 99 AND 99'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id BETWEEN 99 AND 99'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id BETWEEN 99 AND 99)'),
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
            op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
