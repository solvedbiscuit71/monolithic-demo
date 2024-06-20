import sqlite3
from flask import Flask, redirect
from flask_cors import CORS

app = Flask(__name__)
# Comment the below line to disable CORS
CORS(app)

# SQLite 3
con = sqlite3.connect('demo.db')
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
    con = sqlite3.connect('demo.db')
    cur = con.cursor()
    count, = cur.execute('select count from counter where id = 1').fetchone()
    count += 1
    cur.execute('update counter set count = ? where id = 1', (count,))
    con.commit()
    con.close()
    return {'message': 'hello, world', 'count': count}

if __name__ == '__main__':
    app.run(host='localhost', port=8080)