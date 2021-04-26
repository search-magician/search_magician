from src import app
import spacy
from flask import request
from src.youtube.transcript import getRaw, getJson
import json
from flask_cors import CORS


CORS(app)

@app.route("/")
def index():
    return "Hello World!"


@app.route("/vidoes/youtube/<videoId>/er")
def er(videoId):
    nlp = spacy.load("en_core_web_trf")
    strInput = getRaw(videoId)
    doc = nlp(strInput)
    ans = []
    for ent in doc.ents:
        ans.append(
            {
                "text": str(ent.text),
                "start_char": str(ent.start_char),
                "end_char": str(ent.end_char),
                "label": str(ent.label_),
            }
        )
    for ent in ans:
        print(ent)

    return json.dumps(ans)


@app.route("/vidoes/youtube/<videoId>")
def youtube(videoId):
    return getJson(videoId)


@app.route("/vidoes/youtube/<videoId>/raw")
def youtube_raw(videoId):
    return getRaw(videoId)
