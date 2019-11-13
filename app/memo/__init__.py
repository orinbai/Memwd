from flask import Blueprint

auth = Blueprint("memo", __name__)

from . import views
