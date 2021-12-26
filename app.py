from flask import Flask, render_template, flash, redirect, url_for, session, logging, request

app = Flask(__name__)


@app.route("/")
def index():
        return render_template("index.html")

@app.route("/house")
def house():
        return render_template("house.html")

@app.route("/car")
def car():
        return render_template("car.html")

if __name__ == "__main__":
    app.run(debug=True)