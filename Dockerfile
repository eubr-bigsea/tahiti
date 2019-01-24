FROM node:8 as citrus_build
LABEL maintainer="Walter dos Santos Filho <walter AT dcc.ufmg.br> Guilherme Maluf Balzana <guimaluf AT dcc.ufmg.br"

ENV CITRUS_HOME=/usr/local/citrus
WORKDIR $CITRUS_HOME

COPY package*.json $CITRUS_HOME/
RUN npm install

COPY . $CITRUS_HOME
RUN npm run build

#
FROM nginx:1.15-alpine
LABEL maintainer="Walter dos Santos Filho <walter AT dcc.ufmg.br> Guilherme Maluf Balzana <guimaluf AT dcc.ufmg.br"

ENV CITRUS_HOME=/usr/local/citrus
WORKDIR $CITRUS_HOME

COPY extras/nginx.conf.sample /etc/nginx/conf.d/default.conf
COPY --from=citrus_build /usr/local/citrus/dist ./dist

EXPOSE 8080
