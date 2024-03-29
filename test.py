import psycopg2

conn = psycopg2.connect(dbname='hackdb', user='tester', password='tester', host='localhost')
conn.autocommit = True
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users')
cur.execute('CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name varchar(255), password varchar(255), role varchar(255));')

cur.execute('DROP TABLE IF EXISTS rooms')
cur.execute('CREATE TABLE IF NOT EXISTS rooms (id serial PRIMARY KEY, name varchar(255));')

cur.execute('DROP TABLE IF EXISTS meets')
cur.execute('CREATE TABLE IF NOT EXISTS meets (id serial PRIMARY KEY, room_id integer, user_id integer, start_time timestamp, end_time timestamp);')

cur.close()
conn.close()