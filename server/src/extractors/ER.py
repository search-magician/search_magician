import spacy
import json

def main(txt):
    nlp = spacy.load("en_core_web_trf")
    doc = nlp(txt)
    ans = []
    for ent in doc.ents:
        ans.append(
            {
                "text": str(ent.text),
                "start_char": str(ent.start_char),
                "end_char": str(ent.end_char),
                "label": str(ent.label_),
            }
        )
    for ent in ans:
        print(ent)

    return json.dumps(ans)