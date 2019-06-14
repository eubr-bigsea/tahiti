# -*- coding: utf-8 -*-}
"""operations

Revision ID: 6821c3b11408
Revises: 35e7de3e6315
Create Date: 2017-05-02 15:27:10.264045

"""
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '6821c3b11408'
down_revision = '35e7de3e6315'
branch_labels = None
depends_on = None


# noinspection PyBroadException
def upgrade():
    try:
        op.execute(text("START TRANSACTION"))
        insert_operation()
        insert_operation_category()
        insert_operation_category_translation()
        insert_operation_category_operation()
        insert_operation_form()
        insert_operation_form_field()
        op.execute(text("COMMIT"))
    except Exception as e:
        op.execute(text("ROLLBACK"))
        raise


def insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (1, 'en', 'Spark'),
        (1, 'pt', 'Spark'),
        (2, 'en', 'Web service'),
        (2, 'pt', 'Web service'),
        (3, 'en', 'Data source'),
        (3, 'pt', 'Data source'),
        (4, 'en', 'Classification algorithm'),
        (4, 'pt', 'Classification algorithm'),
        (5, 'en', 'Classification model'),
        (5, 'pt', 'Modelo de classificação'),
        (6, 'en', 'Data source and target'),
        (6, 'pt', 'Fonte de dados de entrada e saída'),
        (7, 'en', 'Data transformation'),
        (7, 'pt', 'Transformação de dados'),
        (8, 'en', 'Machine learning'),
        (8, 'pt', 'Aprendizado de máquina'),
        (9, 'en', 'Publish in production'),
        (9, 'pt', 'Publicar em produção'),
        (10, 'en', 'Data utilities'),
        (10, 'pt', 'Utilitários para dados'),
        (11, 'en', 'Data manipulation'),
        (11, 'pt', 'Data manipulation'),
        (12, 'en', 'Text processing'),
        (12, 'pt', 'Text processing'),
        (13, 'en', 'Others'),
        (13, 'pt', 'Outras'),
        (14, 'en', 'Comment'),
        (14, 'pt', 'Comment'),
        (15, 'en', 'Data visualization'),
        (15, 'pt', 'Visualização de dados'),
        (16, 'en', 'Text processing'),
        (16, 'pt', 'Processamento de Texto'),
        (17, 'en', 'Geo'),
        (17, 'pt', 'Geo'),
        (18, 'en', 'ML: Classification'),
        (19, 'en', 'ML: Clustering'),
        (20, 'en', 'ML: Recommendation'),
        (21, 'en', 'ML: Regression'),
        (22, 'en', 'ML: Associative'),
        (23, 'en', 'ML: Feature extraction'),
        (24, 'en', 'ML: Tunning'),
        (25, 'en', 'Evaluation'),
        (26, 'en', 'ML: Models'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1),
        (7, 1),
        (8, 1),
        (9, 1),
        (10, 1),
        (11, 1),
        (12, 1),
        (13, 1),
        (14, 1),
        (15, 1),
        (16, 1),
        (17, 1),
        (20, 2),
        (18, 3),
        (4, 4),
        (1, 5),
        (2, 13),
        (5, 7),
        (6, 7),
        (7, 7),
        (12, 7),
        (13, 7),
        (14, 13),
        (15, 7),
        (16, 7),
        (18, 6),
        (20, 9),
        (21, 7),
        (23, 7),
        (24, 7),
        (26, 9),
        (26, 2),
        (28, 1),
        (17, 7),
        (28, 7),
        (29, 1),
        (30, 3),
        (30, 6),
        (31, 1),
        (32, 1),
        (32, 7),
        (27, 1),
        (27, 7),
        (25, 13),
        (25, 14),
        (33, 1),
        (33, 10),
        (34, 1),
        (34, 10),
        (35, 1),
        (35, 15),
        (36, 1),
        (36, 10),
        (37, 1),
        (37, 7),
        (38, 1),
        (39, 1),
        (40, 1),
        (41, 1),
        (42, 1),
        (43, 1),
        (44, 1),
        (45, 4),
        (45, 1),
        (46, 1),
        (46, 4),
        (47, 1),
        (47, 4),
        (48, 1),
        (49, 1),
        (49, 16),
        (50, 1),
        (50, 16),
        (51, 1),
        (51, 16),
        (52, 1),
        (52, 16),
        (53, 1),
        (53, 17),
        (54, 1),
        (55, 17),
        (57, 1),
        (57, 9),
        (58, 1),
        (58, 6),
        (59, 1),
        (60, 1),
        (61, 3),
        (62, 7),
        (61, 6),
        (68, 15),
        (69, 15),
        (70, 1),
        (70, 15),
        (71, 15),
        (71, 1),
        (72, 1),
        (73, 1),
        (74, 1),
        (75, 1),
        (76, 1),
        (77, 1),
        (78, 1),
        (79, 1),
        (80, 1),
        (80, 15),
        (81, 1),
        (81, 15),
        (1, 18),
        (4, 18),
        (9, 18),
        (31, 18),
        (44, 18),
        (45, 18),
        (46, 18),
        (47, 18),
        (77, 21),
        (78, 21),
        (79, 21),
        (8, 21),
        (73, 21),
        (74, 21),
        (76, 21),
        (10, 19),
        (29, 19),
        (48, 19),
        (56, 19),
        (59, 20),
        (60, 20),
        (40, 23),
        (41, 23),
        (72, 23),
        (75, 23),
        (19, 26),
        (42, 26),
        (22, 26),
        (43, 26),
        (3, 22),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


def insert_operation_category():
    operation_category_table = table('operation_category',
                                     column("id", Integer),
                                     column('type', String),
                                     )
    columns = ['id', 'type']
    all_categories = [
        (1, 'technology'),
        (2, 'service'),
        (3, 'data source'),
        (4, 'algorithm'),
        (5, 'model'),
        (6, 'parent'),
        (7, 'parent'),
        (8, 'parent'),
        (9, 'parent'),
        (10, 'parent'),
        (11, 'parent'),
        (12, 'parent'),
        (13, 'parent'),
        (14, 'comment'),
        (15, 'parent'),
        (16, 'parent'),
        (17, 'parent'),
        (18, 'parent'),
        (19, 'parent'),
        (20, 'parent'),
        (21, 'parent'),
        (22, 'parent'),
        (23, 'parent'),
        (24, 'parent'),
        (25, 'parent'),
        (26, 'parent'),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in all_categories]

    op.bulk_insert(operation_category_table, rows)


