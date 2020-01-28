# Modules
from flask import Flask, redirect, request, session, render_template, jsonify, Blueprint
import sys, os
from datetime import date
routes = Blueprint('routes', __name__)

# DATA
sys.path.append(  os.getcwd()  +  '/cs50x/data/'   )
from course import *
from events import *
from info import *
from media import *
from psets import *
from activities import *
from sections import *
from libs import *


theLectures = lectures
theActivities = activities
theWeeks = weeks.items()
thePsets = psets.items()
today = date.today()


@routes.route('/education')
def education():
    return render_template('education.html', title="Education")

@routes.route('/welcome')
def welcome():
    return render_template(
        'welcome.html', title="Welcome",
        intro_vid=siteVideos['intro'],
        cohort=current_cohort,
        prep_vids=siteVideos['cs50prep']
    )

@routes.route('/syllabus')
def syllabus():
    return render_template('syllabus.html',
        title="Syllabus",
        staff=theStaff,
        weeks=theWeeks,
        psets=thePsets,
        today=today
    )

@routes.route('/lectures')
def lectures():
    return render_template('lectures.html', title="Lectures", weeks=theWeeks, today=today)

@routes.route('/lecture/<num>')
def lecture(num):
    lecture = theLectures[num]
    return render_template('lecture.html',
        title=lecture['title'],
        lecture=lecture,
        lectures=theLectures.items(),
        page=int(num)
    )

@routes.route('/activity/<id>')
def activity(id):
    activity = theActivities[id]
    return render_template('activity.html', title=activity['title'], activity=activity)

@routes.route('/videos')
def videos():
    return render_template('videos.html', title="Videos")

@routes.route('/masterclass')
def masterclass():
    return render_template('masterclass.html', title="CS50 Masterclass")

@routes.route('/registration')
def registration():
    return render_template('registration.html', title="Self-Registration Guide")

@routes.route('/resources')
def resources():
    return render_template('resources.html', title="Resources")

@routes.route('/after_cs50')
def after_cs50():
    return render_template('after_cs50.html', title="After CS50")

@routes.route('/login')
def login():
    return render_template('login.html', title="Login")

@routes.route('/alumni')
def alumni():
    return render_template('/alumni.html', title="Alumni")

@routes.route('/verification')
def verification():
    return render_template('/verification.html', title="Verification")
