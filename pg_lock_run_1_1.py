import psycopg2
import time
import os
import random

host = os.environ.get('PG_DB_HOST')
port = int(os.environ.get('PG_DB_PORT'))
dbname = os.environ.get('PG_DB_NAME')
user = os.environ.get('PG_DB_USER')
password = os.environ.get('PG_DB_PASSWD')
sleeptime = int(os.environ.get('PG_SLEEP'))
locktime = int(os.environ.get('PG_LOCK_TIME'))
lockFilePath = "/db_script/pg_lock_query_1.sql"


# host = "10.10.43.105"
# port = 32233
# dbname = "manager"
# user = "postgres"
# password = "root"
# sleeptime = 5
# locktime = 60
# lockFilePath = "pg_lock_query_1.sql"

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
        connection = psycopg2.connect(
            host=host, dbname=dbname, user=user, password=password, port=port)
        connection.autocommit = False

        for query in lockQueryList:
            query = query.strip()
            if query != '':
                cur = connection.cursor()
                print(query)
                cur.execute(query)
                time.sleep(random.randrange(1,locktime))
                print('Rollback')
                connection.rollback()
                cur.close()
                print('---------------------')

        connection.close()
        time.sleep(random.randrange(1,sleeptime))
    except:
        print('Error')
        if cur != None:
            cur.close()
        if connection != None:
            connection.close()
    count = count + 1
    print('---------------------')