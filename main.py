from flask import Flask, render_template, request, url_for,jsonify, make_response
from flask_mysqldb import MySQL



# Create a flask instance
app = Flask(__name__)

# Secert key for forms
app.config['SECRET_KEY']="This is my secret key"

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

    return render_template("home.html")





# Rental Agreement Form
@app.route('/rentalAgree', methods=['POST','GET'])
def rentalAgreemnet():

    return render_template('rental_agreement_form.html')



@app.route('/getvehicle',methods=['POST','GET'])
def getVehicleType():

    # Search String
    queryString = request.form['queryString']

    print(queryString)

    # Creating a connection cursor
    cursor = mysql.connection.cursor()
    cursor.execute('''select * from vehicletype WHERE vehtype LIKE '{}%' LIMIT 5 '''.format(queryString))
    vehdata = list(cursor.fetchall())
    vehlist=[]

    for vehdatas in vehdata:
        vehlist.append(vehdatas[1])

    # Saving the Actions performed on the DB
    mysql.connection.commit()

    # Closing the cursor
    cursor.close()

    print(vehlist)
    print(len(vehlist))

    response = jsonify({'htmlresponse': render_template('response.html', vehdata=vehlist)})

    return response


# # Rental Agreement Form Class
# class RentalAgreementForm(FlaskForm):
#     durationOfContract =  StringField("Duration Of Contract", validators=[DataRequired()],)
#     # purchaseOrder =  StringField("PO Number", validators=[DataRequired()],)
#     # raNo =  StringField("Rental Agreement Number", validators=[DataRequired()],)
#     # vehNo =  StringField("Vehicle Number", validators=[DataRequired()],)
#     # vehType =  StringField("Vehicle Type", validators=[DataRequired()],)
#     # startDate =  StringField("Start Date", validators=[DataRequired()],)
#     # endDate =  StringField("End Date", validators=[DataRequired()],)
#     # payementTerms =  StringField("Payment Terms", validators=[DataRequired()],)
#     # modeOfpay =  StringField("Mode of Payment", validators=[DataRequired()],)
#     # advPay =  StringField("Advance Payment", validators=[DataRequired()],)
#     # receiptNo =  StringField("Receipt Number", validators=[DataRequired()],)
#     # timeOut =  StringField("Time Out", validators=[DataRequired()],)
#     # timeIn =  StringField("Time In", validators=[DataRequired()],)
#     # kmOut =  StringField("Km Out", validators=[DataRequired()],)
#     # kmIn =  StringField("Km In", validators=[DataRequired()],)
#     # kmAgreed =  StringField("Km Agreed", validators=[DataRequired()],)
#     # termofAgremnt =  StringField("Term Of Agreement", validators=[DataRequired()],)
#     # kmDriven =  StringField("Km Driven", validators=[DataRequired()],)
#
#     # vehType =  StringField("Vehicle", validators=[DataRequired()],)
#     submit = SubmitField("Submit")


if __name__ == '__main__':
    app.run(debug=True)