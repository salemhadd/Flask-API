from flask import Flask, request, jsonify

app = Flask(__name__)

#http://127.0.0.1:5000/get-user/123

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Salem Haddad",
        "email": "salem.haddadbecha@gmail.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200


@app.route("/create-user",methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
