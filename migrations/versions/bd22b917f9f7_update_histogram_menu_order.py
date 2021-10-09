"""Update Histogram menu order

Revision ID: bd22b917f9f7
Revises: c4b87364ce33
Create Date: 2021-10-09 00:07:26.892344

"""
from alembic import op
from sqlalchemy.sql import text
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd22b917f9f7'
down_revision = 'c4b87364ce33'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(text("UPDATE `tahiti`.`operation_form` SET `order` = '1' WHERE (`id` = '142');"))


def downgrade():
    op.execute(text("UPDATE `tahiti`.`operation_form` SET `order` = '10' WHERE (`id` = '142');"))
