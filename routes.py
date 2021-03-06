__author__ = 'alisonbnt'

from app import app
from flask import request, session, redirect, flash, url_for, render_template

from models import *

def set_routes():

    @app.route('/')
    def index():
        quotes = Quote.objects.all()
        return render_template('index.html', quotes=quotes)

    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     error = None
    #     if request.method == 'POST':
    #         if request.form['username'] != app.config['USERNAME']:
    #             error = 'Invalid username'
    #         elif request.form['password'] != app.config['PASSWORD']:
    #             error = 'Invalid password'
    #         else:
    #             session['logged_in'] = True
    #             flash('You were logged in')
    #             return redirect(url_for('show_entries'))
    #     return render_template('login.html', error=error)
