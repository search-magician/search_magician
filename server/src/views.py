import json
from src import app
from flask import request
from flask_cors import CORS
from src.extractors.main import getVideoData

CORS(app)


@app.route("/")
def index():
    return "Hello World!"

@app.route("/vidoes/<videoId>")
def videoData(videoId):
    data = getVideoData(videoId)
    return json.dumps(data, indent=4)

