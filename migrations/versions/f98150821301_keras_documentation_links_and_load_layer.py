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


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String), )

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id',
               'slug')
    data = [
        (5395, 'OUTPUT', '', 1, 'MANY', 5117, 'test-image'), #image-reader
        (5396, 'INPUT', '', 1, 'ONE', 5115, 'model'),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (5395, 'en', 'test image data', 'Image Data'),
        (5396, 'en', 'model', 'Model'),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (5395, 24),
        (5396, 22),
    ]
    rows = [dict(zip(columns, row)) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_form_field():
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
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')

    LIMONERO_IMAGE = "`${LIMONERO_URL}/datasources?simple=true&list=" \
                     "true&enabled=1&formats=TAR_IMAGE_FOLDER," \
                     "HAR_IMAGE_FOLDER,IMAGE_FOLDER`"

    LIMONERO_IMAGE_HDF5 = "`${LIMONERO_URL}/datasources?simple=true&list=" \
                          "true&enabled=1&formats=HDF5`"

    CONDITION_MODEL = '(this.weights.internalValue || "") === ""'
    CONDITION_WEIGHTS = '(this.model.internalValue || "") === ""'

    data = [
        (5609, 'test_images', 'INTEGER', 0, 3, None, 'lookup', LIMONERO_IMAGE,
         None, 'EXECUTION', 5238, None),

        (5610, 'model', 'INTEGER', 0, 1, None, 'lookup', LIMONERO_IMAGE_HDF5,
         None, 'EXECUTION', 5246, CONDITION_MODEL),

        (5611, 'weights', 'INTEGER', 0, 2, None, 'lookup', LIMONERO_IMAGE_HDF5,
         None, 'EXECUTION', 5246, CONDITION_WEIGHTS),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        (5609, 'en', 'Test images', ''),
        (5610, 'en', 'Model', ''),
        (5611, 'en', 'Weights', ''),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (5115, 41),
        (5115, 5246),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (5246, 'en', 'Execution'),
        (5246, 'pt', 'Execução'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (5246, 1, 1, 'execution'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)


all_commands = [
    ("""
        UPDATE operation_port 
        SET `order` = 3 
        WHERE id = 5316
     """,
     """
        UPDATE operation_port 
        SET `order` = 2 
        WHERE id = 5316
     """),
    ("""
        UPDATE operation_port 
        SET `order` = 2 
        WHERE id = 5317
     """,
     """
        UPDATE operation_port 
        SET `order` = 1 
        WHERE id = 5317
     """),

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
    ("""
        UPDATE operation_port_translation 
        SET `name` = 'generator' 
        WHERE id = 5393 
     """,
     """
        UPDATE operation_port_translation 
        SET `name` = 'test generator' 
        WHERE id = 5393 
    """),
    ("""
        UPDATE operation 
        SET `slug` = 'load' 
        WHERE id = 5115 
     """,
     """
        UPDATE operation 
        SET `slug` = 'load-model' 
        WHERE id = 5115 
    """),
    ("""
        UPDATE operation_translation 
        SET 
            `name` = 'Load',  
            `description` = 'Load a pre existing model or weights.'  
        WHERE id = 5115 
     """,
     """
        UPDATE operation_translation 
        SET 
            `name` = 'Load model',  
            `description` = 'Load a pre existing model.'  
        WHERE id = 5115 
    """),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id BETWEEN 5395 AND 5396'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id BETWEEN 5395 AND 5396'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id BETWEEN 5395 AND 5396'),
    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id BETWEEN 5246 AND 5246'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field '
     'WHERE id BETWEEN 5609 AND 5611'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation '
     'WHERE id BETWEEN 5609 AND 5611'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form '
     'WHERE operation_id BETWEEN 5115 AND 5115'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id BETWEEN 5246 AND 5246'),

]


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
