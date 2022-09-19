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
    tracks = conn.execute('select tracks.Name as "Track name", sum(invoice_items.UnitPrice * invoice_items.Quantity) '
                          'as "Price" from invoice_items join invoices on invoice_items.InvoiceId = '
                          'invoices.InvoiceId join tracks on invoice_items.TrackId = tracks.TrackId group by '
                          'tracks.Name order by sum(invoice_items.UnitPrice) DESC, tracks.Name asc;').fetchmany(track_num)
    conn.close()

    return render_template('tracks.html', tracks=tracks)


app.run(debug=True, port=500)
