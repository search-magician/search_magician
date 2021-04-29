import spacy
import json


def main(txt: str) -> json:
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


def getEntitiesList(txt: str) -> list:
    data = main(txt)
    entitiesList = []
    for item in data:
        entitiesList.append(item["text"])

    return entitiesList
