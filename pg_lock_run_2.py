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
loadFilePath = "/db_script/pg_lock_query_2.sql"

# host = "10.10.43.105"
# port = 32233
# dbname = "manager"
# user = "postgres"
# password = "root"
# sleeptime = 5
# loadFilePath = "pg_load_query.sql"

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
        connection = psycopg2.connect(
            host=host, dbname=dbname, user=user, password=password, port=port)
        connection.autocommit = True

        cur = connection.cursor()
        for query in loadQueryList:
            query = query.strip()
            if query != '':
                print(query)
                cur.execute(query)
                time.sleep(random.randrange(1,5))
                print('---------------------')
        cur.close()
        connection.close()
    except:
        print('Error')
        if cur != None:
            cur.close()
        if connection != None:
            connection.close()
    time.sleep(random.randrange(1,sleeptime))
    count = count + 1
    print('---------------------')