import psycopg2
import re

conn = psycopg2.connect(dbname='hackdb', user='tester', password='tester', host='localhost')
conn.autocommit = True
cur = conn.cursor()

#cur.execute('SELECT * FROM users')
username = '1'
sql = 'SELECT username FROM users WHERE username = %s'
record_to_insert = str(username)
cur.execute(sql)


pr = cur.fetchall()
print(pr)

print("-------rooms-------")

#cur.execute('ALTER TABLE rooms ADD floor INTEGER') #Добавление столбца
#cur.execute('ALTER TABLE users RENAME COLUMN password TO uid;') #изменение наименования столбца

cur.close()
conn.close()