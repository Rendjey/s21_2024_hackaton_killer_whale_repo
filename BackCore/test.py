import psycopg2
import re

conn = psycopg2.connect(dbname='hack_db', user='tester', password='tester', host='localhost')
conn.autocommit = True
cur = conn.cursor()

cur.execute('SELECT * FROM user')
pr = cur.fetchall()
print (pr)

print("-------user-------")

cur.close()
conn.close()