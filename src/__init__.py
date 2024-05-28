from flask import Flask, flash
from functools import wraps




app = Flask("Text To Graph Web App", template_folder="src/templates/", static_url_path='', 
            static_folder='src/static')
app.secret_key = 'IIMAS2024'

def exception_handler(function):
    @wraps(function)
    def wrapper(*args, **kwds):

        try:
            return function(*args, **kwds)
        except Exception as e:
            flash(str(e), "danger")

    return wrapper