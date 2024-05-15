from flask import Flask, redirect
from flask_cors import CORS

FRONTEND_ORIGIN='http://localhost:5001/'

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origin": [FRONTEND_ORIGIN]}})

@app.get('/')
def root():
    return redirect('/static/index.html')

@app.get('/api/message')
def generate_message():
    return {'message': 'hello, world'}

if __name__ == '__main__':
    app.run(host='localhost', port=5000)