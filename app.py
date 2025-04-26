from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API is live!"})

@app.route('/signal', methods=['GET'])
def get_signal():
    return jsonify({
        "signal": "Buy",
        "time": "2025-04-26 12:45:30"
    })
