#!/bin/tclsh
# maintainer: Pooja Jain
import os
tmpdir = os.getenv('TMP')

print("SETTING CONFIGURATION")
print("* DB_HOST = "+os.getenv('DB_HOST'))
print("* DB_PORT = "+os.getenv('DB_PORT'))
print("* DB_NAME = "+os.getenv('DB_NAME'))
print("* DB_USER = "+os.getenv('DB_USER'))
print("* DB_PASSWD = "+os.getenv('DB_PASSWD'))
print("* EXE_MINUTES = "+os.getenv('EXE_MINUTES'))
print("* SLEEP_SECONDS = "+os.getenv('SLEEP_SECONDS'))

dbset('db','mysql')
dbset('bm','TPC-C')

diset('connection','mysql_host',os.getenv('DB_HOST'))
diset('connection','mysql_port',os.getenv('DB_PORT'))

diset('tpcc','mysql_user',os.getenv('DB_USER'))
diset('tpcc','mysql_pass',os.getenv('DB_PASSWD'))
diset('tpcc','mysql_dbase',os.getenv('DB_NAME'))
print("DROP SCHEMA STARTED")

deleteschema()
print("DROP SCHEMA COMPLETED")
exit()