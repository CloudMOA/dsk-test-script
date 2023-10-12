import mariadb
import time
import os

host = os.environ.get('MARIA_DB_HOST')
port = int(os.environ.get('MARIA_DB_PORT'))
dbname = os.environ.get('MARIA_DB_NAME')
user = os.environ.get('MARIA_DB_USER')
password = os.environ.get('MARIA_DB_PASSWD')
sleeptime = int(os.environ.get('MARIA_SLEEP'))
initFilePath = "/db_script/maria_init_query.sql"
loadFilePath = "/db_script/maria_load_query.sql"

# host = "10.10.43.105"
# port = 31305
# dbname = "tpcc"
# user = "root"
# password = "root"
# sleeptime = 5
# initFilePath = "maria_init_query.sql"
# loadFilePath = "maria_load_query.sql"

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
    connection = mariadb.connect(
        host=host, database='mysql', user=user, password=password, port=port)
    connection.autocommit = True

    cur = connection.cursor()
    for query in initQueryList:
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
    if cur != None:
        cur.close()
    if connection != None:
        connection.close()
time.sleep(sleeptime)

while True:
    if count > 3:
        querys = open(loadFilePath, 'r')
        loadQueryList = querys.read().split(';')
        querys.close()
        count = 0

    try:
        connection = mariadb.connect(
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
        if cur != None:
            cur.close()
        if connection != None:
            connection.close()
    time.sleep(sleeptime)
    count = count + 1
    print('---------------------')