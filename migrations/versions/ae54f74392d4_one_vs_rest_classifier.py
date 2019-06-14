# coding=utf-8
"""one vs rest classifier

Revision ID: ae54f74392d4
Revises: 049e8dab7779
Create Date: 2017-11-08 17:31:08.188091

"""
import json

from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'ae54f74392d4'
down_revision = '049e8dab7779'
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
    rows = [
        (94, 'one-vs-rest-classifier', 1, 'TRANSFORMATION', 'fa-window-close-o')
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in
            rows]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (94, 'en', 'One vs. rest classifier',
         'Reduction of multiclass classification to binary classification.'),
        (94, 'pt', 'Classificador 1 vs. resto',
         'Redução da classificação multiclasse para a classificação binária.'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    rows = [
        (94, 1),
    ]
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

    rows = [
        (215, 'INPUT', None, 94, 1, 'ONE', 'algorithm'),
        (216, 'OUTPUT', None, 94, 1, 'MANY', 'algorithm'),
    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    rows = [
        (215, 'en', 'algorithm', 'Algorithm'),
        (215, 'pt', 'algoritmo', 'Algoritmo'),

        (216, 'en', 'algorithm', 'Algorithm'),
        (216, 'pt', 'algoritmo', 'Algoritmo'),

    ]
    rows = [dict(list(zip([c.name for c in tb.columns], row))) for row in rows]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        (215, 5),
        (216, 5),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]
    op.bulk_insert(tb, rows)


def _insert_operation_script():
    tb = table(
        'operation_script',
        column('id', Integer),
        column('type', String),
        column('enabled', Integer),
        column('body', String),
        column('operation_id', Integer))

    columns = [c.name for c in tb.columns]
    data = [
        [42, 'JS_CLIENT', 1,
         "copyInputAddField(task, 'prediction', false, null);", 94],
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
        (94, 8),
        (94, 18),
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
        (119, 1, 1, 'paramgrid'),
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
        (94, 119),
        (94, 110),
        (94, 41),
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
        (119, 'en', 'Param grid'),
        (119, 'pt', 'Grade de parâmetros'),
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
        # For SVM operation
        [370, 'max_iter', 'INTEGER', 0, 1, None, 'integer', None, None,
         'EXECUTION', 9],
        [371, 'standardization', 'INTEGER', 0, 2, 1, 'checkbox', None, None,
         'EXECUTION', 9],
        [372, 'threshold', 'FLOAT', 0, 3, None, 'decimal', None, None,
         'EXECUTION', 9],
        [373, 'tol', 'FLOAT', 0, 4, None, 'decimal', None, None,
         'EXECUTION', 9],
        [374, 'weight_attr', 'TEXT', 0, 5, None, 'attribute-selector', None,
         None, 'EXECUTION', 9],

        # For NaiveBayes
        [375, 'model_type', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([
             {'key': 'multinomial', 'value': 'Multinomial (default)'},
             {'key': 'bernoulli', 'value': 'Bernoulli'}]), 'EXECUTION', 64],
        [377, 'thresholds', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         64],
        [378, 'weight_attr', 'TEXT', 0, 5, None, 'attribute-selector', None,
         None, 'EXECUTION', 64],

        # For Perceptron
        [379, 'block_size', 'INTEGER', 0, 1, '128', 'integer', None, None,
         'EXECUTION', 68],
        [380, 'max_iter', 'INTEGER', 0, 2, None, 'integer', None, None,
         'EXECUTION', 68],
        [381, 'seed', 'INTEGER', 0, 3, None, 'integer', None, None,
         'EXECUTION', 68],
        [382, 'solver', 'TEXT', 0, 4, None, 'dropdown', None,
         json.dumps([
             {'key': 'l-bfgs', 'value': 'l-bfgs'},
             {'key': 'gd', 'value': 'gd'}]), 'EXECUTION', 68],
        [383, 'step_size', 'INTEGER', 0, 5, None, 'integer', None, None,
         'EXECUTION', 69],
        [384, 'tol', 'FLOAT', 0, 6, None, 'decimal', None, None,
         'EXECUTION', 69],

        # Decision Tree
        [385, 'cache_node_ids', 'INTEGER', 0, 1, 1, 'checkbox', None, None,
         'EXECUTION', 66],
        [386, 'check_point_interval', 'INTEGER', 0, 2, None, 'integer', None,
         None, 'EXECUTION', 66],
        [387, 'max_bins', 'INTEGER', 0, 3, None, 'integer', None,
         None, 'EXECUTION', 66],
        [388, 'max_depth', 'INTEGER', 0, 4, None, 'integer', None,
         None, 'EXECUTION', 66],
        [389, 'min_info_gain', 'FLOAT', 0, 5, None, 'decimal', None, None,
         'EXECUTION', 66],
        [390, 'min_instances_per_node', 'INTEGER', 0, 6, 1, 'integer', None,
         None, 'EXECUTION', 66],
        [391, 'impurity', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([
             {'key': 'entropy', 'value': 'Entropy'},
             {'key': 'gini', 'value': 'Gini'}]), 'EXECUTION', 66],

        # GBT
        [392, 'cache_node_ids', 'INTEGER', 0, 1, 1, 'checkbox', None, None,
         'EXECUTION', 67],
        [393, 'check_point_interval', 'INTEGER', 0, 2, None, 'integer', None,
         None, 'EXECUTION', 67],
        [394, 'loss_type', 'TEXT', 0, 3, 'logistic', 'dropdown', None,
         json.dumps([
             {'key': 'logistic', 'value': 'Logistic'}]), 'EXECUTION', 67],
        [395, 'max_bins', 'INTEGER', 0, 4, None, 'integer', None,
         None, 'EXECUTION', 67],
        [396, 'max_depth', 'INTEGER', 0, 5, None, 'integer', None,
         None, 'EXECUTION', 67],
        [397, 'max_iter', 'INTEGER', 0, 6, None, 'integer', None, None,
         'EXECUTION', 67],
        [398, 'min_info_gain', 'FLOAT', 0, 7, None, 'decimal', None, None,
         'EXECUTION', 67],
        [399, 'min_instances_per_node', 'INTEGER', 0, 8, 1, 'integer', None,
         None, 'EXECUTION', 67],
        [400, 'step_size', 'INTEGER', 0, 9, None, 'integer', None, None,
         'EXECUTION', 67],
        [401, 'subsampling_rate', 'FLOAT', 0, 5, None, 'decimal', None, None,
         'EXECUTION', 67],

        # Random forest
        [402, 'cache_node_ids', 'INTEGER', 0, 1, 1, 'checkbox', None, None,
         'EXECUTION', 65],
        [403, 'check_point_interval', 'INTEGER', 0, 2, None, 'integer', None,
         None, 'EXECUTION', 65],
        [404, 'feature_subset_strategy', 'TEXT', 0, 3, None, 'select2', None,
         json.dumps([
             {'key': 'auto', 'value': 'Auto'},
             {'key': 'all', 'value': 'All'},
             {'key': 'onethird', 'value': 'One third'},
             {'key': 'sqrt', 'value': 'SQRT'},
             {'key': 'log2', 'value': 'LOG2'},
             {'key': '(0.0-1.0]', 'value': '(0.0-1.0]'},
             {'key': '[1-n]', 'value': '[1-n]'},
         ]), 'EXECUTION', 65],

        [406, 'max_bins', 'INTEGER', 0, 5, None, 'integer', None,
         None, 'EXECUTION', 65],
        [407, 'max_depth', 'INTEGER', 0, 6, None, 'integer', None,
         None, 'EXECUTION', 65],
        [408, 'min_info_gain', 'FLOAT', 0, 7, None, 'decimal', None, None,
         'EXECUTION', 65],
        [409, 'min_instances_per_node', 'INTEGER', 0, 8, 1, 'integer', None,
         None, 'EXECUTION', 65],
        [410, 'num_trees', 'INTEGER', 0, 9, 20, 'integer', None,
         None, 'EXECUTION', 65],
        [411, 'subsampling_rate', 'FLOAT', 0, 10, '1.0', 'decimal', None, None,
         'EXECUTION', 65],

        # Logistic regression
        [412, 'aggregation_depth', 'INTEGER', 0, 1, '2', 'integer', None, None,
         'EXECUTION', 34],
        [413, 'elastic_net_param', 'FLOAT', 0, 2, '0.0', 'decimal', None, None,
         'EXECUTION', 34],
        [414, 'fit_intercept', 'INTEGER', 0, 3, '1', 'checkbox', None, None,
         'EXECUTION', 34],
        [415, 'max_iter', 'INTEGER', 0, 4, None, 'integer', None, None,
         'EXECUTION', 34],
        [416, 'reg_param', 'FLOAT', 0, 5, '0.0', 'decimal', None, None,
         'EXECUTION', 34],
        [417, 'tol', 'FLOAT', 0, 4, None, 'decimal', None, None,
         'EXECUTION', 34],
        [418, 'threshold', 'FLOAT', 0, 3, None, 'decimal', None, None,
         'EXECUTION', 34],
        [419, 'thresholds', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         34],
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
        [370, 'en',
         'Max. iterations',
         'Max number of iterations (>=0).'],
        [370, 'pt', 'Iterações máximas',
         'Número máximo de iterações (>=0).'],

        [371, 'en',
         'Apply standardization',
         'Whether to standardize the training features '
         'before fitting the model.'],
        [371, 'pt', 'Aplicar padronização',
         'Indica se é para padronizar as features de treinamento antes '
         'de ajustar o model.'],

        [372, 'en',
         'Threshold for binary classification',
         'The threshold in binary classification applied to the '
         'linear model prediction'],
        [372, 'pt', 'Limiar para a classificação binária',
         'Limiar na classificação binária aplicada ao modelo '
         'de predição linear'],

        [373, 'en',
         'Convergence tolerance',
         'The convergence tolerance for iterative algorithms (>= 0).'],
        [373, 'pt', 'Tolerância para a convergência',
         'Tolerância de convergência para algoritmos iterativos  (>= 0).'],

        [374, 'en',
         'Weight attribute',
         'Attribute with weights. If empty, all instances have the '
         'same weight (1.0);'],
        [374, 'pt', 'Atributo com pesos',
         'Atributo com pesos. Se não informado, todas as instâncias têm o mesmo'
         'peso (1.0).'],

        # For NaiveBayes
        [375, 'en', 'Model type', 'Model type', ],
        [375, 'pt', 'Tipo de modelo', 'Tipo de modelo'],

        [377, 'en', 'Thresholds', 'Thresholds', ],
        [377, 'pt', 'Limiares', 'Limiares'],

        [378, 'en', 'Weight attribute', 'Weight attribute', ],
        [378, 'pt', 'Atributo com os pesos', 'Atributo com os pesos'],

        # For Perceptron
        [379, 'en', 'Block size', 'Block size', ],
        [379, 'pt', 'Tamanho do bloco', 'Tamanho do bloco'],

        [380, 'en', 'Max iterations', 'Max iterations', ],
        [380, 'pt', 'Iterações máximas', 'Iterações máximas'],

        [381, 'en', 'Seed (random number generation)',
         'Seed (random number generation)', ],
        [381, 'pt', 'Semente (para geração de números aleatórios)',
         'Semente (para geração de números aleatórios)'],

        [382, 'en', 'Solver', 'Solver', ],
        [382, 'pt', 'Solucionador', 'Solucionador'],

        [383, 'en', 'Step size', 'Step size', ],
        [383, 'pt', 'Tamanho do passo', 'Tamanho do passo'],

        [384, 'en', 'Tolerance', 'Tolerance', ],
        [384, 'pt', 'Tolerância', 'Tolerância'],

        # Decision Tree
        [385, 'en', 'Cache node ids.', 'Cache node ids.', ],
        [385, 'pt', 'Manter identificadores dos nós em cache',
         'Manter identificadores dos nós em cache'],

        [386, 'en', 'Check point interval (cache)',
         'Check point interval (cache)', ],
        [386, 'pt', 'Intervalo para checkpoint (cache)',
         'Intervalo para checkpoint (cache)'],

        [387, 'en', 'Max bins', 'Max bins', ],
        [387, 'pt', 'No. máximo de bins', 'No. máximo de bins'],

        [388, 'en', 'Max depth', 'Max depth', ],
        [388, 'pt', 'Profundidade máxima', 'Profundidade máxima'],

        [389, 'en', 'Min info gain', 'Min info gain', ],
        [389, 'pt', 'Ganho mínimo de informação', 'Ganho mínimo de informação'],

        [390, 'en', 'Min instances per node', 'Min instances per node', ],
        [390, 'pt', 'Mínimo de instâncias por nó',
         'Mínimo de instâncias por nó'],

        [391, 'en', 'Impurity', 'Impurity', ],
        [391, 'pt', 'Impureza', 'Impureza'],

        # GBT
        [392, 'en', 'Cache node ids.', 'Cache node ids.', ],
        [392, 'pt', 'Manter identificadores dos nós em cache',
         'Manter identificadores dos nós em cache'],

        [393, 'en', 'Check point interval (cache)',
         'Check point interval (cache)', ],
        [393, 'pt', 'Intervalo para checkpoint (cache)',
         'Intervalo para checkpoint (cache)'],

        [394, 'en', 'Loss type', 'Loss type', ],
        [394, 'pt', 'Tipo de perda', 'Tipo de perda'],

        [395, 'en', 'Max bins', 'Max bins', ],
        [395, 'pt', 'No. máximo de bins', 'No. máximo de bins'],

        [396, 'en', 'Max depth', 'Max depth', ],
        [396, 'pt', 'Profundidade máxima', 'Profundidade máxima'],

        [397, 'en', 'Max iterations', 'Max iterations', ],
        [397, 'pt', 'Iterações máximas', 'Iterações máximas'],

        [398, 'en', 'Min info gain', 'Min info gain', ],
        [398, 'pt', 'Ganho mínimo de informação', 'Ganho mínimo de informação'],

        [399, 'en', 'Min instances per node', 'Min instances per node', ],
        [399, 'pt', 'Mínimo de instâncias por nó',
         'Mínimo de instâncias por nó'],

        [400, 'en', 'Step size', 'Step size', ],
        [400, 'pt', 'Tamanho do passo', 'Tamanho do passo'],

        [401, 'en', 'Subsampling rate', 'Subsampling rate', ],
        [401, 'pt', 'Taxa de subamostragem', 'Taxa de subamostragem'],

        # Random forest
        [402, 'en', 'Cache node ids.', 'Cache node ids.', ],
        [402, 'pt', 'Manter identificadores dos nós em cache',
         'Manter identificadores dos nós em cache'],

        [403, 'en', 'Check point interval (cache)',
         'Check point interval (cache)', ],
        [403, 'pt', 'Intervalo para checkpoint (cache)',
         'Intervalo para checkpoint (cache)'],

        [404, 'en', 'Feature subset strategy', 'Feature subset strategy', ],
        [404, 'pt', 'Estratégia para subconjunto de features',
         'Estratégia para subconjunto de features'],

        [406, 'en', 'Max bins', 'Max bins', ],
        [406, 'pt', 'No. máximo de bins', 'No. máximo de bins'],

        [407, 'en', 'Max depth', 'Max depth', ],
        [407, 'pt', 'Profundidade máxima', 'Profundidade máxima'],

        [408, 'en', 'Min info gain', 'Min info gain', ],
        [408, 'pt', 'Ganho mínimo de informação', 'Ganho mínimo de informação'],

        [409, 'en', 'Min instances per node', 'Min instances per node', ],
        [409, 'pt', 'Mínimo de instâncias por nó',
         'Mínimo de instâncias por nó'],

        [410, 'en', 'Number of trees', 'Number of trees', ],
        [410, 'pt', 'Número de árvores', 'Número de árvores'],

        [411, 'en', 'Subsampling rate', 'Subsampling rate', ],
        [411, 'pt', 'Taxa de subamostragem', 'Taxa de subamostragem'],

        # Logistic regression
        [412, 'en', 'Aggregation depth', 'Aggregation depth', ],
        [412, 'pt', 'Profundidade de agregação', 'Profundidade de agregação'],

        [413, 'en', 'Elastic Net param', 'Elastic Net param', ],
        [413, 'pt', 'Parâmetro para a Elastic Net',
         'Parâmetro para a Elastic Net'],

        [414, 'en', 'Fit intercept', 'Fit intercept', ],
        [414, 'pt', 'Interseção ajustada', 'Interseção ajustada'],

        [415, 'en', 'Max iterations', 'Max iterations', ],
        [415, 'pt', 'Iterações máximas', 'Iterações máximas'],

        [416, 'en', 'Regularization parameter', 'Regularization parameter', ],
        [416, 'pt', 'Parâmetro para regularização',
         'Parâmetro para regularização'],

        [417, 'en', 'Tolerance', 'Tolerance', ],
        [417, 'pt', 'Tolerância', 'Tolerância'],

        [418, 'en', 'Threshold in binary classification prediction',
         'Threshold in binary classification prediction', ],
        [418, 'pt', 'Limiar para classificação binária',
         'Limiar para classificação binária'],

        [419, 'en', 'Thresholds in multi-class classification',
         'Thresholds in multi-class classification to adjust '
         'the probability of predicting each class.', ],
        [419, 'pt', 'Limiar para classificação multiclasse',
         'Limiar para classificação multiclasse para ajustar a probabilidade '
         'de predizer cada classe'],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation, 'DELETE FROM operation WHERE id BETWEEN 94 AND 94'),

    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 94 AND 94'),
    (_insert_operation_port,
     'DELETE FROM operation_port '
     'WHERE (operation_id BETWEEN 94 AND 94)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN '
     '(SELECT id FROM operation_port '
     '  WHERE (operation_id BETWEEN 94 AND 94))'),
    (_insert_operation_script,
     [
         'DELETE FROM operation_script WHERE operation_id BETWEEN 94 AND 94',
     ]
     ),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (SELECT id FROM operation_port '
     'WHERE (operation_id BETWEEN 94 AND 94))'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation '
     'WHERE operation_id BETWEEN 94 AND 94;'),
    (_insert_operation_platform, 'DELETE FROM operation_platform '
                                 'WHERE operation_id BETWEEN 94 AND 94'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 119 AND 119'),
    (_insert_operation_operation_form, 'DELETE FROM operation_operation_form '
                                       'WHERE operation_id BETWEEN 94 AND 94'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 119 AND 119'),

    (_insert_operation_form_field,
     """DELETE FROM operation_form_field
        WHERE id BETWEEN 370 AND 419 """),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id BETWEEN 370 AND 419 '),

    (""" UPDATE operation_form_translation
         SET name = 'Param grid' WHERE id = 34 AND locale = 'en' """,
     """ UPDATE operation_form_translation
         SET name = 'Execution' WHERE id = 34 AND locale = 'en' """,
     ),

    (""" UPDATE operation_form_translation
         SET name = 'Grade de parâmetros' WHERE id = 34 AND locale = 'pt' """,
     """ UPDATE operation_form_translation
         SET name = 'Execução' WHERE id = 34 AND locale = 'pt' """,
     ),
    (""" UPDATE operation_form SET category = 'paramgrid' WHERE id = 34 """,
     """ UPDATE operation_form SET category = 'execution' WHERE id = 34 """),

    (""" UPDATE operation_form_translation
         SET name = 'Param grid' WHERE id = 9 AND locale = 'en' """,
     """ UPDATE operation_form_translation
         SET name = 'Execution' WHERE id = 9 AND locale = 'en' """,
     ),

    (""" UPDATE operation_form_translation
         SET name = 'Grade de parâmetros' WHERE id = 9 AND locale = 'pt' """,
     """ UPDATE operation_form_translation
         SET name = 'Execução' WHERE id = 9 AND locale = 'pt' """,
     ),
    (""" UPDATE operation_form SET category = 'paramgrid' WHERE id = 9 """,
     """ UPDATE operation_form SET category = 'execution' WHERE id = 9 """),

    (""" INSERT INTO operation_form_field_translation (id, locale, label, help)
        VALUES(130, 'pt', 'Atributo com features', 'Atributo com features')""",
     """ DELETE FROM operation_form_field_translation WHERE id = 130 AND
        locale = 'pt' """),

    (""" INSERT INTO operation_form_field_translation (id, locale, label, help)
        VALUES(131, 'pt', 'Atributo com o rótulo', 'Atributo com o rótulo')""",
     """ DELETE FROM operation_form_field_translation WHERE id = 131 AND
        locale = 'pt' """),

    (""" DELETE FROM operation_form_field_translation WHERE id = 185 """,
     [""" INSERT INTO operation_form_field_translation (id, locale, label, help)
        VALUES(185, 'pt', 'Predição (novo atributo)',
        'Predição (novo atributo)') """,
      """ INSERT INTO operation_form_field_translation (id, locale, label, help)
        VALUES(185, 'en', 'Prediction attribute', 'Prediction attribute')"""]),

    (""" DELETE FROM operation_form_field WHERE id = 185 """,
     """
        INSERT INTO operation_form_field(id, name, `type`, required, `order`,
            suggested_widget, scope, form_id) VALUES (185, 'prediction', 'TEXT',
            0, 3, 'text', 'EXECUTION', 34)
    """),
    ("""UPDATE operation_form_field SET
    suggested_widget = 'dropdown' WHERE id = 149""",
     """UPDATE operation_form_field SET suggested_widget =
        'multi-select-dropdown' WHERE id = 149"""),

    ("""UPDATE operation_form_field SET
    suggested_widget = 'decimal', `type` = 'FLOAT' WHERE id = 136""",
     """UPDATE operation_form_field SET suggested_widget =
     'text' , `type` = 'TEXT' WHERE id = 136""")
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
    session.commit()
