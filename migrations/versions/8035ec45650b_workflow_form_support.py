"""Workflow form support

Revision ID: 8035ec45650b
Revises: d7432648e1ea
Create Date: 2018-11-06 09:55:20.244285

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '8035ec45650b'
down_revision = 'd7432648e1ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('platform_form',
                    sa.Column('platform_id', sa.Integer(), nullable=False),
                    sa.Column('operation_form_id', sa.Integer(),
                              nullable=False),
                    sa.ForeignKeyConstraint(['operation_form_id'],
                                            ['operation_form.id'], ),
                    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], )
                    )
    op.add_column(u'operation_category',
                  sa.Column('order', sa.Integer(), nullable=False, default=1))
    op.add_column(u'operation_category',
                  sa.Column('default_order', sa.Integer(), nullable=False,
                            default=1))
    op.add_column(u'workflow',
                  sa.Column('is_system_template', sa.Boolean(), nullable=False,
                            default=0))

    op.add_column(u'operation_form_field',
                  sa.Column('enable_conditions', sa.String(length=2000),
                            nullable=True))
    op.add_column(u'workflow', sa.Column('forms', sa.TEXT(),
                                         nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'workflow', 'forms')
    op.drop_column(u'workflow', 'is_system_template')
    op.drop_column(u'operation_form_field', 'enable_conditions')
    op.drop_column(u'operation_category', 'order')
    op.drop_column(u'operation_category', 'default_order')
    op.drop_column(u'operation', 'enable_conditions')
    op.drop_table('platform_form')
    # ### end Alembic commands ###