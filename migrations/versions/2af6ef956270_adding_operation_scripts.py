"""adding operation scripts

Revision ID: 2af6ef956270
Revises: d653bb706444
Create Date: 2017-06-27 16:57:14.255881

"""
from textwrap import dedent

from alembic import op
from sqlalchemy import Integer, String
from sqlalchemy.sql import table, column
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = '2af6ef956270'
down_revision = 'd653bb706444'
branch_labels = None
depends_on = None


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
        (1, 1, "JS_CLIENT", "copyInputAddField(task, 'prediction', false);", 42),
        (2, 1, "JS_CLIENT", "copyInputAddField(task, 'alias', false);", 7),
        (3, 1, "JS_CLIENT", "copyInputAddField(task, 'alias', false);", 41),
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
            task.uiPorts.output = task.forms.attributes.value.slice()
            Array.prototype.push.apply(task.uiPorts.output,
                task.forms.function.value.map(function(v){
                    return v.alias}));"""), 15),
        (15, 1, "JS_CLIENT",
         "copyInputAddAttributesSplitAlias(task, 'attributes', 'alias');", 40),
        (16, 1, "JS_CLIENT",
         ("copyFromOnlyOneInput(task, 5); "
          "//hard coded id for 'input data 1', first input data port"), 12),
        (17, 1, "JS_CLIENT", "joinSuffixDuplicatedAttributes(task);", 24),
        (18, 1, "JS_CLIENT", "joinSuffixDuplicatedAttributes(task);", 16),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
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
]


def upgrade():
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in all_commands:
            assert isinstance(cmd, tuple)
            if callable(cmd[0]):
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
            if callable(cmd[1]):
                cmd[1]()
            else:
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
