from flask import Blueprint, render_template

blueprint = Blueprint("home", __name__)


@blueprint.route("/")
def home():
    name = "John"
    return render_template("home.html", name=name)
