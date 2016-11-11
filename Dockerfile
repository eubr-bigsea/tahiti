FROM python:2.7-onbuild
MAINTAINER Guilherme Maluf <guimalufb@gmail.com>

EXPOSE 5000
CMD [ "python", "./tahiti/app_api.py", "-c", "tahiti.json" ]
