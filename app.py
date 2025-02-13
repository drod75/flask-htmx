from flask import Flask, render_template, request, redirect, url_for
from flask_htmx import HTMX, make_response
from database import Database

app = Flask(__name__, template_folder='template', static_folder='static')
htmx = HTMX(app)
db = Database()

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)