""" new_visualizations_2020  

Revision ID: c95ef59cb317
Revises: 124773e2d0b1
Create Date: 2020-07-10 16:40:31.925542

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
import sqlalchemy as sa
import json

# revision identifiers, used by Alembic.
revision = 'c95ef59cb317'
down_revision = '124773e2d0b1'
branch_labels = None
depends_on = None

BASE_FORM_ID = 141
BASE_FORM_FIELD_ID = 528
BASE_PORT_ID = 307
MODE_ID = 567

INDICATOR = 130
MARKDOWN = 131
WORD_CLOUD = 132
HEATMAP = 133
BUBBLE_CHART = 134
FORCE_DIRECT = 135
IFRAME = 136
TREEMAP = 137

ALL_OPS = [INDICATOR, MARKDOWN, WORD_CLOUD, HEATMAP, 
        BUBBLE_CHART, FORCE_DIRECT, IFRAME, TREEMAP]

def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', String),
        column('type', String), 
        column('icon', String), 
        column('css_class', String), 
        )

    rows = [
            (INDICATOR, 'indicator', 1, 'TRANSFORMATION', ' ', None),
            (MARKDOWN, 'markdown', 1, 'TRANSFORMATION', ' ', None),
            (WORD_CLOUD, 'word-cloud', 1, 'TRANSFORMATION', ' ', None),
            (HEATMAP, 'heatmap', 1, 'TRANSFORMATION', ' ', None),
            (BUBBLE_CHART, 'bubble-chart', 1, 'TRANSFORMATION', ' ', None),
            (FORCE_DIRECT, 'force-direct', 1, 'TRANSFORMATION', ' ', None),
            (IFRAME, 'iframe', 1, 'TRANSFORMATION', ' ', None),
            (TREEMAP, 'treemap', 1, 'TRANSFORMATION', ' ', None),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)

def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (INDICATOR, 'en', 'Gauge',
         'Allows to display a value as a gauge or a "big number" in a dashboard.'),
        (INDICATOR, 'pt', 'Medidor',
         'Permite exibir um valor como um medidor ou um "número grande" em um dashboard.'),

        (MARKDOWN, 'en', 'Markdown text',
         'Allows to display a value as a gauge or a "big number" in a dashboard.'),
        (MARKDOWN, 'pt', 'Texto em Markdown',
         'Permite exibir um valor como um medidor ou um "número grande" em um dashboard.'),

        (WORD_CLOUD, 'en', 'Word cloud',
         'Generates a word cloud from a textual attribute.'),
        (WORD_CLOUD, 'pt', 'Nuvem de palavras',
         'Gera uma nuvem de palavras a partir de um atributo textual.'),

        (HEATMAP, 'en', 'Heatmap',
         'Heatmaps use colors to represent values (density) in a form of a matrix/table.'),
        (HEATMAP, 'pt', 'Mapa de calor',
            'Mapas de calor usam cores para representar valores (densidades) na forma de uma matriz/tabela.'),

        (BUBBLE_CHART, 'en', 'Bubble chart',
         'Bubble charts represent data using bubbles in a (x, y) plan. Size of bubbles represents a third dimension.'),
        (BUBBLE_CHART, 'pt', 'Gráfico de bolhas',
         'Gráficos de bolha representam dados usando bolhas em um plano (x, y). O tamanho das bolhas representa uma terceira dimensão.'),
  
        (FORCE_DIRECT, 'en', 'Network graphs',
         'Displays graphs (nodes and edges) using force direct algorithm.'),
        (FORCE_DIRECT, 'pt', 'Gráfico de rede',
         'Exibe grafos (nós e arestas) usando um algortimo de força direta (repulsão e atração).'),

        (IFRAME, 'en', 'HTML iframe',
         'Uses a HTML element called iframe to embed an external page into the result.'),
        (IFRAME, 'pt', 'Iframe HTML',
         'Usa um elemento HTML chamado iframe para embutir uma página externa no resultado.'),
        
        (TREEMAP, 'en', 'Treemap',
         'Treemaps display the relationship between items using sizing and color coding in a set of nested rectangles.'),
        (TREEMAP, 'pt', 'Treemap',
         'Treemaps mostram os relacionamentos entre itens usando codificação de tamanho e cores em um conjunto de retângulos aninhados.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [(op_id, 1) for op_id in ALL_OPS]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

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

    new_id = BASE_PORT_ID
    rows = []
    for op_id in ALL_OPS:
        new_id += 1
        rows.append([new_id, 'OUTPUT', None, op_id, 1, 'MANY', 'visualization'])

        if op_id not in [MARKDOWN, IFRAME]:
            new_id += 1
            rows.append([new_id, 'INPUT', None, op_id, 1, 'ONE', 'input data'])

    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]
    op.bulk_insert(tb, rows)
    
def _insert_operation_port_translation():    

    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )
    new_id = BASE_PORT_ID
    data = []
    for op_id in ALL_OPS:
        new_id += 1
        data.append([new_id, 'en', 'visualization', 'Visualization'])
        data.append([new_id, 'pt', 'visualização', 'Visualização'])

        if op_id not in [MARKDOWN, IFRAME]:
            new_id += 1
            data.append([new_id, 'en', 'input data', 'Input data'])
            data.append([new_id, 'pt', 'dados de entrada', 'Dados de entrada'])

    
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    
    base_id_port = BASE_PORT_ID
    new_id = base_id_port

    VISUALIZATION_INTERFACE = 19

    data = []
    for op_id in ALL_OPS:
        new_id += 1
        data.append([new_id, VISUALIZATION_INTERFACE])
        if op_id not in [MARKDOWN, IFRAME]:
            new_id += 1
            data.append([new_id, 1])

    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = [c.name for c in tb.columns]
    data = []
    for op_id in ALL_OPS:
        data.append([op_id, 15])
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

    form_id = BASE_FORM_ID + 1
    data = []
    for op_id in ALL_OPS:
        data.append([form_id, 1, 1, 'execution'])
        form_id += 1

    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = [c.name for c in tb.columns]

    form_id = BASE_FORM_ID + 1
    data = []
    for op_id in ALL_OPS:
        data.append([op_id, 41]) # appearance
        data.append([op_id, 141]) # grid coordinates
        data.append([op_id, form_id])
        data.append([op_id, form_id])
        form_id += 1
    
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

    form_id = BASE_FORM_ID + 1
    data = []
    for op_id in ALL_OPS:
        data.append([form_id, 'en', 'Execution'])
        data.append([form_id, 'pt', 'Execução'])
        form_id += 1

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
        column('enable_conditions', String),
        column('form_id', Integer), )

    mode = [
            {"en": "Gauge", "value": "gauge", "key": "gauge", "pt": "Medidor"},
            {"en": "Delta", "value": "delta", "key": "delta", "pt": "Delta (variação)"},
            {"en": "Value", "value": "number", "key": "number", "pt": "Número"},
            {"en": "Gauge and delta", "value": "gauge+delta", "key": "gauge+delta", "pt": "Medidor e delta (variação)"},
            {"en": "Gauge and number", "value": "gauge+number", "key": "gauge+number", "pt": "Medidor e número"},
            {"en": "Delta and number", "value": "delta+number", "key": "delta+number", "pt": "Delta (variação) e número"},
            {"en": "Gauge, delta and number", "value": "gauge+delta+number", "key": "gauge+delta+number", "pt": "Medidor, delta (variação) e número"},
    ]
    bar_chart_mode = [
            {"en": "Vertical bars", "value": "vertical", "key": "vertical", "pt": "Barras verticais"},
            {"en": "Horizontal bars", "value": "horizontal", "key": "horizontal", "pt": "Barras horizontais"},
            {"en": "Stacked vertical bars", "value": "stacked-vertical", "key": "stacked-vertical", "pt": "Barras verticais empilhadas"},
            {"en": "Stacked horizontal bars", "value": "stacked-horizontal", "key": "stacked-horizontal", "pt": "Barras horizontais empilhadas"},
    ]

    data = [
        # INDICATOR
        [529, 'title', 'TEXT', 0, 0, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 1],
        [530, 'display_value', 'INTEGER', 0, 1, '1', 'checkbox', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 1],
        [531, 'value', 'TEXT', 0, 2, None, 'attribute-selector', None, None, 'EXECUTION',  
            'this.display_value.internalValue && this.display_value.internalValue == 1 ', 
            BASE_FORM_ID + 1],
        [532, 'display_delta', 'INTEGER', 0, 2, '0', 'checkbox', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 1],
        [533, 'delta', 'TEXT', 0, 3, None, 'attribute-selector', None, None, 'EXECUTION', 
            'this.display_delta.internalValue && this.display_delta.internalValue == 1', 
            BASE_FORM_ID + 1],
        [534, 'delta_relative', 'TEXT', 0, 4, None, 'checkbox', None, None, 'EXECUTION', 
            'this.display_delta.internalValue && this.display_delta.internalValue == 1', 
            BASE_FORM_ID + 1],
        [535, 'footer', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 1],
        
        # MARKDOWN
        [536, 'text', 'TEXT', 0, 1, None, 'rich-text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 2],

        # WORD_CLOUD 
        [537, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 3],
        [538, 'word', 'TEXT', 0, 2, None, 'attribute-selector', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 3],
        [539, 'weight', 'TEXT', 0, 3, None, 'attribute-selector', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 3],
        [540, 'scale', 'TEXT', 0, 4, None, 'attribute-selector', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 3],

        # HEATMAP, 
        [541, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 4],
        [542, 'row_attribute', 'TEXT', 1, 2, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 4],
        [543, 'column_attribute', 'TEXT', 1, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 4],
        [544, 'value_attribute', 'TEXT', 1, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 4],
       
        # B5BBLE_CHART
        [545, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [546, 'x_axis_attribute', 'TEXT', 1, 2, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [547, 'y_axis_attribute', 'TEXT', 1, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [548, 'size_attribute', 'TEXT', 0, 4, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [549, 'color', 'TEXT', 0, 4, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [550, 'x_title', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [551, 'y_title', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 5],

        # FORCE_DIRECT 
        [552, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 6],
        [553, 'source_attribute', 'TEXT', 1, 2, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 6],
        [554, 'target_attribute', 'TEXT', 1, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 6],
        [555, 'edge_label_attribute', 'TEXT', 0, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 6],
        [556, 'edge_size_attribute', 'TEXT', 0, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 6],
        [557, 'source_label_attribute', 'TEXT', 0, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 6],
        [558, 'target_label_attribute', 'TEXT', 0, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 6],

        # IFRAME 
        [559, 'link', 'TEXT', 0, 3, None, 'url', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 7],

        # TREEMAP
        [560, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 8],
        [561, 'label_attribute', 'TEXT', 1, 2, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 8],
        [562, 'parent_attribute', 'TEXT', 1, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 8],
        [563, 'value_attribute', 'TEXT', 0, 4, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 8],
        [564, 'display_value', 'INTEGER', 0, 5, '1', 'checkbox', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 8],
        [565, 'display_entry_percentage', 'INTEGER', 0, 6, '0', 'checkbox', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 8],
        [566, 'display_parent_percentage', 'INTEGER', 0, 7, '0', 'checkbox', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 8],

        # BARCHART
        [MODE_ID, 'mode', 'TEXT', 0, 0, 'vertical', 'dropdown', None, json.dumps(bar_chart_mode), 'EXECUTION', None, 
            83],
    ]
    columns = [c.name for c in tb.columns]
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
        [524, 'en', 'Filters', 'Filters to be applied to the input.'],
        [524, 'pt', 'Filtros', 'Filtros a serem aplicados à entrada.'],
        [525, 'en', 'Ignore in design', 'In design/editing mode, filters are ignored.'],
        [525, 'pt', 'Ignore ao executar em ambiente de edição', 
            'Filtros são ignorados durante a edição do workflow.'],
        [526, 'en', 'User can use advanced query editor', 'Users can define custom filters using an advanced query editor.'],
        [526, 'pt', 'Disponibilizar editor de consulta', 'Usuários podem editar os filtros usando um editor avançado de consultas.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN {s} AND {e}'.format(s=INDICATOR, e=TREEMAP)),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN {s} AND {e}'.format(s=INDICATOR, e=TREEMAP)),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {e}'.format(s=INDICATOR, e=TREEMAP)),

    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE operation_id BETWEEN {s} AND {e})'.format(s=INDICATOR, e=TREEMAP)),

    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE operation_id BETWEEN {s} AND {e})'.format(s=INDICATOR, e=TREEMAP)),


    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN {s} AND {e}'.format(s=INDICATOR, e=TREEMAP)),

    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN {s} AND {e}'.format(s=INDICATOR, e=TREEMAP)),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {s} AND {e}'.format(s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {e}'.format(s=INDICATOR, e=TREEMAP)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {s} AND {e}'.format(s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

     (_insert_operation_form_field, """DELETE FROM operation_form_field 
          WHERE form_id BETWEEN {s} AND {e} OR id = {n} """.format(s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS), n=MODE_ID)),
 
#     (_insert_operation_form_field_translation,
#      'DELETE FROM operation_form_field_translation WHERE id IN (' +
#      'SELECT id FROM operation_form_field WHERE form_id BETWEEN {s} AND {e})'.format(s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),
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
