# -*- coding: utf-8 -*-

"""Update Scikit learn

Revision ID: 5b7ffd45dbea
Revises: 736a6469026d
Create Date: 2019-08-26 16:06:25.427703

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '5b7ffd45dbea'
down_revision = '736a6469026d'
branch_labels = None
depends_on = None


all_commands = [
    ("""
    UPDATE operation_form_field_translation SET label='Atributo com a predição (novo)' WHERE id=4107 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Atributo usado para predição (novo)' WHERE id=4107 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Pesos (separados por vírgula, usados em ensembles)' WHERE id=4062 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Peso das classes' WHERE id=4062 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Semente (para geração de números aleatórios)' WHERE id=4026 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Semente' WHERE id=4026 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Atributo com a predição (novo)' WHERE id=4110 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Atributo usado para predição (novo)' WHERE id=4110 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Mix. para ElasticNet' WHERE id=4034 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='L1 ratio' WHERE id=4034 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Camadas (informe os tamanhos separados por vírgula)' WHERE id=4091 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Tamanho das camadas' WHERE id=4091 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Solucionador' WHERE id=4093 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Solver' WHERE id=4093 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Atributo com a predição (novo)' WHERE id=4112 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Atributo usado para predição (novo)' WHERE id=4112 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Quantidade de agrupamentos (K)' WHERE id=4064 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Número de clusters' WHERE id=4064 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Tipo' WHERE id=4065 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Algoritmo' WHERE id=4065 AND locale='pt'"""),
    ("""
    UPDATE operation_form_field_translation SET label='Geração dos centroids iniciais' WHERE id=4066 AND locale='pt';
    """,
     """UPDATE operation_form_field_translation SET label='Método para inicialização' WHERE id=4066 AND locale='pt'""")
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