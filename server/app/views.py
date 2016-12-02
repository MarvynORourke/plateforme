from flask import Flask, render_template, request, redirect, url_for, abort, session, send_from_directory, send_file
from werkzeug import secure_filename
from app import app
from time import time
from os import listdir, remove, getcwd
from controller import *

import io
import random
import unicodedata 

import db

@app.route('/ecourt/<filename>', methods=['GET'])
def redirection_de_gros_porc(filename):
    return redirect(url_for('static', filename=filename))


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    nom_doc = request.args.get('nom_doc')
    course = request.args.get('course')
    
    if db.check_user_connection(user_name, password):
        user_id = db.get_id_user(user_name, password)
        return "Course id : ", add_course(user_id, nom_doc, course)

    return "FAILED TO UPLOAD... :'("

@app.route('/', methods=['GET']) 
@app.route('/register', methods=['GET'])    
def register_page():
    return redirect(url_for('static', filename="register.html"))

@app.route('/register', methods=['POST'])
def register_action():
    #register the guy...
    user_name = request.form['login']
    password = request.form['password']

    db.add_user(user_name, password)
    
    return redirect(url_for('static', filename='ecourt_template.html'))







