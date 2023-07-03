import psycopg2

host = '10.10.43.100'
dbname = 'manager'
user = 'postgres'
password = 'root'
port = 32233

connection = psycopg2.connect(host=host, dbname=dbname,user=user,password=password,port=port)
cur = connection.cursor()

querys = open('query.sql', 'r')
queryList = querys.read().split(';')
for query in queryList:
    cur.execute(query.trim())

cur.close()
connection.close()