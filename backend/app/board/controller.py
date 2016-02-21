from flask import render_template
from flask.ext.security import roles_accepted, login_required
from . import board


@board.route('/board')
@login_required
@roles_accepted('admin', 'board')
def view():
    return render_template('board.html')
