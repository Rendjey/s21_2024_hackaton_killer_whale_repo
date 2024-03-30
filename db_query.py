import psycopg2
import re

conn = psycopg2.connect(dbname='hackdb', user='tester', password='tester', host='localhost')
conn.autocommit = True
cur = conn.cursor()

cur.execute('SELECT * FROM users')
pr = cur.fetchall()
print(pr)

print("-------rooms-------")

#cur.execute('ALTER TABLE users ADD command VARCHAR(256)') #Добавление столбца
#cur.execute('ALTER TABLE users RENAME COLUMN password TO uid;') #изменение наименования столбца

cur.close()
conn.close()