FROM tpcorg/hammerdb:mysql

COPY *.sh ./
COPY *.py ./

ENV DB_HOST "10.10.43.100"
ENV DB_PORT "32233"
ENV DB_NAME "manager"
ENV DB_USER "postgres"
ENV DB_PASSWD "root"
ENV SLEEP "60"

ENTRYPOINT [ "/db_script/start.sh" ]