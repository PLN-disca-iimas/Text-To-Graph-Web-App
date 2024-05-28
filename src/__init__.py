from flask import Flask, flash, redirect, url_for
from functools import wraps




app = Flask("Text To Graph Web App", template_folder="src/templates/", static_url_path='', 
            static_folder='src/static')
app.secret_key = 'IIMAS2024'



# ----------------------------------------------------------------------
# ------------------------- Start Decorators -------------------------
# ----------------------------------------------------------------------
def exception_handler(function):
    @wraps(function)
    def wrapper(*args, **kwds):

        try:
            return function(*args, **kwds)
        except Exception as e:
            flash(str(e), "danger")

    return wrapper
# ----------------------------------------------------------------------
# ------------------------- End Decorators -------------------------
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# ------------------------ Start Error Handlers ------------------------
# ----------------------------------------------------------------------
@app.errorhandler(401)
def not_authorized(e):
    flash(str(e), "warning")
    return redirect(url_for("graph_form"))

@app.errorhandler(404)
def not_found(e):
    flash(str(e), "danger")
    return redirect(url_for("graph_form"))

@app.errorhandler(413)
def bad_content(e):
    flash(str(e), "warning")
    return redirect(url_for("graph_form"))

@app.errorhandler(505)
def internal_error(e):
    flash(str(e), "danger")
    return redirect(url_for("graph_form"))
# ----------------------------------------------------------------------
# ------------------------- End Error Handlers -------------------------
# ----------------------------------------------------------------------