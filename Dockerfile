# Get python package
FROM rappdw/docker-java-python

MAINTAINER Will Milner # email: will@tulcolabs.com

# to avoid not getting error messages on docker stdout
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENVIRONMENT DOCKER

# Directory in container for all project files
ENV HOME=/code

# Override environment varialbe defined in .env.vault file
ENV DJANGO_ENVIRONMENT DOCKER

# create directory to hold code in container
RUN mkdir $HOME
WORKDIR $HOME

ADD requirements.txt $HOME

RUN apt-get update && apt-get -y upgrade

RUN pip install Pillow
RUN pip install -r requirements.txt

# copy application to container folder
ADD . $HOME