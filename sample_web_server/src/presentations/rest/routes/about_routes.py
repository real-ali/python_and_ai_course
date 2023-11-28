from flask import Blueprint, render_template

blueprint = Blueprint("about", __name__)


@blueprint.route("/about")
def about():
    return render_template("about.html")
