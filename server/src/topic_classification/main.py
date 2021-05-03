
import sys
# insert at 1, 0 is the script path 
sys.path.insert(1, '../search_magician/server')

import src.directoryVars as dr 
import test
import classification
from pandas import read_csv
from src.youtube.transcript import getRaw, getJson, _main

def startTheModule():
    print("1- to train the model")
    print("2- to test model via split testing dataset")
    print("3- to predict for new input")
    print("4- Partial Fit")
    ch =input()
    if ch == '1':
        classification.train()
    if ch == '2':
        test.evaluate()
    if ch == '3':
        print("Please Enter Youtube Video ID( After the v= in the link)")
        #vedioUrl=input()
        myfile=dr.addPath('topic_classification/testing/987522.txt')
        transcript = open(myfile, 'r')
        transcript=transcript.read()
        #transcript=getRaw(vedioUrl)
        print(transcript)
        print('')
        predicted_Topics , topics_probability=test.testnew(transcript)
        print("********************************************************")
        print(str(len(predicted_Topics))+' possible topics')
        for i in range(len(predicted_Topics)):
            print("predicted topic : "+ predicted_Topics[i])
            print("predicted Probability "+ str(topics_probability[i]))
    if ch == '4':
        test.partial_Fit()


def getTranscript(transcript):
    return testnew(transcript)


startTheModule()



