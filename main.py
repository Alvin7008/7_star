import flask
from flask import Flask, render_template, request, url_for, jsonify, make_response, flash,session
from flask_mysqldb import MySQL
import hashlib
from flask_login import login_manager, UserMixin, login_user, login_required, logout_user, current_user

# Create a flask instance
app = Flask(__name__)

# Secert key for forms
app.config['SECRET_KEY'] = "This is my secret key"

# Adding Database Config
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/seven_stars'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Prince1988'
app.config['MYSQL_DB'] = 'seven_stars'
mysql = MySQL(app)





# Page not found
@app.errorhandler(404)
def page_not_found(e):
    if (session.get('empno') != None):
        return render_template("404.html"), 404
    else:
        return flask.redirect('/')


# Server error page
@app.errorhandler(500)
def page_not_found(e):
    if (session.get('empno') != None):
        return render_template("500.html"), 500
    else:
        return flask.redirect('/')


# home page
@app.route('/')
def home():
    return render_template("login.html")


# Rental Agreement Form
@app.route('/rentalAgree', methods=['POST', 'GET'])
def rentalAgreemnet():
    if (session.get('empno') != None):
        return render_template('rental_agreement_form.html')
    else:
        return flask.redirect('/')


@app.route('/getvehicle', methods=['POST', 'GET'])
def getVehicleType():
    if (session.get('empno') != None):

        # Search String
        queryString = request.form['queryString']

        # print(queryString)

        # Creating a connection cursor
        cursor = mysql.connection.cursor()
        cursor.execute('''select * from vehicletype WHERE vehtype LIKE '{}%' LIMIT 5 '''.format(queryString))
        vehdata = list(cursor.fetchall())
        vehlist = []

        for vehdatas in vehdata:
            vehlist.append(vehdatas[1])

        # Saving the Actions performed on the DB
        mysql.connection.commit()

        # Closing the cursor
        cursor.close()

        # print(vehlist)
        # print(len(vehlist))

        response = jsonify({'htmlresponse': render_template('response.html', vehdata=vehlist)})

        return response

    else:
        return flask.redirect('/')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if (session.get('empno') != None):

        salt = "5gz"
        name = request.form['name']
        email = request.form['emailid']
        empno = request.form['empno']
        password = str(request.form['pass1']) + salt
        hashedpass = hashlib.md5(password.encode())
        db_password = hashedpass.hexdigest()

        # print(name + "  " + email + "   " + empno + "  " + db_password)

        # Creating a connection cursor
        cursor = mysql.connection.cursor()
        cursor.execute('''select max(id) as id from users ''')

        id = cursor.fetchone()

        if(id[0] is None):
            cursor.execute('''insert into users (id,name,empno,email,password,createdon) values(%s,%s,%s,%s,%s,now())''',
                           (1001, name, empno, email, db_password))

        else:
            cursor.execute('''insert into users (name,empno,email,password,createdon) values(%s,%s,%s,%s,now())''', (name,
                                                                                                                     empno,
                                                                                                                     email,
                                                                                                                     db_password))

        # Saving the Actions performed on the DB
        mysql.connection.commit()

        # Closing the cursor
        cursor.close()

        flash("User Created Successfully")

        return render_template("login.html")
    else:
        return flask.redirect('/')


@app.route('/userauth', methods=['POST','GET'])
def userauthentication():

        salt = "5gz"
        # name = request.form['name']
        # empno = request.form['empno']
        empno = request.form['empnologin']
        password = str(request.form['password']) + salt
        hashedpass = hashlib.md5(password.encode())
        db_password = hashedpass.hexdigest()

        # Creating a connection cursor
        cursor = mysql.connection.cursor()
        cursor.execute('''select * from users where empno=%s and password=%s''',(empno,db_password))

        chk = cursor.rowcount

        # Saving the Actions performed on the DB
        mysql.connection.commit()

        # Closing the cursor
        cursor.close()

        if(chk>0):
            session['empno'] = empno
            return render_template('home.html')
        else:
            flash("Warning!!!  Invalid user!!!")
            return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('empno',None)
    return render_template('login.html')


@app.route('/driverdetails')
def driverdetails():

    if(session.get('empno')!=None):
        return render_template('driver_details.html')
    else:
        return flask.redirect('/')



@app.route('/savedriverdetails', methods=['POST', 'GET'])
def savedriver():
    if (session.get('empno') != None):

        name = request.form['dname']
        emid = request.form['emid']
        licno = request.form['licno']
        emidval = request.form['emidvalidity']
        licsdate = request.form['licsdate']
        licedate = request.form['licedate']
        passno = request.form['passportno']
        pvalidity = request.form['passportval']
        sponname = request.form['sponsorname']


        # Creating a connection cursor
        cursor = mysql.connection.cursor()
        cursor.execute('''select max(id) as id from driver_details ''')

        id = cursor.fetchone()

        if(id[0] is None):
            cursor.execute('''insert into driver_details (id,name,empno,email,password,createdon) values(%s,%s,%s,%s,%s,now())''',
                           (1001, name, ))
        else:
            cursor.execute('''insert into driver_details (name,empno,email,password,createdon) values(%s,%s,%s,%s,now())''', (name,
                                                                                                                     ))


        # Saving the Actions performed on the DB
        mysql.connection.commit()

        # Closing the cursor
        cursor.close()

        flash("User Created Successfully")

        return render_template("login.html")
    else:
        return flask.redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
