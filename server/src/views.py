from src import app
from src.youtube.transcript import getRaw, getJson, _main
from src.topic_classification.main import getTranscript
from src.youtube.transcript import getRaw, getJson
from src.keywords_extraction.extractor import extractKeyWorks
import json


@app.route("/")
def index():
    return "Hello World!"
#f38sotYHqtA

@app.route("/vidoes/youtube/<videoId>")
def youtube(videoId):
    return getJson(videoId)


@app.route("/vidoes/youtube/<videoId>/raw")
def youtube_raw(videoId):
    return getRaw(videoId)


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