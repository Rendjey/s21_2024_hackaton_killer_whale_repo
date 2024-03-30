import psycopg2
from flask import Flask, request
from s21_controller_base import base_controller

app = Flask(__name__)

if __name__ == '__main__':
	app.run(host='0.0.0.0')

def get_db_connection():
    conn = psycopg2.connect(dbname='hackdb', user='tester', password='tester', host='localhost')
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
    status = 'ok'
    request_data = request.json

    try:
        username = str(request_data['username'])
        uid = str(request_data['uid'])
        if(base_controller() == True): #S21 DataBase
            role = "student"
        else:
            role = "adm" 
    except KeyError as e:
        status = 'Unidentified error'
        pdata = {"status": status}
        return pdata
 
    conn = get_db_connection()
    cur = conn.cursor()
    
    sql = "SELECT username FROM users WHERE username = %s"
    record_to_insert = (username,)
    cur.execute(sql, record_to_insert)
    pr = cur.fetchall()
    
    if(str(pr) != "[]"):
        status = {
            "status": "error",
            "description": "Имя занято"
        }
        return status

    sql = "INSERT INTO users (username, uid, role) VALUES (%s, %s, %s)"
    record_to_insert = (username, uid, role)
    cur.execute(sql, record_to_insert)
    conn.commit()

    cur.close()
    conn.close()

    pdata = {"status": "ok"}

    return pdata

@app.route("/login/", methods=['POST'])
def login():
    status = 'ok'
    request_data = request.json

    try:
        uid = str(request_data['uid'])
    except KeyError as e:
        status = 'Unidentified error'
        pdata = {"status": status}
        return pdata
 
    conn = get_db_connection()
    cur = conn.cursor()
    
    sql = "SELECT username FROM users WHERE uid = %s"
    record_to_insert = (uid,)
    cur.execute(sql, record_to_insert)
    pr = cur.fetchall()
    if(str(pr) != "[]"):
        pdata = {
            "status": "ok",
            "username": pr[0][0],
        }
    else:
        pdata = {
            "status": "error",
            "description": "Пользователь не найден"
        }
        
    return pdata
