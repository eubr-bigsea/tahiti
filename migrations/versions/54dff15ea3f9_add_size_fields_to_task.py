"""Add size fields to task

Revision ID: 54dff15ea3f9
Revises: 8a4558f255a4
Create Date: 2019-03-18 10:40:13.391823

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '54dff15ea3f9'
down_revision = '437099b06855'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task',
                  sa.Column('group_id', sa.String(length=250), nullable=True))
    op.add_column('task', sa.Column('height', sa.Integer(), nullable=False))
    op.add_column('task', sa.Column('width', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'task', 'task', ['group_id'], ['id'])
    op.add_column('workflow', sa.Column('type', sa.Enum(
        'WORKFLOW', 'SYSTEM_TEMPLATE', 'SUB_FLOW', 'USER_TEMPLATE',
        name='WorkflowTypeEnumType'),
                                        nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workflow', 'type')
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'width')
    op.drop_column('task', 'height')
    op.drop_column('task', 'group_id')
    # ### end Alembic commands ###