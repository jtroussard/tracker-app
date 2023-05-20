from app import create_app
from app.config.dev_config import DevConfig

app = create_app(DevConfig)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"])
