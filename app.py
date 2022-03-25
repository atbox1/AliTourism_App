from curses import meta
import string
from flask import Flask, redirect, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import true
from flask_wtf import FlaskForm
from wtforms import StringField, validators, form, HiddenField
from wtforms.validators import DataRequired
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView




#from flask_mysqldb import MySQL

app = Flask(__name__)
pymysql.install_as_MySQLdb()

app.config['SECRET_KEY'] = 'dont-reveal-this-a-scret.'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@127.0.0.1/tourism_app_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/Ali/Documents/School/2022/Digital Soloution/Unit 3/Term 1/Assignment/Code/tourism_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

db = SQLAlchemy(app)
admin = Admin(app, name='tourism app db ', template_mode='bootstrap3')
bootstrap = Bootstrap(app)
admin_crud_link = 'http://127.0.0.1:5000/admin/tourism_data/'

class Tourism_Data(db.Model):
    img = db.Column(db.String(255))
    name = db.Column(db.String(60), unique=True)
    full_adress = db.Column(db.String(200), unique=True)
    state = db.Column(db.String(3))
    website = db.Column(db.String(600))
    phone_number = db.Column(db.Integer, unique=True, primary_key=True)
    senior_discount = db.Column(db.Text(35))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    def __init__(self, img, name, full_adress, state, website, phone_number, senior_discount, latitude, longiltude):
        #self.img = img
        self.name = name
        #self.full_adress = full_adress
        #self.state = state
        #state.website = website
        self.phone_number = phone_number
        #self.senior_discount = senior_discount
        #self.latitude = latitude
        #self.longitude = longitude

class Report_Issues_Table(db.Model):
    Problem_Identifer = db.Column(db.Integer, unique=True, primary_key=True)
    Problem_Date = db.Column(db.DateTime)
    Problem = db.Column(db.String(60))
    Problem_Description = db.Column(db.String(255))
    Link_To_Problem = db.Column(db.Text(255))
    
    #def __init__(self, Problem_Identifer, Problem, Problem_Description, Link_To_Problem):
 
        #self.Problem_Identifer = Problem_Identifer
        #self.Problem = Problem
        #self.Problem_Description = Problem_Description
        #self.Link_To_Problem = Link_To_Problem
    

class SearchForm(FlaskForm):
    searched = StringField("searched", validate=[DataRequired()])
    submit = StringField("Submit")

class Report_IssueForm(FlaskForm):
    Problem_Date = HiddenField()
    problem_type = StringField('Problem', [validators.Length(min =4, max = 50)])
    Problem_Description = StringField('Problem Description', [validators.Length(min =4, max = 50)])
    Link_To_Problem = StringField('Link to Problem', [validators.Length(min =4, max = 50)])
    
admin.add_view(ModelView(Tourism_Data, db.session))
admin.add_view(ModelView(Report_Issues_Table, db.session))

@app.route("/")
def index():
    return render_template('index.html', admin_crud_link = admin_crud_link)

@app.route("/popular_location")
def Popular_Location():
    tourism_datas = Tourism_Data.query.all() 
    image_link = url_for('static', filename = 'assets/images/google_maps_api_places/location_image')
    return render_template('popular_location_v2.html', tourism_datas=tourism_datas, image_link = image_link )

@app.route('/popular_location/<phone_number>')
def Location_Card(phone_number):
    tourism_data = Tourism_Data.query.filter_by(phone_number=phone_number).first()  
    image_link = url_for('static', filename = 'assets/images/google_maps_api_places/location_image')
    return render_template('location_card.html', tourism_data=tourism_data, image_link = image_link )

@app.route('/report_problem_form', methods=['GET', 'POST'])
def Issue_Reporter_Form():
    form = Report_IssueForm()
    if form.validate_on_submit():
        report = Report_Issues_Table( Problem = form.problem_type.data, Problem_Description = form.Problem_Description.data, Link_To_Problem = form.Link_To_Problem.data)
        db.session.add(report)
        db.session.commit()
        return redirect(url_for('Popular_Location'))
    return render_template('report_form.html', form=form)

#@app.route('/search', methods=['GET', 'POST'])
#def search():
    form = SearchForm()
    tourism_data = Tourism_Data.query
    #if form.validate_on_submit():
        #searched = form.searched.data
        #tourism_data = tourism_data.filter(Tourism_Data.content.like('%' + searched + '%'))
        #return render_template('location-search.html', searched = searched, form = form)

if name == 'main':

app.run(debug=True)



