from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    total = None
    percent = None

    if request.method == "POST":
        m1 = float(request.form.get("m1", 0))
        m2 = float(request.form.get("m2", 0))
        m3 = float(request.form.get("m3", 0))

        total = m1 + m2 + m3
        percent = (total / 300) * 100

    return render_template("index.html", total=total, percent=percent)

if __name__ == "__main__":
    app.run(debug=True)  
