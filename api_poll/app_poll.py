from flask import Flask, jsonify, request
import poll_service

app = Flask(__name__)
PORT = 5002

@app.route("/")
def home():
    return f"API POLL jalan di Port {PORT}"

@app.route("/polls", methods=['GET'])
def get_polls():
    # mengambil semua data polling
    print("Menerima request GET /polls")
    polls = poll_service.get_all_polls_logic()
    return jsonify(polls)

@app.route("/polls", methods=['POST'])
def create_poll():
    # meneruskan permintaan ke lapisan service
    print("Menerima request POST /polls")
    data_baru = request.json
    
    #validasi dasar
    if 'question' not in data_baru:
        return jsonify({"error": "Data 'question' tidak ditemukan"}), 400
    # melempar data baru ke service layer untuk diproses
    poll_yang_dibuat = poll_service.create_poll_logic(data_baru)
    
    # mengembalikan data yang baru dibuat
    return jsonify(poll_yang_dibuat), 201

if __name__ == "__main__":
    app.run(port=PORT, debug=True)