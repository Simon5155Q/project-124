from flask import Flask, jsonify, request
import random

app = Flask.name(__name__)
@app.route("/details", methods = ["POST"])

data = {
    "id": random.randint(1,100),
    "name": request.json["name"],
    "contact": request.json.get("contact", "")
}

def getDetails():
    return jsonify({
        "data": data
    }),200

if __name__ == "__main__":
    app.run(debug = True)



