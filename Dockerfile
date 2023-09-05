FROM python:3.10-bookworm

RUN pip install psycopg2-binary
RUN pip install pymysql
RUN apt-get update -y
RUN apt-get install -y libmariadb-dev
RUN apt-get install -y vim
RUN pip install mariadb

COPY *.sh /db_script/
COPY *.py /db_script/
COPY *.sql /db_script/
RUN chmod 777 /db_script/*.sh
RUN chmod 777 /db_script/*.py

ENV PG_DB_HOST "10.10.43.100"
ENV PG_DB_PORT "32233"
ENV PG_DB_NAME "manager"
ENV PG_DB_USER "postgres"
ENV PG_DB_PASSWD "root"
ENV PG_SLEEP "60"

ENV MARIA_DB_HOST "10.10.43.100"
ENV MARIA_DB_PORT "31305"
ENV MARIA_DB_NAME "tpcc"
ENV MARIA_DB_USER "root"
ENV MARIA_DB_PASSWD "root"
ENV MARIA_SLEEP "60"

ENV MYSQL_DB_HOST "10.10.43.100"
ENV MYSQL_DB_PORT "31302"
ENV MYSQL_DB_NAME "tpcc"
ENV MYSQL_DB_USER "root"
ENV MYSQL_DB_PASSWD "root"
ENV MYSQL_SLEEP "60"

ENTRYPOINT [ "/db_script/start.sh" ]