# Modules
from flask import Flask, redirect, request, session, render_template, jsonify
from flask_assets import Environment, Bundle
import sys, os
from datetime import date
from random import randint

app = Flask(__name__)
app.config[ "DEBUG" ] = True
assets = Environment(app)

# Routes
sys.path.append(  os.getcwd()  +  '/cs50x/'   )
from main_routes import routes
app.register_blueprint(routes)

from tools_routes import tools
app.register_blueprint(tools, url_prefix='/tools')


# DATA
sys.path.append(  os.getcwd()  +  '/cs50x/data/'   )
from events import *
from info import *


js = Bundle('./js/script.js',
            output='gen/scripts.js')
assets.register('js_all', js)

css = Bundle('./styles/base.css', './styles/style.css',
            output='gen/styles.css')
assets.register('css_all', css)


@app.route('/')
def home():
    today = date.today()
    thisYear = date.today().strftime("%Y")

    return render_template('index.html',
        title="Home",
        events=sessions, today=today,
        thisYear=thisYear,
        staff=theStaff
    )



if __name__ == "__main__":
    app.run()