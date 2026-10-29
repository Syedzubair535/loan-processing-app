from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body>
        <h1>Loan Processing System - CI/CD Demo</h1>
        <button>Apply Loan</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
