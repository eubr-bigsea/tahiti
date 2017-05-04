FROM ubuntu:16.04
MAINTAINER Vinicius Dias <viniciusvdias@dcc.ufmg.br>

# Install python and jdk
RUN apt-get update \
   && apt-get install -qy python-pip

# Install juicer
ENV TAHITI_HOME /usr/local/tahiti
ENV TAHITI_CONFIG $TAHITI_HOME/conf/tahiti-config.yaml
RUN mkdir -p $TAHITI_HOME/conf
RUN mkdir -p $TAHITI_HOME/sbin
RUN mkdir -p $TAHITI_HOME/tahiti
ADD sbin $TAHITI_HOME/sbin
ADD tahiti $TAHITI_HOME/tahiti
ADD migrations $TAHITI_HOME/migrations
ADD logging_config.ini $TAHITI_HOME/

# Install tahiti requirements and entrypoint
ADD requirements.txt $TAHITI_HOME
RUN pip install -r $TAHITI_HOME/requirements.txt
EXPOSE 5000
CMD ["/usr/local/tahiti/sbin/tahiti-daemon.sh", "startf"]
