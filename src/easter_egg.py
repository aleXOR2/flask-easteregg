import os

from flask import Flask
from flask import render_template


STATIC_FOLDER = os.path.abspath("src/static")
app = Flask(__name__, template_folder="templates")
app.config["UPLOAD_FOLDER"] = STATIC_FOLDER


@app.route("/")
def show_index():
    name_file = os.path.join(app.config["UPLOAD_FOLDER"], "user_name.txt")
    with open(name_file, "r") as f:
        user_name = f.read()
    image_file = str(os.path.join(app.config["UPLOAD_FOLDER"], "easter-egg.jpg")).replace(
        os.path.dirname(__file__), ""
    )
    return render_template("index.html", user_name=user_name, easter_egg=image_file)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
