from flask import Flask

from src.controller import controller_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(controller_bp)
    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)