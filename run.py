import psycopg2
import time
import os

host = os.environ.get('DB_HOST')
port = int(os.environ.get('DB_PORT'))
dbname = os.environ.get('DB_NAME')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWD')

print('---------------------')
print('host: ' + host)
print('port: ' + str(port))
print('dbname: ' + dbname)
print('user: ' + user)
print('password: ' + password)
print('---------------------')
queryList = []
count = 0
while True:
    try:
        if count % 100 == 0:
            querys = open('query.sql', 'r')
            queryList = querys.read().split(';')
            querys.close()
            count = 0
        connection = psycopg2.connect(
            host=host, dbname=dbname, user=user, password=password, port=port)
        cur = connection.cursor()
        for query in queryList:
            query = query.strip()
            if query != '':
                print(query)
                cur.execute(query)
                time.sleep(1)
        cur.close()
        connection.close()
        time.sleep(10)
    except:
        print('Error')
        break
    count = count + 1
    print('---------------------')