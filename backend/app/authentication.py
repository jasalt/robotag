# User authentication specific code
from flask import Blueprint, render_template, flash, request, redirect, \
    url_for
from flask_wtf import Form
from wtforms import PasswordField, SubmitField, TextField
from flask.ext.login import LoginManager, login_user, logout_user
from wtforms.validators import DataRequired, AnyOf
from models import User


auth_keys = ['topsecret', 'asdf']

authentication = Blueprint('authentication', __name__)

login_manager = LoginManager()
login_manager.login_view = "authentication.login"


@login_manager.user_loader
def load_user(id):
    # ID is ignored, using single user authentication
    return User()


class LoginForm(Form):
    username = TextField('Käyttäjätunnus tai sähköpostiosoite')
    password = PasswordField('Salasana',
                             validators=[DataRequired(),
                                         AnyOf(auth_keys,
                                               'Salasana on väärä!')])
    submit = SubmitField('Kirjaudu')


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(User(), remember=True, force=True)
        flash("Kirjautuminen onnistui!")
        next = request.args.get('next')
        # note: next should be validated for security purposes!
        return redirect(next or url_for('index.home'))
    return render_template('login.html', form=form)


@authentication.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication.login'))
