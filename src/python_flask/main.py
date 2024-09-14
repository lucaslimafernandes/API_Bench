import time

import jwt
from flask import Flask, jsonify

import models.user

for _ in range(5):

    try:
        models.user.create_user()
    except:
        time.sleep10
        pass

app = Flask(__name__)
SECRET_KEY = "secret-jwt"
app.config['SECRET_KEY'] = SECRET_KEY




@app.route("/ping")
def hello():
    return jsonify({"data": "pong"})


@app.route("/auth/login", methods=["GET"])
def login():
    try:
        data = {
            "email": "test2@test.com",
            "fullname": "Chandler Bing",
            "password": "password123",
        }
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        
        # validate input
        user = models.user.login(
            data["email"],
            data["password"]
        )
        if user:
            try:
                # token should expire after 24 hrs
                user["token"] = jwt.encode(
                    {"user_id": user["id"]},
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
                return {
                    "token": user["token"]
                }
            except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 500
        return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }, 404
    except Exception as e:
        return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
        }, 500




if __name__ == "__main__":

    app.run(debug=False, port=5000)

