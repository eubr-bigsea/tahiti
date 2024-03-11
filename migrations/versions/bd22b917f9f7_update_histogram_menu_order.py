"""Update Histogram menu order

Revision ID: bd22b917f9f7
Revises: c4b87364ce33
Create Date: 2021-10-09 00:07:26.892344

"""
from alembic import op
from sqlalchemy.sql import text
import sqlalchemy as sa
import json
from tahiti.migration_utils import (downgrade_actions, upgrade_actions,
        is_mysql, is_psql, is_sqlite, get_psql_enum_alter_commands, xkpe)

# revision identifiers, used by Alembic.
revision = 'bd22b917f9f7'
down_revision = 'c4b87364ce33'
branch_labels = None
depends_on = None


def upgrade():
    if is_mysql():
        op.execute(text("UPDATE operation_form SET `order` = '1' WHERE (id = '142');"))
    else:
        op.execute(text('UPDATE operation_form SET "order" = 1 WHERE (id = 142);'))

    function_list = {
        "functions": [
            {
                "key": "avg", "value": "Average (AVG)",
                "label": {"pt": "Média (AVG)", "en": "Average (AVG)"},
                "help": {
                    "en": "Computes the average of each group",
                    "pt": "Computa a média de cada grupo"
                }
            },
            {
                "key": "collect_list", "value": "Collect List",
                "label": {"pt": "Agrupa valores em lista", "en": "Collect list"},
                "help": {
                    "en": "Returns a list of values with possible duplicates",
                    "pt": "Retorna a lista de valores, podendo haver repetição."
                }
            },
            {
                "key": "collect_set", "value": "Collect Set",
                "label": {"pt": "Agrupa valores em conjunto", "en": "Collect set"},
                "help": {
                    "en": "Returns a set of values with duplicate elements eliminated",
                    "pt": "Retorna um conjunto de valores sem repetição"
                }
            },
            {
                "key": "count", "value": "Count",
                "label": {"pt": "Conta valores (Count)", "en": "Count"},
                "help": {
                    "en": "Counts the total of records of each group",
                    "pt": "Conta o total de registros em cada grupo"
                }
            },
            {
                "key": "countDistinct", "value": "Count Distinct",
                "label": {"pt": "Conta valores distintos", "en": "Count distinct"},
                "help": {
                    "en": "Counts the total of distinct values of each group",
                    "pt": "Conta o total de valores distintos em cada grupo"
                }
            },
            {
                "key": "approx_count_distinct", "value": "Approximated Count Distinct",
                "label": {"pt": "Conta o total aproximado de valores distintos", "en": "Approx. Count distinct"},
                "help": {
                    "en": "Counts the total of distinct values of each group, but using an approximation",
                    "pt": "Conta o total aproximado de valores distintos em cada grupo"
                }
            },
            {
                "key": "first", "value": "First",
                "help": {
                    "en": "Returns the first value of group.",
                    "pt": "Retorna o primeiro valor do grupo"
                }
            },
            {
                "key": "last", "value": "Last",
                "help": {
                    "en": "Returns the last value of group.",
                    "pt": "Retorna o último valor do grupo."
                }
            },
            {
                "key": "max", "value": "Maximum (MAX)",
                "help": {
                    "en": "Returns the max value of each group for one attribute",
                    "pt": "Retorna o valor máximo de cada grupo"
                }
            },
            {
                "key": "min", "value": "Minimum (MIN)",
                "help": {
                    "en": "Returns the min value of each group for one attribute",
                    "pt": "Retorna o valor mínimo de cada grupo"
                }
            },
            {
                "key": "sum", "value": "Sum",
                "help": {
                    "en": "Returns the sum of values of each group for one attribute",
                    "pt": "Retorna a soma dos valores de cada grupo"
                }
            },
            {
                "key": "sumDistinct", "value": "Sum Distinct",
                "help": {
                    "en": "Returns the sum of distinct values of each group for one attribute",
                    "pt": "Retorna a soma dos valores distintos de cada grupo"
                }
            },
            {
                "key": "stddev", "value": "Standard deviation",
                "help": {
                    "en": "Returns the standard deviation of each group for one attribute",
                    "pt": "Retorna o desvio-padrão de cada grupo"
                }
            },
            {
                "key": "stddev_pop", "value": "Standard deviation (pop)",
                "help": {
                    "en": "Returns the population standard deviation of each group for one attribute",
                    "pt": "Retorna o desvio-padrão populacional de cada grupo"
                }
            },
            {
                "key": "variance", "value": "Variance",
                "help": {
                    "en": "Returns the variance of each group for one attribute",
                    "pt": "Retorna a variância de cada grupo"
                }
            },
            {
                "key": "var_pop", "value": "Variance (pop)",
                "help": {
                    "en": "Returns the populational variance of each group for one attribute",
                    "pt": "Retorna a variância populacional de cada grupo"
                }
            },
            {
                "key": "skewness", "value": "Skewness",
                "help": {
                    "en": "Returns the skewness each group for one attribute",
                    "pt": "Retorna a distorção (skewness) cada grupo"
                }
            },
            {
                "key": "kurtosis", "value": "Kurtosis",
                "help": {
                    "en": "Returns the kurtosis of each group for one attribute",
                    "pt": "Retorna a curtose (kurtosis) de cada grupo"
                }
            },

          ],
        "options": {
            "title": "Aggregate operation",
            "description": "Add one of more lines with attribute to be used, function and alias to compute aggregate function over groups.",
            "show_alias": True,
            "pt": { "title": "Função de agrupamento", "description": "Realiza o agrupamento de dados por um conjunto de atributos." }
        }
    }
    if is_psql():
        op.execute(text("UPDATE operation_form_field SET required = true, \"values\" = '{}' WHERE (id = 71);".format(json.dumps(function_list, ensure_ascii=False))))
    else:
        op.execute(text("UPDATE operation_form_field SET required = true, `values` = '{}' WHERE (id = 71);".format(json.dumps(function_list, ensure_ascii=False))))
    
    op.execute(text("UPDATE operation_form_field SET required = false WHERE id=70;"))
    op.execute(text("""
             UPDATE operation_form_field_translation SET 
               label = 'Selecione o(s) atributos para agrupar', 
                help = 'Escolha um ou mais atributos para agrupar.' WHERE locale='pt' and (id = 70);"""))
    op.execute(text("""
             UPDATE operation_form_field_translation SET 
               label = 'Função de agrupamento', 
                help = 'Função a ser aplicada aos dados agrupados.' WHERE locale='pt' and (id = 71);"""))
    op.execute(text("""
        INSERT INTO operation_script(id, type, enabled, body, operation_id) 
        VALUES (77, 'JS_CLIENT', true, 'copyInputAddAttributesSplitAlias(task, "attributes", "aliases", "_bucketed")', 100)
        """))
    op.execute(text("""
             UPDATE operation_form_field_translation SET 
               label = 'Atributo com a predição', 
                help = 'Atributo com a predição' WHERE id = 99 """))

