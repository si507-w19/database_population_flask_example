
#__author__ == "Jackie Cohen (jczetta)"

import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
from db_populate import * # Import all tools available in db_populate file that I've created and saved in this directory

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./cars_sample.db' # TODO: decide what your new database name will be -- that has to go here
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
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    # make reference will come from a backref on make - cars
    automatic_transmission = db.Column(db.Boolean)
    city_mpg = db.Column(db.Integer)
    highway_mpg = db.Column(db.Integer)
    driveline = db.Column(db.String(250))
    horsepower = db.Column(db.Integer) # Decided based on data -a\ always integer here - string also reasonable
    year_release = db.Column(db.Integer) # reasonable to use a special date/datetime type in appropriate way if needed more detail, but will only ever need a year here, and null is possible


class Make(db.Model):
    __tablename__ = "makes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250)) # name of make e.g. Audi
    # Might add more info later -- but for now this is fine
    # (this is why db org like this is important, because now adding detail about a make -- e.g. original name of inventor! active for purchase since... ? etc is reasonable and easily doable)
    cars = db.relationship('cars', backref='make') # remember one to many relationship -- a make can be related to many cars
    # Backref -- so should be able to do <a car inst>.make ...


class EngineType(db.Model):
    __tablename__ = "enginetypes"
    id = db.Column(db.Integer, primary_key=True)
    # Basing this, in this case, on info available in specific dataset
    # But I can imagine this being an item I'd want to add more data to later as well -- although for now it isn't as complicated as e.g. students, universities...
    name = db.Column(db.String(250))
    # And each engine type may have many cars, but each car has one
    cars = db.relationship('cars', backref="enginetype") # Same as seen in Make model - relationship setup


if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
