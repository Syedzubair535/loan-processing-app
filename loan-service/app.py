from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/apply", methods=["POST"])
def apply():
    return jsonify({
        "status": "APPROVED"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
