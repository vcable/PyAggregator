from flask import Flask
import os

app = Flask(__name__)
app.config["IMAGES"] = os.path.join("static", "img")

from app import routes