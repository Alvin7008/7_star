from flask import Flask, render_template, request, url_for, jsonify, make_response
from flask_mysqldb import MySQL

# Create a flask instance
app = Flask(__name__)

# Secert key for forms
app.config['SECRET_KEY'] = "This is my secret key"

# Adding Database Config
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/seven_stars'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'seven_stars'
mysql = MySQL(app)


# Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Server error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# home page
@app.route('/')
def home():
    return render_template("login.html")


# Rental Agreement Form
@app.route('/rentalAgree', methods=['POST', 'GET'])
def rentalAgreemnet():
    return render_template('rental_agreement_form.html')


@app.route('/getvehicle', methods=['POST', 'GET'])
def getVehicleType():
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


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    name = request.form['name']
    email = request.form['emailid']
    empno = request.form['empno']
    password = request.form['pass1']

    print(name + "  " + email + "   " + empno + "  " + password)

    # Creating a connection cursor
    cursor = mysql.connection.cursor()
    cursor.execute('''select max(id) as id from users ''')

    id = cursor.fetchone()
    print(id[0])

    if(id[0] is None):
        cursor.execute('''insert into users (id,name,empno,email,password,createdon) values(%s,%s,%s,%s,%s,now())''',
                       (1001, name, empno, email, password))

    else:
        cursor.execute('''insert into users (name,empno,email,password,createdon) values(%s,%s,%s,%s,now())''', (name,
                                                                                                                 empno,
                                                                                                                 email,
                                                                                                                 password))


    # Saving the Actions performed on the DB
    mysql.connection.commit()

    # Closing the cursor
    cursor.close()

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