def downgrade():
    if is_mysql():
        op.execute(text("UPDATE operation_form SET `order` = '10' WHERE (id = '142');"))
    else:
        op.execute(text('UPDATE "operation_form" SET "order" = 10 WHERE ("id" = 142);'))
    function_list = {"functions": [{"key": "avg", "value": "Average (AVG)", "help": "Computes the average of each group"}, {"key": "collect_list", "value": "Collect List", "help": "Aggregate function: returns a list of objects with duplicates."}, {"key": "collect_set", "value": "Collect Set", "help": "Aggregate function: returns a set of objects with duplicate elements eliminated."}, {"key": "count", "value": "Count", "help": "Counts the total of records of each group"}, {"key": "first", "value": "First", "help": "Returns the first element of group"}, {"key": "last", "value": "Last", "help": "Returns the last element of group"}, {"key": "max", "value": "Maximum (MAX)", "help": "Returns the max value of each group for one attribute"}, {"key": "min", "value": "Minimum (MIN)", "help": "Returns the min value of each group for one attribute"}, {"key": "sum", "value": "Sum", "help": "Returns the sum of values of each group for one attribute"}], "options": {"title": "Aggregate operation", "description": "Add one of more lines with attribute to be used, function and alias to compute aggregate function over groups.", "show_alias": True}}
    functions = json.dumps(function_list, ensure_ascii=False)
    op.execute(text(f"UPDATE operation_form_field SET required=true, {xkpe('values')} = '{functions}' WHERE (id = 71);"))

    op.execute(text("UPDATE operation_form_field SET required =true WHERE id=70;"))
    op.execute(text("""
             UPDATE operation_form_field_translation SET 
               label = 'Selecione o(s) atributos para a agregação', 
                help = 'Escolha um ou mais atributos para a agregação.' WHERE locale='pt' and (id = 70);"""))
    op.execute(text("""
             UPDATE operation_form_field_translation SET 
               label = 'Função de agregação', 
                help = 'Função a ser aplicada aos dados agregados.' WHERE locale='pt' and (id = 71);"""))

    op.execute(text("DELETE FROM operation_script WHERE operation_id = 100"))
