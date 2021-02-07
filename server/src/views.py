from src import app
import xml.etree.ElementTree as ET
import requests
import json


@app.route("/")
def index():
    return "Hello World!"


@app.route("/vidoes/youtube/<videoId>")
def youtube(videoId):
    url = "http://video.google.com/timedtext?lang=en&v=" + videoId
    response = requests.request("GET", url)
    root = ET.fromstring(response.text)

    res = []
    for child in root:
        print(child.text, child.get("dur"))
        res.append(
            {"start": child.get("start"), "dur": child.get("dur"), "text": child.text}
        )

    return json.dumps(res, indent=4)
