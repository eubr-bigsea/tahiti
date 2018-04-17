"""Remove Field from Form 84

Revision ID: 2eaeb4b0c43f
Revises: dae2718e5272
Create Date: 2018-04-17 14:16:00.326775

"""
import json

from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '2eaeb4b0c43f'
down_revision = 'dae2718e5272'
branch_labels = None
depends_on = None

FORM_ID = 84
FIELD_ID = 192

def upgrade():
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(FIELD_ID))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(FIELD_ID))
  op.execute('DELETE FROM operation_operation_form WHERE operation_form_id={}'.format(FORM_ID))
  op.execute('DELETE FROM operation_form WHERE id={}'.format(FORM_ID))

def downgrade():
  pass
