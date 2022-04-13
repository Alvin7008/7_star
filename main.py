from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



# Create a flask instance
app = Flask(__name__)

# Secert key for forms
app.config['SECRET_KEY']="This is my secret key"



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
    durationOfContract = None
    form = RentalAgreementForm()

    # Validate form
    if form.validate_on_submit():
        durationOfContract = form.durationOfContract.data
        form.durationOfContract.data = ''

    return render_template('rental_agreement_form.html', durationOfContract=durationOfContract, form=form)



# Rental Agreement Form Class
class RentalAgreementForm(FlaskForm):
    durationOfContract =  StringField("Duration Of Contract", validators=[DataRequired()],)
    # purchaseOrder =  StringField("PO Number", validators=[DataRequired()],)
    # raNo =  StringField("Rental Agreement Number", validators=[DataRequired()],)
    # vehNo =  StringField("Vehicle Number", validators=[DataRequired()],)
    # vehType =  StringField("Vehicle Type", validators=[DataRequired()],)
    # startDate =  StringField("Start Date", validators=[DataRequired()],)
    # endDate =  StringField("End Date", validators=[DataRequired()],)
    # payementTerms =  StringField("Payment Terms", validators=[DataRequired()],)
    # modeOfpay =  StringField("Mode of Payment", validators=[DataRequired()],)
    # advPay =  StringField("Advance Payment", validators=[DataRequired()],)
    # receiptNo =  StringField("Receipt Number", validators=[DataRequired()],)
    # timeOut =  StringField("Time Out", validators=[DataRequired()],)
    # timeIn =  StringField("Time In", validators=[DataRequired()],)
    # kmOut =  StringField("Km Out", validators=[DataRequired()],)
    # kmIn =  StringField("Km In", validators=[DataRequired()],)
    # kmAgreed =  StringField("Km Agreed", validators=[DataRequired()],)
    # termofAgremnt =  StringField("Term Of Agreement", validators=[DataRequired()],)
    # kmDriven =  StringField("Km Driven", validators=[DataRequired()],)

    # vehType =  StringField("Vehicle", validators=[DataRequired()],)
    submit = SubmitField("Submit")
