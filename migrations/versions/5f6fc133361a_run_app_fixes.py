"""Run app fixes

Revision ID: 5f6fc133361a
Revises: 690a19ef85c0
Create Date: 2017-05-29 10:20:48.774237

"""
from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = '5f6fc133361a'
down_revision = '690a19ef85c0'
branch_labels = None
depends_on = None


def upgrade():
    try:
        unreversible_data = [
            """DELETE FROM operation_category_operation
                WHERE operation_id IN (61);""",
            """DELETE FROM operation_port_interface_operation_port
            WHERE operation_port_id IN (
                SELECT id FROM operation_port
                    WHERE operation_id IN (61));""",
            """DELETE FROM operation_port WHERE operation_id IN (61);""",
            """DELETE FROM operation_form_field_translation
                WHERE form_id IN(
                    SELECT form_id FROM operation_operation_form
                        WHERE operation_id IN (61));""",
            """DELETE FROM operation_form_field
                WHERE form_id IN(
                    SELECT form_id FROM operation_operation_form
                        WHERE operation_id IN (61));""",
            """DELETE FROM operation_operation_form
                WHERE operation_id IN (61);""",
            """DELETE FROM operation WHERE id IN (61);"""
        ]
        all_commands = [
            """
            UPDATE operation_form_field
                SET values_url = '{{LIMONERO_URL}}/datasources'
                WHERE id IN (1)
            """,
            """
            UPDATE operation_form_field
                SET values_url = '{{LIMONERO_URL}}/datasources?format=SHAPEFILE'
                WHERE id IN (133)
            """,
            """
            UPDATE operation_form_field
                SET values_url = '{{TAHITI_URL}}/applications'
                WHERE id IN (68)
            """,
            "DELETE FROM operation_form_field_translation WHERE id IN (175)",
            "DELETE FROM operation_form_field WHERE id IN (175)",
        ]
        op.execute(text('START TRANSACTION'))
        for cmd in unreversible_data + all_commands:
            op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise


def downgrade():
    try:
        all_commands = [
            """
            UPDATE operation_form_field
            SET values_url =
              'http://beta.ctweb.inweb.org.br/limonero/datasources?token=123456'
            WHERE id IN (1)
            """,
            """
            UPDATE operation_form_field
            SET values_url =
            'http://beta.ctweb.inweb.org.br/limonero/datasources?token=123456&format=SHAPEFILE'
            WHERE id IN (133)
            """,
            """
            UPDATE operation_form_field
            SET values_url =
              'http://beta.ctweb.inweb.org.br/tahiti/applications?token=123456'
                WHERE id IN (68)
            """
        ]
        op.execute(text('START TRANSACTION'))
        for cmd in reversed(all_commands):
            op.execute(text(cmd[1]))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
