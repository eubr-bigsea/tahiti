# coding=utf-8
"""box_plot

Revision ID: 3512b954651e
Revises: ea3e48aa084c
Create Date: 2019-04-26 08:29:24.212398

"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '3512b954651e'
down_revision = 'ea3e48aa084c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE workflow MODIFY COLUMN user_id varchar(50);')
    op.execute(
        'ALTER TABLE workflow_history MODIFY COLUMN user_id varchar(50);')
    op.execute(
        'ALTER TABLE workflow_permission MODIFY COLUMN user_id  varchar(50);')


def downgrade():
    op.execute('ALTER TABLE workflow MODIFY COLUMN user_id int(11);')
    op.execute('ALTER TABLE workflow_history MODIFY COLUMN user_id int(11);')
    op.execute(
        'ALTER TABLE workflow_permission MODIFY COLUMN user_id int(11);')
