from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.dbmodels import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'

    },
        {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html' , title='About')

@app.before_first_request
def create_tables():
    app.app_context().push()
    db.create_all()
    

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_psw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_psw)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account is created! You can log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Welcome to our Homepage ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccesful. Please check email and password', 'danger')
    return render_template('login.html', title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))




lst = [1,2,3,4,5]
@app.route("/json")
def json():
    return render_template('empty.html', title='Json', lst01=lst)