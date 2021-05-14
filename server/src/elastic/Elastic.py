from elasticsearch import Elasticsearch


def index(videoId, videoData):
    es = Elasticsearch(["localhost:9200"])
    ret = es.index(index='videos', body=videoData, id=videoId)
    return ret

def search(query):
    es = Elasticsearch(["localhost:9200"])
    ret = es.search(index='videos', body=query)
    return ret

def test():
    es = Elasticsearch(['localhost:9200'])
    print(es.ping())