from flask import Flask, render_template, request
import re
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dna'

mysql = MySQL(app)


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


@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if request.method == 'POST' and 'Fname' in request.form and 'Sname' in request.form and 'Email' in request.form and 'Phone' in request.form and 'password' in request.form and 'age' in request.form:
        FirstName = request.form['Fname']
        LastName = request.form['Sname']
        email = request.form['Email']
        phone = request.form['Phone']
        password = request.form['password']
        cpassword = request.form['password2']
        age = request.form['age']
        gender = request.form['gender']

        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'

            return render_template('SignUp.html', msg=msg)

        elif re.match(r'[^@]+@[^@]+\.[^@]+', email):
            cursor.execute('SELECT * FROM user WHERE email = % s', (email))
            account = cursor.fetchone()

            if account:
                msg = 'Account already exists !'
                return render_template('SignUp.html', msg=msg)

            elif not re.match(r'[A-Za-z]+', FirstName):
                msg = 'First Name must contain only characters and numbers !'
                return render_template('SignUp.html', msg=msg)

            elif not re.match(r'[A-Za-z]+', LastName):
                msg = 'Last Name must contain only characters and numbers !'
                return render_template('SignUp.html', msg=msg)

            elif password != cpassword:
                msg = 'Password and confirm password should have the same value !'
                return render_template('SignUp.html', msg=msg)

            elif not FirstName or not LastName or not password or not email:
                msg = 'Please fill out the form !'
                return render_template('SignUp.html', msg=msg)

            else:
                cursor.execute('INSERT INTO user (FirstName, LastName, gender, password, email, phone, age, usertype_id) VALUES (% s, % s, % s, % s, % s, % s, % s, % s)',
                               (FirstName, LastName, gender, password, email, phone, age, 3))

                msg = 'You have successfully registered !'
                return render_template('Home.html', msg)

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('SignUp.html', msg)