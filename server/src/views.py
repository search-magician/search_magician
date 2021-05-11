import json
from src import app
from flask import request
from flask_cors import CORS
from src.extractors.main import getVideoData
from src.elastic.Elastic import index as videoIndex
from src.Video import Video
from src.youtube.videoData import getListData
CORS(app)


@app.route("/")
def index():
    return "Hello World!"

@app.route("/videos/<videoId>", methods=["GET"])
def videoData(videoId):
    vid = Video(videoId)
    return vid.getVideoFroElastic()


@app.route("/videos/<videoId>", methods=["POST"])
def addNewVideo(videoId):
    vid = Video(videoId)
    vidJson = vid.getVideoFroElastic()
    return videoIndex(videoId, vidJson)
    
    
@app.route("/playlists/<playlistId>", methods=["POST"])
def addNewPlayList(playlistId):
    listData = getListData(playlistId)
    idList = []
    for item in listData:
        vid = Video(item["id"])
        idList.append(vid)
        vidJson = vid.getVideoFroElastic()
        videoIndex(item["id"], vidJson)
    return idList