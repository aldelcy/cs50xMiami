from flask import Flask, redirect, request, session, render_template
from flask_assets import Environment, Bundle
import sys, os
from datetime import date

sys.path.append(  os.getcwd()  +  '/cs50x/data/'   )
import data
import events

app = Flask(__name__)
app.config[ "DEBUG" ] = True
assets = Environment(app)

js = Bundle('./js/script.js',
             output='gen/scripts.js')
assets.register('js_all', js)

css = Bundle('./styles/style.css',
             output='gen/styles.css')
assets.register('css_all', css)

theLectures = data.lectures.items()
theWeeks = data.weeks.items()
today = date.today()

@app.route('/')
def home():
    return render_template('index.html', title="Home", events=events.events, today=today)

@app.route('/education')
def education():
    return render_template('education.html', title="Education")

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title="Welcome")

@app.route('/syllabus')
def syllabus():
    return render_template('syllabus.html', title="Syllabus")

@app.route('/lectures')
def lectures():
    return render_template('lectures.html', title="Lectures", weeks=theWeeks, today=today)

@app.route('/lecture/<num>')
def lecture(num):
    lecture = data.lectures[num]
    return render_template('lecture.html', title="Lecture", lecture=lecture, lectures=theLectures, page=int(num))

@app.route('/videos')
def videos():
    return render_template('videos.html', title="Videos")

@app.route('/media')
def media():
    return render_template('media.html', title="Media")

@app.route('/registration')
def registration():
    return render_template('registration.html', title="Self-Registration Guide")

@app.route('/resources')
def resources():
    return render_template('resources.html', title="Resources")

@app.route('/after_cs50')
def after_cs50():
    return render_template('after_cs50.html', title="After CS50")

@app.route('/login')
def login():
    return render_template('login.html', title="Login")

@app.route('/alumni')
def alumni():
    return render_template('/alumni.html', title="Alumni")

@app.route('/verification')
def verification():
    return render_template('/verification.html', title="Verification")


if __name__ == "__main__":
    app.run()