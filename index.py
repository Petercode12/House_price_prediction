#! C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
from flask import Flask, request, jsonify
from flask import Flask, redirect, url_for, render_template, request, flash, send_from_directory
import util
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("index.html",p='')

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    print(request.args)
    income = float(request.args['income'])
    hs_age =  float(request.args['hs_age'])
    num_rooms = float(request.args['num_rooms'])
    num_bedrooms = float(request.args['num_bedrooms'])
    population = float(request.args['population'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(income, hs_age, num_rooms, num_bedrooms, population)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return render_template("index.html",p=f'{util.get_estimated_price(income, hs_age, num_rooms, num_bedrooms, population)}')

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug = False, host='0.0.0.0')