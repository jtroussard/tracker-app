from app.src import create_app

app = create_app()

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(port='8002', debug=True)
=======
    port = app.config.get('PORT')
    app.run(port=port, debug=True)
>>>>>>> eecca5a (wrapping up ui work, adds cancel button)
