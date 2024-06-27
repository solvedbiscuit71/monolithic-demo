import os
import sqlite3
from flask import Flask, redirect
from flask_cors import CORS

app = Flask(__name__)
# Comment the below line to disable CORS
CORS(app)

# volume mount in docker (for data persistent)
if not os.path.exists('data/'):
    os.makedirs('data/')

# SQLite 3
con = sqlite3.connect('data/sqlite.db')
cur = con.cursor()
try:
    cur.execute('create table if not exists counter ( id integer primary key, count integer )')
    if cur.execute('select count from counter where id = 1').fetchone() is None:
        cur.execute('insert into counter values (1, 0)')
    con.commit()
    con.close()
except sqlite3.OperationalError:
    print("Operation Failed")
except:
    print("Unknown Error")

@app.get('/')
def root():
    return redirect('/static/index.html')

@app.get('/api/message')
def generate_message():
    con = sqlite3.connect('data/sqlite.db')
    cur = con.cursor()
    count, = cur.execute('select count from counter where id = 1').fetchone()
    count += 1
    cur.execute('update counter set count = ? where id = 1', (count,))
    con.commit()
    con.close()
    return {'message': 'hello, docker', 'count': count}