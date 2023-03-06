from flask import Flask, render_template, redirect, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_name = 'Michael Scott'

@app.route('/')
def home():
    return render_template('home.html', active_page='home', login_name=login_name)

@app.route('/tracker')
def tracker():
    return render_template('tracker.html', active_page='tracker', login_name=login_name)

@app.route('/login')
def login():
    # do things to log in the user
    return render_template('login.html', active_page='login', login_name=login_name)

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
