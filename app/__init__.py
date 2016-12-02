from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
app.config['DEBUG'] = True

from app import views
