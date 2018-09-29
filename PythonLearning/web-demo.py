from flask import Flask, request, render_template,json

import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
           
    
@app.route('/post', methods=['POST'])
def post():
    data = request.get_data()
    f = open("received.txt", "a")
    try:
        f.write(data)
        f.write("\r\n")
    finally:
        f.close()

    return "OK"

@app.route('/get', methods=['GET'])
def get():
    b = request.args.get('sim')
    print b
    return b
    
@app.route('/show', methods=['GET'])
def show():
    data = request.get_data()
    f = open("received.txt", "r")
    try:
        data = f.read(-1)
    finally:
        f.close()
    return data
    
if __name__ == "__main__":
    #http
    app.run('0.0.0.0', debug=True, port=5000)