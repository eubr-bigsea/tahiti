FROM python:3.7.3-alpine3.9 as base

FROM base as pip_builder
RUN apk add --no-cache gcc musl-dev
COPY requirements.txt /
RUN pip install -r /requirements.txt

FROM base
LABEL maintainer="Vinicius Dias <viniciusvdias@dcc.ufmg.br>, Guilherme Maluf <guimaluf@dcc.ufmg.br>"

ENV TAHITI_HOME /usr/local/tahiti
ENV TAHITI_CONFIG $TAHITI_HOME/conf/tahiti-config.yaml

COPY --from=pip_builder /usr/local /usr/local

WORKDIR $TAHITI_HOME
COPY . $TAHITI_HOME

CMD ["/usr/local/tahiti/sbin/tahiti-daemon.sh", "docker"]
