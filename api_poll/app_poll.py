from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "API POLL yang jalan di Port 5002"
if __name__ == "__main__":
    app.run(port=5002)