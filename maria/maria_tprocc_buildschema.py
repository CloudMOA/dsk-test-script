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

dbset('db','maria')
dbset('bm','TPC-C')

diset('connection','maria_host',os.getenv('DB_HOST'))
diset('connection','maria_port',os.getenv('DB_PORT'))

vu = tclpy.eval('numberOfCPUs')
warehouse = int(vu) * 1
diset('tpcc','maria_count_ware',warehouse)
diset('tpcc','maria_num_vu',vu)
diset('tpcc','maria_user',os.getenv('DB_USER'))
diset('tpcc','maria_pass',os.getenv('DB_PASSWD'))
diset('tpcc','maria_dbase',os.getenv('DB_NAME'))
diset('tpcc','maria_storage_engine','innodb')
if (warehouse >= 200):
    diset('tpcc','maria_partition','true')
else:
    diset('tpcc','maria_partition','false')

print("SCHEMA BUILD STARTED")
buildschema()
print("SCHEMA BUILD COMPLETED")
exit()