FROM tpcorg/hammerdb:mysql

COPY *.sh /tpcc_script/
COPY *.py /tpcc_script/

RUN chmod 755 /tpcc_script/*.sh
RUN chmod 755 /tpcc_script/*.py

ENV DB_HOST "10.10.43.100"
ENV DB_PORT "32233"
ENV DB_NAME "manager"
ENV DB_USER "postgres"
ENV DB_PASSWD "root"
ENV SLEEP "60"

ENTRYPOINT [ "/tpcc_script/start.sh" ]