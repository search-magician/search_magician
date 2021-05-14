import json
from src import app
from flask import request
from flask_cors import CORS
from src.extractors.main import getVideoData
from src.elastic.Elastic import index as videoIndex, search as videoSearch, test as elasticTest
from src.Video import Video
from src.youtube.videoData import getListData
from src.Query import Query
import requests
CORS(app)


@app.route("/")
def index():
    return "Hello World!"

@app.route("/videos/<videoId>", methods=["GET"])
def videoData(videoId):
    vid = Video(videoId)
    return vid.getVideoForElastic()


@app.route("/videos/<videoId>", methods=["POST"])
def addNewVideo(videoId):
    vid = Video(videoId)
    vidJson = vid.getVideoForElastic()
    return videoIndex(videoId, vidJson)
    

@app.route("/playlists/<playlistId>", methods=["POST"])
def addNewPlayList(playlistId):
    listData = getListData(playlistId)
    idList = []
    for item in listData:
        vid = Video(item["id"])
        idList.append(item["id"])
        vidJson = vid.getVideoForElastic()
        videoIndex(item["id"], vidJson)
    return json.dumps(idList)

# uses query parm 'q' for query text
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get('q') 
    q = Query(query)
    data = q.getQueryForElastic()
    print(data)
    ret = videoSearch(data)
    return ret

@app.route("/test")
def tt():
    res = requests.get('http://localhost:9200')
    print(res.data)
    return "lol"