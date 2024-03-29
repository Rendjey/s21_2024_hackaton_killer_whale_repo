import re
import random
import psycopg2
from termcolor import colored
from flask import Flask, render_template, request


app = Flask(__name__)

if __name__ == '__main__':
	app.run(host='0.0.0.0')

def get_db_connection():
    conn = psycopg2.connect(dbname='hack_db', user='tester', password='tester', host='localhost')
    conn.autocommit = True
    return conn

@app.route("/")
def home():
    pdata = {
        "status": "ok",
    }
    return pdata
