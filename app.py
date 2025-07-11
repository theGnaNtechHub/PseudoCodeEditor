from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import evaluate_pseudocode

app = Flask(__name__)
CORS(app)  # Enables requests from frontend (React or any origin)
# sample_code = """
#     x = 10
#     y = 5
#     print x * y
#     """

# print(evaluate_pseudocode(sample_code))
@app.route('/', methods=['GET'])
def home():
    return "VteacH Backend is Live!"

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    code = data.get("code", "")
    
    if not code:
        return jsonify({
            "status": "error",
            "message": "No code provided"
        }), 400
    
    result = evaluate_pseudocode(code)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    
