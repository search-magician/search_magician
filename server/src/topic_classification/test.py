from sklearn.datasets import fetch_20newsgroups
import pickle
import sys
from pandas import read_csv
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
    
import src.directoryVars as dr

topics = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
          'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt',
          'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast',
          'talk.politics.misc', 'talk.religion.misc']
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# dictionary -> key : topic index , value : topic name
topics_map = dict(zip(index, topics))
path = dr.addPath('topic_classification')

def evaluate():
    model = pickle.load(open(path+"/svm.sav" , 'rb'))
    print(f"\n\n=================== SVM testing ===================")
    print("score : ", model.best_score_)

def testnew(transcript):
    print(path)
    model = pickle.load(open(path+'/svm.sav', 'rb'))
    transcript = StringIO(transcript)
    trans = read_csv(transcript , error_bad_lines = False)
    predicted = model.predict(trans) 
    print("Score "+str(model.best_score_))
    print(f"\n\n=================== testing ===================")
    predicted_Topics = []
    
    for i in predicted:
        predicted_Topics.append(topics_map[i])
        #print(topics_map[i])

    topics_probability = model.predict_proba(trans)[:, 1]
    return predicted_Topics , topics_probability