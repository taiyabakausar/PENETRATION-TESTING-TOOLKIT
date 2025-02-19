from flask import Flask, request

app = Flask(__name__)

# Hardcoded credentials for testing
USERNAME = "admin"
PASSWORD = "password123"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return "Login successful!"
    else:
        return "Login failed!"

if __name__ == "__main__":
    app.run(debug=True)