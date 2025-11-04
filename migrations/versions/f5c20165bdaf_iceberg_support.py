"""add iceberg format into data writer

Revision ID: f5c20165bdaf
Revises: ec6fa5b00b2d
Create Date: 2025-11-17 10:33:52.223316

"""
import json
from alembic import op
from sqlalchemy.sql import text
import sqlalchemy as sa
from tahiti.migration_utils import is_mysql

# revision identifiers, used by Alembic.
revision = 'f5c20165bdaf'
down_revision = 'ec6fa5b00b2d'
branch_labels = None
depends_on = None


def upgrade():
    values = [{"en": "CSV data file", "value": "CSV data file", "key": "CSV", "pt": "Arquivo de dados CSV"}, {"en": "Iceberg table", "value": "Iceberg table", "key": "ICEBERG", "pt": "Tabela Iceberg"}, {"en": "JSON data file", "value": "JSON data file", "key": "JSON", "pt": "Arquivo de dados JSON"}, {"en": "Parquet data file", "value": "Parquet data file", "key": "PARQUET", "pt": "Arquivo de dados Parquet"}]

    if is_mysql():
        sql = "UPDATE `tahiti`.`operation_form_field` SET `values` = '{}' WHERE `id` = '83';".format(json.dumps(values, ensure_ascii=False))
    else:
        sql = """UPDATE tahiti.operation_form_field SET "values"='{}' WHERE id = 83;""".format(json.dumps(values, ensure_ascii=False))

    op.execute(text(sql))


def downgrade():
    values = [{"en": "CSV data file", "value": "CSV data file", "key": "CSV", "pt": "Arquivo de dados CSV"}, {"en": "JSON data file", "value": "JSON data file", "key": "JSON", "pt": "Arquivo de dados JSON"}, {"en": "Parquet data file", "value": "Parquet data file", "key": "PARQUET", "pt": "Arquivo de dados Parquet"}]

    if is_mysql():
        sql = "UPDATE `tahiti`.`operation_form_field` SET `values`='{}' WHERE `id` = '83';".format(json.dumps(values, ensure_ascii=False))
    else:
        sql = """UPDATE operation_form_field SET "values"='{}' WHERE id = 83;""".format(json.dumps(values, ensure_ascii=False))

    op.execute(text(sql))
    


