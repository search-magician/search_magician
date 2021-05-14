from elasticsearch import Elasticsearch
es = Elasticsearch(["localhost:9200"])

def index(videoId, videoData):
    ret = es.index(index='videos', body=videoData, id=videoId)
    return ret

def search(query):
    ret = es.search(index='videos', body=query)
    return ret

def test():
    print(es.ping())

def createVideoIndex():
    mapping = {
         "settings": {
            "analysis": {
            "normalizer": {
                "my_normalizer": {
                "type": "custom",
                "char_filter": [],
                "filter": ["lowercase", "asciifolding"]
                }
            }
            }
        },
        "mappings": {
            "properties": {
                "classes": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "normalizer": "my_normalizer",
                            "ignore_above": 256
                        }
                    }
                },
                "tags": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "normalizer": "my_normalizer",
                            "ignore_above": 256
                        }
                    }
                },
                "transcript": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "normalizer": "my_normalizer",
                            "ignore_above": 256
                        }
                    }
                }
            }
        }
    }
    es.indices.create(index="videos", body=mapping)

def clear():
    es.indices.delete(index="videos")