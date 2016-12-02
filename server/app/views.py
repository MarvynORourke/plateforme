from flask import Flask, render_template, request, redirect, url_for, abort, session, send_from_directory, send_file
from werkzeug import secure_filename
from app import app
from time import time
from os import listdir, remove, getcwd
from controllers import *

import io
import random
import unicodedata

import db

@app.route('/<filename>', methods=['GET'])
def redirection_de_gros_porc(filename):
    return redirect(url_for('static', filename=filename))




@app.route('/upload', methods=['POST'])
def upload_page():
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    nom_doc = request.args.get('nom_doc')
    course = request.args.get('course')
    
    if check_user_connection(user_name, password):
        user_id = get_id_user(user_name, password)
        add_course(user_id, nom_doc, course)

    
    





