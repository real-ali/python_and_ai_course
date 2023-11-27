from flask import Flask, request

app = Flask(__name__)

data = [
    {
        "id": 1,
        "name": "Ahmad",
        "lastname": "Husaini",
        "age": 32,
    },
    {
        "id": 2,
        "name": "Ahmad ali",
        "lastname": "Husaini",
        "age": 32,
    },
    {
        "id": 3,
        "name": "Ahmad",
        "lastname": "Husaini",
        "age": 32,
    },
    {
        "id": 4,
        "name": "ali",
        "lastname": "Husaini",
        "age": 23,
    },
]


@app.route("/")
def home():
    # application/json
    # return {"id":"ali123"}

    # or like that
    # return jsonify(
    #     id="ali123",
    #     name= "Ali",
    #     last_name= "Hussaini"
    #     )

    # or return as html or another type
    return "<h1>Hello World</h1>"


@app.route("/no_content")
def no_content_handler():
    return ({"message": "no content found"}, 204)


@app.route("/exp")
def index_explicit_handler():
    res = app.make_response({"message": "Hello World!"})
    res.status_code = 200
    return res


@app.route("/data")
def data_handler():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is Empty"}, 500
    except NameError:
        return {"message": "data not found"}, 404


@app.route("/name_search")
def name_search_handler():
    # get valiue from query  -> ex: localhost:5000?name="ali"
    name = request.args.get("name")
    if not name:
        return {"message": "Invalid input parameter"}, 422
    for person in data:
        if name.lower() in person["name"].lower():
            return person

    return ({"message": "person not found"}, 404)


@app.route("/persons")
def get_all_person():
    return data


# Dynamic Routing
@app.route("/person/<int:id>")
def get_person_hanlder(id):
    for person in data:
        if person["id"] == id:
            return person
    return ({"message": f"person not found {id}"}, 404)


# DELETE method
# curl -X DELETE -i -w '\n' localhost:5000/person/3
@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person_hanlder(id):
    for person in data:
        if person["id"] == id:
            data.remove(person)
            return {"message": f"{id}"}, 200
    return ({"message": "person not found"}, 404)
