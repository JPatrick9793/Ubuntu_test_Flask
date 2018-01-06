import os

from flask import Flask, render_template, url_for, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
db = SQLAlchemy(app)
from myproject import models


@app.route('/', methods=['GET'])
def home():
    places = models.Places.query.all()
    if request.method == 'GET':
        return render_template('index.html', places=places)


@app.route('/create', methods=['POST'])
def create():

    if request.method == 'POST':
        # address cannot be blank
        if not (request.form['address'] == ""):
            newPlace = models.Places(address=request.form['address'],
                                     city=request.form['city'],
                                     country=request.form['country'])
            db.session.add(newPlace)
            db.session.commit()

        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()
