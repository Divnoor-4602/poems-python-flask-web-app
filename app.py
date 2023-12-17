from flask import Flask, render_template
from whatsapp_poem_project import fetch_poems

app = Flask(__name__)


def new_poem():
    poem_to_return = fetch_poems().split("\n")
    return poem_to_return


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/poem", methods=["POST"])
def get_poem():
    return render_template("poem.html", poem_text=new_poem())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
