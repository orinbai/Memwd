from flask import Blueprint

auth = Blueprint("mark", __name__)

from . import views
