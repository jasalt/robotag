from flask_admin import Admin, helpers as admin_helpers
from playhouse.flask_utils import FlaskDB

from config import config
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.security import PeeweeUserDatastore, Security


bootstrap = Bootstrap()

# create a peewee database instance -- our models will use this database to
# persist information
db = FlaskDB()

from .models import Role, User, UserRoles

# admin = create_admin()


def create_app(config_name):
    '''Flask application factory function'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.jinja_env.line_statement_prefix = '%'
    bootstrap.init_app(app)

    db.init_app(app)
    app.user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
    security = Security(app, app.user_datastore)

    #     Setup blueprints

    from .public import public as public_blueprint
    app.register_blueprint(public_blueprint)

    from .member import member as member_blueprint
    app.register_blueprint(member_blueprint)

    from .board import board as board_blueprint
    app.register_blueprint(board_blueprint)

    from .invoice import invoice as invoice_blueprint
    app.register_blueprint(invoice_blueprint)

    #     Setup flask-admin

    from .admin.controller import MyModelView, MyAdminView
    admin = Admin(app, 'Admin Panel',
                  template_mode='bootstrap3',
                  index_view=MyAdminView(
                      name='Admin Index',
                      template='admin/index.html',
                      url='/admin'))

    admin.add_view(MyModelView(User))
    admin.add_view(MyModelView(Role))
    admin.add_view(MyModelView(UserRoles))

    # define a context processor for merging flask-admin's template context
    # into the flask-security views.
    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers
        )

    return app
