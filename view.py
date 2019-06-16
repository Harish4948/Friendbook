from flask import Flask,render_template,session,redirect,url_for,flash,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField
from wtforms.validators import InputRequired,Email,Length
from flask_bootstrap import Bootstrap
from db import *
app=Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] =  "pass"
class register_form(FlaskForm):
    email=StringField("Email", validators=[InputRequired(),Email(message="Invalid Email")])
    username=StringField("Username", validators=[InputRequired()])#,Length(min=4,max=16)])
    password=PasswordField("Password", validators=[InputRequired()])#,Length(min=8,max=64)])
    submit=SubmitField("Submit")

class login_form(FlaskForm):
    username=StringField("Username", validators=[InputRequired()])#,Length(min=4,max=16)])
    password=PasswordField("Password", validators=[InputRequired()])#,Length(min=8,max=64)])
    remember=BooleanField("remember me")    
    submit=SubmitField("Submit")


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['GET','POST'])
def register():
    form=register_form()
    print(form.username.data)
    if form.validate_on_submit():
        data=[form.email.data,form.username.data,form.password.data]
        db=users()
        db.register(data)
        return("Successfully Registered!")
    return render_template("register.html",form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=login_form()
    if form.validate_on_submit():
        data=[form.username.data,form.password.data]
        db=users()
        result=db.login(data)
        if result:
            return "Signin successful"
        else:
            return "Invalid username or password"

    return render_template("login.html",form=form)

@app.route("/web_posts",methods=['GET','POST'])
def web_posts():
    return render_template("posts.html")
if __name__ == "__main__":
    app.run(debug=True)