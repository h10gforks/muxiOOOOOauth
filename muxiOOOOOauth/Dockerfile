FROM python:2.7
MAINTAINER neo1218 <neo1218@yeah.net>

ENV DEPLOY_PATH /muxiauth

RUN mkdir -p $DEPLOY_PATH
WORKDIR $DEPLOY_PATH

RUN apt-get update \
  && apt-get install -y mysql-server --no-install-recommends \
  && apt-get clean \
  && pip install PyMySQL \
  && pip install MySQL-python \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

Add requirements.txt requirements.txt
RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com
# RUN pip install --index-url https://pypi.python.org/simple/ -r requirements.txt --trusted-host=pypi.python.org
RUN pip install mysql-python

Add . .
