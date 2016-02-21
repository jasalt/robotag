# Customized Flask-Admin view classes for embedding admin views to custom
# page layout
from flask import abort, redirect, url_for, request
from flask.ext.security import current_user, roles_required, login_required
from flask_admin.contrib.peewee import ModelView
from flask_admin.base import AdminIndexView, expose


# Custom admin index view for
class MyAdminView(AdminIndexView):
    @expose('/')
    @login_required
    @roles_required('admin')
    def index(self):
        arg1 = 'Hello'
        return self.render('admin/index.html', arg1=arg1)


# Create customized model view class
# https://github.com/flask-admin/flask-admin/blob/master/examples/auth/app.py
class MyModelView(ModelView):
    def is_accessible(self):
        if not current_user.is_active() or not current_user.is_authenticated():
            return False
        if current_user.has_role('admin'):
            return True
        return False

    @roles_required('admin')
    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is
        not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated():
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))
