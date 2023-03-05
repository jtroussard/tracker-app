from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run()
