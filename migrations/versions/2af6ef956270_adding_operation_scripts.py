# -*- coding: utf-8 -*-}
"""adding operation scripts

Revision ID: 2af6ef956270
Revises: d653bb706444
Create Date: 2017-06-27 16:57:14.255881

"""
from textwrap import dedent

from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.sql import table, column
from sqlalchemy.sql import text
import collections

# revision identifiers, used by Alembic.
revision = '2af6ef956270'
down_revision = 'd653bb706444'
branch_labels = None
depends_on = None


def insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String))
    columns = [c.name for c in tb.columns]
    data = [
        (239, 'en', 'Prediction attribute (new)', 'Prediction attribute (new)'),
        (239, 'pt', 'Atributo com a predição (novo)',
         'Atributo com a predição (novo)'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_fields():
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
        (239, 'prediction', 'TEXT', 0, 3, None, 'text', None, None,
         'EXECUTION', 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_scripts():
    tb = table(
        'operation_script',
        column('id', Integer),
        column('enabled', Integer),
        column('type', String),
        column('body', String),
        column('operation_id', Integer),
    )

    columns = [c.name for c in tb.columns]
    data = [
        (
            1, 1, "JS_CLIENT",
            "copyInputAddField(task, 'prediction', false, null);",
            42),
        (
            2, 1, "JS_CLIENT", "copyInputAddField(task, 'alias', false, null);",
            7),
        (3, 1, "JS_CLIENT",
         "copyInputAddField(task, 'alias', false, 'features');", 41),
        (4, 1, "JS_CLIENT", "onlyField(task, 'attributes', true)", 6),
        (5, 1, "JS_CLIENT", "copyInput(task);", 37),
        (6, 1, "JS_CLIENT", "copyInput(task);", 5),
        (7, 1, "JS_CLIENT", "copyInput(task);", 13),
        (8, 1, "JS_CLIENT", "copyInput(task);", 17),
        (9, 1, "JS_CLIENT", "copyInput(task);", 21),
        (10, 1, "JS_CLIENT", "copyInput(task);", 23),
        (11, 1, "JS_CLIENT", "copyInput(task);", 27),
        (12, 1, "JS_CLIENT", "copyInput(task);", 28),
        (13, 1, "JS_CLIENT", "copyInput(task);", 32),
        (14, 1, "JS_CLIENT", dedent("""
            task.uiPorts.output = (task.forms.attributes.value || []).slice();
            Array.prototype.push.apply(task.uiPorts.output,
                (task.forms.function.value || []).map(function(v){
                    return v.alias}));""").strip(), 15),
        (15, 1, "JS_CLIENT",
         ("copyInputAddAttributesSplitAlias(task, "
          "'attributes', 'alias', '_indexed');"), 40),
        (16, 1, "JS_CLIENT",
         ("copyFromOnlyOneInput(task, 5); "
          "//hard coded id for 'input data 1', first input data port"), 12),
        (17, 1, "JS_CLIENT", "joinSuffixDuplicatedAttributes(task);", 24),
        (18, 1, "JS_CLIENT", "joinSuffixDuplicatedAttributes(task);", 16),
        (19, 1, "JS_CLIENT", ("copyInputAddAttributesSplitAlias(task, "
                              "'attributes', 'alias', '_vect');"), 52),
        (20, 1, "JS_CLIENT",
         ("copyInputAddAttributesSplitAlias(task, 'attributes', "
          "'alias', '_ngram');"), 51),
        (21, 1, "JS_CLIENT",
         ("copyInputAddAttributesSplitAlias(task, 'attributes', "
          "'alias', '_no_stopwords');"), 50),
        (22, 1, "JS_CLIENT",
         ("copyInputAddAttributesSplitAlias(task, 'attributes', "
          "'alias', '_tokenized');"), 49),
        (23, 1, "JS_CLIENT", "copyAllInputsRemoveDuplicated(task);", 82),
        (24, 1, "JS_CLIENT",
         "copyInputAddField(task, 'prediction', false, null);", 1),
        (25, 1, "JS_CLIENT",
         ("copyInputAddAttributesSplitAlias(task, "
          "'attributes', 'alias', '_onehotenc');"), 75),
        (26, 1, "JS_CLIENT",
         ("copyInputAddAttributesSplitAlias(task, "
          "'polygon_attributes', 'alias', '_within');"), 55),
        (27, 1, "JS_CLIENT", "copyInput(task);", 36),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ('INSERT INTO operation_operation_form VALUES(75, 90)',
     ('DELETE FROM operation_operation_form WHERE operation_id = 75 AND '
      'operation_form_id = 90')
     ),
    (("INSERT INTO operation_form_translation "
     "VALUES(90, 'en', 'Execution'), (90, 'pt', 'Execução')"),
     'DELETE FROM operation_form_translation WHERE id = 90'
     ),
    (_insert_fields, 'DELETE FROM operation_form_field WHERE id IN '
                     '(239, 240, 241);'),
    (insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (239)'),
    (_insert_scripts, 'DELETE FROM operation_script '),
    ('UPDATE operation SET enabled = 1 WHERE id = 2',
     'UPDATE operation SET enabled = 0 WHERE id = 2'),
    ('''DELETE FROM operation_category_operation WHERE operation_id = 30
     AND operation_category_id = 3 ''',
     'INSERT INTO operation_category_operation VALUES(30, 3)'
     ),
    ('INSERT INTO operation_category_operation VALUES(53, 3)',
     '''DELETE FROM operation_category_operation WHERE operation_id = 53
     AND operation_category_id = 3 '''),
    # Fixes incorrect required fields
    # for FeatureAssembler, ConvertWordToVect and RemoveStopWord
    ('UPDATE operation_form_field SET required = 0 WHERE id IN (115, 122, 98);',
     'UPDATE operation_form_field SET required = 1 WHERE id IN (115, 122, 98);')
]


def upgrade():
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in all_commands:
            assert isinstance(cmd, tuple)
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
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
