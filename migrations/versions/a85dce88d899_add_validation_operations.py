"""add validation operations

Revision ID: a85dce88d899 
Revises: bd22b917f9f7
"""
from alembic import context
from alembic import op
from sqlalchemy import Integer, String, Text, Boolean, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'a85dce88d899'
down_revision = 'bd22b917f9f7'
branch_labels = None
depends_on = None

# --------------------------------------------------------------
# ATENTION: You must revise this auto-generated code.
# Please, review offsets and commands before running a migration
# and optionally, perform a database backup. If everything is 
# OK, remove this comment.
# --------------------------------------------------------------

BASE_OP = 20000
BASE_CATEGORY = 20000
BASE_FORM = 20000
BASE_FORM_FIELD = 20000
BASE_PORT = 20000
BASE_INTERFACE = 20000

def _insert_operation(conn):
    tb = table('operation',
                column('id', Integer), 
                column('slug', String), 
                column('enabled', Boolean), 
                column('type', String), 
                column('icon', String), 
                column('css_class', String), 
                column('doc_link', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_OP + 1, 'validation', 1, 'TRANSFORMATION', '', '', ''], 
      [BASE_OP + 2, 'validation-report', 1, 'TRANSFORMATION', '', '', '']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation(conn):
    conn.execute(
        'DELETE from operation WHERE id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 2)

def _insert_operation_translation(conn):
    tb = table('operation_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_OP + 1, 'pt', 'Validação de dados', 'Valida os dados segundo regras.'], 
      [BASE_OP + 2, 'pt', 'Relatório de validação', 'Gera um relatório de validação.'],
      [BASE_OP + 1, 'en', 'Data validation', 'Validates data against rules.'], 
      [BASE_OP + 2, 'en', 'Data validation report', 'Generates a report for data validation.'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_translation(conn):
    conn.execute(
        'DELETE from operation_translation WHERE id BETWEEN %s AND %s', 
        BASE_OP + 1, BASE_OP + 2)

def _insert_operation_category(conn):
    tb = table('operation_category',
                column('id', Integer), 
                column('type', String), 
                column('order', Integer), 
                column('default_order', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_CATEGORY + 1, 'group', 0, 7]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category(conn):
    conn.execute(
        'DELETE from operation_category WHERE id BETWEEN %s AND %s', 
        BASE_CATEGORY + 1, BASE_CATEGORY + 1)

def _insert_operation_category_translation(conn):
    tb = table('operation_category_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_CATEGORY + 1, 'pt', 'Validação'],
      [BASE_CATEGORY + 1, 'en', 'Validation'],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_translation(conn):
    conn.execute(
        'DELETE from operation_category_translation WHERE id BETWEEN %s AND %s', 
        BASE_CATEGORY + 1, BASE_CATEGORY + 1)

def _insert_operation_form(conn):
    tb = table('operation_form',
                column('id', Integer), 
                column('enabled', Boolean), 
                column('order', Integer), 
                column('category', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 1, 1, 1, 'execution'], 
      [BASE_FORM + 2, 0, 1, 'execution']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form(conn):
    conn.execute(
        'DELETE from operation_form WHERE id BETWEEN %s AND %s', 
        BASE_FORM + 1, BASE_FORM + 2)

def _insert_operation_form_translation(conn):
    tb = table('operation_form_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM + 1, 'pt', 'Execução'], 
      [BASE_FORM + 2, 'pt', 'Execução'], 
      [BASE_FORM + 1, 'en', 'Execution'], 
      [BASE_FORM + 2, 'en', 'Execution'], 
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_translation(conn):
    conn.execute(
        'DELETE from operation_form_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM + 1, BASE_FORM + 2)

def _insert_operation_form_field(conn):
    tb = table('operation_form_field',
                column('id', Integer), 
                column('name', String), 
                column('type', String), 
                column('required', Boolean), 
                column('order', Integer), 
                column('default', String), 
                column('suggested_widget', String), 
                column('values_url', String), 
                column('values', String), 
                column('scope', String), 
                column('enable_conditions', String), 
                column('editable', Boolean), 
                column('form_id', Integer))
    columns = [c.name for c in tb.columns]
    import json
    values_category = json.dumps([
        {'key': 'SHAPE', 'en': 'Table (data or structure)', 'pt': 'Tabela (dados ou estrutura)'},
        {'key': 'DOMAIN', 'en': 'Missing values, unique values, and types', 'pt': 'Valores ausentes, únicos e tipos de dados'},
        {'key': 'SET_RANGE', 'en': 'Sets and ranges', 'pt': 'Conjuntos e faixas'},
        {'key': 'STRING', 'en': 'String matching', 'pt': 'Validação de texto'},
        {'key': 'DATE_AND_JSON', 'en': 'Datetime and JSON parsing', 'pt': 'Datas e JSON'},
        {'key': 'AGGREGATE', 'en': 'Aggregate functions', 'pt': 'Agrupamentos (agregação)'},
        {'key': 'MULTI_COLUMN', 'en': 'Multi-column', 'pt': 'Multicolunas'},
        {'key': 'DISTRIBUTION', 'en': 'Distributional functions', 'pt': 'Distribuição'},
    ])
    values_structure = json.dumps({
        'values': [
        {'key': 'column_to_exist', 'en': 'Columns to exist', 'pt': 'Colunas existem'},
        {'key': 'table_columns_to_match_ordered_list', 'en': 'Table columns to match ordered list', 'pt': 'Colunas estão em ordem'},
        {'key': 'table_columns_to_match_set', 'en': 'Table columns to match set', 'pt': 'Colunas estão neste conjunto'},
        {'key': 'table_column_count_to_be_between', 'en': 'Table column count to be between', 'pt': 'Número de colunas está entre'},
        {'key': 'table_column_count_to_equal', 'en': 'Table column count to equal', 'pt': 'Número de colunas igual a'},
        {'key': 'table_row_count_to_be_between', 'en': 'Table row count to be between', 'pt': 'Número de registros está entre'},
        {'key': 'table_row_count_to_equal', 'en': 'Table row count to equal', 'pt': 'Número de registros igual a'},
        ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})

    values_domain = json.dumps({
        'values': [
        {'key': 'column_values_to_be_unique', 'en': 'Column values to be unique', 'pt': 'Valores da coluna são únicos'},
        {'key': 'column_values_to_not_be_null', 'en': 'Column values to not be null', 'pt': 'Valores da coluna não são nulos'},
        {'key': 'column_values_to_be_null', 'en': 'Column values to be null', 'pt': 'Valores da coluna são nulos'},
        {'key': 'column_values_to_be_of_type', 'en': 'Column values to be of type', 'pt': 'Valores da coluna são do tipo'},
        {'key': 'column_values_to_be_in_type_list', 'en': 'Column values to be in type list', 'pt': 'Valores da coluna são de um destes tipos'},
        ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})
    values_set = json.dumps({
        'values': [
        {'key': 'column_values_to_be_in_set', 'en': 'Column values to be in set', 'pt': 'Valores da coluna estão no conjunto'},
        {'key': 'column_values_to_not_be_in_set', 'en': 'Column values to not be in set', 'pt': 'Valores da coluna não estão no conjunto'},
        {'key': 'column_values_to_be_between', 'en': 'Column values to be between', 'pt': 'Valores da coluna estão entre'},
        {'key': 'column_values_to_be_increasing', 'en': 'Column values to be increasing', 'pt': 'Valores da coluna são crescentes'},
        {'key': 'column_values_to_be_decreasing', 'en': 'Column values to be decreasing', 'pt': 'Valores da coluna são decrescentes'},
        ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})

    values_string = json.dumps({
        'values': [
        {'key': 'column_value_lengths_to_be_between', 'en': 'Column value lengths to be between', 'pt': 'Tamanho do valor da coluna está entre'},
        {'key': 'column_value_lengths_to_equal', 'en': 'Column value lengths to equal', 'pt': 'Tamanho do valor da coluna é igual a'},
        {'key': 'column_values_to_match_regex', 'en': 'Column values to match regex', 'pt': 'Valores da coluna casam com expressão regular'},
        {'key': 'column_values_to_not_match_regex', 'en': 'Column values to not match regex', 'pt': 'Valores da coluna não casam com expressão regular'},
        {'key': 'column_values_to_match_regex_list', 'en': 'Column values to match regex list', 'pt': 'Valores da coluna casam com lista de expressões regulares'},
        {'key': 'column_values_to_not_match_regex_list', 'en': 'Column values to not match regex list', 'pt': 'Valores da coluna não casam com lista de expressões regulares'},
        {'key': 'column_values_to_match_like_pattern', 'en': 'Column values to match SQL like pattern', 'pt': 'Valores da coluna casam padrão "SQL LIKE"'},
        {'key': 'column_values_to_not_match_like_pattern', 'en': 'Column values to not match SQL like pattern', 'pt': 'Valores da coluna não casam padrão "SQL LIKE"'},
        {'key': 'column_values_to_match_like_pattern_list', 'en': 'Column values to match SQL like pattern list', 'pt': 'Valores da coluna casam com lista de padrões "SQL LIKE"'},
        {'key': 'column_values_to_not_match_like_pattern_list', 'en': 'Column values to not match SQL like pattern list', 'pt': 'Valores da coluna casam não casam com lista de padrões "SQL LIKE"'},
        ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})

    values_date = json.dumps({
        'values': [
        {'key': 'column_values_to_match_strftime_format', 'en': 'Column values to match strftime format', 'pt': 'Valores da coluna casam com formato (Python)'},
        {'key': 'column_values_to_be_dateutil_parseable', 'en': 'Column values to be dateutil parseable', 'pt': 'Valores da coluna são conversíveis para data'},
        {'key': 'column_values_to_be_json_parseable', 'en': 'Column values to be json parseable', 'pt': 'Valores da coluna são conversíveis para JSON'},
        {'key': 'column_values_to_match_json_schema', 'en': 'Column values to match json schema', 'pt': 'Valores da coluna casam com esquema JSON'},
        ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})

    values_agg = json.dumps({
        'values': [
        {'key': 'column_distinct_values_to_be_in_set', 'en': 'Column distinct values to be in set', 'pt': 'Lista de valores distintos da coluna estão no conjunto'},
        {'key': 'column_distinct_values_to_equal_set', 'en': 'Column distinct values to equal set', 'pt': 'Lista de valores distintos da coluna igual ao conjunto'},
        {'key': 'column_distinct_values_to_contain_set', 'en': 'Column distinct values to contain set', 'pt': 'Lista de valores distintos da coluna contém o conjunto'},
        {'key': 'column_quantile_values_to_be_between', 'en': 'Column quantile values to be between', 'pt': 'Valor do quantil para a coluna está entre'},
        {'key': 'column_unique_value_count_to_be_between', 'en': 'Column unique value count to be between', 'pt': 'Contagem de valores únicos da coluna está entre'},
        {'key': 'column_proportion_of_unique_values_to_be_between', 'en': 'Column proportion of unique values to be between', 'pt': 'Proporção de valores únicos da coluna está entre'},
        {'key': 'column_most_common_value_to_be_in_set', 'en': 'Column most common value to be in set', 'pt': 'Valor mais comum da coluna está no conjunto'},
        {'key': 'column_sum_to_be_between', 'en': 'Column sum to be between', 'pt': 'Soma da coluna está entre'},
        {'key': 'column_mean_to_be_between', 'en': 'Column mean to be between', 'pt': 'Média da coluna está entre'},
        {'key': 'column_median_to_be_between', 'en': 'Column median to be between', 'pt': 'Mediana da coluna está entre'},
        {'key': 'column_stdev_to_be_between', 'en': 'Column stdev to be between', 'pt': 'Desvio-padrão da coluna está entre'},
        {'key': 'column_min_to_be_between', 'en': 'Column min to be between', 'pt': 'Mínimo da coluna está entre'},
        {'key': 'column_max_to_be_between', 'en': 'Column max to be between', 'pt': 'Máximo da coluna está entre'},
        ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})

    values_dist = json.dumps({
        'values': [
        {'key': 'column_parameterized_distribution_ks_test_p_value_to_be_greater_than', 
            'en': 'Column values ​​are in accordance to a continuous distribution with a parametric Kolmogorov-Smirnov test.', 
            'pt': 'Valores da coluna estão de acordo com uma distribuição contínua com um test paramétrico Kolmogorov-Smirnov'},
        {'key': 'column_chisquare_test_p_value_to_be_greater_than', 
            'en': 'Column values are distributed similarly to the provided categorical partition using a Chi-squared test', 
            'pt': 'Os valores das colunas estão distribuídos de forma semelhante à partição categórica fornecida usando um teste de chi-squared'},
        {'key': 'column_bootstrapped_ks_test_p_value_to_be_greater_than', 
            'en': 'Column values are distributed similarly to the provided continuous partition using a bootstrapped Kolmogorov-Smirnov test', 
            'pt': 'Os valores das colunas são distribuídos de forma semelhante à partição contínua fornecida usando um teste de Kolmogorov-Smirnov inicializado'},
        {'key': 'column_kl_divergence_to_be_less_than', 
            'en': 'Kulback-Leibler (KL) divergence (relative entropy) of column with respect to the partition object is lower than the provided threshold', 
            'pt': 'A divergência de Kulback-Leibler (KL) (entropia relativa) da coluna em relação ao objeto de partição é inferior ao limite fornecido'},
        ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})

    values_multi  = json.dumps({
        'values': [
        {'key': 'column_pair_cramers_phi_value_to_be_less_than', 
            'en': 'Expect the values in column_A to be independent of those in column_B.', 
            'pt': 'Os valores em coluna_A devem ser independentes daqueles em coluna_B.'},
        {'key': 'column_pair_values_to_be_equal', 
            'en': 'Column pair values to be equal', 'pt': 'Valores para par de colunas deve ser igual'},
        {'key': 'Values in column A are greater than column B.', 'pt': 'Valores na coluna A são maiores do que os da coluna B'},
        {'key': 'column_pair_values_to_be_in_set', 'en': 'Paired values from columns A and B to belong to a set of valid pairs.', 
            'pt': 'Os valores emparelhados das colunas A e B pertencem a um conjunto de pares válidos.'},
        # Deprected in Great Expectations
        # {'key': 'multicolumn_values_to_be_unique', 'en': 'Multicolumn values to be unique', 'pt': 'multicolumn values to be unique'},
        {'key': 'select_column_values_to_be_unique_within_record', 
            'en': 'Values for each record are unique across the columns listed (records may be duplicated).', 
            'pt': 'Os valores de cada registro são únicos nas colunas listadas (os registros podem ser duplicados)'},
        {'key': 'compound_columns_to_be_unique', 'en': 'Columns are unique together', 'pt': 'Colunas, quando juntas, são únicas'},
        {'key': 'multicolumn_sum_to_equal', 'en': 'The sum of all rows for a set of columns is equal to a specific value', 
        'pt': 'Soma de todas as linhas para um conjunto de colunas é igual a um valor específico'}
    ], 'help': 'https://great-expectations.readthedocs.io/en/latest/autoapi/great_expectations/dataset/dataset/index.html#great_expectations.dataset.dataset.Dataset.expect_${key}'})
    data = [
      [BASE_FORM_FIELD + 1, 'category', 'TEXT', 1, 1, None, 'dropdown', None, values_category, 'DESIGN', None, 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 2, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_structure, 'DESIGN', 'this.category.internalValue === "SHAPE"', 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 3, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_domain, 'DESIGN', 'this.category.internalValue === "DOMAIN"', 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 4, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_set, 'DESIGN', 'this.category.internalValue === "SET_RANGE"', 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 5, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_string, 'DESIGN', 'this.category.internalValue === "STRING"', 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 6, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_date, 'DESIGN', 'this.category.internalValue === "DATE_AND_JSON"', 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 7, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_agg, 'DESIGN', 'this.category.internalValue === "AGGREGATE"', 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 8, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_dist, 'DESIGN', 'this.category.internalValue === "DISTRIBUTION"', 1, BASE_FORM + 1], 
      [BASE_FORM_FIELD + 9, 'validation', 'TEXT', 1, 2, None, 'dropdown', None, values_multi, 'DESIGN', 'this.category.internalValue === "MULTI_COLUMN"', 1, BASE_FORM + 1], 

      [BASE_FORM_FIELD + 10, 'allow_cross_type_comparisons', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_values_to_be_between","column_pair_values_A_to_be_greater_than_B"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 11, 'allow_relative_error', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_quantile_values_to_be_between"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 12, 'bins_A', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_pair_cramers_phi_value_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 13, 'bins_B', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_pair_cramers_phi_value_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 14, 'bootstrap_sample_size', 'INTEGER', 0, 10, None, 'integer', None, None, 'DESIGN', '["column_bootstrapped_ks_test_p_value_to_be_greater_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 15, 'bootstrap_samples', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_bootstrapped_ks_test_p_value_to_be_greater_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 16, 'bucketize_data', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_kl_divergence_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 17, 'columns', 'TEXT', 0, 10, None, 'attribute-selector', None, None, 'DESIGN', '! [undefined, null, "", "table_column_count_to_be_between", "table_column_count_to_equal", "table_row_count_to_be_between", "table_columns_to_match_set", "table_columns_to_match_ordered_list", "table_row_count_to_equal"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 18, 'column_A', 'TEXT', 0, 10, None, 'attribute-selector', None, None, 'DESIGN', '["column_pair_cramers_phi_value_to_be_less_than","column_pair_values_to_be_equal","column_pair_values_A_to_be_greater_than_B","column_pair_values_to_be_in_set"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 19, 'column_B', 'TEXT', 0, 10, None, 'attribute-selector', None, None, 'DESIGN', '["column_pair_cramers_phi_value_to_be_less_than","column_pair_values_to_be_equal","column_pair_values_A_to_be_greater_than_B","column_pair_values_to_be_in_set"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 20, 'column_index', 'INTEGER', 0, 10, None, 'integer', None, None, 'DESIGN', '["column_to_exist"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 21, 'column_list', 'TEXT', 0, 10, None, 'textarea', None, None, 'DESIGN', '["table_columns_to_match_ordered_list","multicolumn_values_to_be_unique","select_column_values_to_be_unique_within_record","compound_columns_to_be_unique","multicolumn_sum_to_equal"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 22, 'column_set', 'TEXT', 0, 10, None, 'textarea', None, None, 'DESIGN', '["table_columns_to_match_set"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
#      [BASE_FORM_FIELD + 23, 'condition_parser', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_be_unique","column_values_to_not_be_null","column_values_to_be_null","column_values_to_be_of_type","column_values_to_be_in_type_list","column_values_to_be_in_set","column_values_to_not_be_in_set","column_values_to_be_between","column_values_to_be_increasing","column_values_to_be_decreasing","column_value_lengths_to_be_between","column_value_lengths_to_equal","column_values_to_match_regex","column_values_to_not_match_regex","column_values_to_match_regex_list","column_values_to_not_match_regex_list","column_values_to_match_strftime_format","column_values_to_be_dateutil_parseable","column_values_to_be_json_parseable","column_values_to_match_json_schema","column_parameterized_distribution_ks_test_p_value_to_be_greater_than","multicolumn_values_to_be_unique","select_column_values_to_be_unique_within_record","compound_columns_to_be_unique"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 24, 'distribution', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_parameterized_distribution_ks_test_p_value_to_be_greater_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 25, 'exact_match', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["table_columns_to_match_set"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 26, 'ignore_row_if', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_pair_values_to_be_equal","column_pair_values_A_to_be_greater_than_B","column_pair_values_to_be_in_set","multicolumn_values_to_be_unique","select_column_values_to_be_unique_within_record","compound_columns_to_be_unique"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 27, 'internal_weight_holdout', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_kl_divergence_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 28, 'json_schema', 'TEXT', 0, 10, None, 'textarea', None, None, 'DESIGN', '["column_values_to_match_json_schema"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 29, 'match_on', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_match_regex_list"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 30, 'max_value', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["table_column_count_to_be_between","table_row_count_to_be_between","column_values_to_be_between","column_value_lengths_to_be_between","column_mean_to_be_between","column_median_to_be_between","column_stdev_to_be_between","column_unique_value_count_to_be_between","column_proportion_of_unique_values_to_be_between","column_sum_to_be_between","column_min_to_be_between","column_max_to_be_between"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 31, 'min_value', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["table_column_count_to_be_between","table_row_count_to_be_between","column_values_to_be_between","column_value_lengths_to_be_between","column_mean_to_be_between","column_median_to_be_between","column_stdev_to_be_between","column_unique_value_count_to_be_between","column_proportion_of_unique_values_to_be_between","column_sum_to_be_between","column_min_to_be_between","column_max_to_be_between"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 32, 'mostly', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_be_unique","column_values_to_not_be_null","column_values_to_be_null","column_values_to_be_of_type","column_values_to_be_in_type_list","column_values_to_be_in_set","column_values_to_not_be_in_set","column_values_to_be_between","column_values_to_be_increasing","column_values_to_be_decreasing","column_value_lengths_to_be_between","column_value_lengths_to_equal","column_values_to_match_regex","column_values_to_not_match_regex","column_values_to_match_regex_list","column_values_to_not_match_regex_list","column_values_to_match_strftime_format","column_values_to_be_dateutil_parseable","column_values_to_be_json_parseable","column_values_to_match_json_schema"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 33, 'n_bins_A', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_pair_cramers_phi_value_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 34, 'n_bins_B', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_pair_cramers_phi_value_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 35, 'or_equal', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_pair_values_A_to_be_greater_than_B"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 36, 'output_strftime_format', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_be_between","column_min_to_be_between","column_max_to_be_between"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 37, 'p', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_chisquare_test_p_value_to_be_greater_than","column_bootstrapped_ks_test_p_value_to_be_greater_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 38, 'p_value', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_parameterized_distribution_ks_test_p_value_to_be_greater_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 39, 'params', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_parameterized_distribution_ks_test_p_value_to_be_greater_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 40, 'parse_strings_as_datetimes', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_values_to_be_in_set","column_values_to_not_be_in_set","column_values_to_be_between","column_values_to_be_increasing","column_values_to_be_decreasing","column_distinct_values_to_be_in_set","column_distinct_values_to_equal_set","column_distinct_values_to_contain_set","column_min_to_be_between","column_max_to_be_between","column_pair_values_A_to_be_greater_than_B"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 41, 'partition_object', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_chisquare_test_p_value_to_be_greater_than","column_bootstrapped_ks_test_p_value_to_be_greater_than","column_kl_divergence_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 42, 'quantile_ranges', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_quantile_values_to_be_between"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 43, 'regex', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_match_regex","column_values_to_not_match_regex"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 44, 'regex_list', 'TEXT', 0, 10, None, 'textarea', None, None, 'DESIGN', '["column_values_to_match_regex_list","column_values_to_not_match_regex_list"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      # Only Pandas
      # [BASE_FORM_FIELD + 45, 'row_condition', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_be_unique","column_values_to_not_be_null","column_values_to_be_null","column_values_to_be_of_type","column_values_to_be_in_type_list","column_values_to_be_in_set","column_values_to_not_be_in_set","column_values_to_be_between","column_values_to_be_increasing","column_values_to_be_decreasing","column_value_lengths_to_be_between","column_value_lengths_to_equal","column_values_to_match_regex","column_values_to_not_match_regex","column_values_to_match_regex_list","column_values_to_not_match_regex_list","column_values_to_match_strftime_format","column_values_to_be_dateutil_parseable","column_values_to_be_json_parseable","column_values_to_match_json_schema","column_parameterized_distribution_ks_test_p_value_to_be_greater_than","multicolumn_values_to_be_unique","select_column_values_to_be_unique_within_record","compound_columns_to_be_unique"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 46, 'strftime_format', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_match_strftime_format"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 47, 'strict_max', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_values_to_be_between","column_mean_to_be_between","column_median_to_be_between","column_stdev_to_be_between","column_proportion_of_unique_values_to_be_between","column_sum_to_be_between","column_min_to_be_between","column_max_to_be_between"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 48, 'strict_min', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_values_to_be_between","column_mean_to_be_between","column_median_to_be_between","column_stdev_to_be_between","column_proportion_of_unique_values_to_be_between","column_sum_to_be_between","column_min_to_be_between","column_max_to_be_between"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 49, 'strictly', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_values_to_be_increasing","column_values_to_be_decreasing"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 50, 'sum_total', 'DECIMAL', 0, 10, None, 'decimal', None, None, 'DESIGN', '["multicolumn_sum_to_equal"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 51, 'tail_weight_holdout', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_chisquare_test_p_value_to_be_greater_than","column_kl_divergence_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 52, 'threshold', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_kl_divergence_to_be_less_than","column_pair_cramers_phi_value_to_be_less_than"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 53, 'ties_okay', 'INTEGER', 0, 10, None, 'checkbox', None, None, 'DESIGN', '["column_most_common_value_to_be_in_set"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 54, 'type_', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_be_of_type"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 55, 'type_list', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_values_to_be_in_type_list"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 56, 'value', 'INTEGER', 0, 10, None, 'integer', None, None, 'DESIGN', '["table_column_count_to_equal","table_row_count_to_equal","column_value_lengths_to_equal"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 57, 'value_pairs_set', 'TEXT', 0, 10, None, 'text', None, None, 'DESIGN', '["column_pair_values_to_be_in_set"].includes(this.validation.internalValue)', 1, BASE_FORM + 1],
      [BASE_FORM_FIELD + 58, 'value_set', 'TEXT', 0, 10, None, 'textarea', None, None, 'DESIGN', '["column_values_to_be_in_set","column_values_to_not_be_in_set","column_distinct_values_to_be_in_set","column_distinct_values_to_equal_set","column_distinct_values_to_contain_set","column_most_common_value_to_be_in_set"].includes(this.validation.internalValue)', 1, BASE_FORM + 1]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field(conn):
    conn.execute(
        'DELETE from operation_form_field WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 58)

def _insert_operation_form_field_translation(conn):
    tb = table('operation_form_field_translation',
                column('id', Integer), 
                column('locale', String), 
                column('label', String), 
                column('help', UnicodeText))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_FORM_FIELD + 1, 'pt', 'Categoria', 'Categoria da validação.'],
      [BASE_FORM_FIELD + 1, 'en', 'Category', 'Validation category'],
      
      [BASE_FORM_FIELD + 2, 'pt', 'Validação', 'Validação a ser realizada.'], 
      [BASE_FORM_FIELD + 3, 'pt', 'Validação', 'Validação a ser realizada.'], 
      [BASE_FORM_FIELD + 4, 'pt', 'Validação', 'Validação a ser realizada.'], 
      [BASE_FORM_FIELD + 5, 'pt', 'Validação', 'Validação a ser realizada.'], 
      [BASE_FORM_FIELD + 6, 'pt', 'Validação', 'Validação a ser realizada.'], 
      [BASE_FORM_FIELD + 7, 'pt', 'Validação', 'Validação a ser realizada.'], 
      [BASE_FORM_FIELD + 8, 'pt', 'Validação', 'Validação a ser realizada.'], 
      [BASE_FORM_FIELD + 9, 'pt', 'Validação', 'Validação a ser realizada.'], 

      [BASE_FORM_FIELD + 2, 'en', 'Validation', 'Validation to be performed.'], 
      [BASE_FORM_FIELD + 3, 'en', 'Validation', 'Validation to be performed.'], 
      [BASE_FORM_FIELD + 4, 'en', 'Validation', 'Validation to be performed.'], 
      [BASE_FORM_FIELD + 5, 'en', 'Validation', 'Validation to be performed.'], 
      [BASE_FORM_FIELD + 6, 'en', 'Validation', 'Validation to be performed.'], 
      [BASE_FORM_FIELD + 7, 'en', 'Validation', 'Validation to be performed.'], 
      [BASE_FORM_FIELD + 8, 'en', 'Validation', 'Validation to be performed.'], 
      [BASE_FORM_FIELD + 9, 'en', 'Validation', 'Validation to be performed.'], 

      [BASE_FORM_FIELD + 10, 'en', 'Allow cross type comparisons', ''],
      [BASE_FORM_FIELD + 11, 'en', 'Allow relative error', ''],
      [BASE_FORM_FIELD + 12, 'en', 'Bins A', ''],
      [BASE_FORM_FIELD + 13, 'en', 'Bins B', ''],
      [BASE_FORM_FIELD + 14, 'en', 'Bootstrap sample size', ''],
      [BASE_FORM_FIELD + 15, 'en', 'Bootstrap samples', ''],
      [BASE_FORM_FIELD + 16, 'en', 'Bucketize data', ''],
      [BASE_FORM_FIELD + 17, 'en', 'Columns', ''],
      [BASE_FORM_FIELD + 18, 'en', 'Column A', ''],
      [BASE_FORM_FIELD + 19, 'en', 'Column B', ''],
      [BASE_FORM_FIELD + 20, 'en', 'Columns indexes (test order)', ''],
      [BASE_FORM_FIELD + 21, 'en', 'Columns list, separated by commas', ''],
      [BASE_FORM_FIELD + 22, 'en', 'Columns set, separated by commas', ''],
#      [BASE FORM_FIELD + 23, 'en', 'Condition parser']
      [BASE_FORM_FIELD + 24, 'en', 'Distribution', ''],
      [BASE_FORM_FIELD + 25, 'en', 'Exact match', ''],
      [BASE_FORM_FIELD + 26, 'en', 'Ignore row if', ''],
      [BASE_FORM_FIELD + 27, 'en', 'Internal weight holdout', ''],
      [BASE_FORM_FIELD + 28, 'en', 'Json schema', ''],
      [BASE_FORM_FIELD + 29, 'en', 'Match on', ''],
      [BASE_FORM_FIELD + 30, 'en', 'Max value', ''],
      [BASE_FORM_FIELD + 31, 'en', 'Min value', ''],
      [BASE_FORM_FIELD + 32, 'en', 'Mostly % of rows evaluate to success (between 0.0 and 1.0)', ''],
      [BASE_FORM_FIELD + 33, 'en', 'N bins A', ''],
      [BASE_FORM_FIELD + 34, 'en', 'N bins B', ''],
      [BASE_FORM_FIELD + 35, 'en', 'Or equal', ''],
      [BASE_FORM_FIELD + 36, 'en', 'Output strftime format', ''],
      [BASE_FORM_FIELD + 37, 'en', 'P', ''],
      [BASE_FORM_FIELD + 38, 'en', 'P value', ''],
      [BASE_FORM_FIELD + 39, 'en', 'Params', ''],
      [BASE_FORM_FIELD + 40, 'en', 'Parse strings as datetimes', ''],
      [BASE_FORM_FIELD + 41, 'en', 'Partition object', ''],
      [BASE_FORM_FIELD + 42, 'en', 'Quantile ranges', ''],
      [BASE_FORM_FIELD + 43, 'en', 'Regex', ''],
      [BASE_FORM_FIELD + 44, 'en', 'Regex list (one per line)', ''],
      # [BASE_FORM_FIELD + 45, 'en', 'Row condition', ''],
      [BASE_FORM_FIELD + 46, 'en', 'Strftime format', ''],
      [BASE_FORM_FIELD + 47, 'en', 'Strict max', ''],
      [BASE_FORM_FIELD + 48, 'en', 'Strict min', ''],
      [BASE_FORM_FIELD + 49, 'en', 'Strictly', ''],
      [BASE_FORM_FIELD + 50, 'en', 'Sum total', ''],
      [BASE_FORM_FIELD + 51, 'en', 'Tail weight holdout', ''],
      [BASE_FORM_FIELD + 52, 'en', 'Threshold', ''],
      [BASE_FORM_FIELD + 53, 'en', 'Ties okay', ''],
      [BASE_FORM_FIELD + 54, 'en', 'Type ', ''],
      [BASE_FORM_FIELD + 55, 'en', 'Type list', ''],
      [BASE_FORM_FIELD + 56, 'en', 'Value', ''],
      [BASE_FORM_FIELD + 57, 'en', 'Value pairs set', ''],
      [BASE_FORM_FIELD + 58, 'en', 'Value set (one item per line)','en',  ''],

       [BASE_FORM_FIELD + 10, 'pt', 'Permitir comparações entre tipos diferentes', ''],
      [BASE_FORM_FIELD + 11, 'pt', 'Permitir erro relativo', ''],
      [BASE_FORM_FIELD + 12, 'pt', 'Bins A', ''],
      [BASE_FORM_FIELD + 13, 'pt', 'Bins B', ''],
      [BASE_FORM_FIELD + 14, 'pt', 'Tamanho da amostra (bootstrap)', ''],
      [BASE_FORM_FIELD + 15, 'pt', 'Amostras (bootstrap)', ''],
      [BASE_FORM_FIELD + 16, 'pt', 'Dividir dados em buckets', ''],
      [BASE_FORM_FIELD + 17, 'pt', 'Colunas', ''],
      [BASE_FORM_FIELD + 18, 'pt', 'Coluna A', ''],
      [BASE_FORM_FIELD + 19, 'pt', 'Coluna B', ''],
      [BASE_FORM_FIELD + 20, 'pt', 'Indices das colunas (testa ordem)', ''],
      [BASE_FORM_FIELD + 21, 'pt', 'Lista de colunas, separadas por vírgula', ''],
      [BASE_FORM_FIELD + 22, 'pt', 'Conjunto de colunas, separadas por vírgula', ''],
#      [BASE FORM_FIELD + 23, 'pt', 'Condition parser']
      [BASE_FORM_FIELD + 24, 'pt', 'Distribuição', ''],
      [BASE_FORM_FIELD + 25, 'pt', 'Casamento exato', ''],
      [BASE_FORM_FIELD + 26, 'pt', 'Ignorar registro se', ''],
      [BASE_FORM_FIELD + 27, 'pt', 'Internal weight holdout', ''],
      [BASE_FORM_FIELD + 28, 'pt', 'Json schema', ''],
      [BASE_FORM_FIELD + 29, 'pt', 'Case com (match on)', ''],
      [BASE_FORM_FIELD + 30, 'pt', 'Valor máximo', ''],
      [BASE_FORM_FIELD + 31, 'pt', 'Valor mínimo', ''],
      [BASE_FORM_FIELD + 32, 'pt', 'Sucesso se majoritariamente válido (% entre 0.0 e 1.0)', ''],
      [BASE_FORM_FIELD + 33, 'pt', 'N bins A', ''],
      [BASE_FORM_FIELD + 34, 'pt', 'N bins B', ''],
      [BASE_FORM_FIELD + 35, 'pt', 'Ou igual', ''],
      [BASE_FORM_FIELD + 36, 'pt', 'Usar formato strftime (Python) para converter datas', ''],
      [BASE_FORM_FIELD + 37, 'pt', 'P', ''],
      [BASE_FORM_FIELD + 38, 'pt', 'P-value', ''],
      [BASE_FORM_FIELD + 39, 'pt', 'Parâmetros', ''],
      [BASE_FORM_FIELD + 40, 'pt', 'Converter texto para datas', ''],
      [BASE_FORM_FIELD + 41, 'pt', 'Objeto particionador', ''],
      [BASE_FORM_FIELD + 42, 'pt', 'Faixas para quantis', ''],
      [BASE_FORM_FIELD + 43, 'pt', 'Expressão regular', ''],
      [BASE_FORM_FIELD + 44, 'pt', 'Lista de expressões regulares (uma por linha)', ''],
      # [BASE_FORM_FIELD + 45, 'pt', 'Condição para o registro', ''],
      [BASE_FORM_FIELD + 46, 'pt', 'Formato strftime (Python)', ''],
      [BASE_FORM_FIELD + 47, 'pt', 'Máximo estrito', ''],
      [BASE_FORM_FIELD + 48, 'pt', 'Mínimo estrito', ''],
      [BASE_FORM_FIELD + 49, 'pt', 'Estritamente', ''],
      [BASE_FORM_FIELD + 50, 'pt', 'Soma total', ''],
      [BASE_FORM_FIELD + 51, 'pt', 'Tail weight holdout', ''],
      [BASE_FORM_FIELD + 52, 'pt', 'Limiar', ''],
      [BASE_FORM_FIELD + 53, 'pt', 'Empates são OK', ''],
      [BASE_FORM_FIELD + 54, 'pt', 'Tipo', ''],
      [BASE_FORM_FIELD + 55, 'pt', 'Lista de tipos', ''],
      [BASE_FORM_FIELD + 56, 'pt', 'Valor', ''],
      [BASE_FORM_FIELD + 57, 'pt', 'Conjunto de pares de valores', ''],
      [BASE_FORM_FIELD + 58, 'pt', 'Conjunto de valores (um item por linha)', ''],
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_form_field_translation(conn):
    conn.execute(
        'DELETE from operation_form_field_translation WHERE id BETWEEN %s AND %s', 
        BASE_FORM_FIELD + 1, BASE_FORM_FIELD + 58)

def _insert_operation_port(conn):
    tb = table('operation_port',
                column('id', Integer), 
                column('slug', String), 
                column('type', String), 
                column('tags', String), 
                column('order', Integer), 
                column('multiplicity', String), 
                column('operation_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_PORT + 1, 'input data', 'INPUT', '', 1, 'ONE', BASE_OP + 1], 
      [BASE_PORT + 2, 'output results', 'OUTPUT', '', 1, 'MANY', BASE_OP + 1], 
      [BASE_PORT + 3, 'input results', 'INPUT', '', 1, 'MANY', BASE_OP + 2]
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port(conn):
    conn.execute(
        'DELETE from operation_port WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 3)

def _insert_operation_port_translation(conn):
    tb = table('operation_port_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String), 
                column('description', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_PORT + 1, 'pt', 'dados de entrada', 'Dados de entrada'], 
      [BASE_PORT + 2, 'pt', 'resultado validação', 'Resultado validação'], 
      [BASE_PORT + 3, 'pt', 'resultado validação', 'Resultado validação'],
      [BASE_PORT + 1, 'en', 'input data', 'input data'], 
      [BASE_PORT + 2, 'en', 'validation result', 'validation result'], 
      [BASE_PORT + 3, 'en', 'validation result', 'validation result']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_translation(conn):
    conn.execute(
        'DELETE from operation_port_translation WHERE id BETWEEN %s AND %s', 
        BASE_PORT + 1, BASE_PORT + 3)

def _insert_operation_port_interface(conn):
    tb = table('operation_port_interface',
                column('id', Integer), 
                column('color', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_INTERFACE + 1, '#ed8']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface(conn):
    conn.execute(
        'DELETE from operation_port_interface WHERE id BETWEEN %s AND %s', 
        BASE_INTERFACE + 1, BASE_INTERFACE + 1)

def _insert_operation_port_interface_translation(conn):
    tb = table('operation_port_interface_translation',
                column('id', Integer), 
                column('locale', String), 
                column('name', String))
    columns = [c.name for c in tb.columns]
    data = [
      [BASE_INTERFACE + 1, 'pt', 'ValidationResult'],
      [BASE_INTERFACE + 1, 'en', 'ValidationResult']
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_translation(conn):
    conn.execute(
        'DELETE from operation_port_interface_translation WHERE id BETWEEN %s AND %s', 
        BASE_INTERFACE + 1, BASE_INTERFACE + 1)

def _insert_operation_category_operation(conn):
    tb = table('operation_category_operation',
                column('operation_id', Integer), 
                column('operation_category_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, BASE_CATEGORY + 1], 
            [BASE_OP + 2, BASE_CATEGORY + 1], 
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_category_operation(conn):
    conn.execute(
            '''DELETE FROM operation_category_operation 
            WHERE operation_id BETWEEN %s AND %s''',
            BASE_OP + 1, BASE_OP + 2)

def _insert_operation_operation_form(conn):
    tb = table('operation_operation_form',
                column('operation_id', Integer), 
                column('operation_form_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
            [BASE_OP + 1, BASE_FORM + 1], 
            [BASE_OP + 2, BASE_FORM + 2], 
            [BASE_OP + 1, 110], 
            [BASE_OP + 2, 110], 
            [BASE_OP + 1, 41], 
            [BASE_OP + 2, 41], 
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_operation_form(conn):
    conn.execute(
            '''DELETE FROM operation_operation_form
            WHERE operation_id BETWEEN %s AND %s''',
            BASE_OP + 1, BASE_OP + 2)

def _insert_operation_port_interface_operation_port (conn):
    tb = table('operation_port_interface_operation_port',
                column('operation_port_interface_id', Integer), 
                column('operation_port_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [1, BASE_PORT + 1],
        [BASE_INTERFACE + 1, BASE_PORT + 2],
        [BASE_INTERFACE + 1, BASE_PORT + 3],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_port_interface_operation_port (conn):
    conn.execute(
            '''DELETE FROM operation_port_interface_operation_port
            WHERE operation_port_id BETWEEN %s AND %s''',
            BASE_PORT + 1, BASE_PORT + 3)

def _insert_operation_platform(conn):
    tb = table('operation_platform',
                column('operation_id', Integer), 
                column('platform_id', Integer))
    columns = [c.name for c in tb.columns]
    data = [
        [BASE_OP + 1, 1],
        [BASE_OP + 2, 1],
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _delete_operation_platform(conn):
    conn.execute('''
        DELETE FROM operation_platform WHERE 
        operation_id BETWEEN %s AND %s''',
        BASE_OP + 1, BASE_OP + 2)

def _execute(conn, cmd):
    if isinstance(cmd, str):
        conn.execute(cmd)
    elif isinstance(cmd, list):
        for row in cmd:
            conn.execute(row)
    else: # it's a method
        cmd(conn)

# -------------------------------------------------------

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()
    commands = [
        _insert_operation,
        _insert_operation_translation,
        _insert_operation_category,
        _insert_operation_category_translation,
        _insert_operation_form,
        _insert_operation_form_translation,
        _insert_operation_form_field,
        _insert_operation_form_field_translation,
        _insert_operation_port,
        _insert_operation_port_translation,
        _insert_operation_port_interface,
        _insert_operation_port_interface_translation,
        _insert_operation_category_operation,
        _insert_operation_operation_form,
        _insert_operation_port_interface_operation_port,
        _insert_operation_platform,
    ]
    try:
        for cmd in commands:
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)() 
    conn = session.connection()

    # Remove it if your DB doesn't support disabling FK checks
    conn.execute('SET FOREIGN_KEY_CHECKS=0;')
    commands = [
        _delete_operation,
        _delete_operation_translation,
        _delete_operation_category,
        _delete_operation_category_translation,
        _delete_operation_form,
        _delete_operation_form_translation,
        _delete_operation_form_field,
        _delete_operation_form_field_translation,
        _delete_operation_port,
        _delete_operation_port_translation,
        _delete_operation_port_interface,
        _delete_operation_port_interface_translation,
        _delete_operation_category_operation,
        _delete_operation_operation_form,
        _delete_operation_port_interface_operation_port,
        _delete_operation_platform,
    ]

    try:
        for cmd in reversed(commands):
            _execute(conn, cmd)
    except:
        session.rollback()
        raise
    # Remove it if your DB doesn't support disabling FK checks
    conn.execute('SET FOREIGN_KEY_CHECKS=1;')
    session.commit()
