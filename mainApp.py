from flask import Flask, render_template, flash, redirect, url_for, session, logging, request

app = Flask(__name__)


@app.route("/", method=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template(index.html)


if __name__ == "__main__":
    app.run(debug=True)