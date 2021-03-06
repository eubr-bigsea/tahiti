"""empty message

Revision ID: b7442131c810
Revises: c95ef59cb317
Create Date: 2020-08-24 17:13:19.186937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7442131c810'
down_revision = 'c95ef59cb317'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workflow', sa.Column('preferred_cluster_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workflow', 'preferred_cluster_id')
    # ### end Alembic commands ###
