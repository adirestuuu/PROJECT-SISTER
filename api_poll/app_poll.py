from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# lokasi database
DB_FILE = 'api_poll/polls.json'

# function membaca dari JSON dan menulis data ke JSON.
def read_db():
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return "API POLL (Port 5002) - Siap Menerima Request!"

# endpoint 1: GET /polls
@app.route("/polls", methods=['GET'])
def get_polls():
    # 1. membaca data dari database
    polls = read_db()
    # 2. return sebagai JSON
    return jsonify(polls)

# endpoint 2: POST /polls
@app.route("/polls", methods=['POST'])
def create_poll():
    # 1. mengambil data JSON yang dikirim user
    data_baru = request.json
    
    # validasi
    if 'question' not in data_baru:
        return jsonify({"error": "Data 'question' tidak ditemukan"}), 400 # 400 = Bad Request

    # 2. membaca database
    db = read_db()
    
    # 3. menambah data baru ke database
    data_baru['id'] = len(db) + 1 
    db.append(data_baru)
    
    # 4. menulis ulang database dengan data yang usudah diperbarui
    write_db(db)
    
    print(f"API Poll: Data baru berhasil disimpan -> {data_baru}")
    
    # 5. respon sukses (201 = created)
    return jsonify(data_baru), 201

if __name__ == "__main__":
    app.run(port=5002, debug=True)