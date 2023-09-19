#!/bin/bash

python /db_script/pg_run.py &
echo "Running pg_run.py"
sleep 1

python /db_script/pg_lock_run.py &
echo "Running pg_lock_run.py"
sleep 1

python /db_script/maria_run.py &
echo "Running maria_run.py"
sleep 1

python /db_script/maria_lock_run.py &
echo "Running maria_lock_run.py"
sleep 1

python /db_script/mysql_run.py &
echo "Running mysql_run.py"
sleep 1

python /db_script/mysql_lock_run.py &
echo "Running mysql_lock_run.py"
sleep 1

for (( ; ; ))
do
    sleep 5
done