from flask import render_template, flash, redirect
from ..scripts import ResetDB, PopulateDB
from . import public


@public.route('/')
def view():
    return render_template('index.html')


@public.route('/init_db')
def init_db():
    '''Utility route for resetting database through web view.
    TODO allow only on development config.'''
    ResetDB.drop_tables()
    PopulateDB.create_roles()
    PopulateDB.create_users()
    flash('''Kaboom. Database repopulated.
    Try account testadmin@example.com, password''')
    return redirect('/login')
