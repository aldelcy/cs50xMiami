from flask import Flask, redirect, request, session, render_template, jsonify
from flask_assets import Environment, Bundle
import sys, os
from datetime import date
from random import randint

sys.path.append(  os.getcwd()  +  '/cs50x/data/'   )
from course import *
from events import *
from info import *
from media import *
from psets import *
from activities import *
from sections import *
from libs import *

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
theActivities = activities
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
        title=lecture['title'],
        lecture=lecture,
        lectures=theLectures.items(),
        page=int(num)
    )

@app.route('/activity/<id>')
def activity(id):
    activity = theActivities[id]
    return render_template('activity.html', title=activity['title'], activity=activity)

@app.route('/random_task')
def random_task():
    random_task = "Artboard – "+str(randint(1,3))
    return render_template('random_task.html', title="Random Task", weeks=theWeeks, random_task=random_task, today=today)

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

@app.route('/spy_submission', methods=["POST"])
def spy_submission():
    return jsonify(  spydecoder( request.form['level'], request.form['code'] )  )

@app.route('/binary_tool')
def binary_tool():
    bit = request.args.get('bit') or 8

    return render_template(
        '/binary_tool.html',
        title="Binary Tool",
        bit=bit
    )

@app.route('/find_ascii', methods=["POST"])
def find_ascii():
    a = int(request.form['ascii'])
    char = False
    if a in ascii:
        char = ascii[a]
    return jsonify( char )

if __name__ == "__main__":
    app.run()