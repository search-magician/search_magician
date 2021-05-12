import nltk
from nltk.corpus import wordnet
import spacy
import numpy as np
from numba import jit
nlp = spacy.load('en_core_web_lg')

nltk.download('wordnet')
def getSynonyms(words):
    synonyms = []
    for w in words:
        for syn in wordnet.synsets(w[0]):
            for l in syn.lemmas():
                if l.name() not in synonyms:
                    synonyms.append(l.name())
    return synonyms



            