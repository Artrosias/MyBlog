from myblog import app
from flask import render_template, redirect, url_for, flash
from myblog.models import Post,User
from flask_login import current_user, login_user, logout_user, login_required
from myblog.forms import LoginForm

@app.route("/")
def home():
    posts = Post.query.all()
    return render_template('homepage.html', posts=posts)

@app.route("/posts/<int:post_id>")
def post_detail(post_id):
    mypost = Post.query.get_or_404(post_id)
    return render_template('post_detail.html',post=mypost)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
    
@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Il nome utente inserito non esiste o la password è sbagliata!')
            return redirect (url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('homepage'))
    return render_template('login.html',form=form)