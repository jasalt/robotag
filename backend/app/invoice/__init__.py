from flask import Blueprint

invoice = Blueprint('invoice', __name__)

from . import controller
