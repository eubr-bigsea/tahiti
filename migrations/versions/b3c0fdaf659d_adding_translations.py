# -*- coding: utf-8 -*-}
"""Adding translations

Revision ID: b3c0fdaf659d
Revises: a2bbcb8b5823
Create Date: 2017-05-12 10:42:09.555626

"""
from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = 'b3c0fdaf659d'
down_revision = 'a2bbcb8b5823'
branch_labels = None
depends_on = None


def upgrade():
    try:
        op.execute(text('START TRANSACTION'))
        insert_operation_form_field_translation()
    except:
        op.execute(text('ROLLBACK'))
        raise


def insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        (193, 'en', 'Dashboard title', 'Dashboard title'),
        (193, 'pt', 'Título do painel de visualização',
         'Título do painel de visualização'),
        (194, 'en',
         'Column names, comma separated (empty = use data source names)',
         'Column names, comma separated (empty = use data source names)'),
        (194, 'pt',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)'),
        (195, 'en', 'Title', 'Title'),
        (195, 'pt', 'Título', 'Título'),
        (196, 'en',
         'Column names, comma separated (empty = use data source names)',
         'Column names, comma separated (empty = use data source names)'),
        (196, 'pt',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)'),
        (197, 'en', 'Title', 'Title'),
        (197, 'pt', 'Título', 'Título'),
        (198, 'en',
         'Column names, comma separated (empty = use data source names)',
         'Column names, comma separated (empty = use data source names)'),
        (198, 'pt',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)'),
        (199, 'en', 'Title', 'Title'),
        (199, 'pt', 'Título', 'Título'),
        (200, 'en',
         'Column names, comma separated (empty = use data source names)',
         'Column names, comma separated (empty = use data source names)'),
        (200, 'pt',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)'),
        (201, 'en', 'Title', 'Title'),
        (201, 'pt', 'Título', 'Título'),
        (202, 'en',
         'Column names, comma separated (empty = use data source names)',
         'Column names, comma separated (empty = use data source names)'),
        (202, 'pt',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)',
         'Nomes das colunas, separadas por vírgula (vazio = usar nomes da '
         'fonte de dados)'),
        (203, 'en', 'Title', 'Title'),
        (203, 'pt', 'Título', 'Título'),
        (204, 'en', 'Input attribute with indexed data',
         'Input attribute with indexed data'),
        (204, 'pt', 'Atributo de entrada com dados indexados',
         'Input attribute with indexed data'),
        (205, 'en', 'Output attribute(s)', 'Output attribute'),
        (205, 'pt', 'Atributo(s) de saída', 'Atributo de saída'),
        (206, 'en', 'Iterations (max)', 'Iterations (max)'),
        (206, 'pt', 'Iterações (máx)', 'Iterações (máx)'),
        (207, 'en', 'Weigth attribute (optional)',
         'Weigth attribute (optional)'),
        (207, 'pt', 'Atributo com pesos (opcional)',
         'Weigth attribute (optional)'),
        (208, 'en', 'Prediction attribute', 'Prediction attribute'),
        (208, 'pt', 'Atributo para predição', 'Atributo para predição'),
        (209, 'en', 'Regularization parameter', 'Regularization parameter'),
        (209, 'pt', 'Parâmetro de regularização', 'Parâmetro de regularização'),
        (210, 'en', 'Solver', 'Solver'),
        (210, 'pt', 'Solucionador (Solver)', 'Solucionador (Solver)'),
        (211, 'en', 'ElasticNet mixing', 'ElasticNet mixing'),
        (211, 'pt', 'ElasticNet mixing', 'ElasticNet mixing'),
        (212, 'en', 'Features attribute', 'Features attribute'),
        (212, 'pt', 'Atributo com features', 'Atributo com features'),
        (213, 'en', 'Label attribute', 'Label attribute'),
        (213, 'pt', 'Atributo com rótulo', 'Atributo com rótulo'),
        (214, 'en', 'Attributes', 'Attributes to be indexed'),
        (214, 'pt', 'Atributos', 'Atributos a serem indexados'),
        (215, 'en', 'Alias', 'Alias(es) for generated indexed fields'),
        (215, 'pt', 'Alias', 'Alias para os campos indexados gerados'),
        (216, 'en', 'Original attribute(s)', 'Original attribute'),
        (216, 'pt', 'Atributo(s) original(ais)', 'Atributo original'),
        (217, 'en', 'Features attribute', 'Features attribute'),
        (217, 'pt', 'Atributo com features', 'Atributo com features'),
        (218, 'en', 'Label attribute', 'Label attribute'),
        (218, 'pt', 'Atributo com rótulo', 'Atributo com rótulo'),
        (219, 'en', 'Prediction attribute', 'Prediction attribute'),
        (219, 'pt', 'Atributo para predição', 'Atributo para predição'),
        (220, 'en', 'Weight attribute', 'Weight attribute'),
        (220, 'pt', 'Atributo com os pesos', 'Atributo com os pesos'),
        (221, 'en', 'Isotonic/increasing', 'Isotonic/increasing'),
        (221, 'pt', 'Isotônica/crescente', 'Isotônica/crescente'),
        (222, 'en',
         'Column names, comma separated (empty = use data source names)',
         'Column names, comma separated (empty = use data source names)'),
        (222, 'pt',
         'Nomes dos atributos, separados por vírgula (vazio = usar nomes da '
         'fonte de dados)',
         'Nomes dos atributos, separados por vírgula (vazio = usar nomes da '
         'fonte de dados)'),
        (223, 'en', 'Title', 'Title'),
        (223, 'pt', 'Título', 'Título'),
        (224, 'en', 'Calculate', 'Calculate'),
        (224, 'pt', 'Calcular', 'Calcular'),
        (225, 'en',
         'Attribute  names, comma separated (empty = use data source names)',
         'Attribute names, comma separated (empty = use data source names)'),
        (225, 'pt',
         'Atributos, separados por vírgula (vazio = usar nomes da '
         'fonte de dados)',
         'Atributos, separados por vírgula (vazio = usar nomes da '
         'fonte de dados)'),
        (226, 'en', 'Title', 'Tiel'),
        (226, 'pt', 'Título', 'Título'),
        (227, 'en', 'Minimum support',
         'The minimum support for an itemset to be identified as frequent. '
         'For example, if an item appears 3 out of 5 transactions, '
         'it has a support of 3/5=0.6.'),
        (227, 'pt', 'Suporte mínimo', 'Suporte mínimo'),
        (228, 'en', 'Attribute with transactions (empty = first attribute)',
         ' Attribute with transactions (empty = first attribute)'),
        (228, 'pt', 'Atributo com transações (vazio = primeiro attributo)',
         'Atributo com transações (vazio = primeiro attributo)'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]

    op.bulk_insert(tb, rows)


def downgrade():
    try:
        op.execute(text('START TRANSACTION'))
        op.execute(text('DELETE FROM operation_form_field_translation '
                        'WHERE id BETWEEN 193 AND 228'))
    except:
        op.execute(text('ROLLBACK'))
        raise
