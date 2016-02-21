from flask import render_template
from flask.ext.security import login_required
from . import invoice


@invoice.route('/invoice/')  # TODO handle invoice id to show details
@login_required
def view():
    return render_template('invoice/main.html')


@invoice.route('/invoice/generator')
@login_required
def generator():
    return render_template('invoice/generator.html')


# TODO  @invoice.route('/invoice/history')
# @login_required
# def history():
#     return render_template('invoice/history.html')
