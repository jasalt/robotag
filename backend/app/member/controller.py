from flask import render_template
from flask.ext.security import login_required
from . import member


@member.route('/member')
@login_required
def view():
    return render_template('member.html')
