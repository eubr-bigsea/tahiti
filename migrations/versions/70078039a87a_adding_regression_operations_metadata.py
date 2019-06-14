# -*- coding: utf-8 -*-
"""adding regression operations metadata

Revision ID: 70078039a87a
Revises: 2af6ef956270
Create Date: 2017-07-12 15:40:28.744981

"""
import json

from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.sql import table, column, text
import collections

# revision identifiers, used by Alembic.
revision = '70078039a87a'
down_revision = '2af6ef956270'
branch_labels = None
depends_on = None

REGRESSION_MODEL = 73
ISOTONIC_REGRESSION = 74
AFT_SURVIVAL_REGRESSION = 76
GBT_REGRESSOR = 77
RANDOM_FOREST_REGRESSOR = 78
GENERALIZED_LINEAR_REGRESSOR = 79


def _insert_operation_form():
    tb = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (102, 1, 1, 'execution'),  # regression-model
        (103, 1, 1, 'execution'),  # isotonic-regression
        (104, 1, 1, 'execution'),  # aft-survival-regression
        (105, 1, 1, 'execution'),  # gbt-regressor
        (106, 1, 1, 'execution'),  # random-forest-regressor
        (107, 1, 1, 'execution'),  # generalized-linear-regressor
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
        [REGRESSION_MODEL, 102],
        [ISOTONIC_REGRESSION, 103],
        [AFT_SURVIVAL_REGRESSION, 104],
        [GBT_REGRESSOR, 105],
        [RANDOM_FOREST_REGRESSOR, 106],
        [GENERALIZED_LINEAR_REGRESSOR, 107],

        [REGRESSION_MODEL, 41],
        [ISOTONIC_REGRESSION, 41],
        [AFT_SURVIVAL_REGRESSION, 41],
        [GBT_REGRESSOR, 41],
        [RANDOM_FOREST_REGRESSOR, 41],
        [GENERALIZED_LINEAR_REGRESSOR, 41],
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
        (102, 'en', 'Execution'),
        (102, 'pt', 'Execução'),

        (103, 'en', 'Execution'),
        (103, 'pt', 'Execução'),

        (104, 'en', 'Execution'),
        (104, 'pt', 'Execução'),

        (105, 'en', 'Execution'),
        (105, 'pt', 'Execução'),

        (106, 'en', 'Execution'),
        (106, 'pt', 'Execução'),

        (107, 'en', 'Execution'),
        (107, 'pt', 'Execução'),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _fix_linear_regression_fields():
    op.execute('DELETE FROM operation_form_field_translation '
               'WHERE id IN (208, 212, 213)')
    op.execute('DELETE FROM operation_form_field '
               'WHERE id IN (208, 212, 213)')
    op.execute("UPDATE operation_form_field_translation "
               "SET label = 'Weight attribute (optional)', "
               "help = 'Weight attribute (optional)' "
               "WHERE id = 207 AND locale = 'en' ")

    op.execute(
        "UPDATE operation_form_field SET `values` = '{}' WHERE id = 210".format(
            json.dumps([
                {"key": "auto", "value": "Auto (selected automatically)"},
                {"key": "normal", "value": "Normal Equation"},
                {"key": "l-bfgs", "value": "Limited-memory BFGS"}
            ])
        ))


