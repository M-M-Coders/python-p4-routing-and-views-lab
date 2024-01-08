from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f'<h1>{title}</h1>' 

@app.route('/print/<string:param>')
def print_string(param):
    print(f'print in console:  {param}')
    return param

@app.route('/count/<int:interger>')
def count(interger):
    count = f""
    for i in range(interger):
        count += f'{i}\n'
    return count