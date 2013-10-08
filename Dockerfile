FROM ubuntu:12.04
MAINTAINER Chris Reeves

ADD . /foo

WORKDIR /foo
RUN cd /foo

RUN apt-get install -y python python-dev python-software-properties
RUN apt-get install -y make
RUN apt-get install -y wget
RUN apt-get install -y tar
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py --no-check-certificate -O - | python
RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py --no-check-certificate -O - | python
RUN make develop

EXPOSE 8080
