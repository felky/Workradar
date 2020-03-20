from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world(name = "Woogbar"):
    return render_template('index.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return proceed_login()
    else:
        return login_form()

def login_form():
    return "Login form"

def proceed_login():
    return "Logged in"


@app.route('/about')
def info(): 
    return "workradar is built on Flask"