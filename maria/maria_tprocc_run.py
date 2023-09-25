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
print(os.getenv('EXE_MINUTES'))
print(os.getenv('SLEEP_MINUTES'))

dbset('db','maria')
dbset('bm','TPC-C')

diset('connection','maria_host',os.getenv('DB_HOST'))
diset('connection','maria_port',os.getenv('DB_PORT'))

diset('tpcc','maria_user',os.getenv('DB_USER'))
diset('tpcc','maria_pass',os.getenv('DB_PASSWD'))
diset('tpcc','maria_dbase',os.getenv('DB_NAME'))
diset('tpcc','maria_driver','timed')
diset('tpcc','maria_rampup','2')
diset('tpcc','maria_duration',os.getenv('EXE_MINUTES'))
diset('tpcc','maria_allwarehouse','true')
diset('tpcc','maria_timeprofile','true')

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
# file_path = os.path.join(tmpdir , "maria_tprocc" )
# fd = open(file_path, "w")
# fd.write(jobid)
# fd.close()
exit()