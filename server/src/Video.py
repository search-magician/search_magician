from src.youtube.transcript import getRaw
from src.extractors.ER import getEntitiesNameList
from src.youtube.videoData import getVideoData
from src.extractors.keywords import extractKeyWords
from src.topic_classification.main import getTranscript as getClasses

class Video:
    def __init__(self, id):
        self.id = id
        self.Er = None
        self.transcript = None
        self.keywords = None
        self.youtubeData = { "title": None, "description": None }
        self.tags = None
        self.classes = None

    def getTranscript(self):
        if self.transcript:
            return self.transcript
        self.transcript = getRaw(self.id)
        return self.transcript
    

    def getEr(self):
        if self.Er:
            return self.Er
        self.Er = getEntitiesNameList(self.getTranscript())
        return self.Er

    def getKeywords(self):
        if self.keywords:
            return self.keywords
        self.keywords = extractKeyWords(self.getTranscript())
        return self.keywords

    def getYoutubeData(self):
        if self.youtubeData["title"]:
            return self.youtubeData
        self.youtubeData = getVideoData(self.id)
        return self.youtubeData

    def getTags(self):
        if self.tags:
            return self.tags
        
        self.tags = []
        for i in self.getEr():
            self.tags.append(i)
        
        for i in self.getKeywords():
            self.tags.append(i[0])

        self.tags = list(set(self.tags))
        return self.tags

    def getClasses(self):
        if self.classes:
            return self.classes

        self.classes , _ = getClasses(self.getTranscript())
        return self.classes

    def getVideoForElastic(self):
        return {"transcript": self.getTranscript(),
            "tags": self.getTags(),
            "classes": self.getClasses()
            }

