from flask import Flask, request, jsonify
from flask import Flask, redirect, url_for, render_template, request, flash
import util
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("template.html")

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    income = float(request.form['income'])
    hs_age =  float(request.form['hs_age'])
    num_rooms = float(request.form['num_rooms'])
    num_bedrooms = float(request.form['num_bedrooms'])
    population = float(request.form['population'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(income, hs_age, num_rooms, num_bedrooms, population)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug = True)