def insert_operation():
    operation_table = table('operation',
                            column("id", Integer),
                            column("slug", String),
                            column('enabled', Integer),
                            column('type', String),
                            column('icon', String),
                            )
    columns = ['id', 'slug', 'enabled', 'type', 'icon']
    all_ops = (
        (1, 'classification-model', 1, 'TRANSFORMATION', 'fa-dashboard'),
        (2, 'topic-report', 1, 'TRANSFORMATION', 'fa-book'),
        (3, 'frequent-item-set', 1, 'TRANSFORMATION', 'fa-cart-plus'),
        (4, 'naive-bayes-classifier', 1, 'TRANSFORMATION', 'fa-tag'),
        (5, 'filter-selection', 1, 'TRANSFORMATION', 'fa-filter'),
        (6, 'projection', 1, 'TRANSFORMATION', 'icon-projection'),
        (7, 'transformation', 1, 'TRANSFORMATION', 'fa-cog'),
        (8, 'linear-regression', 1, 'TRANSFORMATION', 'fa-line-chart'),
        (9, 'svm-classification', 1, 'TRANSFORMATION', 'fa-tag'),
        (10, 'clustering-model', 1, 'TRANSFORMATION', 'fa-users'),
        (11, 'outlier-detection', 0, 'TRANSFORMATION', 'fa-balance-scale'),
        (12, 'add-rows', 1, 'TRANSFORMATION', 'icon-union'),
        (13, 'set-intersection', 1, 'TRANSFORMATION', 'icon-intersection'),
        (14, 'time-series', 1, 'TRANSFORMATION', 'fa-calendar'),
        (15, 'aggregation', 1, 'TRANSFORMATION', 'fa-cube'),
        (16, 'join', 1, 'TRANSFORMATION', 'fa-link'),
        (17, 'split', 1, 'TRANSFORMATION', 'fa-code-fork'),
        (18, 'data-reader', 1, 'TRANSFORMATION', 'fa-database'),
        (19, 'evaluate-model', 1, 'TRANSFORMATION', 'fa-check'),
        (20, 'service-output', 1, 'ACTION', 'fa-gears'),
        (21, 'clean-missing', 1, 'ACTION', 'fa-check'),
        (22, 'score-model', 1, 'ACTION', 'fa-bullseye'),
        (23, 'remove-duplicated-rows', 1, 'ACTION', 'fa-bars'),
        (24, 'add-columns', 1, 'TRANSFORMATION', 'fa-copy'),
        (25, 'comment', 1, 'ACTION', 'fa-commenting-o'),
        (26, 'publish-as-visualization', 1, 'ACTION', 'fa-pie-chart'),
        (27, 'replace-value', 1, 'TRANSFORMATION', 'fa-eraser'),
        (28, 'sample', 1, 'TRANSFORMATION', 'fa-flask'),
        (29, 'k-means-clustering', 1, 'TRANSFORMATION', 'fa-braille'),
        (30, 'data-writer', 1, 'ACTION', 'fa-save'),
        (31, 'logistic-regression', 1, 'TRANSFORMATION', 'fa-exchange'),
        (32, 'sort', 1, 'TRANSFORMATION', 'fa-sort'),
        (33, 'change-attribute', 1, 'TRANSFORMATION', 'fa-edit'),
        (34, 'broadcast-data', 1, 'TRANSFORMATION', 'fa-bullhorn'),
        (35, 'table-visualization', 1, 'VISUALIZATION', 'fa-table'),
        (36, 'run-application', 1, 'TRANSFORMATION', 'fa-lemon-o'),
        (37, 'difference', 1, 'TRANSFORMATION', 'fa-minus-square'),
        (38, 'pearson-correlation', 0, 'TRANSFORMATION', 'fa-long-arrow-up'),
        (39, 'save-model', 1, 'TRANSFORMATION', 'fa-cloud-upload'),
        (40, 'feature-indexer', 1, 'TRANSFORMATION', 'fa-list-ol'),
        (41, 'feature-assembler', 1, 'TRANSFORMATION', 'fa-truck'),
        (42, 'apply-model', 1, 'TRANSFORMATION', 'fa-lightbulb-o'),
        (43, 'cross-validation', 1, 'TRANSFORMATION', 'fa-crosshairs'),
        (44, 'random-forest-classifier', 1, 'TRANSFORMATION', 'fa-random'),
        (45, 'gbt-classifier', 1, 'TRANSFORMATION', 'fa-tree'),
        (46, 'decision-tree-classifier', 1, 'TRANSFORMATION', 'fa-arrow-right'),
        (47, 'perceptron-classifier', 1, 'TRANSFORMATION',
         'fa-angle-double-down'),
        (48, 'lda-clustering', 1, 'TRANSFORMATION', 'fa-file-text'),
        (49, 'tokenizer', 1, 'TRANSFORMATION', 'fa-text-width'),
        (50, 'remove-stop-words', 1, 'TRANSFORMATION', 'fa-hand-stop-o'),
        (51, 'generate-n-grams', 1, 'TRANSFORMATION', 'fa-ellipsis-h'),
        (52, 'word-to-vector', 1, 'TRANSFORMATION', 'fa-long-arrow-right'),
        (53, 'read-shapefile', 1, 'TRANSFORMATION', 'fa-map-o'),
        (54, 'classification-report', 1, 'TRANSFORMATION', 'fa-print'),
        (55, 'within', 1, 'TRANSFORMATION', 'fa-globe'),
        (56, 'gaussian-mixture-clustering', 1, 'TRANSFORMATION', 'fa-bullseye'),
        (57, 'multiplexer', 1, 'TRANSFORMATION', 'fa-puzzle-piece'),
        (58, 'external-input', 1, 'TRANSFORMATION', 'fa-external-link-square'),
        (59, 'recommendation-model', 1, 'TRANSFORMATION', 'fa-star'),
        (60, 'als-recommender', 1, 'TRANSFORMATION', 'fa-signal'),
        (61, 'data_reader_2', 1, 'TRANSFORMATION', 'fa-database'),
        (62, 'filter_2', 1, 'TRANSFORMATION', 'fa-filter'),
        (63, 'graph', 1, 'TRANSFORMATION', 'fa-circle-o'),
        (64, 'correlation', 1, 'TRANSFORMATION', 'fa-circle'),
        (65, 'word_tree', 1, 'TRANSFORMATION', 'fa-tree'),
        (66, 'sentiment_analysis', 1, 'TRANSFORMATION', 'fa-thumbs-o-up'),
        (67, 'recurrence', 1, 'TRANSFORMATION', 'fa-square'),
        (68, 'line-chart', 1, 'VISUALIZATION', 'fa-line-chart'),
        (69, 'bar-chart', 1, 'VISUALIZATION', 'fa-bar-chart'),
        (70, 'pie-chart', 1, 'VISUALIZATION', 'fa-pie-chart'),
        (71, 'area-chart', 1, 'VISUALIZATION', 'fa-area-chart'),
        (72, 'index-to-string', 1, 'TRANSFORMATION', 'fa-keyboard-o'),
        (73, 'regression-model', 1, 'TRANSFORMATION', 'fa-shield'),
        (74, 'isotonic-regression', 1, 'TRANSFORMATION', 'fa-battery-quarter'),
        (75, 'one-hot-encoder', 1, 'TRANSFORMATION', 'fa-qrcode'),
        (76, 'aft-survival-regression', 1, 'TRANSFORMATION', 'fa-fire'),
        (77, 'gbt-regressor', 1, 'TRANSFORMATION', 'fa-id-card-o'),
        (78, 'random-forest-regressor', 1, 'TRANSFORMATION', 'fa-laptop'),
        (79, 'generalized-linear-regressor', 1, 'TRANSFORMATION',
         'fa-plus-square'),
        (80, 'scatter-plot', 1, 'VISUALIZATION', 'fa-square'),
        (81, 'summary-statistics', 1, 'VISUALIZATION', 'fa-calculator'),
    )
    rows = [dict(list(zip(columns, operation))) for operation in all_ops]

    op.bulk_insert(operation_table, rows)


def insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (1, 1, 1, 'execution'),
        (2, 1, 1, 'execution'),
        (3, 1, 1, 'execution'),
        (4, 1, 1, 'execution'),
        (5, 1, 1, 'execution'),
        (6, 1, 1, 'execution'),
        (7, 1, 1, 'execution'),
        (8, 1, 1, 'execution'),
        (9, 1, 1, 'execution'),
        (10, 1, 1, 'execution'),
        (11, 1, 1, 'execution'),
        (12, 1, 1, 'execution'),
        (13, 1, 1, 'execution'),
        (14, 1, 1, 'execution'),
        (15, 1, 1, 'execution'),
        (16, 1, 1, 'execution'),
        (17, 1, 1, 'execution'),
        (18, 1, 1, 'execution'),
        (19, 1, 1, 'execution'),
        (20, 1, 1, 'execution'),
        (21, 1, 1, 'execution'),
        (22, 1, 1, 'execution'),
        (23, 1, 1, 'execution'),
        (24, 1, 1, 'execution'),
        (25, 1, 1, 'execution'),
        (26, 1, 1, 'execution'),
        (27, 1, 1, 'execution'),
        (28, 1, 1, 'execution'),
        (32, 1, 1, 'execution'),
        (33, 1, 1, 'execution'),
        (34, 1, 1, 'paramgrid'),
        (35, 1, 1, 'execution'),
        (39, 0, 3, 'infrastructure'),
        (40, 0, 4, 'security'),
        (41, 1, 2, 'appearance'),
        (42, 1, 1, 'execution'),
        (43, 0, 5, 'logging'),
        (44, 1, 1, 'execution'),
        (45, 1, 1, 'execution'),
        (46, 1, 1, 'execution'),
        (48, 1, 0, 'execution'),
        (49, 1, 0, 'execution'),
        (50, 1, 1, 'execution'),
        (51, 1, 1, 'execution'),
        (52, 1, 1, 'execution'),
        (53, 1, 1, 'execution'),
        (54, 1, 1, 'execution'),
        (55, 1, 1, 'execution'),
        (56, 1, 1, 'execution'),
        (57, 1, 1, 'execution'),
        (58, 1, 1, 'execution'),
        (59, 1, 1, 'execution'),
        (60, 1, 1, 'execution'),
        (61, 1, 1, 'execution'),
        (62, 1, 1, 'execution'),
        (63, 1, 1, 'execution'),
        (64, 1, 0, 'paramgrid'),
        (65, 1, 0, 'paramgrid'),
        (66, 1, 0, 'paramgrid'),
        (67, 1, 0, 'paramgrid'),
        (68, 1, 0, 'paramgrid'),
        (69, 1, 1, 'execution'),
        (70, 1, 1, 'execution'),
        (71, 1, 1, 'execution'),
        (72, 1, 1, 'execution'),
        (73, 1, 1, 'execution'),
        (74, 1, 1, 'execution'),
        (75, 1, 1, 'execution'),
        (76, 1, 1, 'execution'),
        (77, 1, 1, 'execution'),
        (78, 1, 1, 'execution'),
        (79, 1, 1, 'execution'),
        (80, 1, 1, 'execution'),
        (81, 1, 1, 'execution'),
        (82, 1, 1, 'execution'),
        (83, 1, 1, 'execution'),
        (84, 1, 1, 'execution'),
        (85, 1, 1, 'execution'),
        (86, 1, 1, 'execution'),
        (87, 1, 1, 'execution'),
        (88, 1, 1, 'execution'),
        (89, 1, 1, 'execution'),
        (90, 1, 1, 'execution'),
        (91, 1, 1, 'execution'),
        (92, 1, 1, 'execution'),
        (93, 1, 1, 'execution'),
        (94, 1, 1, 'execution'),
        (95, 1, 1, 'execution'),
        (96, 1, 1, 'execution'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(operation_form_table, rows)


def insert_operation_form_field():
    operation_form_field_table = table(
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
        (1, 'data_source', 'INTEGER', 1, 0, None, 'lookup',
         'http://beta.ctweb.inweb.org.br/limonero/datasources?token=123456',
         None, 'EXECUTION', 18),
        (6, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector', None, None,
         'EXECUTION', 6),
        (7, 'max_memory', 'FLOAT', 0, 0, None, 'decimal', None, None,
         'EXECUTION', 39),
        (8, 'max_exec_time', 'INTEGER', 0, 0, None, 'integer', None, None,
         'EXECUTION', 39),
        (9, 'max_cpus', 'INTEGER', 0, 0, None, 'integer', None, None,
         'EXECUTION', 39),
        (10, 'sensitive_data', 'INTEGER', 0, 0, None, 'checkbox', None, None,
         'EXECUTION', 40),
        (11, 'left_attributes', 'TEXT', 1, 0, None, 'attribute-selector', None,
         None, 'EXECUTION', 16),
        (12, 'right_attributes', 'TEXT', 1, 0, None, 'attribute-selector', None,
         None, 'EXECUTION', 16),
        (13, 'join_type', 'TEXT', 1, 0, None, 'dropdown', None,
         '[{"key": "inner", "value": "Inner join"},{"key": "left_outer", '
         '"value": "Left outer join"}, {"key": "right_outer", '
         '"value": "Right outer join"}]',
         'EXECUTION', 16),
        (14, 'keep_right_keys', 'INTEGER', 0, 0, None, 'checkbox', None, None,
         'EXECUTION', 16),
        (15, 'match_case', 'INTEGER', 1, 0, None, 'checkbox', None, None,
         'EXECUTION',
         16),
        (16, 'weights', 'INTEGER', 0, 0, None, 'range', None, '50', 'EXECUTION',
         17),
        (17, 'seed', 'INTEGER', 0, 0, None, 'integer', None, None, 'EXECUTION',
         17),
        (18, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector', None, None,
         'EXECUTION', 20),
        (19, 'cleaning_mode', 'TEXT', 1, 1, None, 'dropdown', None,
         '[{"key": "MEAN", "value": "Replace with mean"}, {"key": "VALUE", '
         '"value": "Replace with value"},{"key": "MEDIAN", "value": '
         '"Replace with approx. median (10% relative target precision)"}, '
         '{"key": "MODE", "value": "Replace with mode"}, {"key": "REMOVE_ROW", '
         '"value": "Remove entire row"}, {"key": "REMOVE_COLUMN", "value":'
         ' "Remove entire column"}]',
         'EXECUTION', 20),
        (20, 'value', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 20),
        (21, 'comment', 'TEXT', 0, 0, None, 'textarea', None, None, 'EXECUTION',
         41),
        (22, 'comment', 'TEXT', 0, 0, None, 'textarea', None, None, 'EXECUTION',
         24),
        (23, 'attributes', 'TEXT', 1, 0, None, 'attribute-function', None,
         '{\r\n    "functions":\r\n	[\r\n	  {"key": "asc", "value": '
         '"Ascending", "help": "Ascending order"},\r\n	  {"key": "desc", '
         '"value": "Descending", "help": "Descending order"}\r\n    ],\r\n   '
         ' "options": {\r\n        "title": "Sort operation",\r\n        '
         '"description": "Sort a data source by a set of attributes",\r\n  '
         '      "show_alias": false\r\n    }\r\n}',
         'EXECUTION', 35),
        (25, 'color', 'TEXT', 0, 1, 'rgb(255, 255, 165)', 'color', None,
         '[\r\n{"background": "transparent", "foreground": "#222222"},\r\n'
         '{"background": "#FF1417", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#FF6611", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#FF8844", "foreground": "#000000"},\r\n'
         '{"background": "#FFEE55", "foreground": "#222222"},\r\n'
         '{"background": "#FEFE38", "foreground": "#222222"},\r\n'
         '{"background": "#FFFF99", "foreground": "#222222"},\r\n'
         '{"background": "#AACC22", "foreground": "#222222"},\r\n'
         '{"background": "#BBDD77", "foreground": "#222222"},\r\n'
         '{"background": "#C8CF82", "foreground": "#222222"},\r\n'
         '{"background": "#92A77E", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#5599EE", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#0088CC", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#226688", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#175279", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#557777", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#DDBB33", "foreground": "#222222"},\r\n'
         '{"background": "#D3A76D", "foreground": "#222222"},\r\n'
         '{"background": "#A9834B", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#AA6688", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#767676", "foreground": "#FFFFFF"},\r\n'
         '{"background": "#FFFFFF", "foreground": "#222222"}\r\n]\r\n',
         'EXECUTION', 41),
        (26, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 42),
        (61, 'new_name', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION',
         42),
        (62, 'new_data_type', 'TEXT', 0, 3, None, 'dropdown', None,
         '[{"key": "keep", "value": "Do not change"}, {"key": "integer", '
         '"value": "Integer"},{"key": "string", "value": "String"}, '
         '{"key": "double", "value": "Double"}, {"key": "Date", "value": '
         '"Date"}, {"key": "Date/time", "value": "Date/time"}]',
         'EXECUTION', 42),
        (63, 'Noneable', 'INTEGER', 0, 4, None, 'dropdown', None,
         '[{"key": "keep", "value": "Do not change"}, {"key": "true", '
         '"value": "Yes"}, {"key": "false", "value": "No"}]',
         'EXECUTION', 42),
        (64, 'is_feature', 'INTEGER', 0, 5, None, 'dropdown', None,
         '[{"key": "keep", "value": "Do not change"}, {"key": "true", '
         '"value": "Yes"}, {"key": "false", "value": "No"}]',
         'EXECUTION', 42),
        (65, 'is_label', 'INTEGER', 0, 6, None, 'dropdown', None,
         '[{"key": "keep", "value": "Do not change"}, {"key": "true", '
         '"value": "Yes"}, {"key": "false", "value": "No"}]',
         'EXECUTION', 42),
        (67, 'log_level', 'TEXT', 0, 1, None, 'dropdown', None,
         '[\r\n  {"key": "DEBUG", "value": "DEBUG"}, \r\n  {"key": "INFO", '
         '"value": "INFO"}, \r\n  {"key": "WARN", "value": "WARNING"},\r\n  '
         '{"key": "ERROR", "value": "ERROR"}\r\n]',
         'EXECUTION', 43),
        (68, 'application', 'INTEGER', 1, 1, None, 'lookup',
         'http://beta.ctweb.inweb.org.br/tahiti/applications?token=123456',
         None, 'EXECUTION', 46),
        (69, 'parameters', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION',
         46),
        (70, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 15),
        (71, 'function', 'TEXT', 1, 2, None, 'attribute-function', None,
         '{\r\n    "functions":\r\n	[\r\n	  {"key": "avg", "value": "Average'
         ' (AVG)", "help": "Computes the average of each group"},\r\n	  '
         '{"key": "count", "value": "Count", "help": "Counts the total of '
         'records of each group"},\r\n	  {"key": "first", "value": "First", '
         '"help": "Returns the first element of group"},\r\n	  {"key": '
         '"last", "value": "Last", "help": "Returns the last element of group"}'
         ',\r\n	  {"key": "max", "value": "Maximum (MAX)", "help": "Returns '
         'the max value of each group for one attribute"},\r\n	  {"key": "'
         'min", "value": "Minimum (MIN)", "help": "Returns the min value of '
         'each group for one attribute"},\r\n	  {"key": "sum", "value": '
         '"Sum", "help": "Returns the sum of values of each group for one '
         'attribute"}\r\n    ],\r\n    "options": {\r\n        "title": '
         '"Aggregate operation",\r\n        "description": "Add one of more '
         'lines with attribute to be used, function and alias to compute '
         'aggregate function over groups.",\r\n        "show_alias": '
         'true\r\n    }\r\n}',
         'EXECUTION', 15),
        (72, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 22),
        (73, 'seed', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION',
         26),
        (74, 'fraction', 'FLOAT', 1, 2, '1', 'percentage', None, None,
         'EXECUTION', 26),
        (75, 'header', 'INTEGER', 0, 2, '0', 'checkbox', None, None,
         'EXECUTION', 18),
        (76, 'separator', 'TEXT', 0, 3, ',', 'text', None, None, 'EXECUTION',
         18),
        (77, 'infer_schema', 'TEXT', 0, 4, 'FROM_LIMONERO', 'dropdown', None,
         '[\r\n  {"key": "FROM_LIMONERO", "value": "From metadata (recommended)'
         '"},\r\n  {"key": "FROM_VALUES", "value": "From data"},\r\n  '
         '{"key": "NO", "value": "Do not infer"}\r\n]',
         'EXECUTION', 18),
        (78, 'attributes', 'TEXT', 1, 0, None, 'attribute-selector', None, None,
         'EXECUTION', 48),
        (79, 'min_missing_ratio', 'FLOAT', 0, 3, None, 'decimal', None, None,
         'EXECUTION', 20),
        (80, 'max_missing_ratio', 'FLOAT', 0, 4, None, 'decimal', None, None,
         'EXECUTION', 20),
        (81, 'name', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION', 28),
        (82, 'path', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION', 28),
        (83, 'format', 'TEXT', 1, 4, None, 'dropdown', None,
         '[\r\n  {\r\n    "key": "CSV", "value": "CSV data file" \r\n  }'
         ',\r\n  {\r\n    "key": "JSON", "value": "JSON data file" \r\n  },'
         '\r\n  {\r\n    "key": "PARQUET", "value": "Parquet data file" \r\n'
         ' }\r\n]',
         'EXECUTION', 28),
        (84, 'tags', 'TEXT', 0, 5, None, 'tag', None, None, 'EXECUTION', 28),
        (85, 'mode', 'INTEGER', 0, 6, None, 'dropdown', None,
         '[\r\n  {\r\n    "key": "append", "value": "Append data to the '
         'existing file" \r\n  },\r\n  {\r\n    "key": "error", "value": '
         '"Do not overwrite, raise error" \r\n  },\r\n  {\r\n    "key": '
         '"ignore", "value": "Ignore if file exists" \r\n  },\r\n  {\r\n    '
         '"key": "overwrite", "value": "Overwrite if file exists" \r\n  }\r\n]',
         'EXECUTION', 28),
        (86, 'header', 'INTEGER', 0, 7, None, 'checkbox', None, None,
         'EXECUTION', 28),
        (87, 'storage', 'INTEGER', 1, 3, None, 'dropdown', None,
         '[\r\n{\r\n    "key": 1, "value": "HDFS - Default Storage" \r\n}\r\n]',
         'EXECUTION', 28),
        (88, 'expression', 'TEXT', 1, 1, None, 'expression', None,
         '[\r\n   {\r\n     "category": "Math", \r\n     "functions": [\r\n   '
         '    {"name": "SQRT", "help": "Return the square root of a number", '
         '"syntax": "SQRT(value_or_attribute)"}\r\n      ]\r\n   },\r\n   '
         '{\r\n       "category": "Datetime", \r\n       "functions":[\r\n  '
         '        {"name": "DATETIME_TO_TS", "help": "Convert a datetime to '
         'timestamp", "syntax": "DATETIME_TO_TS(date_or_attribute)"},\r\n    '
         '      {"name": "GROUP_DATETIME", "help": "Group a date to a bin '
         'using seconds as unit", "syntax": "GROUP_DATETIME(date_or_attribute, '
         'seconds)"},\r\n          {"name": "NOW", "help": "Return current '
         'system hour", "syntax": "NOW()"},\r\n          {"name": "TS_TO_'
         'DATETIME", "help": "Convert a timestamp to datetime", "syntax": '
         '"TS_TO_DATETIME(ts_or_attribute)"}\r\n       ]\r\n   },\r\n   '
         '{\r\n       "category": "String", \r\n       "functions": [\r\n '
         '        {"name": "SUBSTR", "help": "Return a substring of a text",'
         ' "syntax": "SUBSTR(text_or_attribute, start, size)"}\r\n       ]'
         '\r\n   }\r\n]',
         'EXECUTION', 7),
        (89, 'alias', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION', 7),
        (90, 'filter', 'TEXT', 1, 1, None, 'attribute-function', None,
         '{\r\n	"functions": [\r\n            {\r\n		"key": ">",\r\n		'
         '"value": "Greater than (>)",\r\n		"help": "Greater than (>)'
         '"\r\n	    },\r\n            {\r\n		"key": ">=",\r\n		'
         '"value": "Greater or equals to (>=)",\r\n		"help": '
         '"Greater or equals to (>=)"\r\n	    },\r\n            {\r\n		'
         '"key": "<",\r\n		"value": "Less than (<)",\r\n		"help": '
         '"Less than (<)"\r\n	    },\r\n            {\r\n		"key": "<=",'
         '\r\n		"value": "Less or equals to (<=)",\r\n		"help": '
         '"Less or equals to (<=)"\r\n	    },\r\n            {\r\n		'
         '"key": "==",\r\n		"value": "Equals to (=)",\r\n		'
         '"help": "Equals to (=)"\r\n	    },\r\n            {\r\n		'
         '"key": "!=",\r\n		"value": "Different (!=)",\r\n		"help": '
         '"Different (!=)"\r\n	    }\r\n        ],\r\n	"options": '
         '{\r\n		"title": "Filter operation",\r\n		"show_alias": '
         'false,\r\n                "show_value": true\r\n	}\r\n}',
         'EXECUTION', 5),
        (91, 'None_values', 'TEXT', 0, 3, None, 'textarea', None, None,
         'EXECUTION', 18),
        (93, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 50),
        (94, 'indexer_type', 'TEXT', 1, 1, None, 'dropdown', None,
         '[\r\n  {\r\n    "key": "string", "value": "String" \r\n  },\r\n  '
         '{\r\n    "key": "vector", "value": "Vector" \r\n  }\r\n]',
         'EXECUTION', 50),
        (95, 'alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 50),
        (96, 'max_categories', 'INTEGER', 0, 3, None, 'integer', None, None,
         'EXECUTION', 50),
        (97, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 51),
        (98, 'alias', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION', 51),
        (99, 'prediction_attribute', 'TEXT', 1, 1, None, 'attribute-selector',
         None, None, 'EXECUTION', 32),
        (100, 'label_attribute', 'TEXT', 1, 2, None, 'attribute-selector', None,
         None, 'EXECUTION', 32),
        (101, 'metric', 'TEXT', 0, 3, None, 'dropdown', None,
         '[\r\n  {\r\n    "key": "areaUnderROC", "value": "Area under ROC '
         '(Binary classification only)" \r\n  },\r\n  {\r\n    '
         '"key": "areaUnderPR", "value": "Area under PR (Binary classification'
         ' only)" \r\n  },\r\n  {\r\n    "key": "f1", "value": "F1 '
         '(Multiclass classification only)" \r\n  },\r\n  {\r\n    "key": '
         '"weightedPrecision", "value": "Weighted precision (Multiclass '
         'classification only)" \r\n  },\r\n  {\r\n    "key": "weightedRecall",'
         '"value": "Weighted recall (Multiclass classification only)" \r\n },'
         '\r\n  {\r\n    "key": "accuracy", "value": "Accuracy (Multiclass '
         'classification only)" \r\n  },\r\n  {\r\n    "key": "rmse", "value": '
         '"Root mean squared error  (Regression only)" \r\n  },\r\n  {\r\n    '
         '"mse": "mse", "value": "Mean squared error (Regression only)" \r\n },'
         '\r\n  {\r\n    "key": "mae", "value": "Mean absolute error  '
         '(Regression only)" \r\n  }\r\n]',
         'EXECUTION', 32),
        (102, 'type', 'TEXT', 1, 1, 'percent', 'dropdown', None,
         '[\r\n  {\r\n    "key": "percent", "value": "Sample a random '
         'percentage of data" \r\n  },\r\n  {\r\n    "key": "value", "value": '
         '"Sample N random records from data" \r\n  },\r\n  {\r\n    "key": '
         '"head", "value": "Extract top N records from data" \r\n  }\r\n]',
         'EXECUTION', 26),
        (103, 'fold_count', 'INTEGER', 1, 3, '10', 'integer', None, None,
         'EXECUTION', 24),
        (104, 'fold_size', 'INTEGER', 1, 4, '1000', 'integer', None, None,
         'EXECUTION', 24),
        (105, 'value', 'INTEGER', 1, 1, None, 'integer', None, None,
         'EXECUTION', 26),
        (106, 'estimator', 'TEXT', 1, 1, None, 'dropdown', None, None,
         'EXECUTION', 53),
        (107, 'evaluator', 'TEXT', 1, 2, None, 'dropdown', None, None,
         'EXECUTION', 53),
        (108, 'folds', 'INTEGER', 1, 3, None, 'integer', None, None,
         'EXECUTION', 53),
        (109, 'seed', 'INTEGER', 0, 4, None, 'integer', None, None, 'EXECUTION',
         53),
        (110, 'optimizer', 'TEXT', 1, 1, 'em', 'dropdown', None,
         '[\r\n  {\r\n    "key": "em", "value": "EM optimizer" \r\n  },\r\n  '
         '{\r\n    "key": "online", "value": "Online optimizer" \r\n  }\r\n]',
         'EXECUTION', 58),
        (111, 'type', 'TEXT', 1, 1, 'simple', 'dropdown', None,
         '[\r\n  {\r\n    "key": "simple", "value": "Simple, use spaces and '
         'puctuation as delimiters" \r\n  },\r\n  {\r\n    "key": "regex", '
         '"value": "Use regular expression to determine delimiters" \r\n  }]',
         'EXECUTION', 59),
        (112, 'expression', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION',
         59),
        (113, 'min_token_length', 'INTEGER', 0, 5, '2', 'integer', None, None,
         'EXECUTION', 59),
        (114, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 60),
        (115, 'alias', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION', 60),
        (116, 'stop_word_list', 'TEXT', 0, 3, None, 'textarea', None, None,
         'EXECUTION', 60),
        (117, 'stop_word_attribute', 'TEXT', 0, 4, None, 'attribute-selector',
         None, None, 'EXECUTION', 60),
        (118, 'case-sensitive', 'INTEGER', 1, 5, '0', 'checkbox', None, None,
         'EXECUTION', 60),
        (119, 'attributes', 'TEXT', 1, 2, None, 'attribute-selector', None,
         None, 'EXECUTION', 59),
        (120, 'alias', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION', 59),
        (121, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 62),
        (122, 'alias', 'TEXT', 1, 2, None, 'text', None, None, 'EXECUTION', 62),
        (123, 'type', 'TEXT', 1, 3, 'count', 'dropdown', None,
         '[\r\n  {\r\n    "key": "count", "value": "Count term frequency" \r\n}'
         ',\r\n  {\r\n    "key": "word2vec", "value": "Use word2vec algorithm"'
         ' \r\n  }\r\n]',
         'EXECUTION', 62),
        (124, 'vocab_size', 'INTEGER', 0, 4, None, 'integer', None, None,
         'EXECUTION', 62),
        (125, 'minimum_df', 'INTEGER', 0, 5, None, 'integer', None, None,
         'EXECUTION', 62),
        (126, 'number_of_topics', 'INTEGER', 1, 2, '10', 'integer', None, None,
         'EXECUTION', 58),
        (127, 'max_iteractions', 'INTEGER', 0, 3, '3', 'integer', None, None,
         'EXECUTION', 58),
        (128, 'minimum_tf', 'INTEGER', 0, 6, '1', 'integer', None, None,
         'EXECUTION', 62),
        (130, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 1),
        (131, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 1),
        (132, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 10),
        (133, 'shapefile', 'INTEGER', 1, 1, None, 'lookup',
         'http://beta.ctweb.inweb.org.br/limonero/datasources?'
         'token=123456&format=SHAPEFILE',
         None, 'EXECUTION', 63),
        (134, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 64),
        (135, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 64),
        (136, 'smoothing', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         64),
        (137, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 65),
        (138, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 65),
        (140, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 66),
        (141, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 66),
        (143, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 67),
        (144, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 67),
        (146, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 68),
        (147, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 68),
        (149, 'impurity', 'TEXT', 1, 1, 'gini', 'multi-select-dropdown', None,
         '[\r\n  {\r\n    "key": "gini", "value": "Gini" \r\n  },\r\n  {\r\n  '
         '  "key": "entropy", "value": "Entropy" \r\n  }\r\n]',
         'EXECUTION', 65),
        (150, 'report_name', 'TEXT', 1, 1, None, 'text', None, None,
         'EXECUTION', 69),
        (152, 'terms_per_topic', 'INTEGER', 1, 1, None, 'integer', None, None,
         'EXECUTION', 2),
        (153, 'terms_per_topic', 'INTEGER', 1, 2, None, 'integer', None, None,
         'EXECUTION', 2),
        (154, 'latitude', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 70),
        (155, 'polygon', 'TEXT', 1, 3, None, 'attribute-selector', None, None,
         'EXECUTION', 70),
        (156, 'number_of_clusters', 'INTEGER', 1, 1, None, 'integer', None,
         None, 'EXECUTION', 27),
        (157, 'type', 'TEXT', 1, 2, 'kmeans', 'dropdown', None,
         '[\r\n	{"key": "kmeans", "value": "Traditional K-Means"},\r\n	'
         '{"key": "bisecting", "value": "Bisecting K-Means"}\r\n]',
         'EXECUTION', 27),
        (158, 'init_mode', 'TEXT', 1, 3, 'k-means||', 'dropdown', None,
         '[\r\n	{"key": "k-means||", "value": "kmeans|| (kmeans++ variant)"},'
         '\r\n	{"key": "random", "value": "random"}\r\n]',
         'EXECUTION', 27),
        (159, 'max_iterations', 'INTEGER', 1, 4, None, 'integer', None, None,
         'EXECUTION', 27),
        (160, 'tolerance', 'FLOAT', 0, 1, '0.0001', 'decimal', None, None,
         'EXECUTION', 27),
        (161, 'number_of_clusters', 'INTEGER', 1, 1, None, 'integer', None,
         None, 'EXECUTION', 71),
        (162, 'max_iterations', 'INTEGER', 1, 4, None, 'integer', None, None,
         'EXECUTION', 71),
        (163, 'tolerance', 'FLOAT', 0, 1, '0.0001', 'decimal', None, None,
         'EXECUTION', 71),
        (164, 'n', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION',
         61),
        (165, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 61),
        (166, 'alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 61),
        (167, 'longitude', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 70),
        (168, 'polygon_attributes', 'TEXT', 0, 4, None, 'attribute-selector',
         None, None, 'EXECUTION', 70),
        (169, 'alias', 'TEXT', 0, 5, None, 'text', None, None, 'EXECUTION', 70),
        (170, 'doc_concentration', 'FLOAT', 0, 4, None, 'decimal', None, None,
         'EXECUTION', 58),
        (171, 'topic_concentration', 'FLOAT', 0, 5, None, 'decimal', None, None,
         'EXECUTION', 58),
        (172, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 73),
        (173, 'type', 'TEXT', 1, 2, 'SERVICE_INPUT', 'dropdown', None,
         '[\r\n  {"key": "SERVICE_INPUT", "value": "Read as web service '
         'input"}\r\n]',
         'EXECUTION', 73),
        (174, 'choose_input_2_if', 'TEXT', 1, 1, 'NEVER', 'dropdown', None,
         '[\r\n  {"key": "NEVER", "value": "Never choose input 2"},'
         '\r\n  {"key": "WEB_SERVICE", "value": "Workflow is running '
         'as a web service"}\r\n]',
         'EXECUTION', 72),
        (175, 'data_source', 'INTEGER', 1, 1, None, 'lookup',
         'http://ceweb.ctweb.inweb.org.br/datasources', None, 'EXECUTION', 76),
        (176, 'filter', 'TEXT', 1, 1, None, 'query_builder', None, None,
         'EXECUTION', 77),
        (177, 'rank', 'INTEGER', 1, 1, None, 'integer', None, None, 'EXECUTION',
         75),
        (178, 'max_iter', 'INTEGER', 0, 2, None, 'integer', None, None,
         'EXECUTION', 75),
        (179, 'user_col', 'TEXT', 1, 3, None, 'attribute-selector', None, None,
         'EXECUTION', 75),
        (180, 'item_col', 'TEXT', 1, 4, None, 'attribute-selector', None, None,
         'EXECUTION', 75),
        (
            181, 'rating_col', 'TEXT', 1, 5, None, 'attribute-selector', None,
            None,
            'EXECUTION', 75),
        (182, 'reg_param', 'FLOAT', 0, 6, None, 'decimal', None, None,
         'EXECUTION', 75),
        (183, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 34),
        (184, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 34),
        (185, 'prediction', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         34),
        (
            186, 'weight_col', 'TEXT', 0, 4, None, 'attribute-selector', None,
            None,
            'EXECUTION', 34),
        (187, 'family', 'TEXT', 1, 5, None, 'dropdown', None,
         '[\r\n  {"key": "auto", "value": "Auto"},\r\n  {"key": "binomial", '
         '"value": "Binomial"},\r\n  {"key": "multinomial", '
         '"value": "Multinomial"}\r\n]',
         'EXECUTION', 34),
        (188, 'title', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION', 84),
        (
            189, 'labels', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION',
            84),
        (190, 'id_attribute', 'TEXT', 1, 3, None, 'attribute-selector', None,
         None, 'EXECUTION', 84),
        (191, 'value_attribute', 'TEXT', 1, 4, None, 'attribute-selector', None,
         None, 'EXECUTION', 84),
        (192, 'orientation', 'TEXT', 0, 5, None, 'dropdown', None,
         '[\r\n{"key": "VERTICAL_BARS", "value": "Vertical bars"},\r\n'
         '{"key": "HORIZONTAL_BARS", "value": "Horizontal bars"}\r\n]',
         'EXECUTION', 84),
        (193, 'title', 'TEXT', 1, 1, None, 'text', None, None, 'EXECUTION', 25),
        (194, 'column_names', 'TEXT', 0, 1, None, 'text', None, None,
         'EXECUTION', 45),
        (195, 'title', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 45),
        (196, 'column_names', 'TEXT', 0, 1, None, 'text', None, None,
         'EXECUTION', 83),
        (197, 'title', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 83),
        (198, 'column_names', 'TEXT', 0, 1, None, 'text', None, None,
         'EXECUTION', 84),
        (199, 'title', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 84),
        (200, 'column_names', 'TEXT', 0, 1, None, 'text', None, None,
         'EXECUTION', 85),
        (201, 'title', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 85),
        (
            202, 'labels', 'TEXT', 0, 1, None, 'text', None, None, 'EXECUTION',
            86),
        (203, 'title', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 86),
        (
            204, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
            None,
            'EXECUTION', 87),
        (205, 'alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 87),
        (206, 'max_iter', 'INTEGER', 0, 3, '10', 'integer', None, None,
         'EXECUTION', 8),
        (207, 'weight', 'TEXT', 0, 4, None, 'attribute-selector', None, None,
         'EXECUTION', 8),
        (
            208, 'prediction', 'TEXT', 0, 5, None, 'attribute-selector', None,
            None,
            'EXECUTION', 8),
        (209, 'reg_param', 'FLOAT', 0, 6, None, 'decimal', None, None,
         'EXECUTION', 8),
        (210, 'solver', 'TEXT', 0, 7, None, 'lookup', None,
         '[\r\n  {"key": "auto", "value": "Auto"},\r\n  '
         '{"key": "normal", "value": "Normal"}\r\n]',
         'EXECUTION', 8),
        (211, 'elastic_net', 'FLOAT', 0, 8, None, 'decimal', None, None,
         'EXECUTION', 8),
        (212, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 8),
        (213, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 8),
        (214, 'attributes', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 90),
        (215, 'alias', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 90),
        (216, 'original_names', 'TEXT', 1, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 87),
        (217, 'features', 'TEXT', 1, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 89),
        (218, 'label', 'TEXT', 1, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 89),
        (219, 'prediction', 'TEXT', 0, 3, None, 'attribute-selector', None,
         None, 'EXECUTION', 89),
        (220, 'weight', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION',
         89),
        (221, 'isotonic', 'INTEGER', 0, 1, None, 'checkbox', None, None,
         'EXECUTION', 89),
        (222, 'attributes', 'TEXT', 0, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 95),
        (223, 'title', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 95),
        (224, 'calculate', 'TEXT', 0, 3, None, 'dropdown', None,
         '[\r\n  {\r\n    "key": "CORRELATION", "value": "Correlation"\r\n},'
         '\r\n  {\r\n    "key": "COVARIANCE", '
         '"value": "Covariance"\r\n  }\r\n]',
         'EXECUTION', 95),
        (225, 'attributes', 'TEXT', 0, 1, None, 'attribute-selector', None,
         None, 'EXECUTION', 96),
        (226, 'title', 'TEXT', 0, 2, None, 'text', None, None, 'EXECUTION', 96),
        (227, 'min_support', 'FLOAT', 1, 1, None, 'decimal', None, None,
         'EXECUTION', 3),
        (228, 'attribute', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 3)
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_field_table, rows)


# noinspection PyBroadException
def downgrade():
    try:
        op.execute(text('START TRANSACTION'))
        op.execute(text(
            'DELETE FROM operation_form_field WHERE form_id BETWEEN 1 AND 96'))

        op.execute(text(
            'DELETE FROM operation_form WHERE id BETWEEN 1 AND 96'))
        op.execute(
            text('DELETE FROM operation_category_translation '
                 'WHERE id BETWEEN 1 AND 26;'))

        op.execute(
            text('DELETE FROM operation_category_operation '
                 'WHERE operation_category_id BETWEEN 1 AND 26 '
                 'AND operation_id BETWEEN 1 AND 81 ;'))
        op.execute(
            text('DELETE FROM operation_category WHERE id BETWEEN 1 AND 26;'))
        op.execute(text('DELETE FROM operation WHERE id BETWEEN 1 AND 81;'))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise