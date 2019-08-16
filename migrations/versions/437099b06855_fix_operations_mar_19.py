# -*- coding: utf-8 -*-
"""fix_operations_mar_19
Revision ID: 437099b06855
Revises: 8a4558f255a4
Create Date: 2019-03-19 22:24:56.903149
"""
import json

import pymysql
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

isotonic_new = [{"value": "Isotonic/increasing", "key": True,
                 'pt': 'Isotônica/crescente'},
                {"value": "Antitonic/decreasing", "key": False,
                 'pt': 'Antitônica/decrescente'}]

metrics_new = [
    {
        "key": "none",
        "value": "Do not execute cross-validation",
        "en": "Do not execute cross-validation",
        "pt": "Não executar a validação cruzada"
    },
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

fold_new = [
    {"key": "random", "value": "Random",
     "pt": "Aleatória (partição aproximada => mais rápida)",
     "en": "Random (approximated fold => faster) "},
    {"key": "random_exact", "value": "Random",
     "pt": "Aleatória (partição quase exata => mais lenta)",
     "en": "Random (near exact fold => slower) "},
    {"key": "stratified", "value": "Stratified (approximated fold => faster)",
     "pt": "Estratificada (partição aproximada => mais rápida)",
     "en": "Stratified (approximated fold => faster)"},
    {"key": "stratified_exact",
     "value": "Stratified (near exact fold => slower)",
     "pt": "Estratificada (partição quase exata => mais lenta)",
     "en": "Stratified (near exact fold => slower)"}
]


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        # form for cross validation
        (132, 1, 1, 'execution'),
        # form for one-vs-rest
        (133, 1, 1, 'execution'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (132, 'en', 'Execution'),
        (132, 'pt', 'Execução'),
        (133, 'en', 'Execution'),
        (133, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        # form for cross validation
        [104, 132],
        [105, 132],
        [106, 132],
        [107, 132],
        [108, 132],
        [109, 132],
        [110, 132],

        [112, 132],
        [113, 132],
        [114, 132],
        [115, 132],
        [116, 132],
        [117, 132],
        [118, 132],
        [119, 132],
        [120, 132],

        # form for one-vs-rest
        [104, 133],
        [105, 133],
        [106, 133],
        [107, 133],
        [108, 133],
        [109, 133],
        [110, 133],

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

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')

    cross_validation_metrics = [
        {
            "key": "none",
            "value": "Do not execute cross-validation",
            "en": "Do not execute cross-validation",
            "pt": "Não executar a validação cruzada"
        },
        {"en": "Area under ROC curve(binary classification)",
         "value": "Area under ROC curve (binary classification)",
         "key": "areaUnderROC",
         "pt": "Área sob a curva ROC (classificação binária)"},
        {"en": "Area under precision-recall curve (binary classification)",
         "value": "Area under precision-recall curve (binary classification)",
         "key": "areaUnderPR",
         "pt": "Área sob a curva precisão-revocação"},
        {"en": "F1 score (multiclass classification)",
         "value": "F1 score (multiclass classification)", "key": "f1",
         "pt": "F1"},
        {"en": "Weighted precision (multiclass classification)",
         "value": "Weighted precision (multiclass classification)",
         "key": "weightedPrecision",
         "pt": "Precisão ponderada"},
        {"en": "Weighted recall (multiclass classification)",
         "value": "Weighted recall (multiclass classification)",
         "key": "weightedRecall", "pt": "Revocação ponderada"},
        {"en": "Accuracy (multiclass classification)",
         "value": "Accuracy (multiclass classification)", "key": "accuracy",
         "pt": "Acurácia"},
        {"en": "Root mean squared error  (regression)",
         "value": "Root mean squared error  (regression)", "key": "rmse",
         "pt": "Raiz do erro quadrático médio"},
        {"mse": "mse", "en": "Mean squared error (regression)",
         "pt": "Erro quadrático médio",
         "value": "Mean squared error (regression)"},
        {"en": "Mean absolute error (regression)",
         "value": "Mean absolute error regression)", "key": "mae",
         "pt": "Erro absoluto médio"}]

    data = [

        (487, 'cross_validation', 'INTEGER', 0, 10, 'none', 'dropdown',
         None, json.dumps(cross_validation_metrics), 'EXECUTION', 132),
        (488, 'attribute_cross_validation', 'TEXT', 0, 11, None,
         'attribute-selector', None, None, 'EXECUTION', 132),
        (489, 'one_vs_rest', 'INTEGER', 0, 12, None, 'checkbox',
         None, None, 'EXECUTION', 133),
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

    columns = ('id', 'locale', 'label', 'help')
    data = [

        (487, 'en', 'Metric for applying cross-validation',
         'If informed, this metric will be used and cross-validation will be '
         'executed.'),
        (487, 'pt', 'Métrica para validação cruzada',
         'Se informada, essa métrica será usada e a validação '
         'cruzada será executada'),
        (488, 'en', 'Attribute with fold number',
         'Contains the fold number for the row'),
        (488, 'pt', 'Atributo com o número da partição (fold)',
         'Contém o número da partição para a linha'),

        (489, 'en', 'Use one-vs-rest classification',
         'Allow to run any classifier with multi label input data.'),
        (489, 'pt', 'Usar classificação um-contra-todos (one-vs-rest)',
         'Permite executar um classificador com dados de entrada multi rótulos')

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
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
        (49, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 104),
        (50, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 105),
        (51, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 106),
        (52, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 107),
        (53, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 108),
        (54, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 109),
        (55, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 110),
        (56, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 111),
        (57, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 112),
        (58, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 113),
        (59, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 114),
        (60, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 115),
        (61, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 116),
        (62, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 117),
        (63, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 118),
        (64, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 119),
        (65, 'JS_CLIENT', 1,
         'copyInputAddField(task, "prediction", false, null);', 120),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in data]

    op.bulk_insert(tb, rows)


all_commands = [
    (
        """UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (480)
        """.format(pymysql.escape_string(json.dumps(fold_new))),
        '',
    ),
    (
        """UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107)
        """.format(pymysql.escape_string(json.dumps(metrics_new))),
        """UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107)
        """.format(pymysql.escape_string(json.dumps(metrics_new)))),  # same

    ("""UPDATE operation_form_field SET `values` = '{}' WHERE `id` = '254';
    """.format(pymysql.escape_string(json.dumps(isotonic_new))),
     """UPDATE operation_form_field SET `values` = '{}' WHERE `id` = '254';
     """.format(pymysql.escape_string(json.dumps(isotonic_new)))),  # same

    ("ALTER TABLE operation_form_field MODIFY form_id INT(11)",
     "ALTER TABLE operation_form_field MODIFY form_id INT(11) NOT NULL"),

    ("UPDATE operation_form_field SET form_id = NULL WHERE id = 269",
     "UPDATE operation_form_field SET form_id =105 WHERE id = 269"),

    ("UPDATE operation_form_field SET form_id = NULL WHERE id = 206",
     "UPDATE operation_form_field SET form_id = 8 WHERE id = 206"),

    ("UPDATE operation_form_field SET form_id = NULL WHERE id = 211",
     "UPDATE operation_form_field SET form_id = 8 WHERE id = 211"),

    ("UPDATE operation_form_field SET form_id = NULL WHERE id = 209",
     "UPDATE operation_form_field SET form_id = 8 WHERE id = 209"),

    (
        """UPDATE operation_form_field SET `order` = id - 266
            WHERE id BETWEEN 274 AND 278""",
        """UPDATE operation_form_field SET `order` = id - 266
        WHERE id  BETWEEN 274 AND 278"""),
    (
        'UPDATE operation SET enabled = 0 WHERE id = 111',
        'UPDATE operation SET enabled = 1 WHERE id = 111',
    ),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 132 AND 133'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 132 AND 133'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_form_id IN (132, 133) and operation_id '
     'BETWEEN 104 AND 120'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 487 and 489'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 487 and 489'),

    (
        """
        UPDATE operation_form_field_translation
        SET label = 'Atributo(s) previsor(es)',
        `help` = 'Atributo(s) previsor(es)'
        WHERE id IN (130, 132, 217, 242, 346, 348, 352,
        356, 421, 424, 455, 4070, 4105, 4108, 4111)
        AND locale = 'pt';
        """,
        ""
    ),
    (
        """
        UPDATE operation_form_field_translation SET label = 'Features',
        `help` = 'Features'
        WHERE id IN (130, 132, 217, 242, 346, 348, 352, 356, 421, 424, 455,
        4070, 4105, 4108, 4111)
        AND locale = 'en';
        """,
        ''
    ),

    (_insert_operation_script,
     'DELETE FROM operation_script WHERE operation_id BETWEEN 104 AND 120'),

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