def _revert_fix_linear_regression_fields():
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
        [212, 'features', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 8],
        [213, 'label', 'TEXT', 0, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 8],
        [208, 'prediction', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         8]]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = [c.name for c in tb.columns]
    data = [
        [212, 'en', 'Features', 'Features'],
        [213, 'en', 'Label', 'Label'],
        [208, 'en', 'Prediction', 'Prediction'],
        [212, 'pt', 'Features', 'Features'],
        [213, 'pt', 'Label', 'Label'],
        [208, 'pt', 'Prediction', 'Prediction'], ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

    op.execute("UPDATE operation_form_field_translation "
               "SET label = 'Weigth attribute (optional)', "
               "help = 'Weigth attribute (optional)' "
               "WHERE id = 207 AND locale = 'en' ")

    op.execute(
        "UPDATE operation_form_field SET `values` = '{}' WHERE id = 210".format(
            json.dumps([
                {"key": "auto", "value": "Auto"},
                {"key": "normal", "value": "Normal"}
            ])
        ))


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
        [242, 'features', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
         'EXECUTION', 102],
        [243, 'label', 'TEXT', 0, 2, None, 'attribute-selector', None, None,
         'EXECUTION', 102],
        [244, 'prediction', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         102],
        [245, 'max_iter', 'INTEGER', 0, 4, None, 'integer', None, None,
         'EXECUTION', 102],
        [246, 'weight', 'TEXT', 0, 5, None, 'attribute-selector', None, None,
         'EXECUTION', 102],
        [247, 'reg_param', 'DECIMAL', 0, 6, None, 'decimal', None, None,
         'EXECUTION', 102],
        [248, 'elastic_net', 'DECIMAL', 0, 7, None, 'decimal', None, None,
         'EXECUTION', 102],

        # [250, 'features', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
        #  'EXECUTION', 103],
        # [251, 'label', 'TEXT', 0, 2, None, 'attribute-selector', None, None,
        #  'EXECUTION', 103],
        # [252, 'prediction', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
        #  103],
        [253, 'weight', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION',
         103],
        [254, 'isotonic', 'TEXT', 0, 5, None, 'dropdown', None,
         json.dumps([{"key": True, "value": "Isotonic/increasing"},
                     {"key": False, "value": "Orantitonic/decreasing"}, ]),
         'EXECUTION', 103],

        # [255, 'features', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
        #  'EXECUTION', 104],
        # [256, 'label', 'TEXT', 0, 2, None, 'attribute-selector', None, None,
        #  'EXECUTION', 104],
        # [257, 'prediction', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
        #  104],
        [258, 'weight', 'TEXT', 0, 4, None, 'text', None, None, 'EXECUTION',
         104],
        [260, 'max_iter', 'INTEGER', 0, 6, None, 'integer', None, None,
         'EXECUTION', 104],
        [261, 'aggregation_depth', 'INTEGER', 0, 7, None, 'integer', None, None,
         'EXECUTION', 104],
        [262, 'seed', 'INTEGER', 0, 8, None, 'integer', None, None,
         'EXECUTION', 104],
        [263, 'censor', 'INTEGER', 0, 9, None, 'attribute-selector', None, None,
         'EXECUTION', 104],
        [264, 'quantile_probabilities', 'INTEGER', 0, 10, None, 'integer', None,
         None,
         'EXECUTION', 104],
        [265, 'quantiles_col', 'TEXT', 0, 11, None, 'text', None,
         None,
         'EXECUTION', 104],

        # [266, 'features', 'TEXT', 0, 1, None, 'attribute-selector', None, None,
        #  'EXECUTION', 105],
        # [267, 'label', 'TEXT', 0, 2, None, 'attribute-selector', None, None,
        #  'EXECUTION', 105],
        # [268, 'prediction', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
        #  105],
        [269, 'max_iter', 'INTEGER', 0, 4, None, 'integer', None, None,
         'EXECUTION', 105],
        [270, 'max_depth', 'INTEGER', 0, 5, None, 'integer', None, None,
         'EXECUTION', 105],
        [271, 'min_instance', 'INTEGER', 0, 6, None, 'integer', None, None,
         'EXECUTION', 105],
        [272, 'min_info_gain', 'DECIMAL', 0, 7, None, 'decimal', None, None,
         'EXECUTION', 105],
        [273, 'seed', 'INTEGER', 0, 8, None, 'integer', None, None,
         'EXECUTION', 105],

        [274, 'max_depth', 'INTEGER', 0, 1, None, 'integer', None, None,
         'EXECUTION', 106],
        [275, 'max_bins', 'INTEGER', 0, 2, None, 'integer', None, None,
         'EXECUTION', 106],
        [276, 'min_info_gain', 'DECIMAL', 0, 3, None, 'decimal', None, None,
         'EXECUTION',
         106],
        [277, 'num_trees', 'INTEGER', 0, 1, None, 'integer', None, None,
         'EXECUTION', 106],
        [278, 'feature_subset_strategy', 'TEXT', 0, 2, None, 'dropdown', None,
         json.dumps([{"key": "auto", "value": "auto"},
                     {"key": "all", "value": "all"},
                     {"key": "onethird", "value": "onethird"},
                     {"key": "sqrt", "value": "sqrt"},
                     {"key": "log2", "value": "log2"}, ]),
         'EXECUTION', 106],

        # [279, 'prediction', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
        #  107],

        [280, 'weight', 'TEXT', 0, 3, None, 'text', None, None, 'EXECUTION',
         107],
        [281, 'max_iter', 'INTEGER', 0, 2, None, 'integer', None, None,
         'EXECUTION', 107],
        [282, 'family', 'TEXT', 0, 0, None, 'dropdown', None,
         json.dumps([{"key": "gaussian", "value": "Gaussian"},
                     {"key": "binomial", "value": "Binomial"},
                     {"key": "poisson", "value": "Poisson"},
                     {"key": "gamma", "value": "Gamma"}, ]),
         'EXECUTION', 107],
        [283, 'link', 'TEXT', 0, 1, None, 'dropdown', None,
         json.dumps([{"key": "identity", "value": "Identity (Gaussian)"},
                     {"key": "log", "value": "log (Gaussian)"},
                     {"key": "inverse", "value": "inverse(Gaussian)"},
                     {"key": "logit", "value": "logit (Binomial)"},
                     {"key": "probit", "value": "probit (Binomial)"},
                     {"key": "cloglog", "value": "cloglog (Binomial)"},
                     {"key": "log", "value": "log (Poisson)"},
                     {"key": "identity", "value": "identity (Poisson)"},
                     {"key": "sqrt", "value": "sqrt (Poisson)"},
                     {"key": "inverse", "value": "inverse (Gamma)"},
                     {"key": "identity", "value": "identity (Gamma)"},
                     {"key": "log", "value": "log (Gamma)"}, ]),
         'EXECUTION', 107],
        [284, 'reg_param', 'DECIMAL', 0, 2, None, 'decimal', None, None,
         'EXECUTION', 107],
        [285, 'solver', 'TEXT', 0, 6, None, 'dropdown', None,
         json.dumps([{"key": "auto", "value": "Auto"},
                     {"key": "irls", "value": "irls"}]), 'EXECUTION',
         107],

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
        [242, 'en', 'Features', 'Features'],
        [243, 'en', 'Label', 'Label'],
        [244, 'en', 'Prediction', 'Prediction'],
        [245, 'en', 'Max. iterations', 'Max. iterations'],
        [246, 'en', 'Weight', 'Weight'],
        [247, 'en', 'Regularization', 'Regularization'],
        [248, 'en', 'ElasticNet mixing', 'ElasticNet mixing'],

        [253, 'en', 'Weight', 'Weight'],
        [254, 'en', 'Isotonic', 'Isotonic'],

        [258, 'en', 'Weight', 'Weight'],
        [260, 'en', 'Max. iterations', 'Maximum number of iterations'],
        [261, 'en', 'Aggregation depth', 'Aggregation depth'],
        [262, 'en', 'Seed', 'Seed'],
        [263, 'en', 'Censor', 'Censor'],
        [264, 'en', 'Quantile probabilities', 'Quantile probabilities'],
        [265, 'en', 'Quantiles attribute', 'Quantiles attribute'],

        [269, 'en', 'Max. iterations', 'Maximum number of iterations'],
        [270, 'en', 'Max. depth', 'Max. depth'],
        [271, 'en', 'Min. instance', 'Min. instance'],
        [272, 'en', 'Min. info gain', 'Min. info gain'],
        [273, 'en', 'Seed', 'Seed'],

        [274, 'en', 'Max. depth', 'Max. depth'],
        [275, 'en', 'Max. bins', 'Max. bins'],
        [276, 'en', 'Min. info gain', 'Min. info gain'],
        [277, 'en', 'Number of trees', 'Number of trees'],
        [278, 'en', 'Feature subset strategy', 'Feature subset strategy'],

        [280, 'en', 'Weight', 'Weight'],
        [281, 'en', 'Max. iterations', 'Maximum number of iterations'],
        [282, 'en', 'Family', 'Family'],
        [283, 'en', 'Link prediction', 'Link prediction'],
        [284, 'en', 'Regularization', 'Regularization'],
        [285, 'en', 'Solver', 'Solver'],

        [245, 'pt', 'Max. iterations', 'Max. iterations'],
        [246, 'pt', 'Weight', 'Weight'],
        [247, 'pt', 'Regularization', 'Regularization'],
        [248, 'pt', 'ElasticNet mixing', 'ElasticNet mixing'],

        [253, 'pt', 'Weight', 'Weight'],
        [254, 'pt', 'Isotonic', 'Isotonic'],

        [258, 'pt', 'Weight', 'Weight'],
        [260, 'pt', 'Max. iterations', 'Maximum number of iterations'],
        [261, 'pt', 'Aggregation depth', 'Aggregation depth'],
        [262, 'pt', 'Seed', 'Seed'],
        [263, 'pt', 'Censor', 'Censor'],
        [264, 'pt', 'Quantile probabilities', 'Quantile probabilities'],
        [265, 'pt', 'Quantiles attribute', 'Quantiles attribute'],

        [269, 'pt', 'Max. iterations', 'Maximum number of iterations'],
        [270, 'pt', 'Max. depth', 'Max. depth'],
        [271, 'pt', 'Min. instance', 'Min. instance'],
        [272, 'pt', 'Min. info gain', 'Min. info gain'],
        [273, 'pt', 'Seed', 'Seed'],

        [274, 'pt', 'Profundidade máxima', 'Profundidade máxima'],
        [275, 'pt', 'Máximo de bins', 'Máximo de bins'],
        [276, 'pt', 'Ganho de informação (info gain) mínimo',
         'Ganho de informação (info gain) mínimo'],
        [277, 'pt', 'Número de árvores', 'Número de árvores'],
        [278, 'pt', 'Estratégia para subconjuto de features',
         'Estratégia para subconjuto de features'],

        [280, 'pt', 'Weight', 'Weight'],
        [281, 'pt', 'Max. iterations', 'Maximum number of iterations'],
        [282, 'pt', 'Família', 'Família'],
        [283, 'pt', 'Link prediction', 'Link prediction'],
        [284, 'pt', 'Regularization', 'Regularization'],
        [285, 'pt', 'Solver', 'Solver'],

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("INSERT INTO operation_script "
     "VALUES (28, 'JS_CLIENT', '1', 'copyInputAddField(task, \\'prediction\\', "
     "false, \\'prediction\\');', '73'); ", "DELETE FROM operation_script WHERE id = 28"),
    (_fix_linear_regression_fields, _revert_fix_linear_regression_fields),
    ("UPDATE operation_port_interface_operation_port "
     "SET operation_port_interface_id = 17 WHERE operation_port_id = 14",
     "UPDATE operation_port_interface_operation_port "
     "SET operation_port_interface_id = 1 WHERE operation_port_id = 14"),
    ("UPDATE operation_port_interface SET color = '#808000' WHERE id = 17",
     "UPDATE operation_port_interface SET color = 'pink' WHERE id = 17",),
    # ("INSERT INTO operation_form_translation VALUES(41, 'en', 'Appearance');",
    #  'DELETE FROM operation_form_translation  WHERE id = 41'),
    # (u"INSERT INTO operation_form_translation VALUES(41, 'pt', 'Aparência');",
    #  'DELETE FROM operation_form_translation  WHERE id = 41'),
    ('INSERT INTO operation_operation_form VALUES(75, 41);',
     'DELETE FROM operation_operation_form WHERE operation_id = 75 '
     'AND operation_form_id = 41;'),
    ('INSERT INTO operation_operation_form VALUES(75, 41);',
     'DELETE FROM operation_operation_form WHERE operation_id = 75 '
     'AND operation_form_id = 41;'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN {0} AND {1}'.format(102,
                                                                      107)),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id IN ({0}, {1}, {2}, {3}, {4}, {5})'.format(
         REGRESSION_MODEL, ISOTONIC_REGRESSION, AFT_SURVIVAL_REGRESSION,
         GBT_REGRESSOR, RANDOM_FOREST_REGRESSOR,
         GENERALIZED_LINEAR_REGRESSOR)),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id IN ('
     'SELECT operation_form_id FROM operation_operation_form '
     '  WHERE operation_id IN ({0}, {1}, {2}, {3}, {4}, {5}))'.format(
         REGRESSION_MODEL, ISOTONIC_REGRESSION, AFT_SURVIVAL_REGRESSION,
         GBT_REGRESSOR, RANDOM_FOREST_REGRESSOR,
         GENERALIZED_LINEAR_REGRESSOR)),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 242 AND 285'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id IN (SELECT id FROM operation_form_field '
     '   WHERE form_id IN ('
     'SELECT operation_form_id FROM operation_operation_form '
     '  WHERE operation_id IN ({0}, {1}, {2}, {3}, {4}, {5})))'.format(
         REGRESSION_MODEL, ISOTONIC_REGRESSION, AFT_SURVIVAL_REGRESSION,
         GBT_REGRESSOR, RANDOM_FOREST_REGRESSOR,
         GENERALIZED_LINEAR_REGRESSOR)),
]


def upgrade():
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in all_commands:
            if isinstance(cmd[0], collections.Callable):
                cmd[0]()
            else:
                op.execute(text(cmd[0]))
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
                # print cmd[1]
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
