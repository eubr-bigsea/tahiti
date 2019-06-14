# coding=utf-8
"""Donut chart

Revision ID: 6e79129492af
Revises: 1732958a754a
Create Date: 2017-08-21 17:13:02.474400

"""
import json

from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '6e79129492af'
down_revision = '1732958a754a'
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
        (89, 'donut-chart', 1, 'TRANSFORMATION', 'fa-circle-o-notch '),
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
        (89, 'en', 'Donut chart', 'Donut chart'),
        (89, 'pt', 'Gráfico de rosca (donut)', 'Gráfico de rosca (donut)'),
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
        (89, 1),
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
        (197, 'INPUT', None, 89, 1, 'ONE', 'input data'),
        (198, 'OUTPUT', None, 89, 1, 'MANY', 'visualization'),

        # Freq itemset
        (199, 'OUTPUT', None, 3, 2, 'MANY', 'rules output'),
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
        (197, 'en', 'input data', 'Input data'),
        (198, 'en', 'visualization', 'Visualization'),

        (197, 'pt', 'dados de entrada', 'Dados de entrada'),
        (198, 'pt', 'visualização', 'Visualização'),

        # Freq itemset
        (199, 'en', 'rules output', 'Rules output'),
        (199, 'pt', 'saída das regras', 'Saída das regras'),
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
        (197, 1),
        (198, 19),

        (199, 1),
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
        (89, 15),
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
        (113, 1, 1, 'execution'),
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
        (89, 113),
        (89, 41),
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
        (113, 'en', 'Execution'),
        (113, 'pt', 'Execução'),
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
    columns = [c.name for c in tb.columns]

    data = [
        [338, 'value_attribute', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 113],
        [339, 'id_attribute', 'TEXT', 0, 2, None, 'attribute-selector', None,
         None, 'EXECUTION', 113],
        [340, 'title', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         113],
        [341, 'x_format', 'TEXT', 0, 7, None, 'select2', None,
         json.dumps(supported_formats), 'EXECUTION', 113],
        [342, 'x_prefix', 'TEXT', 0, 8, None, 'text', None, None, 'EXECUTION',
         113],
        [343, 'x_suffix', 'TEXT', 0, 9, None, 'text', None, None, 'EXECUTION',
         113],

        [345, 'x_title', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         113],

        # Freq itemset
        [344, 'min_confidence', 'FLOAT', 0, 2, '0.9', 'decimal', None, None,
         'EXECUTION', 3],
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
        [338, 'en', 'Attribute with value', 'Attribute with value'],
        [339, 'en', 'Optional label attribute (blank: use value as label',
         'Attribute used as label'],
        [340, 'en', 'Title', 'Title'],
        [341, 'en', 'X-axis values format',
         'Format to be applied to the values in X-axis'],
        [342, 'en', 'X-axis prefix (added to the value when displaying it)',
         'X-axis prefix (added to the value display)'],
        [343, 'en', 'X-axis suffix (added to the value when displaying it)',
         'X-axis suffix(added to the value display)'],

        [338, 'pt', 'Atributo com o valor', 'Atributo com o valor'],
        [339, 'pt',
         'Atributo usado como rótulo (vazio: usar o valor como rótulo)',
         'Atributo usado para o rótulo'],
        [340, 'pt', 'Título', 'Título'],
        [341, 'pt', 'Formato para eixo X', 'Formato para valores eixo X'],
        [342, 'pt', 'Prefixo para eixo X',
         'Prefixo para eixo X (adicionado ao valor ao exibi-lo)'],
        [343, 'pt', 'Sufixo para eixo X',
         'Sufixo para eixo X (adicionado ao valor ao exibi-lo)'],

        [344, 'en', 'Min. confidence (for rules generation)',
         'Min. confidence (for rules generation)'],
        [344, 'pt', 'Confiança mínima (para geração das regras)',
         'Confiança mínima (para geração das regras)'],

        [345, 'en', 'Inner title',
         'Inner title displayed in the center of the donut'],
        [345, 'pt', 'Título interno',
         'Título interno, exibido no centro.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 89 AND 89'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 89 AND 89'),
    (_insert_operation_port,
        'DELETE FROM operation_port '
        'WHERE (operation_id BETWEEN 89 AND 89) OR id = 199'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN 89 AND 89) OR id = 199)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE (operation_id BETWEEN 89 AND 89) OR id = 199)'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN 89 AND 89;'),
    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN 89 AND 89'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 113 AND 113'),
    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN 89 AND 89'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 113 AND 113'),
    (_insert_operation_form_field,
     """DELETE FROM operation_form_field
        WHERE (form_id BETWEEN 113 AND 113) OR (id = 344)"""),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE (form_id BETWEEN 113 AND 113) OR (id = 344))'),
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
            # print cmd[1]
            op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
