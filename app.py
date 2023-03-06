from flask import Flask, render_template, redirect, url_for, flash
from config import Config

from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'this-is-a-super-secret-key-wubalubadubdub'

login_name = 'Michael Scott'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', active_page='home', login_name=login_name)

@app.route('/tracker')
def tracker():
    return render_template('tracker.html', active_page='tracker', login_name=login_name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    # for now we will redefine login_name here - TODO check login status and set variable as needed
    login_name = ""
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@test.com' and form.password.data == 'password':
            login_name = form.email.data
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', active_page='login', login_name=login_name, form=form)

@app.route('/logout')
def logout():
    # do things to log out the user
    print('user logged out')
    return redirect(url_for('home'))

@app.route('/register')
def register():
    # do things to register a new user
    return render_template('register.html', active_page='register', login_name=login_name)

if __name__ == '__main__':
    app.run()
