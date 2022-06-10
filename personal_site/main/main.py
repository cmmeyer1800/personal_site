from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main_bp.route("/projects", methods=["GET"])
def projects():
    return render_template("projects.html")