FROM python:3.9.5-alpine3.14 as base

RUN apk add --no-cache bash

FROM base as pip_builder
RUN apk add --no-cache gcc g++ musl-dev postgresql-dev
COPY requirements.txt /
RUN pip install -r /requirements.txt

FROM base
LABEL maintainer="Vinicius Dias <viniciusvdias@dcc.ufmg.br>, Guilherme Maluf <guimaluf@dcc.ufmg.br>"

ENV TAHITI_HOME /usr/local/tahiti
ENV TAHITI_CONFIG $TAHITI_HOME/conf/tahiti-config.yaml
RUN apk add dumb-init
COPY --from=pip_builder /usr/local /usr/local

WORKDIR $TAHITI_HOME
COPY . $TAHITI_HOME

ENV FLASK_APP=tahiti.app

COPY bin/entrypoint /usr/local/bin/
ENTRYPOINT ["/usr/bin/dumb-init", "--", "/usr/local/bin/entrypoint"]
CMD ["server"]
