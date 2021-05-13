
import sys
# insert at 1, 0 is the script path 
sys.path.insert(1, '../search_magician/server')

import spacy
import json


def _main(txt: str) -> json:
    nlp = spacy.load("en_core_web_trf")
    doc = nlp(txt)
    data = []
    for ent in doc.ents:
        data.append(
            {
                "text": str(ent.text),
                "start_char": str(ent.start_char),
                "end_char": str(ent.end_char),
                "label": str(ent.label_),
            }
        )
    return data


def getEntitiesNameList(txt: str) -> list:
    '''
        return a list of entities name in the txt
    '''
    data = _main(txt)
    entitiesList = []
    for item in data:
        entitiesList.append(item["text"])
    entitiesList = list(set(entitiesList))
    return entitiesList


def getEntitiesList(txt: str) -> list:
    '''
        return a list of entities name and type in the txt
    '''
    data = _main(txt)
    entitiesList = []
    for item in data:
        entitiesList.append({"text": item["text"], "type": item["label"]})
    
    # entitiesList = list(set(entitiesList))
    return entitiesList