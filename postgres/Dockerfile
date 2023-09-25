FROM tpcorg/hammerdb:postgres

COPY *.sh /tpcc_script/
COPY *.py /tpcc_script/

RUN chmod 755 /tpcc_script/*.sh
RUN chmod 755 /tpcc_script/*.py

ENV DB_HOST "10.10.43.105"
ENV DB_PORT "31305"
ENV DB_NAME "tpcc"
ENV DB_USER "root"
ENV DB_PASSWD "root"
ENV DB_POSTGRES_PASSWD "postgres"
ENV EXE_MINUTES "5"
ENV SLEEP_SECONDS "60"
ENV ACTION "run"

ENTRYPOINT [ "/tpcc_script/start.sh" ]