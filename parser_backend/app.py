from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import evaluate_pseudocode, get_syntax_hints, get_learning_suggestions

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "VteacH Pseudo-code Editor Backend is Live!"

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json(force=True)
        code = data.get("code", "").strip()
        step_by_step = data.get("step_by_step", False)

        if not code:
            print("[ERROR] Empty code received.")
            return jsonify({
                "status": "error",
                "message": "No code provided"
            }), 400

        print(f"[INFO] Code received:\n{code}\n---")
        print(f"[INFO] Step-by-step mode: {step_by_step}")

        result = evaluate_pseudocode(code, step_by_step)
        print(f"[RESULT] {result}")

        return jsonify(result)

    except Exception as e:
        print(f"[EXCEPTION] {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Internal server error: {str(e)}"
        }), 500

@app.route('/syntax-hints', methods=['POST'])
def syntax_hints():
    """Get syntax hints and suggestions for the code."""
    try:
        data = request.get_json(force=True)
        code = data.get("code", "").strip()

        if not code:
            return jsonify({
                "status": "error",
                "message": "No code provided"
            }), 400

        hints = get_syntax_hints(code)
        return jsonify({
            "status": "success",
            "hints": hints
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error getting syntax hints: {str(e)}"
        }), 500

@app.route('/learning-suggestions', methods=['POST'])
def learning_suggestions():
    """Get learning suggestions based on the code content."""
    try:
        data = request.get_json(force=True)
        code = data.get("code", "").strip()

        if not code:
            return jsonify({
                "status": "error",
                "message": "No code provided"
            }), 400

        suggestions = get_learning_suggestions(code)
        return jsonify({
            "status": "success",
            "suggestions": suggestions
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error getting learning suggestions: {str(e)}"
        }), 500

@app.route('/validate', methods=['POST'])
def validate():
    """Validate code syntax without executing it."""
    try:
        data = request.get_json(force=True)
        code = data.get("code", "").strip()

        if not code:
            return jsonify({
                "status": "error",
                "message": "No code provided"
            }), 400

        # Use the evaluate function but only for validation
        result = evaluate_pseudocode(code)
        
        if result["status"] == "error":
            return jsonify({
                "status": "error",
                "valid": False,
                "errors": result.get("errors", []),
                "message": result.get("message", "Syntax validation failed")
            })
        else:
            return jsonify({
                "status": "success",
                "valid": True,
                "message": "Code syntax is valid"
            })

    except Exception as e:
        return jsonify({
            "status": "error",
            "valid": False,
            "message": f"Validation error: {str(e)}"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "Pseudo-code Editor Backend",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)
