from app import app, aggregator
from flask import render_template


@app.route("/")
@app.route("/home")
def home():
    data = aggregator.Aggregator()
    articles = data.pp_articles
    return render_template("home.html", articles=articles)