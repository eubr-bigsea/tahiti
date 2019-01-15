# -*- coding: utf-8 -*-

"""Adding Split into K folds operaion

Revision ID: 5bfa53aaa86d
Revises: b76fe74daeb6
Create Date: 2019-01-11 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = '5bfa53aaa86d'
down_revision = 'b76fe74daeb6'
branch_labels = None
depends_on = None


def _insert_operation():
    tb = table('operation',
                            column("id", Integer),
                            column("slug", String),
                            column('enabled', Integer),
                            column('type', String),
                            column('icon', String),
                            )
    columns = ['id', 'slug', 'enabled', 'type', 'icon']
    data = [
    (104, 'split-k-fold', 1, 'TRANSFORMATION', 'fa-code-branch'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (104,1),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        (104, 32),  # preprocessamento
        (104, 38),  # amostragem
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
        (130, 1, 1, 'execution'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)

def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (130, 'en', 'Execution'),
        (130, 'pt', 'Execução'),
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
        (104, 41),  # appearance
        (104, 130), # own execution form
        (104, 110), # results
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [

        (104, 'en', 'Split data into K Fold', 'This operation involves dividing the dataset into k folds or partitions of approximately equal size'),
        (104, 'pt', 'Divisão dos dados em K Partições (Validação Cruzada)', 'Esta operação realiza a divisão do conjunto de dados em k partições ou grupos de tamanho aproximadamente igual'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [
        (239, 'INPUT', None, 104, 1, 'ONE', 'input data'),
        (240, 'OUTPUT', None, 104, 1, 'MANY', 'output data'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (239,'en', 'input data', 'Input data'),
        (239,'pt', 'dados de entrada', 'Dados de entrada'),
        (240,'en', 'output data', 'Output data'),
        (240,'pt', 'dados de saída', 'Dados de saída'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (239, 1), #data
        (240, 1), #data
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
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        # 'split-k-fold'
        (477, 'k_fold', 'INTEGER', 1, 0, 7, 'integer', None, None, 'EXECUTION', 130),
        (478, 'type', 'TEXT', 1, 2, 'Random', 'dropdown', None,
		'[{"key": \"Random\", \"value\": \"Random\", "pt": \"Aleatório\", "en": \"Random\"},'
         '{\"key\": \"Stratified\", \"value\": \"Stratified\", "pt": \"Estratificada\", "en": \"Stratified\"}]', 'EXECUTION', 130),
        (479, 'label', 'TEXT', 1, 3, None, 'attribute-selector', None, None, 'EXECUTION', 130),
        (480, 'alias_fold', 'TEXT', 1, 4, None, 'text', None, None, 'EXECUTION', 130),
        (481, 'seed', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 130),
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
        # split-k-folds
        (477, 'en', 'K Folds', 'Number of K folds.'),
        (477, 'pt', 'K Partições', 'Número de partições.'),
        (478, 'en', 'Type', 'Type of cross validation method.'),
        (478, 'pt', 'Tipo de Validação Cruzada', 'Tipo de validação cruzada.'),
        (479, 'en', 'Label', 'Select the feature as label from dataset.'),
        (479, 'pt', 'Classe', 'Selecione o atributo considerado como classe/rótulo (label).'),
        (480, 'en', 'Fold Alias', 'Alias to the new feature column that is an identifier for each object fold.'),
        (480, 'pt', 'Alias', 'Nome da nova coluna que indica a que fold o objeto pertence.'),
        (481, 'en', 'Seed', 'Seed used by the random number generator. Also used for reproducibility.'),
        (481, 'pt', 'Semente', 'Semente usada pelo gerador de números aleatórios. Também usado para reprodutibilidade.'),

	]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)



all_commands = [

	(_insert_operation, 'DELETE FROM operation WHERE id = 104'),
	(_insert_new_operation_platform, 'DELETE FROM operation_platform WHERE operation_id = 104' ),
	(_insert_operation_category_operation, 'DELETE FROM operation_category_operation WHERE operation_id = 104'),
	(_insert_operation_form, 'DELETE FROM operation_form WHERE id = 130'),
	(_insert_operation_form_translation, 'DELETE FROM operation_form_translation WHERE id = 130'),
	(_insert_operation_operation_form, 'DELETE FROM operation_operation_form WHERE operation_id = 104'),
	(_insert_operation_translation, 'DELETE FROM operation_translation WHERE id = 104'),
	(_insert_operation_port, 'DELETE FROM operation_port WHERE id BETWEEN 239 AND 240'),
	(_insert_operation_port_translation, 'DELETE FROM operation_port_translation WHERE id BETWEEN 239 AND 240' ),
	(_insert_operation_port_interface_operation_port, 'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id BETWEEN 239 and 240'),
	(_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 477 and 481'),
	(_insert_operation_form_field_translation,
    'DELETE FROM operation_form_field_translation WHERE id BETWEEN 477 and 481'),
    ]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
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
            if isinstance(cmd[1], (unicode, str)):
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
