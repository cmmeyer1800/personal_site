from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    from personal_site.main.main import main_bp

    app.register_blueprint(main_bp, url_prefix="/")

    return app