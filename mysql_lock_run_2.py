import pymysql
import time
import os

host = os.environ.get('MYSQL_DB_HOST')
port = int(os.environ.get('MYSQL_DB_PORT'))
dbname = os.environ.get('MYSQL_DB_NAME')
user = os.environ.get('MYSQL_DB_USER')
password = os.environ.get('MYSQL_DB_PASSWD')
sleeptime = int(os.environ.get('MYSQL_SLEEP'))
loadFilePath = "/db_script/mysql_lock_query_2.sql"

# host = "10.10.43.105"
# port = 31302
# dbname = "tpcc"
# user = "root"
# password = "root"
# sleeptime = 5
# loadFilePath = "mysql_lock_query_2.sql"

print('---------------------')
print('host: ' + host)
print('port: ' + str(port))
print('dbname: ' + dbname)
print('user: ' + user)
print('password: ' + password)
print('sleep: ' + str(sleeptime))
print('---------------------')

loadQueryList = []
count = 0

querys = open(loadFilePath, 'r')
loadQueryList = querys.read().split(';')
querys.close()

while True:
    if count > 3:
        querys = open(loadFilePath, 'r')
        loadQueryList = querys.read().split(';')
        querys.close()
        count = 0

    try:
        connection = pymysql.connect(
            host=host, database=dbname, user=user, password=password, port=port)
        connection.autocommit = True

        cur = connection.cursor()
        for query in loadQueryList:
            query = query.strip()
            if query != '':
                print(query)
                cur.execute(query)
                time.sleep(1)
                print('---------------------')
        cur.close()
        connection.close()
    except:
        print('Error')
    time.sleep(sleeptime)
    count = count + 1
    print('---------------------')