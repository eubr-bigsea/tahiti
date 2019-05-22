# encoding=utf8

"""Renames field from forms 85 and 113

Revision ID: db303e910542
Revises: 30c5dab11452
Create Date: 2018-04-17 15:48:16.729916

"""
from alembic import op
import sqlalchemy as sa

PIE_X_PREFIX = 342
PIE_X_SUFIX = 343
DONUT_X_PREFIX = 308
DONUT_X_SUFIX = 309

# revision identifiers, used by Alembic.
revision = 'db303e910542'
down_revision = '30c5dab11452'
branch_labels = None
depends_on = None

def upgrade():
  op.execute('UPDATE operation_form_field_translation \
      set label = "Label prefix", help = "Text added on the beggining of label string" \
      WHERE id={} \
      AND locale="en"'.format(PIE_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Label prefix", help = "Text added on the beggining of label string" \
      WHERE id={} \
      AND locale="en"'.format(DONUT_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Prefixo para rótulo", help = "Texto adicionado ao início do rótulo" \
      WHERE id={} \
      AND locale="pt"'.format(PIE_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Prefixo para rótulo", help = "Texto adicionado ao início do rótulo" \
      WHERE id={} \
      AND locale="pt"'.format(DONUT_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Label sufix", help = "Text appended on the end of label string" \
      WHERE id={} \
      AND locale="en"'.format(PIE_X_SUFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Label sufix", help = "Text appended on the end of label string" \
      WHERE id={} \
      AND locale="en"'.format(DONUT_X_SUFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Sufixo para rótulo", help = "Texto adicionado ao final do rótulo" \
      WHERE id={} \
      AND locale="pt"'.format(PIE_X_SUFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Sufixo para rótulo", help = "Texto adicionado ao final do rótulo" \
      WHERE id={} \
      AND locale="pt"'.format(DONUT_X_SUFIX))


def downgrade():
  op.execute('UPDATE operation_form_field_translation \
      set label = "X-axis prefix (added to the value when displaying it)", help = "X-axis prefix (added to the value when displaying it)" \
      WHERE id={} \
      AND locale="en"'.format(PIE_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Prefixo para eixo X", help = "Prefixo para eixo X (adicionado ao valor ao exibi-lo)" \
      WHERE id={} \
      AND locale="pt"'.format(PIE_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "X-axis prefix (added to the value when displaying it)", help = "X-axis prefix (added to the value when displaying it)" \
      WHERE id={} \
      AND locale="en"'.format(DONUT_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "Prefixo para eixo X", help = "Prefixo para eixo X (adicionado ao valor ao exibi-lo)" \
      WHERE id={} \
      AND locale="pt"'.format(DONUT_X_PREFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "X-axis sufix (added to the value when displaying it)", help = "X-axis sufix (added to the value when displaying it)" \
      WHERE id={} \
      AND locale="en"'.format(PIE_X_SUFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "sufixo para eixo X", help = "sufixo para eixo X (adicionado ao valor ao exibi-lo)" \
      WHERE id={} \
      AND locale="pt"'.format(PIE_X_SUFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "X-axis sufix (added to the value when displaying it)", help = "X-axis sufix (added to the value when displaying it)" \
      WHERE id={} \
      AND locale="en"'.format(DONUT_X_SUFIX))
  op.execute('UPDATE operation_form_field_translation \
      set label = "sufixo para eixo X", help = "sufixo para eixo X (adicionado ao valor ao exibi-lo)" \
      WHERE id={} \
      AND locale="pt"'.format(DONUT_X_SUFIX))
