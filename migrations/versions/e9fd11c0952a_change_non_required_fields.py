"""change non-required fields

Revision ID: e9fd11c0952a
Revises: fef08022f308
Create Date: 2019-02-05 09:00:10.098050

"""
from alembic import op
from sqlalchemy.sql import text
import collections

# revision identifiers, used by Alembic.
revision = 'e9fd11c0952a'
down_revision = 'fef08022f308'
branch_labels = None
depends_on = None

NON_REQUIRED = [
    '232',  # summary statistics attributes
]

all_commands = [
    (
        """UPDATE operation_form_field SET required = 0
        WHERE id IN ({non_required})
        """.format(non_required=','.join(NON_REQUIRED)),

        """UPDATE operation_form_field SET required = 1
        WHERE id IN ({non_required})
        """.format(non_required=','.join(NON_REQUIRED)),
    ),
    (
        """UPDATE operation_form_field
        SET enable_conditions = 'this.type.internalValue === "percent"'
        WHERE id =  74 """,
        """UPDATE operation_form_field SET enable_conditions = NULL
        WHERE id = 74 """,
    ),
    (
        """UPDATE operation_form_field
        SET enable_conditions = 'this.type.internalValue !== "percent"'
        WHERE id =  105 """,
        """UPDATE operation_form_field SET enable_conditions = NULL
        WHERE id = 105 """,
    ),
    (
        """UPDATE operation_form_field
        SET enable_conditions = 'false'
        WHERE id =  90 """,
        """UPDATE operation_form_field SET enable_conditions = NULL
        WHERE id = 90 """,
    )

]


def upgrade():
    last = ''
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in all_commands:
            assert isinstance(cmd, tuple)
            last = cmd[0]
            if isinstance(cmd[0], collections.Callable):
                cmd[0]()
            else:
                op.execute(text(cmd[0]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise


def downgrade():
    last = ''
    try:
        op.execute(text('START TRANSACTION'))
        for cmd in reversed(all_commands):
            last = cmd[1]
            if isinstance(cmd[1], collections.Callable):
                cmd[1]()
            else:
                op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        print('-' * 20)
        print('Last', last)
        print('-' * 20)
        raise
