from math import ceil

import requests
from configurations import configuration

def main(videoId):
    url = 'https://youtube.googleapis.com/youtube/v3/search?relatedToVideoId='+videoId+'&type=video&key='+configuration.API_KEY
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    json_object = response.json()
    resultsNum = json_object["pageInfo"]["totalResults"]
    resultsPerPage = json_object["pageInfo"]["resultsPerPage"]
    pages = ceil(resultsNum / resultsPerPage)
    ret = []
    for i in range(pages):
        nextPageToken = ''
        try:
            nextPageToken = json_object["nextPageToken"]
        except:
            print("--Last page of results--")
        items = json_object["items"]
        for item in items:
            for key, value in item["id"].items():
                if key == 'videoId':
                    ret.append(value)
                    print(value)
        if nextPageToken is not None :
            response = requests.get(getNextPageUrl(nextPageToken, videoId), headers=headers)
            json_object = response.json()
    return ret
def getNextPageUrl(nextPageToken, videoId):
    url = 'https://youtube.googleapis.com/youtube/v3/search?pageToken='+nextPageToken+'&relatedToVideoId='+videoId+'&type=video&key='+configuration.API_KEY
    return url


if __name__ == "__main__":
    main('LnJwH_PZXnM')