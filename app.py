from flask import Flask, render_template

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


@app.route('/sign')
def sign():
    return render_template('SignUp.html')


@app.route('/signIn')
def log():
    return render_template('SignIn.html')
