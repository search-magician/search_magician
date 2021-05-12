import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
def getSynonyms(words):
    synonyms = []
    for w in words:
        for syn in wordnet.synsets(w[0]):
            for l in syn.lemmas():
                if l.name() not in synonyms:
                    synonyms.append(l.name())
    return synonyms



            