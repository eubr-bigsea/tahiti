"""Keras documentation links.

Revision ID: f98150821301
Revises: cb687f5f7b55
Create Date: 2019-09-16 13:25:26.619790

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json


# revision identifiers, used by Alembic.
revision = 'f98150821301'
down_revision = 'cb687f5f7b55'
branch_labels = None
depends_on = None

CORE_BASE_URL = 'https://keras.io/layers/core/#'
CORE_LIST = [('5011', 'dense'), ('5012', 'dropout'), ('5013', 'flatten'),
             ('5014', 'activation'), ('5015', 'reshape'), ('5016', 'permute'),
             ('5017', 'repeatVector'), ('5018', 'lambda'),
             ('5019', 'activityRegularization'), ('5023', 'masking'),
             ('5024', 'spatialDropout1D'), ('5025', 'spatialDropout2D'),
             ('5026', 'spatialDropout3D'), ('5100', 'input')]

all_commands = [
    ("""
        ALTER TABLE `operation` 
        ADD COLUMN `doc_link` VARCHAR(200) NULL DEFAULT NULL AFTER `css_class`
     """,
     """
        ALTER TABLE `operation` 
        DROP COLUMN `doc_link`
     """),

    ("""
        UPDATE operation_form_field 
        SET `order` = 1 
        WHERE id = 5475 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 2, `default` = 1
        WHERE id = 5541 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 3, `default` = NULL, `required` = 0
        WHERE id = 5474
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 4
        WHERE id = 5479 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 5 
        WHERE id = 5480 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 6 
        WHERE id = 5481 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 7, `default` = NULL
        WHERE id = 5482 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 8 
        WHERE id = 5483 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 9 
        WHERE id = 5484
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 10 
        WHERE id = 5485 
     """, ""),
    ("""
        UPDATE operation_form_field 
        SET `order` = 11 
        WHERE id = 5486 
     """, ""),

]

# for _id, slug in CORE_LIST:
#     all_commands.append(
#         (
#         """
#             UPDATE operation
#             SET doc_link = concat('{url}', '{slug}')
#             WHERE id = {operation_id}
#          """.format(url=CORE_BASE_URL, slug=slug, operation_id=_id), ""),
#     )
#     print(all_commands[-1])


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if cmd[0]:
                if isinstance(cmd[0], str):
                    connection.execute(cmd[0])
                elif isinstance(cmd[0], list):
                    for row in cmd[0]:
                        connection.execute(row)
                else:
                    cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in reversed(all_commands):
            if cmd[1]:
                if isinstance(cmd[1], str):
                    connection.execute(cmd[1])
                elif isinstance(cmd[1], list):
                    for row in cmd[1]:
                        connection.execute(row)
                else:
                    cmd[1]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()
