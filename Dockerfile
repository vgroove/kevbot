#
# Kevbot Dockerfile
#
# https://github.com/vgroove/kevbot
#

# Pull base image.
FROM python:3

# Create directory for code to be mounted
RUN mkdir -p /app/kevbot

# Install pip packages
ADD requirements.txt /
RUN pip install -r /requirements.txt

# Define working directory.
# For development purposes, kevbot directory is mounted as volume
VOLUME ["/app/kevbot"]
WORKDIR /app/kevbot

# Add code to pythonpath
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Define default command.
CMD ["python", "__init__.py"]
