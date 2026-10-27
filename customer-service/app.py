from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def customer():
    return jsonify({
        "customer": "John",
        "score": "750"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
