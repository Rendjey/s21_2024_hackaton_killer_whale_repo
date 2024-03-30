import psycopg2
from termcolor import colored
from flask import Flask, request

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

@app.route("/registration/", methods=['POST'])
def registration():
    request_data = request.json
    nickname = request_data['username']
    pdata = {
        "status": "ok",
        "username": str(nickname),
    }
    message = colored("nickname", "light_green") + " : " + colored(nickname, "light_blue") + "\n"
    print(message)
    return pdata