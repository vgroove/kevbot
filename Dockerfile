#
# Kevbot Dockerfile
#
# https://github.com/vgroove/kevbot
#

# Pull base image.
FROM ubuntu:16.04

# Copy over code
ADD kevbot /kevbot
ADD venv/requirements.txt /

# Install and configure Python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Install pip packages
RUN pip3 install -r /requirements.txt

# Define working directory.
WORKDIR /kevbot

# Define default command.
CMD ["python", "__init__.py"]
