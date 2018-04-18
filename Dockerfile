#
# Kevbot Dockerfile
#
# https://github.com/vgroove/kevbot
#

# Pull base image.
FROM python:3

# Create directory for code to be mounted
RUN mkdir /kevbot

# Install pip packages
ADD requirements.txt /
RUN pip install -r /requirements.txt

# Define working directory.
# For development purposes, kevbot directory is mounted as volume
VOLUME ["/kevbot"]
WORKDIR /kevbot

# Define default command.
CMD ["python", "__init__.py"]
