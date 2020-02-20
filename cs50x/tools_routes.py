# Modules
from flask import Flask, redirect, request, session, render_template, jsonify, Blueprint, url_for
import sys, os
from datetime import date
from random import randint
tools = Blueprint('tools', __name__)


# DATA
sys.path.append(  os.getcwd()  +  '/cs50x/data/'   )
from activities import *
from libs import *

theChallenges = challenges


@tools.route('/')
def cs50_tools():
    tools = {
        'Birary Tool': url_for('tools.binary_tool'),
        'Random Tasks': url_for('tools.random_task')
        # 'Test Assesment: 1': url_for('tools.random_task')
    }
    return render_template('/tools/index.html', title="Challenges", tools=tools, challenges=theChallenges)

@tools.route('/random_task')
def random_task():
    random_task = "Artboard – "+str(randint(1,3))
    return render_template('/tools/random_task.html', title="Random Task", random_task=random_task)


@tools.route('/assessment/')
def assessment():
    return render_template('/tools/assessment.html', title="Assessment")


@tools.route('/challenge/<id>')
def challenge(id):
    challenge = theChallenges[id]
    return render_template('/tools/challenge.html', title=challenge['title'], challenge=challenge)


@tools.route('/spy_submission', methods=["POST"])
def spy_submission():
    return jsonify(  spydecoder( request.form['level'], request.form['code'] )  )

@tools.route('/binary_tool')
def binary_tool():
    bit = request.args.get('bit') or 8

    return render_template(
        '/tools/binary_tool.html',
        title="Binary Tool",
        bit=bit
    )

@tools.route('/find_ascii', methods=["POST"])
def find_ascii():
    a = int(request.form['ascii'])
    char = False
    if a in ascii:
        char = ascii[a]
    return jsonify( char )