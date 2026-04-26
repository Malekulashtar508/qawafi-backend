from flask import Flask, request, jsonify
from flask_cors import CORS
from qawafi_server.bait_analysis import BaitAnalysis

app = Flask(__name__)
CORS(app)

analysis = BaitAnalysis()

@app.route('/')
def home():
    return "Qawafi API Running"

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get("text")

    with open("input.txt", "w", encoding="utf-8") as f:
        f.write(text)

    result = analysis.analyze(read_from_path="input.txt", override_tashkeel=True)
    return jsonify(result)
