from myblog import app
from flask import render_template
from myblog.models import Post


@app.route("/")
def home():
    posts = Post.query.all()
    return  render_template('homepage.html', posts=posts)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    mypost = Post.query.get_or_404(post_id)
    return render_template('post_detail.html',post=mypost)


@app.route("/about")
def about():
    return  render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')
    