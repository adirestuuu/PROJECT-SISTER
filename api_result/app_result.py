from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "API RESULT yang jalan di Port 5004."
if __name__ == "__main__":
    app.run(port=5004)