from flask import Flask, request, render_template,json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
           
    
@app.route('/post', methods=['POST'])
def post():
    data = request.get_data()
    with open("received.txt", "a") as f:
        f.write(data + "\n")
    return "OK"

@app.route('/get', methods=['GET'])
def get():
    b = request.args.get('sim')
    print(b)
    return b
    
@app.route('/show', methods=['GET'])
def show():
    data = request.get_data()
    with open("received.txt", "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
