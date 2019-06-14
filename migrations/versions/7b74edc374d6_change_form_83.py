"""Change Form 83

Revision ID: 7b74edc374d6
Revises: 31fdc250f191
Create Date: 2018-04-16 17:09:45.418110

"""
import json

from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '7b74edc374d6'
down_revision = '31fdc250f191'
branch_labels = None
depends_on = None

X_FORMAT_ID = 298
Y_FORMAT_ID = 299
FORM_ID = 83
NEW_FIELD_ID = 455

def upgrade():
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(X_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(Y_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(X_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(Y_FORMAT_ID))

def downgrade():
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
      column('form_id', Integer),
  )

  columns = [c.name for c in tb.columns]

  supported_formats = [
        {"key": "%Y-%m-%dT%H:%M:%S.%LZ",
         "value": "%Y-%m-%dT%H:%M:%S.%LZ"},
        {"key": "%m-%d", "value": "%m-%d"},
        {"key": "%d-%", "value": "%d-%m"},
        {"key": "%Y-%m-%d", "value": "%Y-%m-%d"},
        {"key": "%m-%Y-%d", "value": "%m-%Y-%d"},
        {"key": "%m-%Y-%d", "value": "%m-%Y-%d"},
        {"key": "%m-%Y-%d %H:%M",
         "value": "%m-%Y-%d %H:%M"},
        {"key": "%m-%Y-%d %H:%M",
         "value": "%m-%Y-%d %H:%M"},
        {"key": "%m-%Y-%d %H:%M:%S", "value": "%m-%Y-%d %H:%M:%S"},
        {"key": "%m-%Y-%d %H:%M:%S",
         "value": "%m-%Y-%d %H:%M:%S"},
        {"key": "%H:%M", "value": "%H:%M"},
        {"key": "%H:%M:%S", "value": "%H:%M:%S"},

        {"key": ".2", "value": ".2"},
        {"key": ".4", "value": ".4"},
        {"key": "%", "value": "%"},
        {"key": "p", "value": "p"},
        {"key": "d", "value": "d"}
  ]

  data = [
    [X_FORMAT_ID, 'x_format', 'TEXT', 0, 8, None, 'select2', None, json.dumps(supported_formats), 'EXECUTION', FORM_ID],
    [Y_FORMAT_ID, 'y_format', 'TEXT', 0, 9, None, 'select2', None, json.dumps(supported_formats), 'EXECUTION', FORM_ID]
  ]

  rows = [dict(list(zip(columns, row))) for row in data]
  op.bulk_insert(tb, rows)

  tb = table(
      'operation_form_field_translation',
      column('id', Integer),
      column('locale', String),
      column('label', String),
      column('help', String), )

  columns = [c.name for c in tb.columns]

  data = [
      [X_FORMAT_ID, 'en', 'X-axis format', 'X-axis format'],
      [X_FORMAT_ID, 'pt', 'Formato para eixo X', 'Formato para eixo X'],
      [Y_FORMAT_ID, 'en', 'Y-axis format', 'Y-axis format'],
      [Y_FORMAT_ID, 'pt', 'Formato para eixo Y', 'Formato para eixo Y'],
  ]

  rows = [dict(list(zip(columns, row))) for row in data]
  op.bulk_insert(tb, rows)
