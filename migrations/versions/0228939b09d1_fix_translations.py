"""fix translations

Revision ID: 0228939b09d1
Revises: 3ada503c2991
Create Date: 2017-06-13 16:12:48.309231

"""

from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = '0228939b09d1'
down_revision = '3ada503c2991'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(text(
        ''' UPDATE `operation_form_field`
            SET NAME = REPLACE(NAME, 'None', 'null')
            WHERE NAME LIKE 'None%'; '''))
    op.execute(text("""
        UPDATE `operation_form_field_translation`
        SET label = REPLACE(label, 'None', 'null')
        WHERE label LIKE '%None%';"""))

    op.execute(text("""
        UPDATE `operation_translation`
        SET description =
            'Splits dataset into 2 different data sets using weights'
        WHERE id = 17 and locale = 'en'"""))


def downgrade():
    op.execute(text(
        ''' UPDATE `operation_form_field`
            SET NAME = REPLACE(NAME, 'null', 'None')
            WHERE NAME LIKE 'null%'; '''))

    op.execute(text("""
        UPDATE `operation_form_field_translation`
        SET label = REPLACE(label, 'null', 'None')
        WHERE label LIKE '%null%';"""))

    op.execute(text("""
        UPDATE `operation_translation`
        SET description =
            'Splits dataset in 2 different data sets using weights'
        WHERE id = 17 and locale = 'en' """))
