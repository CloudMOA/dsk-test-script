FROM python:3.10-alpine3.17

RUN apt install build-dep python-psycopg2
RUN pip install psycopg2-binary

COPY run.py /run.py
COPY query.sql /query.sql

ENTRYPOINT [ "/run.py" ]