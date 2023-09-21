import pymysql
import time
import os

host = os.environ.get('MYSQL_DB_HOST')
port = int(os.environ.get('MYSQL_DB_PORT'))
dbname = os.environ.get('MYSQL_DB_NAME')
user = os.environ.get('MYSQL_DB_USER')
password = os.environ.get('MYSQL_DB_PASSWD')
sleeptime = int(os.environ.get('MARIA_SLEEP'))
initFilePath = "/db_script/mysql_init_query.sql"
loadFilePath = "/db_script/mysql_load_query.sql"

# host = "10.10.43.105"
# port = 31302
# dbname = "tpcc"
# user = "root"
# password = "root"
# sleeptime = 5
# initFilePath = "mysql_init_query.sql"
# loadFilePath = "mysql_load_query.sql"

print('---------------------')
print('host: ' + host)
print('port: ' + str(port))
print('dbname: ' + dbname)
print('user: ' + user)
print('password: ' + password)
print('sleep: ' + str(sleeptime))
print('---------------------')

initQueryList = []
loadQueryList = []
count = 0

querys = open(initFilePath, 'r')
initQueryList = querys.read().split(';')
querys.close()
querys = open(loadFilePath, 'r')
loadQueryList = querys.read().split(';')
querys.close()

try:
    connection = pymysql.connect(
        host=host, database='mysql', user=user, password=password, port=port)
    connection.autocommit = True

    cur = connection.cursor()
    for query in initQueryList:
        query = query.strip()
        if query != '':
            print(query)
            cur.execute(query)
            time.sleep(1)
    cur.close()
    connection.close()
except:
    print('Error')
time.sleep(sleeptime)

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
        cur.close()
        connection.close()
    except:
        print('Error')
    time.sleep(sleeptime)
    count = count + 1
    print('---------------------')