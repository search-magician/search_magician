from src import app
from src.youtube.transcript import getRaw, getJson
from src.part_matching.main import suggestInterval
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

CORS(app)

@app.route("/")
def index():
    return "Hello World!"


@app.route("/vidoes/youtube/<videoId>")
def youtube(videoId):
    return getJson(videoId)


@app.route("/vidoes/youtube/<videoId>/raw")
def youtube_raw(videoId):
    return getRaw(videoId)

@app.route('/search/interval-suggestion/<videoId>', methods=['POST'])
def suggestIntervalEndpoint(videoId):
    query = (request.json)["query"]
    ret = suggestInterval(videoId, query)
    return jsonify(ret)