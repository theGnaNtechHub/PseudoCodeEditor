from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import evaluate_pseudocode

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "VteacH Backend is Live!"

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json(force=True)
        code = data.get("code", "").strip()

        if not code:
            print("[ERROR] Empty code received.")
            return jsonify({
                "status": "error",
                "message": "No code provided"
            }), 400

        print(f"[INFO] Code received:\n{code}\n---")

        result = evaluate_pseudocode(code)
        print(f"[RESULT] {result}")

        return jsonify(result)

    except Exception as e:
        print(f"[EXCEPTION] {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Internal server error: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
