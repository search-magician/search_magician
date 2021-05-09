from elasticsearch import Elasticsearch
es = Elasticsearch()


def index(videoId, videoData):
    ret = es.index(index='videos', body=videoData, id=videoId)
    return ret