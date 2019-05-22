# coding=utf-8
"""adjusts

Revision ID: b993656aa211
Revises: 790ae4e8f5d6
Create Date: 2018-04-23 14:47:29.842149

"""
import json

from alembic import context
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = 'b993656aa211'
down_revision = '790ae4e8f5d6'
branch_labels = None
depends_on = None

isotonic_old = [{"value": "Isotonic/increasing", "key": True},
                {"value": "Orantitonic/decreasing", "key": False}]
isotonic_new = [{"value": "Isotonic/increasing", "key": True},
                {"value": "Antitonic/decreasing", "key": False}]

metrics_new = [
    {
        "key": "areaUnderROC",
        "value": "Area under ROC curve (binary classification)",
        "en": "Area under ROC curve(binary classification)",
        "pt": "Área sob a curva ROC (classificação binária)"
    },
    {
        "key": "areaUnderPR",
        "value": "Area under precision-recall curve (binary classification)",
        "en": "Area under precision-recall curve (binary classification)",
        "pt": "Área sob a curva precisão-revocação"
    },
    {
        "key": "f1", "value": "F1 score (multiclass classification)",
        "en": "F1 score (multiclass classification)",
        "pt": "F1"
    },
    {
        "key": "weightedPrecision",
        "value": "Weighted precision (multiclass classification)",
        "en": "Weighted precision (multiclass classification)",
        "pt": "Precisão ponderada"
    },
    {
        "key": "weightedRecall",
        "value": "Weighted recall (multiclass classification)",
        "en": "Weighted recall (multiclass classification)",
        "pt": "Revocação ponderada"
    },
    {
        "key": "accuracy", "value": "Accuracy (multiclass classification)",
        "en": "Accuracy (multiclass classification)",
        "pt": "Acurácia"
    },
    {
        "key": "rmse", "value": "Root mean squared error  (regression)",
        "en": "Root mean squared error  (regression)",
        "pt": "Raíz do erro quadrático médio"
    },
    {
        "mse": "mse", "value": "Mean squared error (regression)",
        "en": "Mean squared error (regression)",
        "pt": "Erro quadrático médio"
    },
    {
        "key": "mae", "value": "Mean absolute error regression)",
        "en": "Mean absolute error (regression)",
        "pt": "Erro absoluto médio"
    }
]

metrics_old = [
    {
        "key": "areaUnderROC",
        "value": "Area under ROC (Binary classification only)"
    },
    {
        "key": "areaUnderPR",
        "value": "Area under PR (Binary classification only)"
    },
    {
        "key": "f1", "value": "F1 (Multiclass classification only)"
    },
    {
        "key": "weightedPrecision",
        "value": "Weighted precision (Multiclass classification only)"
    },
    {
        "key": "weightedRecall",
        "value": "Weighted recall (Multiclass classification only)"
    },
    {
        "key": "accuracy", "value": "Accuracy (Multiclass classification only)"
    },
    {
        "key": "rmse", "value": "Root mean squared error  (Regression only)"
    },
    {
        "mse": "mse", "value": "Mean squared error (Regression only)"
    },
    {
        "key": "mae", "value": "Mean absolute error  (Regression only)"
    }
]


