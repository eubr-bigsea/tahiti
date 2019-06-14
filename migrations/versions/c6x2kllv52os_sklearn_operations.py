# -*- coding: utf-8 -*-

"""Adding Scikit-learn Operations

Revision ID: c6x2kllv52os
Revises: bca9291ljsj5
Create Date: 2018-06-14 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = 'c6x2kllv52os'
down_revision = 'bca9291ljsj5'
branch_labels = None
depends_on = None



def _insert_platform():
    tb = table(
        'platform',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('icon', String), )

    columns = ('id', 'slug', 'enabled', 'icon')
    data = [
        (4, 'scikit-learn', 1, '')
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)

def _insert_platform_translation():
    tb = table(
        'platform_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (4, 'en', 'Scikit-learn', 'Scikit-learn 0.19.1'),
        (4, 'pt', 'Scikit-learn', 'Scikit-learn 0.19.1'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _add_operations_platform_from_spark():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (3001, 4), # data-reader
        (30, 4), # data-writer

        (24, 4),#'add-columns'
        (12, 4),#'add-rows'
        (15, 4),#'aggregation'
        (21, 4),#'clean-missing'
        (37, 4),#'difference'
        (3014, 4),#'drop
        (5, 4), #filter
        (16, 4),#'join'
        (6, 4), #'projection'
        (23, 4),#'remove-duplicated-rows'
        (27, 4), #replace-value
        (28, 4),#'sample'
        (13, 4),#'set-intersection'
        (32, 4),#'sort'
        (17, 4),#'split'
        (7, 4), #'tranformation'

        (25, 4),#'comment'

        (3031, 4),#'read-shapefile'
        (55, 4),#'within'

        (41, 4),  # Feature indexer
        (92, 4),  # Max-abs scaler
        (91, 4),  # Min-max scaler
        (90, 4),  # Standard scaler
        (75, 4),  # One Hot Encoder
        (41, 4),  # Feature Assembler
        (95, 4),  # PCA

        (3026, 4),  # Load model
        (3027, 4),  # Save model
        (42, 4),  # Apply model

        (73, 4),  # Regression Model
        (78, 4),  # Random Forest Regressor
        (8, 4),  # Linear Regression
        (74, 4),  # IsotonicRegression

        (49, 4), #tokenizer
        (50, 4), #remove-stop-words
        (51, 4), #generate-n-grams
        (52, 4), # word-to-vector

        (10, 4), # clustering-model
        (56, 4), # gaussian-mixture-clustering
        (29, 4), # k-means-clustering
        (48, 4), # lda-clustering

        (1, 4), # classification-model
        (4, 4), # naive-bayes-classifier
        (9, 4), # svm-classification
        (3005, 4), # knn-classifier
        (3008, 4), # logistic-regression

        (3, 4),   # fp-growth
        (85, 4),  # association rule
        (86, 4),  # sequence mining

        (26, 4),  #publish-as-visualization
        (35, 4),  #table-visualization
        (68, 4),  #line-chart
        (69, 4),  #bar-chart
        (70, 4),  #pie-chart
        (71, 4),  #area-chart
        (80, 4),  #scatter-plot
        (81, 4),  #summary-statistics
        (88, 4) , #map-chart
        (89, 4),  #donut-chart

    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)



all_commands = [
    (_insert_platform, 'DELETE FROM platform WHERE id = 4' ),
    (_insert_platform_translation,
        'DELETE FROM platform_translation WHERE id = 4'),
	(_add_operations_platform_from_spark,
        'DELETE FROM operation_platform WHERE platform_id = 4'),

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
