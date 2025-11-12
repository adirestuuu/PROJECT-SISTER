from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "API USER yang jalan di Port 5001"
if __name__ == "__main__":
    app.run(port=5001)