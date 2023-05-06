from flask import *
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        result = request.form["url"]
        #print(request.form["url"])
        return render_template("home.html", result = result)
    return render_template("home.html", result = "")

if __name__ == "__main__":
    app.run()