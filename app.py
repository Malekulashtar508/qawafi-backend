from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

app = Flask(__name__)
CORS(app)

# clone repo if not exists
if not os.path.exists("qawafi"):
    os.system("git clone https://github.com/ARBML/qawafi.git")

# add to path
sys.path.append("qawafi")

from qawafi_server.bait_analysis import BaitAnalysis

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

app.run(host="0.0.0.0", port=10000)
