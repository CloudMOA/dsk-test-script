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
print(os.getenv('SLEEP'))

dbset('db','mysql')
dbset('bm','TPC-C')

diset('connection','mysql_host',os.getenv('DB_HOST'))
diset('connection','mysql_port',os.getenv('DB_PORT'))

vu = tclpy.eval('numberOfCPUs')
warehouse = int(vu) * 1
diset('tpcc','mysql_count_ware',warehouse)
diset('tpcc','mysql_num_vu',vu)
diset('tpcc','mysql_user',os.getenv('DB_USER'))
diset('tpcc','mysql_pass',os.getenv('DB_PASSWD'))
diset('tpcc','mysql_dbase',os.getenv('DB_NAME'))
diset('tpcc','mysql_storage_engine','innodb')
if (warehouse >= 200): 
    diset('tpcc','mysql_partition','true') 
else:
    diset('tpcc','mysql_partition','false') 

print("SCHEMA BUILD STARTED")
buildschema()
print("SCHEMA BUILD COMPLETED")
exit()