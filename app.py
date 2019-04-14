
#__author__ == "Jackie Cohen (jczetta)"

import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_songs.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

##### Set up Models #####

# TODO: relationships to set up
# One to many: each Car has only one EngineType, each engine type may be associated with many cars
# One to many: each car has one make, each make may be associated with many cars

class Car(db.Model):
    pass # To fill in based on data to store

class Make(db.Model):
    pass # To fill in based on data to store
    # Do I have all the data I migt want for a car make right now? Maybe not now, but start simple.

class EngineTypes(db.Model):
    pass # To fill in based on data to store
