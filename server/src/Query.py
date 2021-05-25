from src.extractors.ER import getEntitiesNameList
from src.extractors.keywords import extractKeyWords
from src.topic_classification.main import getTranscript as getClasses

class Query:
    def __init__(self, txt):
        self.Er = None
        self.txt = txt
        self.keywords = None
        self.tags = None
        self.classes = None

    def getEr(self):
        if self.Er:
            return self.Er
        self.Er = getEntitiesNameList(self.txt)
        return self.Er

    def getKeywords(self):
        if self.keywords:
            return self.keywords
        self.keywords = extractKeyWords(self.txt)
        return self.keywords

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

        self.classes , _ = getClasses(self.txt)
        return self.classes

    def getQueryForElastic(self):
        return ({
        "_source": False,
            "query": {
                "bool":{
                    "should":[
                        {"match":{"transcript": self.txt}},
                        {"terms":{"tags": self.getTags() }},
                        {"terms":{"classes": self.getClasses()}}
                    ]
                }
            }
        })

