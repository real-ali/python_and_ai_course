from flask import Blueprint, render_template

blueprint = Blueprint("user", __name__)


@blueprint.route("/users/<username>")
def user_profile(username):
    return render_template("profile.html", username=username)
