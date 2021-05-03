from src.extractors.ER import getEntitiesList
from src.extractors.keywords import extractKeyWords
from src.youtube.transcript import getRaw
from src.topic_classification.main import getTranscript as getClasses

def getVideoData(videoId):
    transRaw = getRaw(videoId)
    ER = getEntitiesList(transRaw)
    keywords = extractKeyWords(transRaw)
    
    classes , classes_prob = getClasses(transRaw)

    return {"transcript": transRaw,
            "ER": ER,
            "keywords": keywords,
            "classes":{
                "classes": classes,
                "prob": classes_prob.tolist()
                }
            }
