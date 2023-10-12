import pymysql
import time
import os

host = os.environ.get('MYSQL_DB_HOST')
port = int(os.environ.get('MYSQL_DB_PORT'))
dbname = os.environ.get('MYSQL_DB_NAME')
user = os.environ.get('MYSQL_DB_USER')
password = os.environ.get('MYSQL_DB_PASSWD')
sleeptime = int(os.environ.get('MYSQL_SLEEP'))
locktime = int(os.environ.get('MYSQL_LOCK_TIME'))
lockFilePath = "/db_script/mysql_lock_query_1.sql"

# host = "10.10.43.100"
# port = 31302
# dbname = "tpcc"
# user = "root"
# password = "root"
# sleeptime = 5
# locktime = 60
# lockFilePath = "mysql_lock_query_1.sql"

print('---------------------')
print('host: ' + host)
print('port: ' + str(port))
print('dbname: ' + dbname)
print('user: ' + user)
print('password: ' + password)
print('sleep: ' + str(sleeptime))
print('locktime: ' + str(locktime))
print('---------------------')

lockQueryList = []
count = 0

querys = open(lockFilePath, 'r')
lockQueryList = querys.read().split(';')
querys.close()

while True:
    if count > 3:
        querys = open(lockFilePath, 'r')
        lockQueryList = querys.read().split(';')
        querys.close()
        count = 0

    try:
        for query in lockQueryList:
            query = query.strip()

            connection = pymysql.connect(
                host=host, database=dbname, user=user, password=password, port=port)
            connection.autocommit = False

            if query != '':
                cur = connection.cursor()
                print(query)
                cur.execute(query)
                time.sleep(locktime)
                print('Rollback')
                connection.rollback()
                cur.close()
                print('---------------------')
            connection.close()
            time.sleep(sleeptime)
    except:
        print('Error')
    count = count + 1
    print('---------------------')