def update_values_field():
    values = [
        [13, [{"en": "Inner join", "value": "Inner join", "key": "inner",
               "pt": "Inner join"},
              {"en": "Left outer join", "value": "Left outer join",
               "key": "left_outer", "pt": "Left outer join"},
              {"en": "Right outer join", "value": "Right outer join",
               "key": "right_outer", "pt": "Right outer join"}]],
        [19, [{"en": "Replace with mean", "value": "Replace with mean",
               "key": "MEAN", "pt": "Substituir com a média"},
              {"en": "Replace with value", "value": "Replace with value",
               "key": "VALUE", "pt": "Substituir por valor"}, {
                  "en": "Replace with approx. median (10% relative target precision)",
                  "value": "Replace with approx. median (10% relative target precision)",
                  "key": "MEDIAN",
                  "pt": "Substituir com a mediana aproximada (10% de precisão relativa)"},
              {"en": "Replace with mode", "value": "Replace with mode",
               "key": "MODE", "pt": "Substituir com a moda"},
              {"en": "Remove entire row", "value": "Remove entire row",
               "key": "REMOVE_ROW", "pt": "Remover toda a linha"},
              {"en": "Remove entire column", "value": "Remove entire column",
               "key": "REMOVE_COLUMN", "pt": "Remover toda a coluna"}]],
        [62, [{"en": "Do not change", "value": "Do not change", "key": "keep",
               "pt": "Não alterar"},
              {"en": "Integer", "value": "Integer", "key": "integer",
               "pt": "Integer"},
              {"en": "String", "value": "String", "key": "string",
               "pt": "String"},
              {"en": "Double", "value": "Double", "key": "double",
               "pt": "Double"},
              {"en": "Date", "value": "Date", "key": "Date", "pt": "Date"},
              {"en": "Date/time", "value": "Date/time", "key": "Date/time",
               "pt": "Date/time"}]],
        [63, [{"en": "Do not change", "value": "Do not change", "key": "keep",
               "pt": "Não alterar"},
              {"en": "Yes", "value": "Yes", "key": "true", "pt": "Sim"},
              {"en": "No", "value": "No", "key": "false", "pt": "Não"}]],
        [64, [{"en": "Do not change", "value": "Do not change", "key": "keep",
               "pt": "Não alterar"},
              {"en": "Yes", "value": "Yes", "key": "true", "pt": "Sim"},
              {"en": "No", "value": "No", "key": "false", "pt": "Não"}]],
        [65, [{"en": "Do not change", "value": "Do not change", "key": "keep",
               "pt": "Não alterar"},
              {"en": "Yes", "value": "Yes", "key": "true", "pt": "Sim"},
              {"en": "No", "value": "No", "key": "false", "pt": "Não"}]],
        [77, [{"en": "From metadata (recommended)",
               "value": "From metadata (recommended)", "key": "FROM_LIMONERO",
               "pt": "A partir dos metadados (recomendado)"},
              {"en": "From data", "value": "From data", "key": "FROM_VALUES",
               "pt": "A partir dos dados"},
              {"en": "Do not infer", "value": "Do not infer", "key": "NO",
               "pt": "Não inferir"}]],
        [83, [{"en": "CSV data file", "value": "CSV data file", "key": "CSV",
               "pt": "Arquivo de dados CSV"},
              {"en": "JSON data file", "value": "JSON data file", "key": "JSON",
               "pt": "Arquivo de dados JSON"},
              {"en": "Parquet data file", "value": "Parquet data file",
               "key": "PARQUET", "pt": "Arquivo de dados Parquet"}]],
        [85, [{"en": "Append data to the existing file",
               "value": "Append data to the existing file", "key": "append",
               "pt": "Acrescentar dados ao arquivo existente"},
              {"en": "Do not overwrite, raise error",
               "value": "Do not overwrite, raise error", "key": "error",
               "pt": "Não sobrescrever, gerar erro"},
              {"en": "Ignore if file exists", "value": "Ignore if file exists",
               "key": "ignore", "pt": "Ignorar se existir"},
              {"en": "Overwrite if file exists",
               "value": "Overwrite if file exists", "key": "overwrite",
               "pt": "Sobrescrever se existir"}]],
        [87, [
            {"en": "HDFS - Default Storage", "value": "HDFS - Default Storage",
             "key": 1, "pt": "HDFS - Armazenamento padrão"}]],
        [94,
         [{"en": "String", "value": "String", "key": "string", "pt": "String"},
          {"en": "Vector", "value": "Vector", "key": "vector",
           "pt": "Vetor"}]],
        [102, [{"en": "Sample a random percentage of data",
                "value": "Sample a random percentage of data", "key": "percent",
                "pt": "Amostrar um percentual aleatório dos dados"},
               {"en": "Sample N random records from data",
                "value": "Sample N random records from data", "key": "value",
                "pt": "Amostrar N registros a partir dos dados"},
               {"en": "Extract top N records from data",
                "value": "Extract top N records from data", "key": "head",
                "pt": "Extrair os primeiro N registros dos dados"}]],
        [110, [{"en": "EM optimizer (Expectation Maximization)",
                "value": "EM optimizer (Expectation Maximization)", "key": "em",
                "pt": "Otimizador EM (Expectation Maximization)"},
               {"en": "Online optimizer", "value": "Online optimizer",
                "key": "online", "pt": "Otimizador online"}]],
        [111, [{"en": "Simple, use spaces as delimiters", "key": "simple",
                "value": "Simple, use spaces as delimiters",
                "pt": "Simples, use espaços como delimitadores"},
               {"en": "Use regular expression to determine delimiters",
                "key": "regex",
                "value": "Use regular expression to determine delimiters",
                "pt": "Use uma expressão regular para determinar os delimitadores"}]],
        [123, [{"en": "Count term frequency", "key": "count",
                "value": "Count term frequency",
                "pt": "Contar a frequência do termo"},
               {"en": "Use word2vec algorithm", "key": "word2vec",
                "value": "Use Word2vec algorithm",
                "pt": "Usar o algoritmo Word2vec"}, {
                   "en": "Map the sequence of terms to their TF using hashing trick",
                   "key": "hashing_tf",
                   "value": "Map the sequence of terms to their TF using hashing trick",
                   "pt": "Mapear a sequência de termos para TF (frequência do termo) usando hashing"}]],
        [149, [{"en": "Gini", "value": "Gini impurity",
                "key": "gini", "pt": "Coeficiente Gini"},
               {"en": "Entropy", "value": "Entropy", "key": "entropy",
                "pt": "Entropia"}]],
        [157, [{"en": "Traditional K-Means", "value": "Traditional K-Means",
                "key": "kmeans", "pt": "K-Means traditional"},
               {"en": "Bisecting K-Means", "value": "Bisecting K-Means",
                "key": "bisecting", "pt": "Bisecting K-Means"}]],
        [158, [{"en": "kmeans|| (kmeans++ variant)",
                "value": "kmeans|| (kmeans++ variant)", "key": "k-means||",
                "pt": "kmeans|| (kmeans++ variant)"},
               {"en": "random", "value": "random", "key": "random",
                "pt": "aleatório"}]],
        [173, [{"en": "Read as web service input",
                "value": "Read as web service input", "key": "SERVICE_INPUT",
                "pt": "Ler como entrada para o web service"}]],
        [174, [{"en": "Never choose input 2", "value": "Never choose input 2",
                "key": "NEVER", "pt": "Nunca usar a entrada 2"},
               {"en": "Workflow is running as a web service",
                "value": "Workflow is running as a web service",
                "key": "WEB_SERVICE",
                "pt": "Workflow está executando como um web service"}]],
        [187,
         [{"en": "Auto", "value": "Auto", "key": "auto", "pt": "Automático"},
          {"en": "Binomial", "value": "Binomial", "key": "binomial",
           "pt": "Binomial"}, {"en": "Multinomial", "value": "Multinomial",
                               "key": "multinomial",
                               "pt": "Multinomial"}]],
        [210, [{"en": "Auto (selected automatically)", "key": "auto",
                "value": "Automatically selected",
                "pt": "Selecionado automaticamente"},
               {"en": "Normal Equation", "key": "normal",
                "value": "Normal Equation", "pt": "Equação normal"},
               {"en": "Limited-memory BFGS", "key": "l-bfgs",
                "value": "Limited-memory BFGS",
                "pt": "BFGS com memória limitada"}]],
        [224, [
            {"en": "Correlation", "value": "Correlation", "key": "CORRELATION",
             "pt": "Correlação"},
            {"en": "Covariance", "value": "Covariance", "key": "COVARIANCE",
             "pt": "Covariância"}]],
        [230, [{"en": "Geospatial Data - Bulma",
                "value": "Geospatial Data - Bulma", "key": "BULMA",
                "pt": "Geospatial Data - Bulma"}]],
        [235, [
            {"en": "Save best model", "key": "BEST", "value": "Save best model",
             "pt": "Salvar o melhor modelo"},
            {"en": "Save all (names will be suffixed with model rank)",
             "key": "ALL",
             "value": "Save all (names will be suffixed with model rank)",
             "pt": "Salvar todos (nomes serão sufixados com o ranking do modelo)"}]],
        [237, [{"en": "Overwrite", "key": "OVERWRITE", "value": "Overwrite",
                "pt": "Sobrescrever"},
               {"en": "Raise error", "key": "ERROR", "value": "Raise error",
                "pt": "Gerar erro"}]],
        [254, [{"en": "Isotonic/increasing", "value": "Isotonic/increasing",
                "key": True, "pt": "Isotônico/crescente"},
               {"en": "Antitonic/decreasing", "value": "Antitonic/decreasing",
                "key": False, "pt": "Antitônico/decrescente"}]],
        [278,
         [{"en": "auto", "key": "auto", "value": "auto", "pt": "automático"},
          {"en": "all", "key": "all", "value": "all", "pt": "todos"},
          {"en": "onethird", "key": "onethird", "value": "onethird",
           "pt": "um terço"},
          {"en": "sqrt", "key": "sqrt", "value": "sqrt", "pt": "raiz quadrada"},
          {"en": "log2", "key": "log2", "value": "log2",
           "pt": "log2 (logaritmo na base 2)"}]],
        [282, [{"en": "Gaussian", "key": "gaussian", "value": "Gaussian",
                "pt": "Gaussiano"},
               {"en": "Binomial", "key": "binomial", "value": "Binomial",
                "pt": "Binomial"},
               {"en": "Poisson", "key": "poisson", "value": "Poisson",
                "pt": "Poisson"},
               {"en": "Gamma", "key": "gamma", "value": "Gamma",
                "pt": "Gamma"}]],
        [283, [{"en": "Identity (Gaussian)", "key": "identity",
                "value": "Identidade (Gaussiano)", "pt": "Identity (Gaussian)"},
               {"en": "log (Gaussian)", "key": "log", "value": "log (Gaussian)",
                "pt": "log (Gaussiano)"},
               {"en": "inverse(Gaussian)", "key": "inverse",
                "value": "inverse (Gaussian)", "pt": "inverso (Gaussiano)"},
               {"en": "logit (Binomial)", "key": "logit",
                "value": "logit (Binomial)", "pt": "logit (Binomial)"},
               {"en": "probit (Binomial)", "key": "probit",
                "value": "probit (Binomial)", "pt": "probit (Binomial)"},
               {"en": "cloglog (Binomial)", "key": "cloglog",
                "value": "cloglog (Binomial)", "pt": "cloglog (Binomial)"},
               {"en": "log (Poisson)", "key": "log", "value": "log (Poisson)",
                "pt": "log (Poisson)"},
               {"en": "identity (Poisson)", "key": "identity",
                "value": "identity (Poisson)", "pt": "identidade (Poisson)"},
               {"en": "sqrt (Poisson)", "key": "sqrt",
                "value": "sqrt (Poisson)",
                "pt": "sqrt/raiz quadrada (Poisson)"},
               {"en": "inverse (Gamma)", "key": "inverse",
                "value": "inverse (Gamma)", "pt": "inverso (Gamma)"},
               {"en": "identity (Gamma)", "key": "identity",
                "value": "identity (Gamma)", "pt": "identidade (Gamma)"},
               {"en": "log (Gamma)", "key": "log", "value": "log (Gamma)",
                "pt": "log (Gamma)"}]],
        [285,
         [{"en": "Auto", "key": "auto", "value": "Auto", "pt": "Automático"},
          {"en": "irls", "key": "irls", "value": "irls", "pt": "irls"}]],
        [306, [{"en": "Pie", "key": "pie", "value": "Pie", "pt": "Pizza (pie)"},
               {"en": "Donut", "key": "donut", "value": "Donut",
                "pt": "Rosca (donut)"}]],
        [332, [{"en": "Bar", "key": "bar", "value": "Bar", "pt": "Barras"},
               {"en": "Points", "key": "points", "value": "Points",
                "pt": "Pontos"},
               {"en": "Heatmap", "key": "heatmap", "value": "Heatmap",
                "pt": "Mapa de calor (heatmap)"},
               {"en": "Polygon (Geo JSON)", "key": "polygon",
                "value": "Polygon (Geo JSON)",
                "pt": "Polígono (Geo JSON)"}
               ]],
        [358, [{"en": "Convert invalid data to NULL", "key": "PERMISSIVE",
                "value": "Convert invalid data to NULL",
                "pt": "Converter dados inválidos para NULO (null)"},
               {"en": "Ignore whole corrupted record", "key": "DROPMALFORMED",
                "value": "Ignore whole corrupted record",
                "pt": "Ignorar todo o registro corrompido"},
               {"en": "Stop processing and raise error", "key": "FAILFAST",
                "value": "Stop processing and raise error",
                "pt": "Parar o processamento e gerar erro"}]],
        [369,
         [{"en": "Danish", "value": "Danish", "key": "danish",
           "pt": "Dinamarquês"},
          {"en": "Dutch", "value": "Dutch", "key": "dutch", "pt": "Holandês"},
          {"en": "English", "value": "English", "key": "english",
           "pt": "Inglês"},
          {"en": "Finnish", "value": "Finnish", "key": "finnish",
           "pt": "Finlandês"},
          {"en": "French", "value": "French", "key": "french", "pt": "Francês"},
          {"en": "German", "value": "German", "key": "german", "pt": "Alemão"},
          {"en": "Hungarian", "value": "Hungarian", "key": "hungarian",
           "pt": "Húngaro"},
          {"en": "Italian", "value": "Italian", "key": "italian",
           "pt": "Italiano"},
          {"en": "Norwegian", "value": "Norwegian", "key": "norwegian",
           "pt": "Norueguês"},
          {"en": "Portuguese", "value": "Portuguese", "key": "portuguese",
           "pt": "Português"},
          {"en": "Russian", "value": "Russian", "key": "russian",
           "pt": "Russo"},
          {"en": "Spanish", "value": "Spanish", "key": "spanish",
           "pt": "Espanhol"},
          {"en": "Swedish", "value": "Swedish", "key": "swedish",
           "pt": "Sueco"},
          {"en": "Turkish", "value": "Turkish", "key": "turkish",
           "pt": "Turco"}]],
        [375, [{"en": "Multinomial (default)", "key": "multinomial",
                "value": "Multinomial (default)",
                "pt": "Multinomial (padrão)"},
               {"en": "Bernoulli", "key": "bernoulli", "value": "Bernoulli",
                "pt": "Bernoulli"}]],
        [391, [{"en": "Entropy", "key": "entropy", "value": "Entropy",
                "pt": "Entropia"},
               {"en": "Gini", "key": "gini", "value": "Gini",
                "pt": "Impureza Gini"}]],
        [394, [{"en": "Logistic", "key": "logistic", "value": "Logistic",
                "pt": "Logistic"}]],
        [404,
         [{"en": "Auto", "key": "auto", "value": "Auto", "pt": "Automático"},
          {"en": "All", "key": "all", "value": "All", "pt": "Tudo"},
          {"en": "One third", "key": "onethird", "value": "One third",
           "pt": "Um terço"},
          {"en": "SQRT", "key": "sqrt", "value": "SQRT",
           "pt": "SQRT (raiz quadrada)"},
          {"en": "LOG2", "key": "log2", "value": "LOG2",
           "pt": "LOG2 (log base 2)"},
          {"en": "(0.0-1.0]", "key": "(0.0-1.0]", "value": "(0.0-1.0]",
           "pt": "(0.0-1.0]"},
          {"en": "[1-n]", "key": "[1-n]", "value": "[1-n]",
           "pt": "[1-n]"}]],
        [426, [
            {"en": "Min hash LSH for Jackard distance", "key": "min-hash-lsh",
             "value": "Min hash LSH for Jackard distance",
             "pt": "Min hash LSH para distância de Jackard"},
            {"en": "Bucketed random projection for Euclidean distance",
             "key": "bucketed-random",
             "value": "Bucketed random projection for Euclidean distance",
             "pt": "Projeção aleatória em buckets para a distância euclidiana"}]],
        [448, [{"en": "None", "key": "none", "value": "None", "pt": "Nenhum"},
               {"en": "Rows", "key": "rows", "value": "Rows", "pt": "Linhas"},
               {"en": "Range", "key": "range", "value": "Range",
                "pt": "Faixa"}]],
        [3004, [{"en": "From data", "value": "From data", "key": "FROM_VALUES",
                 "pt": "A partir dos dados"},
                {"en": "Do not infer", "value": "Do not infer", "key": "NO",
                 "pt": "Não inferir"}]],
        [3008, [{"en": "Count term frequency", "value": "Count term frequency",
                 "key": "count", "pt": "Contar a frequência do termo"},
                {"en": "Use Bag of Words", "value": "Use bag of words",
                 "key": "BoW", "pt": "Usar bag of words"}]],
        [3028, [{"en": "String", "value": "String", "key": "string",
                 "pt": "String"}]],
        [3039, [{"en": "kmeans|| (kmeans++ variant)",
                 "value": "kmeans|| (kmeans++ variant)", "key": "k-means||",
                 "pt": "kmeans|| (kmeans++ variant)"},
                {"en": "random", "value": "random", "key": "random",
                 "pt": "aleatório"}]],
        [3042, [{"en": " Precision, Recall and F1 (F-mesure)",
                 "value": " Precision, Recall and F1 (F-mesure)", "key": "f1",
                 "pt": " Precisão, Revocação e F1 (F-mesure)"},
                {"en": "Accuracy", "value": "Accuracy", "key": "accuracy",
                 "pt": "Accurácia"},
                {"en": "Root mean squared error (regression)",
                 "value": "Root mean squared error (regression)",
                 "key": "rmse",
                 "pt": "Raíz do erro quadrático médio (regression)"},
                {"mse": "mse", "en": "Mean squared error (regression)",
                 "pt": "Erro quadrático médio (regression)",
                 "value": "Mean squared error (regression)"},
                {"en": "Mean absolute error  (regression)",
                 "value": "Mean absolute error (regression)",
                 "key": "mae",
                 "pt": "Erro absoluto médio (regression)"}]],
        [3045, [{"en": "Replace by regex expression (only to string)",
                 "value": "Replace by regex expression (only to string)",
                 "key": "regex",
                 "pt": "Substituir com expressão regular (apenas texto)"},
                {"en": "Replace by value", "value": "Replace by value",
                 "key": "value", "pt": "Substituir por valor"}]],
        [3051, [{"en": "CSV data file", "value": "CSV data file", "key": "CSV",
                 "pt": "Arquivo de dados CSV"},
                {"en": "JSON data file", "value": "JSON data file",
                 "key": "JSON", "pt": "Arquivo de dados JSON"}]],
        [3053, [{"en": "Do not overwrite, raise error",
                 "value": "Do not overwrite, raise error", "key": "error",
                 "pt": "Não sobrescrever, gerar erro"},
                {"en": "Ignore if file exists",
                 "value": "Ignore if file exists", "key": "ignore",
                 "pt": "Ignorar se arquivo existe"},
                {"en": "Overwrite if file exists",
                 "value": "Overwrite if file exists", "key": "overwrite",
                 "pt": "Sobrescrever se arquivo existe"}]],
        [3080, [{"en": "Range Normalization", "value": "Range Normalization",
                 "key": "range",
                 "pt": "Normalização por faixa (range normalization)"},
                {"en": "Standard Score Normalization",
                 "value": "Standard Score Normalization", "key": "standard",
                 "pt": "Normalização de pontuação padrão (Standard Score Normalization)"}]],
        [3083, [{"en": "Do not change", "value": "Do not change", "key": "keep",
                 "pt": "Não alterar"},
                {"en": "Integer", "value": "Integer", "key": "integer",
                 "pt": "Integer"},
                {"en": "String", "value": "String", "key": "string",
                 "pt": "String"},
                {"en": "Double", "value": "Double", "key": "double",
                 "pt": "Double"},
                {"en": "Date", "value": "Date", "key": "Date", "pt": "Date"},
                {"en": "Date/time", "value": "Date/time", "key": "Date/time",
                 "pt": "Date/time"}]],
        [3084, [{"en": "Ignore whole corrupted record", "key": "DROPMALFORMED",
                 "value": "Ignore whole corrupted record",
                 "pt": "Ignorar todo o registro corrompido"},
                {"en": "Stop processing and raise error", "key": "FAILFAST",
                 "value": "Stop processing and raise error",
                 "pt": "Parar o processamento e gerar erro"}]],
        [3090, [{"en": "Overwrite", "key": "OVERWRITE", "value": "Overwrite",
                 "pt": "Sobrescrever"},
                {"en": "Raise error", "key": "ERROR", "value": "Raise error",
                 "pt": "Gerar erro"}]],
        [3096, [{"en": "Replace with mean", "value": "Replace with mean",
                 "key": "MEAN", "pt": "Substituir pela média"},
                {"en": "Replace with value", "value": "Replace with value",
                 "key": "VALUE", "pt": "Substituir por valor"},
                {"en": "Replace with approx. median",
                 "value": "Replace with app",
                 "pt": 'Substituir com a mediana aproximada'}
                ]]
    ]
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for pk, v in values:
            sql = '''
                UPDATE operation_form_field SET `VALUES` = %s
                WHERE id = %s '''
            connection.execute(sql, [json.dumps(v), pk])
    except:
        session.rollback()
        raise
    session.commit()


