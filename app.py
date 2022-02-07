from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import apis

app = Flask(__name__)

api = Api(app)

#API
api.add_resource(apis.LinearRegressionApi, '/ml')

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