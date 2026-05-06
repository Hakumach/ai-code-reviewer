from flask import Flask, request, jsonify

app = Flask(__name__)

def analyze_code(code):
    feedback = []

    if "print" in code:
        feedback.append("Avoid excessive print statements in production code.")

    if len(code) < 20:
        feedback.append("Code is very short, consider adding more logic.")

    if "==" in code:
        feedback.append("Check for proper comparison logic.")

    if "password" in code.lower():
        feedback.append("Avoid hardcoding sensitive information like passwords.")

    if not feedback:
        feedback.append("Code looks clean and well-structured!")

    return feedback

@app.route("/", methods=["GET"])
def home():
    return "AI Code Reviewer is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    code = data.get("code", "")

    result = analyze_code(code)

    return jsonify({"feedback": result})

if __name__ == "__main__":
    app.run(debug=True)
