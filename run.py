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
querys = open('query.sql', 'r')
queryList = querys.read().split(';')
while True:
    try:
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
    print('---------------------')