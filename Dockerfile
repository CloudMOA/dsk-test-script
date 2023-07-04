FROM python:3.10-alpine3.17

RUN pip install psycopg2-binary

COPY run.py /run.py
COPY query.sql /query.sql
RUN chmod 777 /run.py

ENTRYPOINT [ "python", "/run.py" ]