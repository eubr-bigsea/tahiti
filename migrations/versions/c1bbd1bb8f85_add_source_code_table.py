"""add source code table

Revision ID: c1bbd1bb8f85
Revises: cf0607926635
Create Date: 2023-11-27 17:16:10.717069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1bbd1bb8f85'
down_revision = 'cf0607926635'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('source_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('suspicious', sa.Boolean(), nullable=False),
    sa.Column('requirements', sa.String(length=200), nullable=True),
    sa.Column('imports', sa.String(length=200), nullable=True),
    sa.Column('help', sa.String(length=400), nullable=True),
    sa.Column('code', sa.String(length=4000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('source_code')
    # ### end Alembic commands ###
