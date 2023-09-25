#!/bin/bash

export TMP=`pwd`/TMP
mkdir -p $TMP

if [ "$ACTION" == "create" ]; then
    echo "BUILD HAMMERDB SCHEMA"
    echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    ./hammerdbcli py auto /tpcc_script/maria_tprocc_buildschema.py
    echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
fi

if [ "$ACTION" == "run" ]; then
    while true; do
        echo "RUN HAMMERDB TEST"
        echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
        ./hammerdbcli py auto /tpcc_script/maria_tprocc_run.py
        echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
        sleep $SLEEP_SECONDS
    done
fi

if [ "$ACTION" == "delete" ]; then
    echo "DROP HAMMERDB SCHEMA"
    echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    ./hammerdbcli py auto /tpcc_script/maria_tprocc_deleteschema.py
    echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
fi
