from app.src import create_app

app = create_app()

if __name__ == "__main__":
    port = app.config.get('PORT')
    app.run(port=port, debug=True)
