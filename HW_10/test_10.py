from statistics import mean
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return '<a href="http://127.0.0.1:500/avr_data">avr_data</a><br>' \
           '<a href="http://127.0.0.1:500/requirements">requirements</a>'


@app.route("/avr_data")
def avr_data():
    height = list()
    weight = list()
    with open("hw.csv", "r", encoding="utf8") as file:
        contents = file.readlines()
        for item1 in range(1, len(contents) - 1):
            a = contents[item1].split(", ")
            height.append(round(float(a[1]) * 2.54, 3))
            weight.append(round(float(a[2]) * 0.453592, 3))

    return '<p>Avr_Height: ' + str(round(mean(height), 2)) + '<br>' \
           'Avr_Weight: ' + str(round(mean(weight), 2)) + '</p>'


@app.route("/requirements")
def requirements():
    with open("requirements.txt", "r", encoding="utf8") as file:
        contents = file.read().split()

    return contents


app.run(debug=True, port=500)
