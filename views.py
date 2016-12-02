from flask import Flask, render_template, request, redirect, url_for, abort, session, send_from_directory, send_file
from werkzeug import secure_filename
from app import app
from time import time
from os import listdir, remove, getcwd
from controllers import *

import io
import random
import unicodedata

@app.route('/login', methods=['POST'])
def index_page():
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    if check_user_connection(user_name, password)
    





