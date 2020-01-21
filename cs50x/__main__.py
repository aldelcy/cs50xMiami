from flask import Flask, redirect, request, session, render_template
from flask_assets import Environment, Bundle
import sys, os
from datetime import date

sys.path.append(  os.getcwd()  +  '/cs50x/data/'   )
from course import *
from events import *
from info import *
from media import *

app = Flask(__name__)
app.config[ "DEBUG" ] = True
assets = Environment(app)

js = Bundle('./js/script.js',
             output='gen/scripts.js')
assets.register('js_all', js)

css = Bundle('./styles/base.css', './styles/style.css',
             output='gen/styles.css')
assets.register('css_all', css)

theLectures = lectures
theWeeks = weeks.items()
thePsets = psets.items()
today = date.today()

theStaff = staff.items()
for (i, person) in theStaff:
        person['fullname'] = person['fname'] + " " + person['lname']


@app.route('/')
def home():
    thisYear = date.today().strftime("%Y")
    
    return render_template('index.html', 
        title="Home", 
        events=sessions, today=today, 
        thisYear=thisYear,
        staff=theStaff
    )

@app.route('/education')
def education():
    return render_template('education.html', title="Education")

@app.route('/welcome')
def welcome():
    return render_template(
        'welcome.html', title="Welcome",
        intro_vid=siteVideos['intro'],
        cohort=current_cohort,
        prep_vids=siteVideos['cs50prep']
    )

@app.route('/syllabus')
def syllabus():
    return render_template('syllabus.html',
        title="Syllabus",
        staff=theStaff,
        weeks=theWeeks,
        psets=thePsets,
        today=today
    )

@app.route('/lectures')
def lectures():
    return render_template('lectures.html', title="Lectures", weeks=theWeeks, today=today)

@app.route('/lecture/<num>')
def lecture(num):
    lecture = theLectures[num]
    return render_template('lecture.html',
        title="Lecture",
        lecture=lecture,
        lectures=theLectures.items(),
        page=int(num)
    )

@app.route('/videos')
def videos():
    return render_template('videos.html', title="Videos")

@app.route('/masterclass')
def masterclass():
    return render_template('masterclass.html', title="CS50 Masterclass")

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