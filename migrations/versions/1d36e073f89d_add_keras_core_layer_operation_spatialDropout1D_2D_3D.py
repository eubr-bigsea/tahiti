# -*- coding: utf-8 -*-
"""Add Keras Core Layer Operation SpatialDropout1D, SpatialDropout2D and SpatialDropout3D

Revision ID: 1d36e073f89d
Revises: e2679b474622
Create Date: 2018-11-06 10:14:02.799653

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = '1d36e073f89d'
down_revision = 'e2679b474622'
branch_labels = None
depends_on = None

KERAS_PLATAFORM_ID = 5


def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer), )

    columns = ('operation_id', 'platform_id')
    data = [
        # SpatialDropout1D
        (5024, KERAS_PLATAFORM_ID),
        # SpatialDropout2D
        (5025, KERAS_PLATAFORM_ID),
        # SpatialDropout3D
        (5026, KERAS_PLATAFORM_ID),

    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation():
    tb = table(
        'operation',
        column('id', Integer),
        column('slug', String),
        column('enabled', Integer),
        column('type', String),
        column('icon', Integer),)

    columns = ('id', 'slug', 'enabled', 'type', 'icon')
    data = [
        # SpatialDropout1D
        (5024, "spatialDropout1D", 1, 'ACTION', ''),
        # SpatialDropout2D
        (5025, "spatialDropout2D", 1, 'ACTION', ''),
        # SpatialDropout3D
        (5026, "spatialDropout3D", 1, 'ACTION', ''),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category():
    tb = table(
        'operation_category',
        column('id', Integer),
        column('type', String),
        column('order', Integer),
        column('default_order', Integer),
        )

    columns = ('id', 'type', 'order', 'default_order')
    data = [
        # SpatialDropout1D
        (5024, "subgroup", 9, 9),
        # SpatialDropout2D
        (5025, "subgroup", 9, 9),
        # SpatialDropout3D
        (5026, "subgroup", 9, 9),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_category_id', 'operation_id')
    data = [
        # Core Layers - SpatialDropout1D
        (5010, 5024),
        # Core Layers - SpatialDropout2D
        (5010, 5025),
        # Core Layers - SpatialDropout3D
        (5010, 5026),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String))

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (5024, "en", 'SpatialDropout1D', 'Spatial 1D version of Dropout. This version '
                                         'performs the same function as Dropout, '
                                         'however it drops entire 1D feature maps '
                                         'instead of individual elements. If adjacent '
                                         'frames within feature maps are strongly correlated '
                                         '(as is normally the case in early convolution layers) '
                                         'then regular dropout will not regularize the '
                                         'activations and will otherwise just result in '
                                         'an effective learning rate decrease. In this case, '
                                         'SpatialDropout1D will help promote independence between '
                                         'feature maps and should be used instead.'),
        (5025, "en", 'SpatialDropout2D', 'Spatial 2D version of Dropout. This version performs '
                                         'the same function as Dropout, however it drops entire 2D '
                                         'feature maps instead of individual elements. If adjacent '
                                         'pixels within feature maps are strongly correlated (as is '
                                         'normally the case in early convolution layers) then '
                                         'regular dropout will not regularize the activations '
                                         'and will otherwise just result in an effective learning '
                                         'rate decrease. In this case, SpatialDropout2D will help '
                                         'promote independence between feature maps and '
                                         'should be used instead.'),
        (5026, "en", 'SpatialDropout3D', 'Spatial 3D version of Dropout. This version performs '
                                         'the same function as Dropout, however it drops entire '
                                         '3D feature maps instead of individual elements. If '
                                         'adjacent voxels within feature maps are strongly '
                                         'correlated (as is normally the case in early convolution '
                                         'layers) then regular dropout will not regularize '
                                         'the activations and will otherwise just result in an '
                                         'effective learning rate decrease. In this case, '
                                         'SpatialDropout3D will help promote independence between '
                                         'feature maps and should be used instead.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String),)

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        # SpatialDropout1D
        (5124, 'INPUT', '', 1, 'ONE', 5024, 'input data'),
        (5224, 'OUTPUT', '', 1, 'ONE', 5024, 'output data'),
        # SpatialDropout2D
        (5125, 'INPUT', '', 1, 'ONE', 5025, 'input data'),
        (5225, 'OUTPUT', '', 1, 'ONE', 5025, 'output data'),
        # SpatialDropout3D
        (5126, 'INPUT', '', 1, 'ONE', 5026, 'input data'),
        (5226, 'OUTPUT', '', 1, 'ONE', 5026, 'output data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer))

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        # SpatialDropout1D
        (5124, 1),
        (5224, 1),
        # SpatialDropout2D
        (5125, 1),
        (5225, 1),
        # SpatialDropout3D
        (5126, 1),
        (5226, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

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
        # SpatialDropout1D
        (5124, "en", 'input data', 'Input data'),
        (5224, "en", 'output data', 'Output data'),
        # SpatialDropout2D
        (5125, "en", 'input data', 'Input data'),
        (5225, "en", 'output data', 'Output data'),
        # SpatialDropout3D
        (5126, "en", 'input data', 'Input data'),
        (5226, "en", 'output data', 'Output data'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

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
        # SpatialDropout1D, SpatialDropout2D, SpatialDropout3D - rate
        (5142, 1, 1, 'execution'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)


def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        # SpatialDropout1D, SpatialDropout2D, SpatialDropout3D - rate
        (5142, 'en', 'Execution'),
        (5142, 'pt', 'Execução'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        # SpatialDropout1D, SpatialDropout2D, SpatialDropout3D - appearance
        (5024, 41),
        (5025, 41),
        (5026, 41),
        # SpatialDropout1D, SpatialDropout2D, SpatialDropout3D - rate
        (5024, 5142),
        (5025, 5142),
        (5026, 5142),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
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
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [

        # SpatialDropout1D - rate
        (5142, 'rate', 'DECIMAL', 1, 1, 0.0, 'decimal', None, None, 'EXECUTION', 5142),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
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

        # SpatialDropout1D - rate
        (5142, 'en', 'Rate', 'Float between 0 and 1. Fraction of the input units to drop.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    (_insert_operation,
     'DELETE FROM operation WHERE id BETWEEN 5024 AND 5026'),
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id BETWEEN 5024 AND 5026'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id BETWEEN 5024 AND 5026'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id BETWEEN 5024 AND 5026'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform '
     'WHERE operation_id BETWEEN 5024 AND 5026 AND platform_id = {}'.format(KERAS_PLATAFORM_ID)),

    (_insert_operation_port,
     'DELETE FROM operation_port WHERE id IN (5124, 5224, 5125, 5225, 5126, 5226)'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port '
     'WHERE operation_port_id IN (5124, 5224, 5125, 5225, 5126, 5226)'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id IN (5124, 5224, 5125, 5225, 5126, 5226)'),

    (_insert_operation_form,
     'DELETE FROM operation_form WHERE id IN (5142)'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id IN (5142)'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id IN (5142)'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id IN (5142)'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id BETWEEN 5024 AND 5026'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()

