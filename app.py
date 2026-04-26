from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

app = Flask(__name__)
CORS(app)

# Clone repo
if not os.path.exists("qawafi"):
    os.system("git clone https://github.com/ARBML/qawafi.git")

# Install its dependencies
if os.path.exists("qawafi/demo_requirements.txt"):
    os.system("pip install -r qawafi/demo_requirements.txt")

# Add to path
sys.path.append("qawafi")

analysis = None

@app.route('/')
def home():
    return "Qawafi API Running"

@app.route('/analyze', methods=['POST'])
def analyze():
    global analysis

    if analysis is None:
        from qawafi_server.bait_analysis import BaitAnalysis
        analysis = BaitAnalysis()

    text = request.json.get("text")

    with open("input.txt", "w", encoding="utf-8") as f:
        f.write(text)

    result = analysis.analyze(read_from_path="input.txt", override_tashkeel=True)
    return jsonify(result)

app.run(host="0.0.0.0", port=10000)
