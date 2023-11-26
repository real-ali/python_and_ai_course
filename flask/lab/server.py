from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def home():
    # application/json
    # return {"id":"ali123"}

    #or like that
    # return jsonify(
    #     id="ali123",
    #     name= "Ali",
    #     last_name= "Hussaini"
    #     )

    #or return as html or another type
    return "<h1>Hello World</h1>"