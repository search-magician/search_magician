from apiclient.discovery import build
import json 
api_key = 'AIzaSyDtrJTNrq_Czfa261UXZIoqkLeo5sizg-I'

def getVideoData(id):
    youtube = build("youtube", "v3", developerKey=api_key)
    req = youtube.videos().list(part="snippet", id=id)
    res = req.execute()
    title = res['items'][0]['snippet']['title']
    des = res['items'][0]['snippet']['description']
    res = json.dumps({"title":title, "description":des}, indent=4, sort_keys=True)
    return res


def getListData(id):
    youtube = build("youtube", "v3", developerKey=api_key)
    req = youtube.playlistItems().list(part="snippet", playlistId=id)
    res = req.execute()
    ret = []
    for item in res['items']:
        ret.append({"title": item['snippet']['title'], "description": item['snippet']['description']})

    res = json.dumps(ret, indent=4, sort_keys=True)
    return res


if __name__ == "__main__":
    res = getListData("PLyzOVJj3bHQuloKGG59rS43e29ro7I57J")
    print(res)