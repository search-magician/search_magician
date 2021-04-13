from src import app
import spacy
from flask import request
from src.youtube.transcript import getRaw, getJson, _main
import json


@app.route("/")
def index():
    return "Hello World!"

@app.route("/er")
def er():
    nlp = spacy.load("en_core_web_trf")
    strInput = str(request.data)
    doc = nlp(strInput)
    ans = ""
    for ent in doc.ents:
        ans += " <div> " + ent.text + " " + str(ent.start_char) + " " + str(ent.end_char) + " " + ent.label_ + " </div> "
    return ans

@app.route("/vidoes/youtube/<videoId>")
def youtube(videoId):
    return getJson(videoId)

@app.route("/vidoes/youtube/<videoId>/raw")
def youtube_raw(videoId):
    return getRaw(videoId)
