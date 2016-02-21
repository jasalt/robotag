# http://pythonhosted.org/Flask-Testing/
from flask import current_app
from flask.ext.testing import TestCase
from app import create_app as the_create_app  # , db
from app.scripts import ResetDB


class BasicsTestCase(TestCase):
    def create_app(self):
        return the_create_app('testing')

    def setUp(self):
        '''Initialize database for test environment. Teardown should be
        handled by utilizing FlaskDB Peewee helper'''
        print("Clear and rebuild database")
        ResetDB.drop_tables()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
