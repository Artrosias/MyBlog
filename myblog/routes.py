from myblog import app, db, utils, errors
from flask import render_template, redirect, url_for, flash, request, abort
from myblog.models import Post,User
from flask_login import current_user, login_user, logout_user, login_required
from myblog.forms import LoginForm, PostForm

@app.route("/")
def home():
   # posts = Post.query.all()
   page_number = request.args.get('page', 1, type=int)
   posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page_number, per_page=3, error_out=True)
   
   if posts.has_next:
        next_page = url_for('home', page = posts.next_num)
   else:
        next_page = None

   if posts.has_prev:
        previous_page = url_for('home', page = posts.prev_num)
   else:
        previous_page = None
   
   return render_template('homepage.html', posts=posts, current_page=page_number, next_page=next_page, previous_page=previous_page)

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
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Il nome utente inserito non esiste o la password è sbagliata!')
            return redirect (url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html',form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, description=form.description.data, body=form.body.data, author=current_user)
        if form.image.data:
            try:
                image = utils.save_image(form.image.data)
                new_post.image = image
            except:
                db.session.add(new_post)
                db.session.commit()
                flash("Si è verificato un errore nel salvataggio dell'immagine. Riprova!")
                return redirect(url_for('post_update', post_id=new_post.id))
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('post_detail', post_id=new_post.id))
    return render_template('post_editor.html', form=form)

@app.route("/post/<int:post_id>/update")
@login_required
def post_update(post_id):
    post_instance =  Post.query.get_or_404(post_id)
    if post_instance.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post_instance.title = form.title.data
        post_instance.description = form.description.data
        post_instance.body = form.body.data
        if form.image.data:
            try:
                image = utils.save_image(form.image.data)
                post_instance.image = image
            except:
                db.session.add(post_instance)
                db.session.commit()
                flash("Si è verificato un errore nel salvataggio dell'immagine. Riprova!")
                return redirect(url_for('post_update', post_id=post_instance.id))
        

        db.session.commit()
        return redirect(url_for('post_detail', post_id=post_instance.id))
    elif request.method == "GET":
        form.title.data = post_instance.title
        form.description.data = post_instance.description
        form.body.data = post_instance.body
    return render_template('post_editor.html', form=form)

@app.route("/post/<int:post_id>/delete", methods=["GET"])
@login_required
def post_delete(post_id):
    post_istance = Post.query.get_or_404(post_id)
    if post_istance.author != current_user:
        abort(403)
    db.session.delete(post_istance)
    db.session.commit()
    return redirect(url_for('home'))
  

