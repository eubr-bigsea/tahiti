"""improving sklearn evaluate model

Revision ID: e60c72ccb127
Revises: fafbc8e926fc
Create Date: 2021-03-02 09:25:03.390334

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json


# revision identifiers, used by Alembic.
revision = 'e60c72ccb127'
down_revision = 'fafbc8e926fc'
branch_labels = None
depends_on = None

FIELD_ID = 4373


def _add_operations_platform_from_spark():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (128, 4),  # vector-disassembler

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
            column('form_id', Integer),
            column('enable_conditions', Integer),
    )

    columns = [c.name for c in tb.columns]
    data = [

        # evaluate-model
        (FIELD_ID, 'clustering_metric', 'TEXT', 0, 2,
         'homogeneity_completeness_v_measure', 'dropdown', None, json.dumps([
             {'key': 'calinski_harabasz_score',
              'value': 'Calinski and Harabasz'},
             {'key': 'davies_bouldin_score', 'value': 'Davies-Bouldin'},
             {'key': 'homogeneity_completeness_v_measure',
              'value': 'Homogeneity, completeness and V-Measure'},
             {'key': 'fowlkes_mallows_score', 'value': 'Fowlkes-Mallows index'},
             {'key': 'adjusted_mutual_info_score',
              'value': 'Adjusted Mutual Information'}
         ]), 'EXECUTION', 4017,
         'this.model_type.internalValue === "clustering"'),

        (FIELD_ID + 1, 'regression_metric', 'TEXT', 0, 2, 'r2_score',
         'dropdown', None, json.dumps([
            {'key': 'explained_variance_score', 'value': 'Explained variance'},
            {'key': 'max_error', 'value': 'Maximum residual error'},
            {'key': 'mean_absolute_error', 'value': 'Mean absolute error'},
            {'key': 'mean_squared_error', 'value': 'Mean squared error'},
            {'key': 'mean_squared_log_error',
                'value': 'Mean squared logarithmic error'},
            {'key': 'median_absolute_error', 'value': 'Median absolute error'},
            {'key': 'r2_score', 'value': 'R^2 (coefficient of determination)'},
            ]), 'EXECUTION', 4017,
         'this.model_type.internalValue === "regression"'),

        (FIELD_ID + 2, 'classification_metric', 'TEXT', 0, 2, 'f1_score',
         'dropdown', None, json.dumps([
            {'key': 'balanced_accuracy_score', 'value': 'Balanced accuracy'},
            {'key': 'f1_score', 'value': 'F1'},
            {'key': 'precision_score', 'value': 'Weighted Precision'},
            {'key': 'recall_score', 'value': 'Weighted Recall'},
            {'key': 'jaccard_score', 'value': 'Jaccard'},
            {'key': 'roc_auc_score', 'value': 'Area Under ROC'},
            {'key': 'cohen_kappa_score', 'value': 'Cohen’s kappa'},
            {'key': 'matthews_corrcoef',
                'value': 'Matthews correlation coefficient'},
            ]), 'EXECUTION', 4017,
         'this.model_type.internalValue === "classification"'),

        (FIELD_ID + 3, 'feature', 'TEXT', 0, 4, None, 'attribute-selector',
         None, '{\"multiple\": true}', 'EXECUTION', 4017,
         '["calinski_harabasz_score", "davies_bouldin_score"]'
         '.includes(this.clustering_metric.internalValue) && '
         'this.model_type.internalValue === "clustering"'),

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

        (FIELD_ID, 'en', 'Clustering metric',
         'Metric to evaluate a clustering model.'),
        (FIELD_ID, 'pt', 'Métrica de agrupamento',
         'Métrica para avaliar um modelo de agrupamento.'),

        (FIELD_ID + 1, 'en', 'Regression metric',
         'Metric to evaluate a regression model.'),
        (FIELD_ID + 1, 'pt', 'Métrica de regressão',
         'Métrica para avaliar um modelo de regressão.'),

        (FIELD_ID + 2, 'en', 'Classification metric',
         'Metric to evaluate a classification model.'),
        (FIELD_ID + 2, 'pt', 'Métrica de classificação',
         'Métrica para avaliar um modelo de classificação.'),

        (FIELD_ID + 3, 'en', 'Feature attribute',
         'Feature attribute.'),
        (FIELD_ID + 3, 'pt', 'Atributo de features',
         'Atributo usado como features.'),


    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_add_operations_platform_from_spark,
     "DELETE FROM operation_platform "
     "WHERE operation_id = 128 AND platform_id = 4"),

    ("UPDATE operation_form_field SET `order` = 3 WHERE id = 4085",  # pred.
     "UPDATE operation_form_field SET `order` = 1 WHERE id = 4085"),
    ("UPDATE operation_form_field SET `order` = 4 WHERE id = 4086",  # label
     "UPDATE operation_form_field SET `order` = 2 WHERE id = 4086"),
    ("UPDATE operation_form_field SET `order` = 1 WHERE id = 4087",  # model
     "UPDATE operation_form_field SET `order` = 4 WHERE id = 4087"),

    ("""
    UPDATE operation_form_field SET `enable_conditions` = 
    '! ["calinski_harabasz_score", "davies_bouldin_score"].includes(
    this.clustering_metric.internalValue) || 
    this.model_type.internalValue !== "clustering" ' WHERE id = 4086
    """,
     "UPDATE operation_form_field SET `enable_conditions` = '' WHERE id=4086"),

    (_insert_operation_form_field,
     "DELETE FROM operation_form_field WHERE id BETWEEN {} AND {}"
     .format(FIELD_ID, FIELD_ID + 3)),

    (_insert_operation_form_field_translation,
     "DELETE FROM operation_form_field_translation WHERE id BETWEEN {} AND {}"
     .format(FIELD_ID, FIELD_ID+3)),

    ("""
    UPDATE operation_form_field_translation 
    SET `label` = 'Label attribute', `help` = 'Label attribute'
    WHERE id = 4086
    """, """
    UPDATE operation_form_field_translation 
    SET `label` = 'Label attribute (if classification or regression)', 
    `help` = 'Label attribute (if classification or regression)'
    WHERE id = 4086
    """),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
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
