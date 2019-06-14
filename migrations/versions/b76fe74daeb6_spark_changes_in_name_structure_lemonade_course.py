# -*- coding: utf-8 -*-
"""Spark: changes in name structure: lemonade course

Revision ID: b76fe74daeb6
Revises: cbab033d8049
Create Date: 2018-12-17 12:54:50.130377

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = 'b76fe74daeb6'
down_revision = 'cbab033d8049'
branch_labels = None
depends_on = None

SPARK_PLATAFORM_ID = 1


all_commands = [
    ('UPDATE operation_category_translation '
     'SET name = "Input and output" '
     'WHERE id = 6 AND locale = "en"',
     'UPDATE operation_category_translation '
     'SET name = "Data source and target" '
     'WHERE id = 6 AND locale = "en"'),
    ('UPDATE operation_category_translation '
     'SET name = "Entrada e saída" '
     'WHERE id = 6 AND locale = "pt"',
     'UPDATE operation_category_translation '
     'SET name = "Fonte de dados de entrada e saída" '
     'WHERE id = 6 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Read data" '
     'WHERE id = 18 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Data reader" '
     'WHERE id = 18 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Ler dados" '
     'WHERE id = 18 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Leitor de dados" '
     'WHERE id = 18 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Save data" '
     'WHERE id = 30 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Data writer" '
     'WHERE id = 30 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Salvar dados" '
     'WHERE id = 30 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Escritor de dados" '
     'WHERE id = 30 AND locale = "pt"'),

    ('DELETE FROM operation_category_operation '
     'WHERE operation_id = 22 AND operation_category_id = 26',
     'INSERT INTO operation_category_operation '
     '(`operation_id`, `operation_category_id`) VALUES (22, 26)'),
    ('UPDATE operation_category_operation '
     'SET operation_category_id = 6 '
     'WHERE operation_id = 22 AND operation_category_id = 8',
     'UPDATE operation_category_operation '
     'SET operation_category_id = 8 '
     'WHERE operation_id = 22 AND operation_category_id = 6'),

    ('DELETE FROM operation_category_operation '
     'WHERE operation_id = 39 AND operation_category_id = 26',
     'INSERT INTO operation_category_operation '
     '(`operation_id`, `operation_category_id`) VALUES (39, 26)'),
    ('UPDATE operation_category_operation '
     'SET operation_category_id = 6 '
     'WHERE operation_id = 39 AND operation_category_id = 8',
     'UPDATE operation_category_operation '
     'SET operation_category_id = 8 '
     'WHERE operation_id = 39 AND operation_category_id = 6'),

    ('DELETE FROM operation_category_operation '
     'WHERE operation_id = 25 AND operation_category_id = 13',
     'INSERT INTO operation_category_operation '
     '(`operation_id`, `operation_category_id`) VALUES (25, 13)'),
    ('UPDATE operation_category_operation '
     'SET operation_category_id = 6 '
     'WHERE operation_id = 25 AND operation_category_id = 14',
     'UPDATE operation_category_operation '
     'SET operation_category_id = 14 '
     'WHERE operation_id = 25 AND operation_category_id = 6'),

    ('UPDATE operation_category_translation '
     'SET name = "Data manipulation" '
     'WHERE id = 7 AND locale = "en"',
     'UPDATE operation_category_translation '
     'SET name = "Data transformation" '
     'WHERE id = 7 AND locale = "en"'),
    ('UPDATE operation_category_translation '
     'SET name = "Manipulação de dados" '
     'WHERE id = 7 AND locale = "pt"',
     'UPDATE operation_category_translation '
     'SET name = "Transformação de dados" '
     'WHERE id = 7 AND locale = "pt"'),

    ('INSERT INTO operation_category '
     '(`id`, `type`, `order`, `default_order`) VALUES '
     '(29, "subgroup", 0, 0), '
     '(30, "subgroup", 0, 0), '
     '(31, "subgroup", 0, 0)',
     'DELETE FROM operation_category '
     'WHERE id IN (29, 30, 31)'),

    ('INSERT INTO operation_category_translation '
     '(`id`, `locale`, `name`) VALUES '
     '(29, "en", "By row (Example/Instance)"), '
     '(29, "pt", "Por linha (Exemplo/Instância)"), '
     '(30, "en", "By column (Attribute/Variable)"), '
     '(30, "pt", "Por coluna (Atributo/Variável)"), '
     '(31, "en", "General"), '
     '(31, "pt", "Geral")',
     'DELETE FROM operation_category_translation '
     'WHERE id IN (29, 30, 31)'),

    ('INSERT INTO operation_category_operation '
     '(`operation_id`, `operation_category_id`) VALUES '
     '(12, 29), '
     '(15, 29), '
     '(23, 29), '
     '(24, 30), '
     '(27, 30), '
     '(37, 30), '
     '(32, 30), '
     '(7, 30), '
     '(99, 30), '
     '(21, 31), '
     '(16, 31), '
     '(13, 31), '
     '(5, 31), '
     '(6, 31)',
     'DELETE FROM operation_category_operation '
     'WHERE operation_id IN (12, 15, 23, 24, 27, 37, 32, 7, 99, 21, 16, 13, 5, 6) AND '
     'operation_category_id IN (29, 30, 31)'),

    ('UPDATE operation_translation '
     'SET name = "Add new row(s)" '
     'WHERE id = 12 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Add rows" '
     'WHERE id = 12 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Adicionar nova(s) linha(s)" '
     'WHERE id = 12 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Adicionar linhas" '
     'WHERE id = 12 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Group by function" '
     'WHERE id = 15 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Aggregation" '
     'WHERE id = 15 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Agrupar linhas por função" '
     'WHERE id = 15 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Agregação" '
     'WHERE id = 15 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Remove duplicated rows" '
     'WHERE id = 23 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Remove duplicated rows" '
     'WHERE id = 23 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Remover linhas duplicadas" '
     'WHERE id = 23 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Remover linhas duplicadas" '
     'WHERE id = 23 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Add new column(s)" '
     'WHERE id = 24 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Add Columns" '
     'WHERE id = 24 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Adicionar nova(s) coluna(s)" '
     'WHERE id = 24 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Adicionar colunas" '
     'WHERE id = 24 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Replace value" '
     'WHERE id = 27 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Replace value" '
     'WHERE id = 27 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Substituir valor" '
     'WHERE id = 27 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Substituir valor" '
     'WHERE id = 27 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Difference between columns" '
     'WHERE id = 37 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Difference" '
     'WHERE id = 37 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Diferença entre colunas" '
     'WHERE id = 37 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Diferença" '
     'WHERE id = 37 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Sort" '
     'WHERE id = 32 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Sort" '
     'WHERE id = 32 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Ordenar" '
     'WHERE id = 32 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Ordenar" '
     'WHERE id = 32 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Transform by function" '
     'WHERE id = 7 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Transformation" '
     'WHERE id = 7 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Transformar valores por função" '
     'WHERE id = 7 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Transformar" '
     'WHERE id = 7 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Transform by sliding window" '
     'WHERE id = 99 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Window transformation" '
     'WHERE id = 99 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Transformar em janela (deslizante)" '
     'WHERE id = 99 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Transformação em janela" '
     'WHERE id = 99 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Handle missing values" '
     'WHERE id = 21 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Clean missing" '
     'WHERE id = 21 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Tratar dados ausentes" '
     'WHERE id = 21 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Limpar dados ausentes" '
     'WHERE id = 21 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Join" '
     'WHERE id = 16 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Join" '
     'WHERE id = 16 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Junção" '
     'WHERE id = 16 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Junção (join)" '
     'WHERE id = 16 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Set intersection" '
     'WHERE id = 13 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Set intersection" '
     'WHERE id = 13 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Intersecção" '
     'WHERE id = 13 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Interseção" '
     'WHERE id = 13 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Filter by function" '
     'WHERE id = 5 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Filter (selection)" '
     'WHERE id = 5 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Filtrar por função" '
     'WHERE id = 5 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Filtrar (seleção)" '
     'WHERE id = 5 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Select attribute(s)" '
     'WHERE id = 6 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Projection/Select columns" '
     'WHERE id = 6 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Selecionar atributo(s)" '
     'WHERE id = 6 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Projeção/Selecionar atributos" '
     'WHERE id = 6 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Execute SQL query" '
     'WHERE id = 93 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Execute SQL query" '
     'WHERE id = 93 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Executar consulta SQL" '
     'WHERE id = 93 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Executar consulta SQL" '
     'WHERE id = 93 AND locale = "pt"'),

    ('INSERT INTO operation_category '
     '(`id`, `type`, `order`, `default_order`) VALUES '
     '(32, "group", 0, 0), '
     '(33, "subgroup", 0, 0), '
     '(34, "subgroup", 0, 0), '
     '(35, "subgroup", 0, 0), '
     '(36, "subgroup", 0, 0), '
     '(37, "subgroup", 0, 0), '
     '(38, "subgroup", 0, 0), '
     '(39, "subgroup", 0, 0), '
     '(40, "group", 0, 0), '
     '(41, "group", 0, 0), '
     '(42, "subgroup", 0, 0)',
     'DELETE FROM operation_category '
     'WHERE id BETWEEN 32 and 42'),

    ('INSERT INTO operation_category_translation '
     '(`id`, `locale`, `name`) VALUES '
     '(32, "en", "Data preprocessing"), '
     '(32, "pt", "Pré-processamento dos dados"), '
     '(33, "en", "Attribute representation"), '
     '(33, "pt", "Representação de atributos"), '
     '(34, "en", "Rescaling"), '
     '(34, "pt", "Redefinir escala"), '
     '(35, "en", "Discretization"), '
     '(35, "pt", "Discretização"), '
     '(36, "en", "Dimensionality reduction"), '
     '(36, "pt", "Redução de dimensionalidade"), '
     '(37, "en", "Text operations"), '
     '(37, "pt", "Operações textuais"), '
     '(38, "en", "Sampling"), '
     '(38, "pt", "Amostragem"), '
     '(39, "en", "Anomaly detection"), '
     '(39, "pt", "Detecção de anomalias"), '
     '(40, "en", "Model and Evaluation"), '
     '(40, "pt", "Modelo e Avaliação"), '
     '(41, "en", "Advanced"), '
     '(41, "pt", "Avançado"), '
     '(42, "en", "Geographical"), '
     '(42, "pt", "Geográfico")',
     'DELETE FROM operation_category_translation '
     'WHERE id BETWEEN 32 and 42'),

    ('DELETE FROM operation_category_operation '
     'WHERE operation_id IN '
     '(40, 41, 75, 90, 91, 92, 100, 101, 95, 96, 49, 50, 51, 52, 17, 28, 102, 19, 42, 43, 53, 55, 82, 93, 48, 2) '
     'AND operation_category_id IN (8, 23, 16, 7, 27, 26, 3, 17, 13, 19)',
     'INSERT INTO operation_category_operation '
     '(`operation_id`, `operation_category_id`) VALUES '
     '(40, 23), '
     '(40, 8), '
     '(41, 23), '
     '(41, 8), '
     '(75, 23), '
     '(75, 8), '
     '(90, 23), '
     '(90, 8), '
     '(91, 23), '
     '(91, 8), '
     '(92, 23), '
     '(92, 8), '
     '(100, 23), '
     '(100, 8), '
     '(101, 23), '
     '(101, 8), '
     '(95, 23), '
     '(95, 8), '
     '(96, 23), '
     '(96, 8), '
     '(49, 16), '
     '(49, 8), '
     '(50, 16), '
     '(50, 8), '
     '(51, 16), '
     '(51, 8), '
     '(52, 16), '
     '(52, 8), '
     '(17, 7), '
     '(28, 7), '
     '(102, 27), '
     '(102, 8), '
     '(19, 26), '
     '(19, 8), '
     '(42, 26), '
     '(42, 8), '
     '(43, 26), '
     '(43, 8), '
     '(53, 17), '
     '(53, 3), '
     '(55, 17), '
     '(82, 13), '
     '(93, 7), '
     '(48, 19), '
     '(48, 8), '
     '(2, 19), '
     '(2, 8)'),

    ('INSERT INTO operation_category_operation '
     '(`operation_id`, `operation_category_id`) VALUES '
     '(40, 32), '
     '(40, 33), '
     '(41, 32), '
     '(41, 33), '
     '(75, 32), '
     '(75, 33), '
     '(90, 32), '
     '(90, 34), '
     '(91, 32), '
     '(91, 34), '
     '(92, 32), '
     '(92, 34), '
     '(100, 32), '
     '(100, 35), '
     '(101, 32), '
     '(101, 35), '
     '(95, 32), '
     '(95, 36), '
     '(96, 32), '
     '(96, 36), '
     '(49, 32), '
     '(49, 37), '
     '(50, 32), '
     '(50, 37), '
     '(51, 32), '
     '(51, 37), '
     '(52, 32), '
     '(52, 37), '
     '(17, 32), '
     '(17, 38), '
     '(28, 32), '
     '(28, 38), '
     '(102, 8), '
     '(102, 39), '
     '(19, 40), '
     '(42, 40), '
     '(43, 40), '
     '(82, 41), '
     '(53, 41), '
     '(53, 42), '
     '(55, 41), '
     '(55, 42), '
     '(93, 41), '
     '(48, 32), '
     '(48, 37), '
     '(2, 32), '
     '(2, 37)',
     'DELETE FROM operation_category_operation '
     'WHERE operation_id IN '
     '(40, 41, 75, 90, 91, 92, 100, 101, 95, 96, 49, 50, 51, 52, 17, 28, 102, 19, 42, 43, 53, 55, 82, 93, 48, 2) AND '
     'operation_category_id IN (32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42)'),

    ('UPDATE operation_translation '
     'SET name = "Percentual splitting" '
     'WHERE id = 17 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Split" '
     'WHERE id = 17 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Divisão percentual" '
     'WHERE id = 17 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Dividir" '
     'WHERE id = 17 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Sample examples" '
     'WHERE id = 28 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Sample" '
     'WHERE id = 28 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Amostrar exemplos" '
     'WHERE id = 28 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Amostra" '
     'WHERE id = 28 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Convert categorical to numeric" '
     'WHERE id = 40 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Feature indexer" '
     'WHERE id = 40 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Converter categórico para numérico" '
     'WHERE id = 40 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Indexador de Feature" '
     'WHERE id = 40 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Vectorize attribute(s)" '
     'WHERE id = 41 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Feature assembler" '
     'WHERE id = 41 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Vetorizar atributo(s)" '
     'WHERE id = 41 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Definidor de feature" '
     'WHERE id = 41 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Tokenizer" '
     'WHERE id = 49 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Tokenizer" '
     'WHERE id = 49 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Dividir texto por delimitador" '
     'WHERE id = 49 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Dividir texto" '
     'WHERE id = 49 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Remove stop words" '
     'WHERE id = 50 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Remove stop words" '
     'WHERE id = 50 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Remover palavras-comuns (stopwords)" '
     'WHERE id = 50 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Remove \'stop words\'" '
     'WHERE id = 50 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Generate N-Grams" '
     'WHERE id = 51 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Generate NGrams" '
     'WHERE id = 51 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gerar N-Gramas" '
     'WHERE id = 51 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Gerar N-Gramas" '
     'WHERE id = 51 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Count term frequency" '
     'WHERE id = 52 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Convert words to vector" '
     'WHERE id = 52 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Contar frequência dos termos" '
     'WHERE id = 52 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Converter palavras em vetor" '
     'WHERE id = 52 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "One-hot encoder" '
     'WHERE id = 75 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "One Hot Encoder" '
     'WHERE id = 75 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Codificação distribuída (One-Hot encoder)" '
     'WHERE id = 75 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "One Hot Encoder" '
     'WHERE id = 75 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Default (Z-score)" '
     'WHERE id = 90 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Standard scaler" '
     'WHERE id = 90 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Padrão (Z-score)" '
     'WHERE id = 90 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Escalador padrão" '
     'WHERE id = 90 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Min-Max" '
     'WHERE id = 91 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Min-max scaler" '
     'WHERE id = 91 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Mínimo-Máximo" '
     'WHERE id = 91 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Escalador min-máx" '
     'WHERE id = 91 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Max-Abs" '
     'WHERE id = 92 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Max-abs scaler" '
     'WHERE id = 92 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Máximo-Absoluto" '
     'WHERE id = 92 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Escalador máx-abs" '
     'WHERE id = 92 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Principal Component Analysis (PCA)" '
     'WHERE id = 95 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Principal component analysis" '
     'WHERE id = 95 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Análise de Componentes Principais (PCA)" '
     'WHERE id = 95 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Análise de componentes principais" '
     'WHERE id = 95 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Locality-sensitive hashing" '
     'WHERE id = 96 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Locality-sensitive hashing" '
     'WHERE id = 96 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Hashing sensível a contexto" '
     'WHERE id = 96 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Locality-sensitive hashing" '
     'WHERE id = 96 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Bucket discretizer" '
     'WHERE id = 100 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Bucketizer" '
     'WHERE id = 100 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Intervalar" '
     'WHERE id = 100 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Divisão em buckets" '
     'WHERE id = 100 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Quantile discretizer" '
     'WHERE id = 101 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Quantile discretizer" '
     'WHERE id = 101 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Por quantis" '
     'WHERE id = 101 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Discretizador em quantis" '
     'WHERE id = 101 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Decision tree" '
     'WHERE id = 46 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Decision tree classifier" '
     'WHERE id = 46 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Árvore de decisão" '
     'WHERE id = 46 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classif. Árv. Decisão" '
     'WHERE id = 46 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Random forest" '
     'WHERE id = 44 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Random forest classifier" '
     'WHERE id = 44 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Random forest" '
     'WHERE id = 44 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador random forest" '
     'WHERE id = 44 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Gradient Boosted Tree" '
     'WHERE id = 45 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "GBT classifier" '
     'WHERE id = 45 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gradient Boosted Tree (GBT)" '
     'WHERE id = 45 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador GBT" '
     'WHERE id = 45 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Support Vector Machines (SVM)" '
     'WHERE id = 9 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Support Vector Machines" '
     'WHERE id = 9 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Support Vector Machines (SVM)" '
     'WHERE id = 9 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador SVM" '
     'WHERE id = 9 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Naïve Bayes" '
     'WHERE id = 4 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Naïve Bayes classifier" '
     'WHERE id = 4 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Naïve Bayes" '
     'WHERE id = 4 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador Naive Bayes" '
     'WHERE id = 4 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Logistic regression" '
     'WHERE id = 31 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Logistic regression" '
     'WHERE id = 31 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão logística" '
     'WHERE id = 31 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressão logística" '
     'WHERE id = 31 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Multi-layer Perceptron" '
     'WHERE id = 47 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Perceptron classifier" '
     'WHERE id = 47 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Perceptron multicamadas" '
     'WHERE id = 47 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador Perceptron" '
     'WHERE id = 47 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Voting classifier" '
     'WHERE id = 84 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Voting classifier" '
     'WHERE id = 84 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Classificação por voto da maioria" '
     'WHERE id = 84 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Classificador por votos" '
     'WHERE id = 84 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Linear regression" '
     'WHERE id = 8 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Linear regression" '
     'WHERE id = 8 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão linear" '
     'WHERE id = 8 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressão linear" '
     'WHERE id = 8 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Isotonic regression" '
     'WHERE id = 74 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Isotonic Regression" '
     'WHERE id = 74 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão isotônica" '
     'WHERE id = 74 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressão Isotônica" '
     'WHERE id = 74 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Gradient boosted tree regressor" '
     'WHERE id = 77 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "GBT Regressor" '
     'WHERE id = 77 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gradient boosted tree regressor" '
     'WHERE id = 77 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressor GBT" '
     'WHERE id = 77 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Random forest regressor" '
     'WHERE id = 78 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Random Forest Regressor" '
     'WHERE id = 78 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Random forest regressor" '
     'WHERE id = 78 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressor Random Forest" '
     'WHERE id = 78 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Generalized linear regression" '
     'WHERE id = 79 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Generalized Linear Regressor" '
     'WHERE id = 79 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regressão linear generalizada" '
     'WHERE id = 79 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regressor Linear Generalizado" '
     'WHERE id = 79 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Process LDA topics" '
     'WHERE id = 2 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Process topics" '
     'WHERE id = 2 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Processar tópicos do LDA" '
     'WHERE id = 2 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Processar tópicos" '
     'WHERE id = 2 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "K-means" '
     'WHERE id = 29 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "K-Means Clustering" '
     'WHERE id = 29 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "K-means" '
     'WHERE id = 29 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Agrupamento K-Means" '
     'WHERE id = 29 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Latent Dirichlet Allocation (LDA)" '
     'WHERE id = 48 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "LDA Clustering" '
     'WHERE id = 48 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Latent Dirichlet Allocation (LDA)" '
     'WHERE id = 48 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Agrupamento LDA" '
     'WHERE id = 48 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Gaussian mixture" '
     'WHERE id = 56 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Gaussian Mix. Clustering" '
     'WHERE id = 56 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Mistura de Gaussianas" '
     'WHERE id = 56 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Agrupamento Gaussian Mix." '
     'WHERE id = 56 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Frequent itemsets mining" '
     'WHERE id = 3 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Frequent itemsets mining" '
     'WHERE id = 3 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Mineração de itemsets frequentes" '
     'WHERE id = 3 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Mineração de itemsets freq." '
     'WHERE id = 3 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Association rules" '
     'WHERE id = 85 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Association rules" '
     'WHERE id = 85 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Regras de associação" '
     'WHERE id = 85 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Regras de associação" '
     'WHERE id = 85 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Sequence mining" '
     'WHERE id = 86 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Sequence mining" '
     'WHERE id = 86 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Mineração de sequências" '
     'WHERE id = 86 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Mineração de sequências" '
     'WHERE id = 86 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Local Outlier Factor (LOF)" '
     'WHERE id = 102 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Outlier detection" '
     'WHERE id = 102 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Local Outlier Factor (LOF)" '
     'WHERE id = 102 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Detecção de anomalias" '
     'WHERE id = 102 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Evaluate with cross validation" '
     'WHERE id = 43 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Cross validation" '
     'WHERE id = 43 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Avaliação com validação cruzada" '
     'WHERE id = 43 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Validação cruzada" '
     'WHERE id = 43 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Summary of statistics" '
     'WHERE id = 81 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Summary statistics" '
     'WHERE id = 81 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Sumário estatístico" '
     'WHERE id = 81 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Sumário estatístico" '
     'WHERE id = 81 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Bar chart" '
     'WHERE id = 69 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Bar chart" '
     'WHERE id = 69 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gráfico de barra(s)" '
     'WHERE id = 69 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Gráfico de barras" '
     'WHERE id = 69 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Scatter plot" '
     'WHERE id = 87 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Scatter plot chart" '
     'WHERE id = 87 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gráfico de dispersão" '
     'WHERE id = 87 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Gráfico de dispersão" '
     'WHERE id = 87 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Line chart" '
     'WHERE id = 68 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Line chart" '
     'WHERE id = 68 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Grafico de linha(s)" '
     'WHERE id = 68 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Gráfico de linha" '
     'WHERE id = 68 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Pie chart" '
     'WHERE id = 70 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Pie chart" '
     'WHERE id = 70 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gráfico de pizza" '
     'WHERE id = 70 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Gráfico de pizza" '
     'WHERE id = 70 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Map visualization" '
     'WHERE id = 88 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Map visualization" '
     'WHERE id = 88 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Mapa" '
     'WHERE id = 88 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Visualização em mapa" '
     'WHERE id = 88 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Donut chart" '
     'WHERE id = 89 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Donut chart" '
     'WHERE id = 89 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Gráfico de rosca" '
     'WHERE id = 89 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Gráfico de rosca (donut)" '
     'WHERE id = 89 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Table" '
     'WHERE id = 35 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Table visualization" '
     'WHERE id = 35 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Tabela" '
     'WHERE id = 35 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Visualização em tabela" '
     'WHERE id = 35 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Find shapefile points" '
     'WHERE id = 55 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Geo Within" '
     'WHERE id = 55 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Localizar ponto" '
     'WHERE id = 55 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Localizar ponto" '
     'WHERE id = 55 AND locale = "pt"'),

    ('UPDATE operation_translation '
     'SET name = "Read shapefile" '
     'WHERE id = 53 AND locale = "en"',
     'UPDATE operation_translation '
     'SET name = "Read shapefile " '
     'WHERE id = 53 AND locale = "en"'),
    ('UPDATE operation_translation '
     'SET name = "Ler arquivo shapefile" '
     'WHERE id = 53 AND locale = "pt"',
     'UPDATE operation_translation '
     'SET name = "Ler shapefile" '
     'WHERE id = 53 AND locale = "pt"'),

    # ('UPDATE operation '
    #  'SET enabled = 0 '
    #  'WHERE id IN (1, 10, 59, 60, 73, 76, 94, 97, 98, 103)',
    #  'UPDATE operation '
    #  'SET enabled = 1 '
    #  'WHERE id IN (1, 10, 59, 60, 73, 76, 94, 97, 98, 103)'),

    ('UPDATE operation_category '
     'SET `default_order` = 7 '
     'WHERE id = 41',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 41'),

    ('UPDATE operation_category '
     'SET `default_order` = 6 '
     'WHERE id = 15',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 15'),

    ('UPDATE operation_category '
     'SET `default_order` = 5 '
     'WHERE id = 40',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 40'),

    ('UPDATE operation_category '
     'SET `default_order` = 4 '
     'WHERE id = 8',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 8'),

    ('UPDATE operation_category '
     'SET `default_order` = 3 '
     'WHERE id = 32',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 32'),

    ('UPDATE operation_category '
     'SET `default_order` = 2 '
     'WHERE id = 7',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 7'),

    ('UPDATE operation_category '
     'SET `default_order` = 1 '
     'WHERE id = 6',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 6'),

    ('UPDATE operation_category '
     'SET `default_order` = 1 '
     'WHERE id = 29',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 29'),

    ('UPDATE operation_category '
     'SET `default_order` = 2 '
     'WHERE id = 30',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 30'),

    ('UPDATE operation_category '
     'SET `default_order` = 3 '
     'WHERE id = 31',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 31'),

    ('UPDATE operation_category '
     'SET `default_order` = 1 '
     'WHERE id = 33',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 33'),

    ('UPDATE operation_category '
     'SET `default_order` = 2 '
     'WHERE id = 34',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 34'),

    ('UPDATE operation_category '
     'SET `default_order` = 3 '
     'WHERE id = 35',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 35'),

    ('UPDATE operation_category '
     'SET `default_order` = 4 '
     'WHERE id = 36',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 36'),

    ('UPDATE operation_category '
     'SET `default_order` = 5 '
     'WHERE id = 37',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 37'),

    ('UPDATE operation_category '
     'SET `default_order` = 6 '
     'WHERE id = 38',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 38'),

    ('UPDATE operation_category '
     'SET `default_order` = 1 '
     'WHERE id = 18',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 18'),

    ('UPDATE operation_category '
     'SET `default_order` = 2 '
     'WHERE id = 21',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 21'),

    ('UPDATE operation_category '
     'SET `default_order` = 3 '
     'WHERE id = 19',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 19'),

    ('UPDATE operation_category '
     'SET `default_order` = 4 '
     'WHERE id = 22',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 22'),

    ('UPDATE operation_category '
     'SET `default_order` = 5 '
     'WHERE id = 39',
     'UPDATE operation_category '
     'SET `default_order` = 0 '
     'WHERE id = 39'),



]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            # print cmd[0]
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
            # print cmd[0]
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