def revert_values_fields():
    old_values = [
        [13, [{"value": "Inner join", "key": "inner"},
              {"value": "Left outer join", "key": "left_outer"},
              {"value": "Right outer join", "key": "right_outer"}]],
        [19, [{"value": "Replace with mean", "key": "MEAN"},
              {"value": "Replace with value", "key": "VALUE"}, {
                  "value": "Replace with approx. median "
                           "(10% relative target precision)",
                  "key": "MEDIAN"},
              {"value": "Replace with mode", "key": "MODE"},
              {"value": "Remove entire row", "key": "REMOVE_ROW"},
              {"value": "Remove entire column", "key": "REMOVE_COLUMN"}]],
        [62, [{"value": "Do not change", "key": "keep"},
              {"value": "Integer", "key": "integer"},
              {"value": "String", "key": "string"},
              {"value": "Double", "key": "double"},
              {"value": "Date", "key": "Date"},
              {"value": "Date/time", "key": "Date/time"}]],
        [63, [{"value": "Do not change", "key": "keep"},
              {"value": "Yes", "key": "true"},
              {"value": "No", "key": "false"}]],
        [64, [{"value": "Do not change", "key": "keep"},
              {"value": "Yes", "key": "true"},
              {"value": "No", "key": "false"}]],
        [65, [{"value": "Do not change", "key": "keep"},
              {"value": "Yes", "key": "true"},
              {"value": "No", "key": "false"}]],
        [77, [{"value": "From metadata (recommended)", "key": "FROM_LIMONERO"},
              {"value": "From data", "key": "FROM_VALUES"},
              {"value": "Do not infer", "key": "NO"}]],
        [83, [{"value": "CSV data file", "key": "CSV"},
              {"value": "JSON data file", "key": "JSON"},
              {"value": "Parquet data file", "key": "PARQUET"}]],
        [85, [{"value": "Append data to the existing file", "key": "append"},
              {"value": "Do not overwrite, raise error", "key": "error"},
              {"value": "Ignore if file exists", "key": "ignore"},
              {"value": "Overwrite if file exists", "key": "overwrite"}]],
        [87, [{"value": "HDFS - Default Storage", "key": 1}]],
        [94, [{"value": "String", "key": "string"},
              {"value": "Vector", "key": "vector"}]],
        [102,
         [{"value": "Sample a random percentage of data", "key": "percent"},
          {"value": "Sample N random records from data", "key": "value"},
          {"value": "Extract top N records from data", "key": "head"}]],
        [110, [{"value": "EM optimizer", "key": "em"},
               {"value": "Online optimizer", "key": "online"}]],
        [111, [{"key": "simple", "value": "Simple, use spaces as delimiters"},
               {"key": "regex",
                "value": "Use regular expression to determine delimiters"}]],
        [123, [{"key": "count", "value": "Count term frequency"},
               {"key": "word2vec", "value": "Use word2vec algorithm"},
               {"key": "hashing_tf",
                "value": "Map the sequence of terms to their TF "
                         "using hashing trick"}]],
        [149, [{"value": "Gini", "key": "gini"},
               {"value": "Entropy", "key": "entropy"}]],
        [157, [{"value": "Traditional K-Means", "key": "kmeans"},
               {"value": "Bisecting K-Means", "key": "bisecting"}]],
        [158, [{"value": "kmeans|| (kmeans++ variant)", "key": "k-means||"},
               {"value": "random", "key": "random"}]],
        [173, [{"value": "Read as web service input", "key": "SERVICE_INPUT"}]],
        [174, [{"value": "Never choose input 2", "key": "NEVER"},
               {"value": "Workflow is running as a web service",
                "key": "WEB_SERVICE"}]],
        [187, [{"value": "Auto", "key": "auto"},
               {"value": "Binomial", "key": "binomial"},
               {"value": "Multinomial", "key": "multinomial"}]],
        [210, [{"key": "auto", "value": "Auto (selected automatically)"},
               {"key": "normal", "value": "Normal Equation"},
               {"key": "l-bfgs", "value": "Limited-memory BFGS"}]],
        [224, [{"value": "Correlation", "key": "CORRELATION"},
               {"value": "Covariance", "key": "COVARIANCE"}]],
        [230, [{"value": "Geospatial Data - Bulma", "key": "BULMA"}]],
        [235, [{"key": "BEST", "value": "Save best model"},
               {"key": "ALL",
                "value": "Save all (names will be suffixed with model rank)"}]],
        [237, [{"key": "OVERWRITE", "value": "Overwrite"},
               {"key": "ERROR", "value": "Raise error"}]],
        [254, [{"value": "Isotonic/increasing", "key": True},
               {"value": "Antitonic/decreasing", "key": False}]],
        [278, [{"key": "auto", "value": "auto"}, {"key": "all", "value": "all"},
               {"key": "onethird", "value": "onethird"},
               {"key": "sqrt", "value": "sqrt"},
               {"key": "log2", "value": "log2"}]],
        [282, [{"key": "gaussian", "value": "Gaussian"},
               {"key": "binomial", "value": "Binomial"},
               {"key": "poisson", "value": "Poisson"},
               {"key": "gamma", "value": "Gamma"}]],
        [283, [{"key": "identity", "value": "Identity (Gaussian)"},
               {"key": "log", "value": "log (Gaussian)"},
               {"key": "inverse", "value": "inverse(Gaussian)"},
               {"key": "logit", "value": "logit (Binomial)"},
               {"key": "probit", "value": "probit (Binomial)"},
               {"key": "cloglog", "value": "cloglog (Binomial)"},
               {"key": "log", "value": "log (Poisson)"},
               {"key": "identity", "value": "identity (Poisson)"},
               {"key": "sqrt", "value": "sqrt (Poisson)"},
               {"key": "inverse", "value": "inverse (Gamma)"},
               {"key": "identity", "value": "identity (Gamma)"},
               {"key": "log", "value": "log (Gamma)"}]],
        [285,
         [{"key": "auto", "value": "Auto"}, {"key": "irls", "value": "irls"}]],
        [306,
         [{"key": "pie", "value": "Pie"}, {"key": "donut", "value": "Donut"}]],
        [332,
         [{"key": "bar", "value": "bar"}, {"key": "points", "value": "points"},
          {"key": "heatmap", "value": "heatmap"}]],
        [358, [{"key": "PERMISSIVE", "value": "Convert invalid data to NULL"},
               {"key": "DROPMALFORMED",
                "value": "Ignore whole corrupted record"},
               {"key": "FAILFAST",
                "value": "Stop processing and raise error"}]],
        [369, [{"value": "danish", "key": "danish"},
               {"value": "dutch", "key": "dutch"},
               {"value": "english", "key": "english"},
               {"value": "finnish", "key": "finnish"},
               {"value": "french", "key": "french"},
               {"value": "german", "key": "german"},
               {"value": "hungarian", "key": "hungarian"},
               {"value": "italian", "key": "italian"},
               {"value": "norwegian", "key": "norwegian"},
               {"value": "portuguese", "key": "portuguese"},
               {"value": "russian", "key": "russian"},
               {"value": "spanish", "key": "spanish"},
               {"value": "swedish", "key": "swedish"},
               {"value": "turkish", "key": "turkish"}]],
        [375, [{"key": "multinomial", "value": "Multinomial (default)"},
               {"key": "bernoulli", "value": "Bernoulli"}]],
        [391, [{"key": "entropy", "value": "Entropy"},
               {"key": "gini", "value": "Gini"}]],
        [394, [{"key": "logistic", "value": "Logistic"}]],
        [404, [{"key": "auto", "value": "Auto"}, {"key": "all", "value": "All"},
               {"key": "onethird", "value": "One third"},
               {"key": "sqrt", "value": "SQRT"},
               {"key": "log2", "value": "LOG2"},
               {"key": "(0.0-1.0]", "value": "(0.0-1.0]"},
               {"key": "[1-n]", "value": "[1-n]"}]],
        [426,
         [{"key": "min-hash-lsh", "value": "Min hash LSH for Jackard distance"},
          {"key": "bucketed-random",
           "value": "Bucketed random projection for Euclidean distance"}]],
        [448,
         [{"key": "none", "value": "None"}, {"key": "rows", "value": "Rows"},
          {"key": "range", "value": "Range"}]],
        [3004, [{"value": "From data", "key": "FROM_VALUES"},
                {"value": "Do not infer", "key": "NO"}]],
        [3008, [{"value": "Count term frequency", "key": "count"},
                {"value": "Use Bag of Words", "key": "BoW"}]],
        [3028, [{"value": "String", "key": "string"}]],
        [3039, [{"value": "kmeans|| (kmeans++ variant)", "key": "k-means||"},
                {"value": "random", "key": "random"}]],
        [3042, [{"value": " Precision, Recall and F1 (F-mesure)", "key": "f1"},
                {"value": "Accuracy", "key": "accuracy"},
                {"value": "Root mean squared error  (Regression only)",
                 "key": "rmse"},
                {"mse": "mse", "value": "Mean squared error (Regression only)"},
                {"value": "Mean absolute error  (Regression only)",
                 "key": "mae"}]],
        [3045, [{"value": "Replace by regex expression (only to string)",
                 "key": "regex"},
                {"value": "Replace by value", "key": "value"}]],
        [3051, [{"value": "CSV data file", "key": "CSV"},
                {"value": "JSON data file", "key": "JSON"}]],
        [3053, [{"value": "Do not overwrite, raise error", "key": "error"},
                {"value": "Ignore if file exists", "key": "ignore"},
                {"value": "Overwrite if file exists", "key": "overwrite"}]],
        [3080, [{"value": "Range Normalization", "key": "range"},
                {"value": "Standard Score Normalization", "key": "standard"}]],
        [3083, [{"value": "Do not change", "key": "keep"},
                {"value": "Integer", "key": "integer"},
                {"value": "String", "key": "string"},
                {"value": "Double", "key": "double"},
                {"value": "Date", "key": "Date"},
                {"value": "Date/time", "key": "Date/time"}]],
        [3084,
         [{"key": "DROPMALFORMED", "value": "Ignore whole corrupted record"},
          {"key": "FAILFAST", "value": "Stop processing and raise error"}]],
        [3090, [{"key": "OVERWRITE", "value": "Overwrite"},
                {"key": "ERROR", "value": "Raise error"}]],
        [3096, [{"value": "Replace with mean", "key": "MEAN"},
                {"value": "Replace with value", "key": "VALUE"},
                {"value": "Replace with approx. median", "key": "MEDIAN"},
                {"value": "Replace with mode", "key": "MODE"},
                {"value": "Remove entire row", "key": "REMOVE_ROW"},
                {"value": "Remove entire column", "key": "REMOVE_COLUMN"}]],
        [3100, [{"value": "Inner join", "key": "inner"},
                {"value": "Left outer join", "key": "left_outer"},
                {"value": "Right outer join", "key": "right_outer"}]],
    ]
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for pk, v in old_values:
            import pdb
            sql = '''
                UPDATE operation_form_field SET `VALUES` = %s
                WHERE id = %s '''
            connection.execute(sql, [json.dumps(v), pk])
    except:
        session.rollback()
        raise
    session.commit()


