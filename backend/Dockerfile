FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www

ADD ./backend $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

# Copy init.csv from the parent directory
COPY ./init.csv $CONTAINER_HOME/init.csv

ARG DB_NAME
ENV DB_NAME $DB_NAME

RUN pip install -r $CONTAINER_HOME/requirements.txt
