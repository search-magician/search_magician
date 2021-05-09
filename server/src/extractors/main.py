from src.extractors.ER import getEntitiesList
from src.extractors.keywords import extractKeyWords
from src.youtube.transcript import getRaw
from src.topic_classification.main import getTranscript as getClasses
from src.youtube.videoData import getVideoData


def getVideoData(videoId):
    transRaw = getRaw(videoId)
    ER = getEntitiesList(transRaw)
    keywords = extractKeyWords(transRaw)
    classes , classes_prob = getClasses(transRaw)

    tags = []
    for i in ER:
        tags.append(i["text"])
    
    for i in keywords:
        tags.append(i[0])

    tags = list(set(tags))

    return {"transcript": transRaw,
            "tags": tags,
            "classes": classes
            }
