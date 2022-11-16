from flask import render_template
from myblog import app

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404