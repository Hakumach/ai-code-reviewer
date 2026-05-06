from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_code(code):
    feedback = []
    score = 10  # start perfect, deduct points

    lines = code.split("\n")

    # 🔴 Too many print statements
    if code.count("print(") > 3:
        feedback.append("Too many print statements — consider using logging")
        score -= 2

    # 🔴 Code too short
    if len(lines) < 5:
        feedback.append("Code is very short — may lack functionality")
        score -= 1

    # 🔴 Long function
    if len(lines) > 50:
        feedback.append("Function is too long — consider splitting it")
        score -= 2

    # 🔴 Missing comments
    if "#" not in code:
        feedback.append("No comments found — consider documenting your code")
        score -= 1

    # 🔴 Bad variable names
    bad_names = ["x", "y", "z", "data"]
    if any(f"{name} =" in code for name in bad_names):
        feedback.append("Use more descriptive variable names")
        score -= 1

    # Keep score in range
    score = max(score, 0)

    if not feedback:
        feedback.append("Code looks clean and well-structured")

    return score, feedback


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    score = None

    if request.method == "POST":
        code = request.form.get("code")

        if code:
            score, feedback = analyze_code(code)
            result = feedback

    return render_template("index.html", result=result, score=score)


if __name__ == "__main__":
    app.run(debug=True)