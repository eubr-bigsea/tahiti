# -*- coding: utf-8 -*-
"""Fixing required fields

Revision ID: 8d2b3386d63f
Revises: 995d4fa1bfd0
Create Date: 2017-05-23 18:23:45.911491

"""
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '690a19ef85c0'
down_revision = '8d2b3386d63f'
branch_labels = None
depends_on = None


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String),
               )
    all_ops = (
        (82, 'execute-python', 1, 'TRANSFORMATION', 'fa-code'),
        (83, 'entity-matching', 1, 'TRANSFORMATION', 'fa-vcard-o'),
    )
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    all_ops = [
        (82, 'en', 'Execute Python code', 'Execute Python code'),
        (82, 'pt', 'Executar código Python', 'Executar código Python'),
        (83, 'en', 'Entity matching', 'Entity matching'),
        (83, 'pt', 'Resolução de entidades', 'Resolução de entidades'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    all_ops = [
        (82, 1),
        (83, 1),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String), )

    all_ops = [
        (177, 'INPUT', None, 82, 1, 'ONE'),
        (178, 'INPUT', None, 82, 2, 'ONE'),
        (179, 'OUTPUT', None, 82, 1, 'MANY'),
        (180, 'OUTPUT', None, 82, 1, 'MANY'),

        (181, 'INPUT', None, 83, 1, 'ONE'),
        (182, 'INPUT', None, 83, 2, 'ONE'),
        (183, 'OUTPUT', None, 83, 1, 'MANY'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    all_ops = [
        (177, 'en', 'input data 1', 'Input 1'),
        (178, 'en', 'input data 2', 'Input 2'),
        (179, 'en', 'output data 1', 'Output 1'),
        (180, 'en', 'output data 2', 'Output 2'),

        (177, 'pt', 'dados entrada 1', 'Entrada 1'),
        (178, 'pt', 'dados entrada 2', 'Entrada 2'),
        (179, 'pt', 'dados saída 1', 'Saída 1'),
        (180, 'pt', 'dados saída 2', 'Saída 2'),


        (181, 'en', 'input data 1', 'Input 1'),
        (182, 'en', 'input data 2', 'Input 2'),
        (183, 'en', 'output data 1', 'Output 1'),

        (181, 'pt', 'dados entrada 1', 'Entrada 1'),
        (182, 'pt', 'dados entrada 2', 'Entrada 2'),
        (183, 'pt', 'dados saída 1', 'Saída 1'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], operation))) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (177, 1),
        (178, 1),
        (179, 1),
        (180, 1),

        (181, 1),
        (182, 1),
        (183, 1),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (82, 13),
        (83, 13),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

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
        (97, 1, 1, 'execution'),
        (98, 1, 1, 'execution'),
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
        (82, 97),
        (82, 41),

        (83, 98),
        (83, 41),
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
        (97, 'en', 'Execution'),
        (97, 'pt', 'Execução'),

        (98, 'en', 'Execution'),
        (98, 'pt', 'Execução'),
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
        (229, 'code', 'TEXT', 1, 0,
         ('# Write your Python code here\n'
          '# Inputs are available as in1 and in2, '
          'outputs are out1 and out2'), 'code',
         None, None, 'EXECUTION', 97),

        (230, 'algorithm', 'TEXT', 1, 0,
         '', 'dropdown',
         None, '[{"key": "BULMA", "value": "Geospatial Data - Bulma"}]',
            'EXECUTION', 98),
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
        (229, 'en', 'Code', 'Code'),
        (229, 'pt', 'Código', 'Código'),

        (230, 'en', 'Algorithm', 'Algorithm'),
        (230, 'pt', 'Algoritmo', 'Algoritmo'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 82 AND 83'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 82 AND 83'),
    (_insert_operation_port, 'DELETE FROM operation_port '
                             'WHERE operation_id BETWEEN 82 AND 83'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port WHERE operation_id BETWEEN 82 AND 83)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN 82 AND 83)'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN 82 AND 83;'),
    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN 82 AND 83'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 97 AND 98'),
    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN 82 AND 83'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 97 AND 98'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id BETWEEN 97 AND 98'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id BETWEEN 97 AND 98)'),
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
