from flask import Flask, render_template
from src.presentations.rest.routes import (
    home_routes,
    contact_routes,
    about_routes,
    profile_routes,
)
import os


app = Flask("My app")
# by default its on templates folder -- root level
# Set the path to the templates folder
app.template_folder = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "src/presentations/rest/templates"
)
app.register_blueprint(home_routes.blueprint)
app.register_blueprint(about_routes.blueprint)
app.register_blueprint(contact_routes.blueprint)
app.register_blueprint(profile_routes.blueprint)
if __name__ == "__main__":
    app.run(debug=True)
