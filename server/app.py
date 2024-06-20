from flask import Flask, redirect
from flask_cors import CORS

app = Flask(__name__)
# Comment the below line to disable CORS
CORS(app)

@app.get('/')
def root():
    return redirect('/static/index.html')

@app.get('/api/message')
def generate_message():
    return {'message': 'hello, world'}

if __name__ == '__main__':
    app.run(host='localhost', port=8080)