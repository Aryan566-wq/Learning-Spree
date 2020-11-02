
import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, JoinGroup, PostForm, MakeGroup
from flaskblog.models import User, Group, Post
from flask_login import login_user, current_user, logout_user, login_required
#username = kahanzz, email=kahanvora@gmail.com password = d123


@app.route("/")
@app.route("/home")
def home():
    group = Group.query.filter_by(id=14).first()
    print(group)
    print(group.name)
    name = group.name
    posts = Post.query.all()
    post_for_group = []
    for post in posts:
        if post.group_id == group.id:
            post_for_group.append(post)
    post_for_group.reverse()
    return render_template("home.html", posts=post_for_group, name=name)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data, joined_group=0)
        print(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.password.data == user.password:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else    redirect(url_for('home'))     
    return render_template('login.html', title='Login', form=form)


@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    posts = Post.query.all()
    post_for_group = []
    return render_template("account.html", image_file=image_file)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
    
@app.route("/account/edit", methods=["GET", "POST"])
@login_required
def acc_edit():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        print(form.picture.data)
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            print(current_user.image_file)
            print(current_user.image_file)
            print(current_user.image_file)
            print(current_user.image_file)
            print(current_user.image_file)
            print(current_user.image_file)
            print(current_user.image_file)
            print(current_user.image_file)
        current_user.password = form.password.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.password.data = current_user.password
        form.email.data = current_user.email
    return render_template("acc-update.html", form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/new/group", methods=["POST", "GET"])
@login_required
def new_group():
    group = Group()
    db.session.add(group)
    db.session.commit()
    group_code = group.group_id
    group_id = group.id
    print(group.id)
    db.session.commit()
    form = MakeGroup()
    if form.validate_on_submit():
        group.name = form.name.data 
        db.session.commit()
        print(group.name)
        print(group)
        group = Group.query.filter_by(id=group_id).first()
        print(group.name)
        f = open("flaskblog/static/" + str(group_id), "w")
        f.write(form.name.data)
        f.close()
        return redirect("/home")
    return render_template("new-group.html", group_id=(group_code+str(group_id+1)), form=form)

@app.route("/group/join", methods=["POST", "GET"])
@login_required
def join_group():
    form = JoinGroup()
    if form.validate_on_submit():
        id = form.code.data [16:]
        data = form.code.data [:16]
        group = Group.query.filter_by(id=id).first()
        if group:
            if group.group_id == data:
                current_user.joined_group = 1
                current_user.group = id
                db.session.commit()
                print(group.name)
                group_new = Group.query.filter_by(id=id).first()
                print(group_new.group_id)
                print(group_new.name)
                return redirect("/home")
    return render_template("join-group.html", form=form)

@app.route("/group")
@login_required
def the_main_group():
    if current_user.joined_group == 0:
        return redirect("/home")
        
    group = Group.query.filter_by(id=current_user.group).first()
    print(group)
    print(group.name)
    import os
    if os.path.exists("flaskblog/static/" + str(group.id)):
        f = open("flaskblog/static/" + str(group.id), "r")
        name = f.read()
        f.close()
    else: 
        name = "None"
    posts = Post.query.all()
    post_for_group = []
    for post in posts:
        if post.group_id == group.id:
            post_for_group.append(post)
    post_for_group.reverse()
    return render_template("group.html", posts=post_for_group, name=name)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        group = Group.query.filter_by(id=current_user.group).first()
        print(group)
        print(current_user)
        print(form.content.data)
        print(form.title.data)
        post = Post(title=form.title.data, content=form.content.data, author=current_user, group_id=group.id)
        db.session.add(post)
        db.session.commit()
        flash("Post Created!", "success")   
        return redirect(url_for('home'))
    return render_template('create_post.html', title="New Post", form=form, legend="New Post")
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):  
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')
@login_required
@app.route("/main-join")
def main_join():
    group = Group.query.filter_by(id=14).first()
    group.name = "Main"
    db.session.commit()
    current_user.group = 14
    print(group.name)
    print(group.name)
    db.session.commit()
    print(group.name)
    print(group.name)
    f = open("flaskblog/static/" + str(14), "w")
    f.write("Main")
    f.close()
    print(current_user.group)
    return redirect("/")
    #fe25331ec75ba7bc14

@login_required
@app.route("/code-join")
def code_join():
    group = Group.query.filter_by(id=23).first()
    group.name = "Code"
    db.session.commit()
    current_user.group = 23
    print(group.name)
    print(group.name)
    db.session.commit()
    f = open("flaskblog/static/" + str(23), "w")
    f.write("Code")
    f.close()
    print(group.name)
    print(group.name)
    print(current_user.group)
    return redirect("/")

@login_required
@app.route("/sci-join")
def sci_join():
    group = Group.query.filter_by(id=25).first()
    group.name = "Science"
    db.session.commit()
    current_user.group = 25
    print(group.name)
    print(group.name)
    db.session.commit()
    f = open("flaskblog/static/" + str(25), "w")
    f.write("Science")
    f.close()
    print(group.name)
    print(group.name)
    print(current_user.group)
    return redirect("/")

@app.route("/download/todolist")
def npd():
    return render_template("npd.html")