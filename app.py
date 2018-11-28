from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_indeed

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/indeed_db")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
