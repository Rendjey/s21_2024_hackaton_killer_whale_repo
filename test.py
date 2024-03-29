import os
import psycopg2

conn = psycopg2.connect(dbname='test_db', user='tester', password='tester', host='localhost')

cur = conn.cursor()
