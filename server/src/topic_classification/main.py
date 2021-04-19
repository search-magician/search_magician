#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html?highlight=news%20group#sklearn.datasets.fetch_20newsgroups
from src.topic_classification.test import testnew
import src.topic_classification.classification
from pandas import read_csv

def startTheModule():
    print("1- to train the model")
    print("2- to test model via split testing dataset")
    print("3- to predict for new input")
    ch =input()
    if ch == '1':
        classification.train()
    if ch == '2':
        test.evaluate()
    if ch == '3':
        transcript = read_csv('./testing/987522.txt', error_bad_lines=False)
        test.testnew(transcript)

def getTranscript(transcript):
    return testnew(transcript)


#startTheModule()

