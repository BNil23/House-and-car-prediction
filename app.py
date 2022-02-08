from flask import request
from flask import Flask, render_template, redirect
from flask_restful import Api, Resource, reqparse
import apis

app = Flask(__name__)

api = Api(app)

#API
api.add_resource(apis.HousePricePredictionApi, '/housePredict')
api.add_resource(apis.CarPricePredictionApi, '/carPredict')

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/house")
def house():
        return render_template("house.html")

@app.route("/car", methods = ['POST', 'GET'])
def car():
        if request.method == 'GET':
                return render_template("car.html")
        if request.method == 'POST':
                brand = request.form.get('brand_select')
                model = request.form.get('model_select')
                year = request.form['year']
                fuel = request.form.get('fuel_select')
                gear = request.form.get('gear_select')
                engineCapacity = request.form['engineCapacity']
                motorPower = request.form['motorPower']
                kilometer = request.form['kilometer']
                accident = request.form['accident']
                url = "/carPredict?marka=" + brand + "&seri=" + model +"&yil=" + year + "&yakit=" + fuel + "&vites=" + gear + "&motor_hacmi=" + engineCapacity + "&motor_gucu=" + motorPower + "&km=" + kilometer + "&tramer=" + accident
                return redirect(url)   

if __name__ == "__main__":
    app.run(debug=True)