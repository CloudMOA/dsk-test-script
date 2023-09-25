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
print("* SLEEP_MINUTES = "+os.getenv('SLEEP_MINUTES'))

dbset('db','mysql')
dbset('bm','TPC-C')

diset('connection','mysql_host',os.getenv('DB_HOST'))
diset('connection','mysql_port',os.getenv('DB_PORT'))

diset('tpcc','mysql_user',os.getenv('DB_USER'))
diset('tpcc','mysql_pass',os.getenv('DB_PASSWD'))
diset('tpcc','mysql_dbase',os.getenv('DB_NAME'))
diset('tpcc','mysql_driver','timed')
diset('tpcc','mysql_rampup','2')
diset('tpcc','mysql_duration',os.getenv('EXE_MINUTES'))
diset('tpcc','mysql_allwarehouse','true')
diset('tpcc','mysql_timeprofile','true')

loadscript()
print("TEST STARTED")
vuset('vu','vcpu')
vucreate()
tcstart()
tcstatus()
jobid = tclpy.eval('vurun')
vudestroy()
tcstop()
print("TEST COMPLETE")
exit()