all_commands = [
    ("""
        UPDATE operation_form_field SET
        `values_url`='`${LIMONERO_URL}/datasources?format=SHAPEFILE&simple=true&list=true&enabled=1`'
        WHERE id = 133
        """,
     """
        UPDATE operation_form_field SET
        `values_url` ='`${LIMONERO_URL}/datasources?format=SHAPEFILE'
        WHERE id = 133
    """,),
    ("""
    INSERT IGNORE INTO
        operation_operation_form(operation_id, operation_form_id)
        VALUES (96, 110);
    """,
     """
     DELETE FROM operation_operation_form WHERE operation_form_id = 110 AND
        operation_id = 96
     """),
    ("""
    INSERT IGNORE INTO
        operation_operation_form(operation_id, operation_form_id)
        VALUES (2, 110);
    """,
     """
     DELETE FROM operation_operation_form WHERE operation_form_id = 110 AND
        operation_id = 2
     """),

    ("DELETE FROM operation_form_field_translation WHERE id = 153",
     "SELECT 1"),
    ("DELETE FROM operation_form_field WHERE id = 153", 'SELECT 1'),

    ('''INSERT INTO operation_port_interface_operation_port (operation_port_id,
        operation_port_interface_id) VALUES (37, 15);''',
     '''DELETE FROM operation_port_interface_operation_port WHERE
         operation_port_id = 37 AND  operation_port_interface_id = 15'''),

    ('''INSERT INTO operation_port_interface_operation_port (operation_port_id,
        operation_port_interface_id) VALUES (93, 15);''',
     '''DELETE FROM operation_port_interface_operation_port WHERE
         operation_port_id = 93 AND  operation_port_interface_id = 15'''),
    ('''
    UPDATE operation_form_field_translation
    SET label = 'Evaluated item id attribute' WHERE id = 180 AND locale = 'en'
    ''', '''SELECT 1'''),
    ('''UPDATE operation_form SET enabled = 0 WHERE id = 101;''',
     '''UPDATE operation_form SET enabled = 1 WHERE id = 101;'''),
    ('''UPDATE operation_form_field SET form_id = 1, `order`= 4
    WHERE form_id = 101 AND id = 236;''',
     '''UPDATE operation_form_field SET form_id = 101, `order`= 3
     WHERE form_id = 1 AND id = 236;'''),
    ('''UPDATE operation_form_field_translation SET
        label = 'Weights (comma-separated, used in ensembles)',
        help = 'Weights (comma-separated, used in ensembles).'
        WHERE id = 236 and locale = 'en';''',
     '''
     UPDATE operation_form_field_translation SET
        label = 'Weights (comma-separated, if empty, all estimators will have same weight)',
        help = 'Weights (if empty, all estimators will have same weight, otherwise, implies "soft" voting).'
        WHERE id = 236 and locale = 'en'
     '''),
    ('''UPDATE operation_form_field_translation SET
        label = 'Pesos (separados por vírgula, usados em ensembles)',
        help = 'Pesos (separados por vírgula, usados em ensembles)'
        WHERE id = 236 and locale = 'pt';''', '''
     UPDATE operation_form_field_translation SET
        label = 'Pesos (separados por vírgula, se vazio, os estimadores terão o mesmo peso)',
        help = 'Pesos (se vazio, os estimadores terão o mesmo peso).'
        WHERE id = 236 and locale = 'pt'
     '''),
    ("""UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107)
        """.format(json.dumps(metrics_new)),
     """UPDATE operation_form_field SET `values` = '{}' WHERE `id` IN (101, 107)
         """.format(json.dumps(metrics_old))),

    ("""UPDATE operation_form_field SET `values` = '{}' WHERE `id` = '254';
        """.format(json.dumps(isotonic_new)),
     """UPDATE operation_form_field SET `values` = '{}' WHERE `id` = '254';
         """.format(json.dumps(isotonic_old))),

    ('''UPDATE operation_translation SET name = 'Mineração de itemsets freq.'
        WHERE id = 3 AND locale = 'pt' ''',
     '''UPDATE operation_translation SET name = 'Mineiração de itemsets freq.'
        WHERE id = 3 AND locale = 'pt' '''),

    ('''UPDATE operation_form_translation SET name = 'Execução'
        WHERE id = 50 AND locale = 'pt' ''',
     '''UPDATE operation_form_translation SET name = 'Execution'
        WHERE id = 50 AND locale = 'pt' ''',),

    ('''UPDATE operation_translation SET name = 'Indexador de Feature'
        WHERE id = 40 AND locale = 'pt' ''',
     '''UPDATE operation_translation SET name = 'Indexador Feature'
        WHERE id = 40 AND locale = 'pt' ''',),
    ('''
    DELETE FROM operation_form_field_translation WHERE id IN (75, 76);
    ''', '''
        INSERT INTO
            operation_form_field_translation(`id`, `locale`, `label`,`help`)
            VALUES
            ('75','en','Use first line as header',
                'Does file first line contain header information about attributes?');
                INSERT INTO `operation_form_field_translation`
            ('75','pt','Usar a primeira linha como cabeçalho',
                'Arquivo contém cabeçalho com informações sobre atributos?'),
            ('76','en','Attribute separator',
                'Character used as attribute separator'),
            ('76','pt','Separador de atributos',
                'Caractere usado como separador de atributo (pode usar {tab} ou {new_line}).');

    '''),
    ('''
    DELETE FROM operation_form_field WHERE id IN (75, 76);
    ''', '''
    INSERT INTO `operation_form_field` (`id`, `name`, `type`, `required`,
        `order`, `default`, `suggested_widget`, `values_url`, `values`,
        `scope`, `form_id`)
        VALUES
        ('75','header','INTEGER','0','2','0', 'checkbox',NULL,NULL,'EXECUTION','18'),
        ('76','separator','TEXT','0','3',',','text',NULL,NULL, 'EXECUTION','18'),
    '''),
    ('''INSERT INTO `operation_form_field` (`id`, `name`, `type`, `required`,
        `order`, `default`, `suggested_widget`, `values_url`, `values`,
        `scope`, `form_id`) VALUES(455,'features','TEXT','1','1',NULL,
        'attribute-selector',NULL,NULL,'EXECUTION', 53)''',
     'DELETE FROM operation_form_field WHERE id = 455'),
    ('''
    INSERT INTO `operation_form_field_translation` (`id`, `locale`, `label`,
        `help`) VALUES
        (455,'en','Features attribute','Features attribute'),
        (455,'pt','Atributo com features',
        'Atributo com features');''',
     'DELETE FROM operation_form_field_translation WHERE id = 455'),

    ('''INSERT INTO `operation_form_field` (`id`, `name`, `type`, `required`,
        `order`, `default`, `suggested_widget`, `values_url`, `values`,
        `scope`, `form_id`) VALUES(456,'polygon','INTEGER','0','5',NULL,
        'lookup','`${LIMONERO_URL}/datasources?format=GEO_JSON&simple=true&list=true&enabled=1`', NULL,
        'EXECUTION', 112)''',
     'DELETE FROM operation_form_field WHERE id = 456'),
    ('''
    INSERT INTO `operation_form_field_translation` (`id`, `locale`, `label`,
        `help`) VALUES
        (456,'en','Polygons boundaries (Geo JSON)',
        'Polygons boundaries (Geo JSON)'),
        (456,'pt','Limites do polígono(s) (Geo JSON)',
            'Limite do polígono(s) (Geo JSON)');''',
     'DELETE FROM operation_form_field_translation WHERE id = 456'),
    # --
    ('''INSERT INTO `operation_form_field` (`id`, `name`, `type`, `required`,
        `order`, `default`, `suggested_widget`, `values_url`, `values`,
        `scope`, `form_id`) VALUES(457,'geojson_id','TEXT','0','6','id',
        'text', NULL, NULL,
        'EXECUTION', 112)''',
     'DELETE FROM operation_form_field WHERE id = 457'),
    ('''
    INSERT INTO `operation_form_field_translation` (`id`, `locale`, `label`,
        `help`) VALUES(457,'en',
        'Name of the property in Geo JSON used to relate data',
        'Name of the property in Geo JSON used to relate data.'),
        (457,'pt',
        'Nome da propriedade no Geo JSON usada para relacionar os dados',
        'Nome da propriedade no Geo JSON usada para relacionar os dados.');''',
     'DELETE FROM operation_form_field_translation WHERE id = 457'),

    # ---
    ('''INSERT INTO `operation_form_field` (`id`, `name`, `type`, `required`,
        `order`, `default`, `suggested_widget`, `values_url`, `values`,
        `scope`, `form_id`) VALUES(458,'extra_data','TEXT','0','7',NULL,
        'attribute-selector', NULL, NULL,
        'EXECUTION', 112)''',
     'DELETE FROM operation_form_field WHERE id = 458'),
    ('''
    INSERT INTO `operation_form_field_translation` (`id`, `locale`, `label`,
        `help`) VALUES
        (458,'en','Extra data (Geo JSON)', 'Extra data (Geo JSON)'),
        (458,'pt','Dados extras (Geo JSON)', 'Dados extras (Geo JSON)');''',
     'DELETE FROM operation_form_field_translation WHERE id = 458'),
    # ---
    [update_values_field, revert_values_fields],
    ('''
    UPDATE operation_form_field_translation SET
         label =
            'Atributo usado para o valor (opcional, obrigatório se Geo JSON)',
         help =
            'Atributo usado para o valor (opcional, obrigatório se Geo JSON)'
     WHERE id = 335 AND locale = 'pt'
    ''',
     '''
     UPDATE operation_form_field_translation SET
         label = 'Atributo usado para o valor (opcional)',
         help = 'Atributo usado para o valor (opcional)'
     WHERE id = 335 AND locale = 'pt' '''),

    ('''
    UPDATE operation_form_field_translation SET
         label =
            'Atributo usado para rótulo (exceto Geo JSON) ou identificador do polígono (se Geo JSON)',
         help =
            'Atributo usado para rótulo (exceto Geo JSON) ou identificador do polígono (se Geo JSON).'
     WHERE id = 336 AND locale = 'pt'
    ''',
     '''
     UPDATE operation_form_field_translation SET
         label = 'Atributo para rótulo (opcional)',
         help = 'Atributo para rótulo (opcional)'
     WHERE id = 336 AND locale = 'pt' '''),

    ('''
    UPDATE operation_form_field_translation SET
         label =
            'Attribute for the value (optional, required if Geo JSON)',
         help =
            'Attribute for the value (optional, required if Geo JSON).'
     WHERE id = 335 AND locale = 'en'
    ''',
     '''
     UPDATE operation_form_field_translation SET
         label = 'Attribute for the value (optional)',
         help = 'Attribute for the value (optional)'
     WHERE id = 335 AND locale = 'en' '''),

    ('''
    UPDATE operation_form_field_translation SET
         label =
            'Label attribute (except Geo JSON) or polygons\\' identifier(Geo JSON)',
         help =
            'Label attribute (except Geo JSON) or polygons\\' identifier(Geo JSON).'
     WHERE id = 336 AND locale = 'en'
    ''',
     '''
     UPDATE operation_form_field_translation SET
         label = 'Label attribute (optional)',
         help = 'Label attribute (optional)'
     WHERE id = 336 AND locale = 'en' '''),

    ('''UPDATE operation SET enabled = 0
        WHERE id IN (20, 33, 34, 36, 57, 58, 62, 83)''',
     '''UPDATE operation SET enabled = 1
     WHERE id IN (20, 33, 34, 36, 57, 58, 62, 83)'''),

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
    connection.execute('SET foreign_key_checks = 0;')

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
    connection.execute('SET foreign_key_checks = 1;')
    session.commit()
