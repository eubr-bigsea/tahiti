"""empty message

Revision ID: d7b25721d1ff
Revises: 3baf65d9906d
Create Date: 2017-03-28 18:05:59.132136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7b25721d1ff'
down_revision = '3baf65d9906d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation_ui_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('ATTRIBUTE_LIST', name='OperationUiCodeTypeEnumType'), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation_ui_code')
    # ### end Alembic commands ###
