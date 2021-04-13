from src import app
import spacy
from flask import request

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
    return ans;