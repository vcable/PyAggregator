from app import app, aggregator
from flask import render_template
import os

py_logo = os.path.join(app.config["IMAGES"], "pylogo.svg")

@app.route("/")
@app.route("/home")
def home():
    data = aggregator.Aggregator()
    pp_articles = data.pp_articles
    rp_articles = data.rp_articles
    r_python_posts = data.r_python_posts
    import_articles = data.import_articles
    stack_overflow = data.stack_questions
    guru_articles = data.guru_articles
    return render_template("home.html", pp_articles=pp_articles, rp_articles=rp_articles,
                           r_python_posts=r_python_posts, import_articles=import_articles,
                           stack_overflow=stack_overflow, guru_articles=guru_articles, py_logo=py_logo)
    
@app.route("/contact")
def contact():
    return render_template("contact.html", py_logo=py_logo)