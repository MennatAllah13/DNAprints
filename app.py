from flask import Flask, render_template

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')