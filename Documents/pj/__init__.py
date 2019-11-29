from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import pymysql 

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.89.117.205/flasklessonsql'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'jRo3rAZu1egplp6bmh6q8IuUjifoTriP'

from application import routes 