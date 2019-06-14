# -*- coding: utf-8 -*-
"""New chart types

Revision ID: 1732958a754a
Revises: 223eb6c3933b
Create Date: 2017-08-18 12:07:18.598354

"""
import json

from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '1732958a754a'
down_revision = '223eb6c3933b'
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
        (87, 'plot-chart', 1, 'TRANSFORMATION', 'fa-lemon-o'),
        (88, 'map-chart', 1, 'TRANSFORMATION', 'fa-map-marker'),
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
        (87, 'en', 'Scatter plot chart', 'Scatter plot chart'),
        (87, 'pt', 'Gráfico de dispersão', 'Gráfico de dispersão'),
        (88, 'en', 'Map visualization', 'Map visualization'),
        (88, 'pt', 'Visualização em mapa', 'Visualização em mapa'),
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
        (87, 1),
        (88, 1),
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
        column('multiplicity', String),
        column('slug', String))

    all_ops = [
        (191, 'INPUT', None, 87, 1, 'ONE', 'input data'),
        (192, 'OUTPUT', None, 87, 1, 'MANY', 'visualization'),

        (193, 'INPUT', None, 88, 1, 'ONE', 'input data'),
        (194, 'OUTPUT', None, 88, 1, 'MANY', 'visualization'),
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
        (191, 'en', 'input data', 'Input data'),
        (192, 'en', 'visualization', 'Visualization'),

        (191, 'pt', 'dados entrada', 'Dados de entrada'),
        (192, 'pt', 'visualização', 'Visualização'),

        (193, 'en', 'input data', 'Input data'),
        (194, 'en', 'visualization', 'Visualization'),
        (193, 'pt', 'dados entrada', 'Dados de entrada'),
        (194, 'pt', 'visualização', 'Visualização'),

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
        (191, 1),
        (193, 1),

        (192, 19),
        (194, 19),
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
        (87, 15),
        (88, 15),
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
        (111, 1, 1, 'execution'),
        (112, 1, 1, 'execution'),
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
        (87, 111),
        (87, 41),

        (88, 112),
        (88, 41),
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
        (111, 'en', 'Execution'),
        (111, 'pt', 'Execução'),

        (112, 'en', 'Execution'),
        (112, 'pt', 'Execução'),
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

    supported_formats = [
        {"key": "%Y-%m-%dT%H:%M:%S.%LZ",
         "value": "%Y-%m-%dT%H:%M:%S.%LZ"},
        {"key": "%m-%d", "value": "%m-%d"},
        {"key": "%d-%", "value": "%d-%m"},
        {"key": "%Y-%m-%d", "value": "%Y-%m-%d"},
        {"key": "%m-%Y-%d", "value": "%m-%Y-%d"},
        {"key": "%m-%Y-%d", "value": "%m-%Y-%d"},
        {"key": "%m-%Y-%d %H:%M",
         "value": "%m-%Y-%d %H:%M"},
        {"key": "%m-%Y-%d %H:%M",
         "value": "%m-%Y-%d %H:%M"},
        {"key": "%m-%Y-%d %H:%M:%S", "value": "%m-%Y-%d %H:%M:%S"},
        {"key": "%m-%Y-%d %H:%M:%S",
         "value": "%m-%Y-%d %H:%M:%S"},
        {"key": "%H:%M", "value": "%H:%M"},
        {"key": "%H:%M:%S", "value": "%H:%M:%S"},

        {"key": ".2", "value": ".2"},
        {"key": ".4", "value": ".4"},
        {"key": "%", "value": "%"},
        {"key": "p", "value": "p"},
        {"key": "d", "value": "d"}
    ]

    map_types = [
        {"key": "bar", "value": "bar"},
        {"key": "points", "value": "points"},
        {"key": "heatmap", "value": "heatmap"},
    ]
    columns = [c.name for c in tb.columns]
    data = [
        [279, 'series_attribute', 'TEXT', 1, 4, None, 'attribute-selector',
         None, None, 'EXECUTION', 111],

        [311, 'x_axis_attribute', 'TEXT', 1, 0, None, 'attribute-selector',
         None, None, 'EXECUTION', 111],
        [312, 'y_axis_attribute', 'TEXT', 1, 1, None, 'attribute-selector',
         None, None, 'EXECUTION', 111],
        [313, 'z_axis_attribute', 'TEXT', 0, 2, None, 'attribute-selector',
         None, None, 'EXECUTION', 111],
        [314, 't_axis_attribute', 'TEXT', 0, 3, None, 'attribute-selector',
         None, None, 'EXECUTION', 111],

        [315, 'x_title', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION',
         111],
        [316, 'y_title', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION',
         111],
        [317, 'z_title', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION',
         111],
        [318, 't_title', 'TEXT', 0, 7, None, 'text', None, None, 'EXECUTION',
         111],

        [319, 'x_format', 'TEXT', 0, 8, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION',
         111],
        [320, 'y_format', 'TEXT', 0, 9, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION',
         111],
        [321, 'z_format', 'TEXT', 0, 10, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION',
         111],
        [322, 't_format', 'TEXT', 0, 11, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION',
         111],

        [323, 'x_prefix', 'TEXT', 0, 12, None, 'text', None, None, 'EXECUTION',
         111],
        [324, 'y_prefix', 'TEXT', 0, 13, None, 'text', None, None, 'EXECUTION',
         111],
        [325, 'z_prefix', 'TEXT', 0, 14, None, 'text', None, None, 'EXECUTION',
         111],
        [326, 't_prefix', 'TEXT', 0, 15, None, 'text', None, None, 'EXECUTION',
         111],

        [327, 'x_suffix', 'TEXT', 0, 16, None, 'text', None, None, 'EXECUTION',
         111],
        [328, 'y_suffix', 'TEXT', 0, 17, None, 'text', None, None, 'EXECUTION',
         111],
        [329, 'z_suffix', 'TEXT', 0, 18, None, 'text', None, None, 'EXECUTION',
         111],
        [330, 't_suffix', 'TEXT', 0, 19, None, 'text', None, None, 'EXECUTION',
         111],

        [331, 'title', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         111],

        [332, 'type', 'TEXT', 0, 0, 'points', 'dropdown', None,
         json.dumps(map_types), 'EXECUTION', 112],
        [333, 'latitude', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
         'EXECUTION',
         112],
        [334, 'longitude', 'TEXT', 0, 2, None, 'attribute-selector', None, None,
         'EXECUTION',
         112],
        [335, 'value', 'TEXT', 0, 3, None, 'attribute-selector', None, None,
         'EXECUTION',
         112],
        [336, 'label', 'TEXT', 0, 4, None, 'attribute-selector', None, None,
         'EXECUTION',
         112],
        [337, 'title', 'TEXT', 0, 0, None, 'text', None, None, 'EXECUTION',
         112],

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
        [279, 'en', 'Attribute used for series (optional)',
         'Attribute used for series (optional)'],
        [279, 'pt', 'Atributo usado para séries', 'Atributo usado para séries'],

        [311, 'en', 'X-axis attribute', 'X-axis attribute'],
        [311, 'pt', 'Atributo para eixo X', 'Atributo para eixo X'],
        [312, 'en', 'Y-axis attribute', 'Y-axis attribute'],
        [312, 'pt', 'Atributo para eixo Y', 'Atributo para eixo Y'],
        [313, 'en', 'Z-axis attribute (optional)', 'Z-axis attribute'],
        [313, 'pt', 'Atributo para eixo Z (opcional)', 'Atributo para eixo Z'],
        [314, 'en', 'Size attribute (optional)', 'Size attribute'],
        [314, 'pt', 'Atributo para tamanho (opcional)',
         'Atributo para tamanho'],

        [315, 'en', 'X-axis title', 'X-axis title'],
        [315, 'pt', 'Título para o eixo X', 'Título para o eixo X'],
        [316, 'en', 'Y-axis title', 'Y-axis title'],
        [316, 'pt', 'Título para o eixo Y', 'Título para o eixo Y'],
        [317, 'en', 'Z-axis title(optional)', 'Z-axis title'],
        [317, 'pt', 'Título para o eixo Z (opcional)',
         'Título para o eixo Z'],
        [318, 'en', 'Size title (optional)', 'Size title'],
        [318, 'pt', 'Título para o tamanho (opcional)',
         'Título para o tamanho'],

        [319, 'en', 'X-axis format', 'X-axis format'],
        [319, 'pt', 'Formato para eixo X', 'Formato para eixo X'],
        [320, 'en', 'Y-axis format', 'Y-axis format'],
        [320, 'pt', 'Formato para eixo Y', 'Formato para eixo Y'],
        [321, 'en', 'Z-axis format(optional)', 'Z-axis format'],
        [321, 'pt', 'Formato para eixo Z (opcional)', 'Formato para eixo Z'],
        [322, 'en', 'Size format(optional)', 'Size format'],
        [322, 'pt', 'Formato para tamanho (opcional)',
         'Formato para tamanho'],

        [323, 'en', 'X-axis prefix', 'X-axis prefix'],
        [323, 'pt', 'Prefixo para eixo X', 'Prefixo para eixo X'],
        [324, 'en', 'Y-axis prefix', 'Y-axis fprefix'],
        [324, 'pt', 'Prefixo para eixo Y', 'Prefixo para eixo Y'],
        [325, 'en', 'Z-axis prefix(optional)', 'Z-axis prefix'],
        [325, 'pt', 'Prefixo para eixo Z (opcional)', 'Prefixo para eixo Z'],
        [326, 'en', 'Size prefix(optional)', 'Size prefix'],
        [326, 'pt', 'Prefixo para tamanho (opcional)',
         'Prefixo para tamanho'],

        [327, 'en', 'X-axis suffix', 'X-axis suffix'],
        [327, 'pt', 'Sufixo para eixo X', 'Sufixo para eixo X'],
        [328, 'en', 'Y-axis suffix', 'Y-axis suffix'],
        [328, 'pt', 'Sufixo para eixo Y', 'Sufixo para eixo Y'],
        [329, 'en', 'Z-axis suffix(optional)', 'Z-axis suffix'],
        [329, 'pt', 'Sufixo para eixo Z (opcional)', 'Sufixo para eixo Z'],
        [330, 'en', 'Size suffix(optional)', 'Size suffix'],
        [330, 'pt', 'Sufixo para tamanho (opcional)',
         'Sufixo para tamanho'],

        [331, 'en', 'Title', 'Title'],
        [331, 'pt', 'Título', 'Título'],

        [332, 'en', 'Map type', 'Map type'],
        [332, 'pt', 'Tipo de mapa', 'Tipo de mapa'],
        [333, 'en', 'Attribute with the latitude',
         'Attribute with the latitude'],
        [333, 'pt', 'Atributo com a latitude', 'Atributo com a latitude'],
        [334, 'en', 'Attribute with the longitude',
         'Attribute with the longitude'],
        [334, 'pt', 'Atributo com a longitude', 'Atributo com a longitude'],
        [335, 'en', 'Attribute for the value (optional)',
         'Attribute for the value (optional)'],
        [335, 'pt', 'Atributo usado para o valor (opcional)',
         'Atributo usado para o valor (opcional)'],
        [336, 'en', 'Label attribute (optional)', 'Label attribute (optional)'],
        [336, 'pt', 'Atributo para rótulo (opcional)',
         'Atributo para rótulo (opcional)'],
        [337, 'en', 'Title', 'Title'],
        [337, 'pt', 'Título', 'Título'],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 87 AND 88'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 87 AND 88'),
    (_insert_operation_port, 'DELETE FROM operation_port '
                             'WHERE operation_id BETWEEN 87 AND 88'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port WHERE operation_id BETWEEN 87 AND 88)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN 87 AND 88)'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN 87 AND 88;'),
    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN 87 AND 88'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 111 AND 112'),
    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN 87 AND 88'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 111 AND 112'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE form_id BETWEEN 111 AND 112'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id BETWEEN 111 AND 112)'),
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
