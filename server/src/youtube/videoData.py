from apiclient.discovery import build
import json
from src.extractors.ER import getEntitiesNameList
from src.extractors.keywords import extractKeyWords
import os


def getVideoData(id: str) -> json:
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)
    req = youtube.videos().list(part="snippet", id=id)
    res = req.execute()
    title = res["items"][0]["snippet"]["title"]
    des = res["items"][0]["snippet"]["description"]
    res = json.dumps({"title": title, "description": des}, indent=4, sort_keys=True)
    return res


def getListData(id: str) -> json:
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)
    req = youtube.playlistItems().list(part="snippet", playlistId=id)
    res = req.execute()
    ret = []
    for item in res["items"]:
        ret.append(
            {
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
            }
        )

    return ret


def getTopicsFromList(id: str) -> json:
    listData = getListData(id)
    for item in listData:
        item["ER"] = getEntitiesNameList(item["description"])
        item["ER"].append(getEntitiesNameList(item["title"]))
        item["keywords"] = extractKeyWords(item["description"])
        item["keywords"].append(extractKeyWords(item["title"]))
    return listData


if __name__ == "__main__":
    res = getListData("PLyzOVJj3bHQuloKGG59rS43e29ro7I57J")
    print(res)
