import mariadb
import time
import os

host = os.environ.get('MARIA_DB_HOST')
port = int(os.environ.get('MARIA_DB_PORT'))
dbname = os.environ.get('MARIA_DB_NAME')
user = os.environ.get('MARIA_DB_USER')
password = os.environ.get('MARIA_DB_PASSWD')
sleeptime = int(os.environ.get('MARIA_SLEEP'))
lockFilePath = "/db_script/maria_lock_query.sql"

# host = "10.10.43.100"
# port = 31305
# dbname = "tpcc"
# user = "root"
# password = "root"
# sleeptime = 5
# lockFilePath = "maria_lock_query.sql"

print('---------------------')
print('host: ' + host)
print('port: ' + str(port))
print('dbname: ' + dbname)
print('user: ' + user)
print('password: ' + password)
print('sleep: ' + str(sleeptime))
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

            connection = mariadb.connect(
                host=host, database=dbname, user=user, password=password, port=port)
            connection.autocommit = False

            if query != '':
                cur = connection.cursor()
                print(query)
                cur.execute(query)
                time.sleep(60)
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