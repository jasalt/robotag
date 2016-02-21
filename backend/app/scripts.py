from flask import current_app
from flask.ext.script import Command
from flask.ext.security.confirmable import confirm_user

from . import create_app
from .models import Role, User, UserRoles


class ResetDB(Command):
    '''Drop and recreate tables'''
    def run(self):
        app = create_app('development')  # HACK -ish? Better way to do this?
        self.drop_tables()  # TODO handle configuration variations

    @staticmethod
    def drop_tables():
        for m in (Role, User, UserRoles):
            m.drop_table(fail_silently=True)
            m.create_table(fail_silently=True)
            print('ResetDB: rebuilt ' + str(m))


class PopulateDB(Command):
    '''Populate database with predefined content.'''
    def run(self):
        app = create_app('development')  # TODO see previous
        self.create_roles()
        self.create_users()

    @staticmethod
    def create_roles():
        current_app.user_datastore.create_role(name='admin',
                                               description='Database admin')
        current_app.user_datastore.create_role(name='board',
                                               description='Board member')
        current_app.user_datastore.commit()
        print("PopulateDB: created ''admin' and 'board' roles")

    @staticmethod
    def create_users():
        for u in (('testadmin', 'testadmin@example.com',
                   'password', ['admin'], True),
                  ('testboardmember', 'testboard@example.com',
                   'password', ['board'], True),
                  ('testmember', 'testmember@example.com',
                   'password', [], True)):
            user = current_app.user_datastore.create_user(
                username=u[0], email=u[1], password=u[2],
                roles=u[3], active=u[4])
            confirm_user(user)
            current_app.user_datastore.commit()
            print("PopulateDB: add user " + str(u))
