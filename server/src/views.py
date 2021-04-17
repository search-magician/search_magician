from src import app
from src.youtube.transcript import getRaw, getJson, _main
import json


@app.route("/")
def index():
    return "Hello World!"


@app.route("/vidoes/youtube/<videoId>")
def youtube(videoId):
    return getJson(videoId)


@app.route("/vidoes/youtube/<videoId>/raw")
def youtube_raw(videoId):
    return getRaw(videoId)
