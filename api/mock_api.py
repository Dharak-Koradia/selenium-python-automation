from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "tomsmith": "SuperSecretPassword!"
}

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        return jsonify({"message": "Invalid credentials", "status": "fail"}), 401
    
@app.route("/health")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
