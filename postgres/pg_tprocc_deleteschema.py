#!/bin/tclsh
# maintainer: Pooja Jain
import os
tmpdir = os.getenv('TMP')

print("SETTING CONFIGURATION")
print(os.getenv('DB_HOST'))
print(os.getenv('DB_PORT'))
print(os.getenv('DB_NAME'))
print(os.getenv('DB_USER'))
print(os.getenv('DB_PASSWD'))
print(os.getenv('DB_POSTGRES_PASSWD'))
print(os.getenv('EXE_MINUTES'))
print(os.getenv('SLEEP_MINUTES'))

dbset('db','pg')
dbset('bm','TPC-C')

diset('connection','pg_host',os.getenv('DB_HOST'))
diset('connection','pg_port',os.getenv('DB_PORT'))
diset('connection','pg_sslmode','prefer')

diset('tpcc','pg_superuser','postgres')
diset('tpcc','pg_superuserpass',os.getenv('DB_POSTGRES_PASSWD'))
diset('tpcc','pg_defaultdbase','postgres')
diset('tpcc','pg_user',os.getenv('DB_USER'))
diset('tpcc','pg_pass',os.getenv('DB_PASSWD'))
diset('tpcc','pg_dbase',os.getenv('DB_NAME'))

print("DROP SCHEMA STARTED")
deleteschema()
print("DROP SCHEMA COMPLETED")
exit()