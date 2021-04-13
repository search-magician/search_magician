import xml.etree.ElementTree as ET
import requests
import json


def _main(videoId):
    url = "http://video.google.com/timedtext?lang=en&v=" + videoId
    response = requests.request("GET", url)
    root = ET.fromstring(response.text)

    res = []
    for child in root:
        print(child.text, child.get("dur"))
        res.append(
            {"start": child.get("start"), "dur": child.get("dur"), "text": child.text}
        )
    return res


def getJson(videoId):
    res = _main(videoId)
    return json.dumps(res, indent=4)


def getRaw(videoId):
    res = _main(videoId)
    rawText = ""
    for sen in res:
        rawText += sen["text"] + "\n"

    return rawText
