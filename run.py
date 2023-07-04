import psycopg2
import time

host = '10.10.43.100'
dbname = 'manager'
user = 'postgres'
password = 'root'
port = 32233

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