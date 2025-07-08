from app import AppFactory

app = AppFactory().get_app()

if __name__ == "__main__":
    app.run(debug=True)