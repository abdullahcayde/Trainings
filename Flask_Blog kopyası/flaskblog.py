from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f2f70944ec6c0483f84ecac47b556761'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@a.a' and form.password.data == '123':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccesful. !!!', 'danger')
    return render_template('login.html', title='Login',form=form)

@app.route("/listpage")
def list01():
    lst = [1,2,3,4,5]
    return render_template('empty.html' , lst=lst, title='Json')

@app.route("/json")
def json():
    lst = [1,2,3,4,5]
    return lst

if __name__ == '__main__':
    app.run(debug=True)