FROM python:3.10-alpine3.17

RUN pip install psycopg2-binary

COPY run.py /run.py
COPY query.sql /query.sql
RUN chmod 777 /run.py

ENV DB_HOST "10.10.43.100"
ENV DB_PORT "32233"
ENV DB_NAME "manager"
ENV DB_USER "postgres"
ENV DB_PASSWD "root"

ENTRYPOINT [ "python", "/run.py" ]