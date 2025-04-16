from flask import Flask, request, jsonify
from MedicalKeywordExtractor import extract_and_categorize

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Keyword Extraction App is running!"

@app.route('/extract_keywords', methods=['POST'])
def extract_keywords():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No input text provided"}), 400

    try:
        result = extract_and_categorize(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=port)         
