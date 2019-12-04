from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import DateTime
from datetime import datetime

DB_URL = 'postgres://skywalker:password@localhost:5432/simple_app'

class Config(object):
  SQLALCHEMY_DATABASE_URI = DB_URL
  SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)



profiles = [
  {
    "name": "Rico",
    "designation": "Amory",
    "temperament": "Razz"
  },
  {
    "name": "Skipper",
    "designation": "Commander",
    "temperament": "Calm"
  },
  {
    "name": "Kowalski",
    "designation": "Tech support",
    "temperament": "Calm"
  }
]


class ProfileModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  designation = db.Column(db.String(), nullable=False)
  temperament = db.Column(db.String(), nullable=False)
  created_at =  db.Column(DateTime, default=datetime.utcnow)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/profiles')
def lists():
  return render_template('profiles.html', profiles=profiles)

@app.route('/add-profile')
def add_profile():
  new_profile = ProfileModel(
    name = 'Rico',
    designation = 'Amory',
    temperament = 'Razz'
  )
  new_profile2 = ProfileModel(
    name = 'Skipper',
    designation = 'Commander',
    temperament = 'Calm'
  )
  new_profile3 = ProfileModel(
    name = 'Kowalski',
    designation = 'Tech Support',
    temperament = 'Calm'
  )

  db.session.add(new_profile)
  db.session.add(new_profile2)
  db.session.add(new_profile3)

  db.session.commit()

  db.session.close()



  return redirect('/profiles')

if '__name__' == '__main__':
  app.run()