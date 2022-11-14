from myblog import app
from flask import render_template


@app.route("/")
def home():
    return  render_template('homepage.html')

@app.route("/about")
def about():
    return  render_template('about.html')


@app.router("/contact")
def contact():
    return render_template('contact.html')