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

COLOR_FORM_ID=142
COLOR_SCALE_FORM_ID=143
BASE_FORM_ID = 143
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
            (INDICATOR, 'indicator', 1, 'VISUALIZATION', ' ', None),
            (MARKDOWN, 'markdown', 1, 'VISUALIZATION', ' ', None),
            (WORD_CLOUD, 'word-cloud', 1, 'VISUALIZATION', ' ', None),
            (HEATMAP, 'heatmap', 1, 'VISUALIZATION', ' ', None),
            (BUBBLE_CHART, 'bubble-chart', 1, 'VISUALIZATION', ' ', None),
            (FORCE_DIRECT, 'force-direct', 1, 'VISUALIZATION', ' ', None),
            (IFRAME, 'iframe', 1, 'VISUALIZATION', ' ', None),
            (TREEMAP, 'treemap', 1, 'VISUALIZATION', ' ', None),
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
    data.append([COLOR_FORM_ID, 1, 10, 'execution'])
    data.append([COLOR_SCALE_FORM_ID, 1, 10, 'execution'])
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
    data.append([COLOR_FORM_ID, 'en', 'Execution'])
    data.append([COLOR_FORM_ID, 'pt', 'Execução'])

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

    aggregation = [
        {"key": "count", "en": "Number of occurencies", "pt": "Número de ocorrências"}, 
        {"key": "first", "en": "First value", "pt": "Primeiro valor"}, 
        {"key": "last", "en": "Last value", "pt": "Último valor"}, 
        {"key": "max", "en": "Maximum value", "pt": "Valor máximo"}, 
        {"key": "min", "en": "Minimum value", "pt": "Valor mínimo"}, 
        {"key": "avg", "en": "Average value", "pt": "Valor médio"}, 
        {"key": "sum", "en": "Sum of values", "pt": "Soma dos valores"}, 
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
        [568, 'display_gauge', 'INTEGER', 0, 5, '0', 'checkbox', None, None, 'EXECUTION', None, 
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
        [571, 'aggregation_function', 'TEXT', 1, 4, 'sum', 'dropdown', None, json.dumps(aggregation), 'EXECUTION', None, 
            BASE_FORM_ID + 4],
        [573, 'row_title', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 4],
        [574, 'column_title', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 4],

       
        # BUBBLE_CHART
        [545, 'title', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [546, 'x_axis_attribute', 'TEXT', 1, 2, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [547, 'y_axis_attribute', 'TEXT', 1, 3, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [548, 'size_attribute', 'TEXT', 0, 4, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [549, 'color_attribute', 'TEXT', 0, 4, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [570, 'text_attribute', 'TEXT', 0, 5, None, 'attribute-selector', None, '{"multiple": false}', 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [550, 'x_title', 'TEXT', 0, 6, None, 'text', None, None, 'EXECUTION', None, 
            BASE_FORM_ID + 5],
        [551, 'y_title', 'TEXT', 0, 7, None, 'text', None, None, 'EXECUTION', None, 
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
        [MODE_ID, 'display_mode', 'TEXT', 0, 0, 'vertical', 'dropdown', None, json.dumps(bar_chart_mode), 'EXECUTION', None, 
            83],

        [569, 'color_palette', 'TEXT', 0, 10, None, 'color-palette', None, None, 'EXECUTION', None, COLOR_FORM_ID],
        [572, 'color_scale', 'TEXT', 0, 10, None, 'color-scale', None, None, 'EXECUTION', None, COLOR_SCALE_FORM_ID],
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
        # Indicator
        [529, 'en', 'Title', 'Title for the indicator.'],
        [529, 'pt', 'Tiítulo', 'Título do indicador.'],
        [530, 'en', 'Display value', 'Displays the value in the indicator.'],
        [530, 'pt', 'Exibir valor', 'Exibe o valor no indicador.'],
        [531, 'en', 'Value', 'Attribute used for the value.'],
        [531, 'pt', 'Valor', 'Atributo usado para o valor.'],
        [532, 'en', 'Display delta', 'Displays delta variation in the indicator.'],
        [532, 'pt', 'Exibir delta', 'Exibe o delta (variação) no indicador.'],
        [533, 'en', 'Reference value (for delta)', 'Attribute used for calculating the delta value.'],
        [533, 'pt', 'Valor de referência (para o delta)', 'Atributo usado para calcular o delta (variação).'],
        [534, 'en', 'Relative (%) delta', 'Uses a relative value for delta (percentage of value). If false, delta is calculated using the difference.'],
        [534, 'pt', 'Delta relativo (%)', 'Usa um valor relativo para o delta (percentual do valor). Se falso, delta é calculado usando a diferença..'],
        [568, 'en', 'Display gauge', 'Displays a gauge in the indicator.'],
        [568, 'pt', 'Exibir medidor', 'Exibe um meditor no indicador.'],
        [535, 'en', 'Footer', 'Text to be displayed in the footer of the indicator.'],
        [535, 'pt', 'Rodapé', 'Texto exibido na parte de baixo do indicador.'],
        
        # MARKDOWN
        [536, 'en', 'Text (Markdown)', 'Rich text encoded in Markdown language.'],
        [536, 'pt', 'Texto (Markdown)', 'Text formatado na linguagem Markdown.'],

        # WORD_CLOUD 
        [537, 'en', 'Title', 'Title for the word cloud.'],
        [537, 'pt', 'Título', 'Título para a nuvem de palavras.'],
        [538, 'en', 'Attribute with words', 'Attributes with words used in the cloud.'],
        [538, 'pt', 'Atributo com as palavras', 'Atributo com as palavras usadas na nuvem.'],
        [539, 'en', 'Attribute with weights (optional)', 'Attributes with weights for the words used in the cloud.'],
        [539, 'pt', 'Atributo com os pesos (opcional)', 'Atributo com os pesos das palavras usadas na nuvem.'],
        [540, 'en', 'Normalization scale', 'Scale used to normalize values.'],
        [540, 'pt', 'Escala de normalização', 'Escala usada para normalizar os valores.'],

        # HEATMAP, 
        [541, 'en', 'Title', 'Title for the heatmap'],
        [541, 'pt', 'Título', 'Título para o mapa de calor.'],
        [542, 'en', 'Attribute used in the rows', 'Attribute used in the rows of heatmap.'],
        [542, 'pt', 'Atributo usado nas linhas', 'Atributo usado nas linhas do heatmap.'],
        [543, 'en', 'Attribute used in the columns', 'Attribute used in the columns of heatmap.'],
        [543, 'pt', 'Atributo usado nas colunas', 'Atributo usado nas colunas do heatmap.'],
        [544, 'en', 'Attribute used as value', 'Attribute used as value for the intensity (heat).'],
        [544, 'pt', 'Atributo usado como valor', 'Atributo usado como valor para a intensidade (calor).'],
        [571, 'en', 'Compute values using', 'Compute values using specified function.'],
        [571, 'pt', 'Computar valores usando', 'Computar valores usando a função especificada.'],
        [573, 'en', 'Title for the rows axis', 'Title for the rows axis.'],
        [573, 'pt', 'Título para o eixo das linhas', 'Título para o eixo das linhas.'],
        [574, 'en', 'Title for the column axis', 'Title for the column axis.'],
        [574, 'pt', 'Título para o eixo das colunas', 'Título para o eixo das colunas.'],

      
        # BUBBLE_CHART
        [545, 'en', 'Title', 'Title for the bubble chart.'],
        [545, 'pt', 'Título', 'Título para o gráfico de bolhas.'],
        [546, 'en', 'x-axis attribute', 'Attribute used for the x-axis.'],
        [546, 'pt', 'Atributo para o eixo X', 'Atributo usado para o eixo X.'],
        [547, 'en', 'y-axis attribute', 'Attributs used for the y-axis.'],
        [547, 'pt', 'Atributo para o eixo Y', 'Atributo usado para o eixo Y.'],
        [548, 'en', 'Size attribute', 'Attribute used for the bubble size.'],
        [548, 'pt', 'Atributo para o tamanho', 'Atributo usado para o tamanho da bolha.'],
        [549, 'en', 'Color attribute', 'Attribute used for the bubble color.'],
        [549, 'pt', 'Atributo para a cor', 'Atributo usado para a cor da bolha.'],
        [570, 'en', 'Text attribute', 'Attribute used for the bubble text displayed when pointing with cursor.'],
        [570, 'pt', 'Atributo para o texto', 'Atributo usado para o texto da bolha ao apontar com o mouse.'],
        [550, 'en', 'Title for x-axis', 'Title for the x-axis.'],
        [550, 'pt', 'Título para o eixo x', 'Título para o eixo x.'],
        [551, 'en', 'Title for y-axis', 'Title for the y-axis.'],
        [551, 'pt', 'Título para o eixo y', 'Título para o eixo y.'],

        # FORCE_DIRECT 
        [552, 'en', 'Title', 'Title for the visualization.'], 
        [552, 'pt', 'Título', 'Título para a visualização.'],
        [553, 'en', 'Source attribute', 'Source attribute (source node).'],
        [553, 'pt', 'Atributo com o nó de origem', 'Atributo com o nó de origem.'],
        [554, 'en', 'Target attribute', 'Target attribute (target node).'],
        [554, 'pt', 'Atributo com o nó de destino', 'Atributo com o nó de destino.'],
        [555, 'en', 'Edge label attribute', 'Edge label attribute.'],
        [555, 'pt', 'Atributo com o rótulo da aresta', 'Atributo com o rótulo da aresta.'],
        [556, 'en', 'Edge size attribute', 'Edge size attribute.'],
        [556, 'pt', 'Atributo com o tamanho da aresta', 'Atributo com o tamanho da aresta.'],
        [557, 'en', 'Source label attribute', 'Source node label attribute.'],
        [557, 'pt', 'Atributo com o rótulo do nó de origem', 'Atributo com o rótulo do nó de origem.'],
        [558, 'en', 'Target label attribute', 'Target node label attribute.'],
        [558, 'pt', 'Atributo com o rótulo do nó de destino', 'Atributo com o rótulo do nó de destino.'],

        # IFRAME 
        [559, 'en', 'Link for the page', 'Link for the page displayed in the iframe element.'],
        [559, 'pt', 'Link para a página', 'Link para a página exibida no iframe.'],

        # TREEMAP
        [560, 'en', 'Title', 'Title for the visualization.'], 
        [560, 'pt', 'Título', 'Título para a visualização.'],
        [561, 'en', 'Cell label attribute', 'Cell label attribute used in the treemap.'],
        [561, 'pt', 'Atributo com o rótulo para a célula', 'Atributo com o rótulo para a célula.'],
        [562, 'en', 'Parent attribute', 'Cell parent used to build the hierarchy.'],
        [562, 'pt', 'Atributo com o pai da célula', 'Atributo com o pai da célula.'],
        [563, 'en', 'Value attribute', 'Attribute with the cell value.'],
        [563, 'pt', 'Atributo com o valor', 'Atributo com o valor da célula.'],
        [564, 'en', 'Display value', 'Displays the cell value.'],
        [564, 'pt', 'Exibir o valor da célula', 'Exibe o valor da célula.'],
        [565, 'en', 'Display cell\'s percentage', 'Display cell\'s percentage in relation to its parent.'],
        [565, 'pt', 'Exibir o % para a célula', 'Exibe o percentual do valor da célula em relação à célula pai.'],
        [566, 'en', 'Display parent\'s percentage', 'Display parent\'s percentage.'],
        [566, 'pt', 'Exibir o percentual da célula pai', 'Exibe o percentual da célula pai.'],

        # BARCHART
        [MODE_ID, 'en', 'Display mode', 'How to display the bar chart.'],
        [MODE_ID, 'pt', 'Modo de exibição', 'Como exibir o gráfico de barras.'],

        [569, 'en', 'Color palette', 'Choose the color palette used in the visualization.'],
        [569, 'pt', 'Paleta de cores', 'Escolha a paleta de cores usada na visualização.'],

        [572, 'en', 'Color scale', 'Choose the color scale used in the visualization.'],
        [572, 'pt', 'Escala de cores', 'Escolha a escala de cores usada na visualização.'],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

VISUALIZATIONS_WITH_COLOR_PALETTE=[68, 69, 70, 71, 80, 87, 88, 89, 123, 124, 132, 134, 135, 137, 4040]
VISUALIZATIONS_WITH_COLOR_SCALE=[133]
# operations and COLOR form
PAIRS=list(zip(VISUALIZATIONS_WITH_COLOR_PALETTE, [COLOR_FORM_ID]*len(VISUALIZATIONS_WITH_COLOR_PALETTE))) 
PAIRS.extend(list(zip(VISUALIZATIONS_WITH_COLOR_SCALE, [COLOR_SCALE_FORM_ID]*len(VISUALIZATIONS_WITH_COLOR_SCALE))))
INSERT_PAIRS= ','.join(['({}, {})'.format(*x) for x in PAIRS])

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
     'DELETE FROM operation_form WHERE id BETWEEN {s} AND {e} OR id = {n} or id = {p}'.format(
         n=COLOR_FORM_ID, p=COLOR_SCALE_FORM_ID, s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN {s} AND {e} OR operation_id = {n}'.format(
                                           s=INDICATOR, e=TREEMAP, n=COLOR_FORM_ID)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN {s} AND {e} OR id = {n} OR id = {p}'.format(
         n=COLOR_FORM_ID, p=COLOR_SCALE_FORM_ID, s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS))),

     (_insert_operation_form_field, """DELETE FROM operation_form_field 
          WHERE form_id BETWEEN {s} AND {e} OR id = {m} OR form_id IN ({n}, {p}) """.format(
              s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS), m=MODE_ID, n=COLOR_FORM_ID, p=COLOR_SCALE_FORM_ID)),
 
     (_insert_operation_form_field_translation,
      'DELETE FROM operation_form_field_translation WHERE id IN (' +
      'SELECT id FROM operation_form_field WHERE form_id BETWEEN {s} AND {e} OR id={m} OR form_id IN ({n}, {p}))'.format(
          s=BASE_FORM_ID + 1, e=BASE_FORM_ID + 1 + len(ALL_OPS), m=MODE_ID, n=COLOR_FORM_ID, p=COLOR_SCALE_FORM_ID)),

     ("UPDATE operation set type = 'VISUALIZATION' WHERE id IN (87, 88, 89, 123, 124, 4040)" , 
        "UPDATE operation set type = 'ACTION' WHERE id IN (87, 88, 89, 123, 124, 4040)"),

     ("INSERT INTO operation_operation_form values {}".format(INSERT_PAIRS) , 
        "DELETE FROM operation_operation_form WHERE operation_form_id IN ({}, {})".format(COLOR_FORM_ID, COLOR_SCALE_FORM_ID)),
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
