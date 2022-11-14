from myblog import app
from flask import render_template

@app.route("/")
def home():
    posts = [{"title":"Primo titolo", "body": "Primo contenuto"},
             {"title": "Secondo titolo", "body": "Secondo contenuto"}]
    return render_template('homepage.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
    