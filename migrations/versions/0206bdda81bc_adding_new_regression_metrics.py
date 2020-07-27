"""Adding new regression metrics

Revision ID: 0206bdda81bc
Revises: 2b4ce751c4de
Create Date: 2020-07-27 17:06:02.862772

"""

import json

import pymysql
from alembic import context
from alembic import op
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '0206bdda81bc'
down_revision = '2b4ce751c4de'
branch_labels = None
depends_on = None

metrics_evaluation_new = [
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
        "key": "mae", "value": "Mean absolute error (regression)",
        "en": "Mean absolute error (regression)",
        "pt": "Erro absoluto médio"
    },
    {
        "key": "mape", "value": "Mean absolute percentage error (regression)",
        "en": "Mean absolute percentage error (regression)",
        "pt": "Média Percentual Absoluta do Erro"
    },
    {
        "key": "r2", "value": "Coefficient of determination R2 (regression)",
        "en": "Coefficient of determination  R2 (regression)",
        "pt": "Coeficiente de determinação (R2)"
    }
]

metrics_cross_new = [
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
        "key": "mae", "value": "Mean absolute error (regression)",
        "en": "Mean absolute error (regression)",
        "pt": "Erro absoluto médio"
    },
    {
        "key": "r2", "value": "Coefficient of determination R2 (regression)",
        "en": "Coefficient of determination  R2 (regression)",
        "pt": "Coeficiente de determinação (R2)"
    },

]

metrics_old = [
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
        "key": "mae", "value": "Mean absolute error (regression)",
        "en": "Mean absolute error (regression)",
        "pt": "Erro absoluto médio"
    }
]

all_commands = [
    (
        """UPDATE operation_form_field SET `values` = '{}' WHERE `id` = 101
        """.format(pymysql.escape_string(json.dumps(metrics_evaluation_new))),
        """UPDATE operation_form_field SET `values` = '{}' WHERE `id` = 101
        """.format(pymysql.escape_string(json.dumps(metrics_old)))
    ),

    (
        """UPDATE operation_form_field SET `values` = '{}' WHERE `id` = 487
        """.format(pymysql.escape_string(json.dumps(metrics_cross_new))),
        """UPDATE operation_form_field SET `values` = '{}' WHERE `id` = 487
        """.format(pymysql.escape_string(json.dumps(metrics_old)))
    ),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()
    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                if cmd[0] != '':
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
                if cmd[1] != '':
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
