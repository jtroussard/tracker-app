import os 
from app import create_app
from app.config.dev_config import DevConfig

app = create_app(os.environ.get('FLASK_ENV', 'development'))
print(app.config["PORT"])
print(app.config["ENV"])
print(app.config["DEBUG"])

if __name__ == "__main__":
    app.run(debug=True)
