from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    login_name = 'Michael Scott'
    return render_template('home.html', active_page='home', login_name=login_name)

if __name__ == '__main__':
    app.run()
