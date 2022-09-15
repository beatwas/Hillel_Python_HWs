import sqlite3
from statistics import mean
from flask import Flask
from flask import render_template

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect("example.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/best_selling/<int:track_num>")
def best_selling(track_num):
    conn = get_connection()
    tracks = conn.execute('SELECT * FROM tracks').fetchmany(track_num)
    conn.close()

    return render_template('tracks.html', tracks=tracks)


app.run(debug=True, port=500)
