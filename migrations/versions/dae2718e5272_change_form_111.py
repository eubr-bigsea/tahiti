"""Change Form 111

Revision ID: dae2718e5272
Revises: 7b74edc374d6
Create Date: 2018-04-16 17:18:13.248431

"""
import json

from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = 'dae2718e5272'
down_revision = '7b74edc374d6'
branch_labels = None
depends_on = None

Z_AXIS_ATTRIBUTE = 313
T_AXIS_ATTRIBUTE = 314
Z_TITLE = 317
T_TITLE = 318
X_FORMAT_ID = 319
Y_FORMAT_ID = 320
Z_FORMAT_ID = 321
T_FORMAT_ID = 322
Z_SUFIX = 325
T_SUFIX = 326
Z_PREFIX = 329
T_PREFIX = 330

FORM_ID = 111
NEW_FIELD_ID = 456

def upgrade():
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(Z_AXIS_ATTRIBUTE))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(T_AXIS_ATTRIBUTE))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(Z_TITLE))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(T_TITLE))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(X_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(Y_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(Z_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(T_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(Z_SUFIX))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(T_SUFIX))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(Z_PREFIX))
  op.execute('DELETE FROM operation_form_field WHERE id={}'.format(T_PREFIX))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(Z_AXIS_ATTRIBUTE))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(T_AXIS_ATTRIBUTE))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(Z_TITLE))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(T_TITLE))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(X_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(Y_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(Z_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(T_FORMAT_ID))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(Z_SUFIX))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(T_SUFIX))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(Z_PREFIX))
  op.execute('DELETE FROM operation_form_field_translation WHERE id={}'.format(T_PREFIX))

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
    [Z_AXIS_ATTRIBUTE, 'z_axis_attribute', 'TEXT', 0, 8, 'attribute-selector', None, {"multiple: false"}, 'EXECUTION', 111]
    [T_AXIS_ATTRIBUTE, 't_axis_attribute', 'TEXT', 0, 8, 'attribute-selector', None, {"multiple: false"}, 'EXECUTION', 111]
    [Z_TITLE, 'z_title', 'TEXT', 0, 8, 'text', None, {"multiple: false"}, 'EXECUTION', 111]
    [T_TITLE, 't_title', 'TEXT', 0, 8, 'text', None, {"multiple: false"}, 'EXECUTION', 111]
    [X_FORMAT_ID, 'x_format', 'TEXT', 0, 8, None, 'select2', None, json.dumps(supported_formats), 'EXECUTION', FORM_ID],
    [Y_FORMAT_ID, 'y_format', 'TEXT', 0, 9, None, 'select2', None, json.dumps(supported_formats), 'EXECUTION', FORM_ID]
    [Z_FORMAT_ID, 'z_format', 'TEXT', 0, 9, None, 'select2', None, json.dumps(supported_formats), 'EXECUTION', FORM_ID]
    [T_FORMAT_ID, 't_format', 'TEXT', 0, 9, None, 'select2', None, json.dumps(supported_formats), 'EXECUTION', FORM_ID]
    [Z_SUFIX, 'z_sufix', 'TEXT', 0, 8, 'text', None, None, 'EXECUTION', 111]
    [T_SUFIX, 't_sufix', 'TEXT', 0, 8, 'text', None, None, 'EXECUTION', 111]
    [Z_PREFIX, 'z_prefix', 'TEXT', 0, 8, 'text', None, None, 'EXECUTION', 111]
    [T_PREFIX, 't_prefix', 'TEXT', 0, 8, 'text', None, None, 'EXECUTION', 111]
  ]

  rows = [dict(list(zip(columns, row))) for row in data]
  op.bulk_insert(tb, rows)
