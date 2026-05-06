from flask import Flask, request, jsonify

app = Flask(__name__)

def analyze_code(code):
    feedback = []

    # Basic structure checks
    if "print(" in code:
        feedback.append("Avoid excessive print statements in production code.")

    if len(code.strip()) < 20:
        feedback.append("Code is very short, consider adding more logic.")

    # Logic checks
    if "==" in code:
        feedback.append("Ensure proper comparison logic is being used.")

    if "=" in code and "==" not in code:
        feedback.append("Check if assignment (=) is being used correctly instead of comparison (==).")

    # Security checks
    if "password" in code.lower():
        feedback.append("Avoid hardcoding sensitive information like passwords.")

    if "import *" in code:
        feedback.append("Avoid using wildcard imports (import *), it can make code unclear.")

    if "eval(" in code:
        feedback.append("Avoid using eval() as it can be unsafe.")

    if "exec(" in code:
        feedback.append("Avoid using exec() as it can be dangerous.")

    # Code quality
    if "TODO" in code or "todo" in code:
        feedback.append("Unresolved TODO found. Consider completing or removing it.")

    if "while True" in code:
        feedback.append("Be cautious with infinite loops (while True).")

    # Clean result
    if not feedback:
        feedback.append("Code looks clean and well-structured!")

    return feedback


@app.route("/", methods=["GET"])
def home():
    return "AI Code Reviewer is running!"


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        code = data.get("code", "")

        if not code:
            return jsonify({"error": "No code provided"}), 400

        result = analyze_code(code)

        return jsonify({
            "input_length": len(code),
            "feedback": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)