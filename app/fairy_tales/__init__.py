from flask import Blueprint

fairy_tales = Blueprint('fairy_tales', __name__)

from . import routes
