import mariadb
import time
import os

host = os.environ.get('MARIA_DB_HOST')
port = int(os.environ.get('MARIA_DB_PORT'))
dbname = os.environ.get('MARIA_DB_NAME')
user = os.environ.get('MARIA_DB_USER')
password = os.environ.get('MARIA_DB_PASSWD')
sleeptime = int(os.environ.get('MARIA_SLEEP'))
filepath1 = "/db_script/maria_query.sql"
filepath2 = "/db_script/maria_lock_query.sql"

# host = "10.10.43.100"
# port = 31305
# dbname = "tpcc"
# user = "root"
# password = "root"
# sleeptime = 5
# filepath1 = "maria_query.sql"
# filepath2 = "maria_lock_query.sql"

print('---------------------')
print('host: ' + host)
print('port: ' + str(port))
print('dbname: ' + dbname)
print('user: ' + user)
print('password: ' + password)
print('sleep: ' + str(sleeptime))
print('---------------------')

queryList = []
lockQueryList = []
count = 0

querys = open(filepath1, 'r')
queryList = querys.read().split(';')
querys.close()
querys = open(filepath2, 'r')
lockQueryList = querys.read().split(';')
querys.close()
while True:
    if count > 3:
        querys = open(filepath1, 'r')
        queryList = querys.read().split(';')
        querys.close()
        querys = open(filepath2, 'r')
        lockQueryList = querys.read().split(';')
        querys.close()
        count = 0

    try:
        connection = mariadb.connect(
            host=host, database=dbname, user=user, password=password, port=port)
        connection.autocommit = True

        cur = connection.cursor()
        for query in queryList:
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

    try:
        connection = mariadb.connect(
            host=host, database=dbname, user=user, password=password, port=port)
        connection.autocommit = False

        for query in lockQueryList:
            query = query.strip()
            if query != '':
                cur = connection.cursor()
                print(query)
                cur.execute(query)
                time.sleep(30)
                print('Rollback')
                connection.rollback()
                cur.close()
        connection.close()
    except:
        print('Error')

    time.sleep(sleeptime)
    count = count + 1
    print('---------------------')