import json
from src import app
from flask import request
from src.youtube.transcript import getRaw, getJson
from flask_cors import CORS
from src.extractors.ER import main as ER
from src.youtube.videoData import getTopicsFromList


CORS(app)


@app.route("/")
def index():
    return "Hello World!"
#f38sotYHqtA

@app.route("/vidoes/youtube/<videoId>/er")
def er(videoId):
    txt = getRaw(videoId)
    return json.dumps(ER(txt), indent=4)


@app.route("/vidoes/youtube/<videoId>")
def youtube(videoId):
    return getJson(videoId)


@app.route("/vidoes/youtube/<videoId>/raw")
def youtube_raw(videoId):
    return getRaw(videoId)


<<<<<<< HEAD
@app.route("/playlist/<id>/")
def getListData(id):
    return json.dumps(getTopicsFromList(id), indent=4)
=======
@app.route("/vidoes/youtube/<videoId>/classification")
def topic_classification(videoId):
   transcript = getRaw(videoId)
   topics , topics_prob = getTranscript(transcript)
   json = {
       "topics" : topics,
       "topics_prob" : topics_prob.tolist()
   }
   return json

@app.route("/vidoes/youtube/<videoId>/keywords")
def extract_keywords(videoId):
   transcript = getRaw(videoId)
   json = extractKeyWorks(transcript)
   return json
>>>>>>> ad1dd16a9864b08db774d736294c2852931127bd
