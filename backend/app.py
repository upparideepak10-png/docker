from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.json or {}
    name = data.get("name", "Guest")
    message = data.get("message", "No message provided")
    return jsonify({
        "status": "success",
        "reply": f"Hello {name}, your message '{message}' has been received successfully by the Flask backend!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
