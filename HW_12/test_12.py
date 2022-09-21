import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/rates", methods=['GET'])
def show_rates():
    data = requests.get('https://bitpay.com/api/rates').json()
    reformat = dict()

    for item in data:
        reformat[item["code"].lower()] = {'name': item["name"], 'rate': item["rate"]}

    if request.method == 'GET':
        if request.args.get('currency') is not None:
            return render_template('currency.html', code=request.args.get('currency'), reformat_data=reformat)
    return render_template('request.html', data=data)


app.run(debug=False, port=5000)
