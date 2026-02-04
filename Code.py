from Fask import Flask, render_templete, request, redirect, url_for, session, flash 
from flask_sqlalchemy import SQLAlchemy
from workzeug.security import generate_password_hash, check_password_hash
from dataetime import datetime  

#app configurations from sir

app = Flask(__name__)
app.secret_key = "supersecretkey" #will be changed this is just code from sir to start of with
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tastetracker_ps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) 

#data base modules also from sir
