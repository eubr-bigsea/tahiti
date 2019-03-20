# -*- coding: utf-8 -*-
"""fix_operations_mar_19
Revision ID: 437099b06855
Revises: 8a4558f255a4
Create Date: 2019-03-19 22:24:56.903149
"""
import pymysql
import json
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column
# revision identifiers, used by Alembic.
revision = '437099b06855'
down_revision = '8a4558f255a4'
branch_labels = None
depends_on = None


isotonic_old = [{"value": "Isotonic/increasing", "key": True},
                {"value": "Orantitonic/decreasing", "key": False}]
isotonic_new = [{"value": "Isotonic/increasing", "key": True},
                {"value": "Antitonic/decreasing", "key": False}]

metrics_new = [
    {
        "key": "areaUnderROC",
        "value": "Area under ROC curve (binary classification)",
        "en": "Area under ROC curve(binary classification)",
        "pt": "Área sob a curva ROC (classificação binária)"
    },
    {
        "key": "areaUnderPR",
        "value": "Area under precision-recall curve (binary classification)",
        "en": "Area under precision-recall curve (binary classification)",
        "pt": "Área sob a curva precisão-revocação"
    },
    {
        "key": "f1", "value": "F1 score (multiclass classification)",
        "en": "F1 score (multiclass classification)",
        "pt": "F1"
    },
    {
        "key": "weightedPrecision",
        "value": "Weighted precision (multiclass classification)",
        "en": "Weighted precision (multiclass classification)",
        "pt": "Precisão ponderada"
    },
    {
        "key": "weightedRecall",
        "value": "Weighted recall (multiclass classification)",
        "en": "Weighted recall (multiclass classification)",
        "pt": "Revocação ponderada"
    },
    {
        "key": "accuracy", "value": "Accuracy (multiclass classification)",
        "en": "Accuracy (multiclass classification)",
        "pt": "Acurácia"
    },
    {
        "key": "rmse", "value": "Root mean squared error  (regression)",
        "en": "Root mean squared error  (regression)",
        "pt": "Raíz do erro quadrático médio"
    },
    {
        "mse": "mse", "value": "Mean squared error (regression)",
        "en": "Mean squared error (regression)",
        "pt": "Erro quadrático médio"
    },
    {
        "key": "mae", "value": "Mean absolute error regression)",
        "en": "Mean absolute error (regression)",
        "pt": "Erro absoluto médio"
    }
]

all_commands = [
   (
    """UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107)
    """.format(pymysql.escape_string(json.dumps(metrics_new))),
    """UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107)
    """.format(pymysql.escape_string(json.dumps(metrics_new)))), # same

    ("""UPDATE operation_form_field SET `values` = '{}' WHERE `id` = '254';
    """.format(pymysql.escape_string(json.dumps(isotonic_new))),
    """UPDATE operation_form_field SET `values` = '{}' WHERE `id` = '254';
    """.format(pymysql.escape_string(json.dumps(isotonic_old)))),
 ]
def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()
    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
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
            if isinstance(cmd[1], (unicode, str)):
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
