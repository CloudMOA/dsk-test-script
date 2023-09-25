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

vu = tclpy.eval('numberOfCPUs')
warehouse = int(vu) * 1
diset('tpcc','pg_count_ware',warehouse)
diset('tpcc','pg_num_vu',vu)
diset('tpcc','pg_superuser','postgres')
diset('tpcc','pg_superuserpass',os.getenv('DB_POSTGRES_PASSWD'))
diset('tpcc','pg_defaultdbase','postgres')
diset('tpcc','pg_user',os.getenv('DB_USER'))
diset('tpcc','pg_pass',os.getenv('DB_PASSWD'))
diset('tpcc','pg_dbase',os.getenv('DB_NAME'))
diset('tpcc','pg_tspace','pg_default')
if (warehouse >= 200):
    diset('tpcc','pg_partition','true')
else:
    diset('tpcc','pg_partition','false')

print("SCHEMA BUILD STARTED")
buildschema()
print("SCHEMA BUILD COMPLETED")
exit()