from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return "<p> This is a home page </p>"

