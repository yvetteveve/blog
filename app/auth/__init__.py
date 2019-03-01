
# from . import views
# from . import views, forms
from flask import Blueprint


auth = Blueprint('auth', __name__)
from . import views,forms