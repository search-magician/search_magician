from sklearn.datasets import fetch_20newsgroups
import pickle
import sys
from pandas import read_csv
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
    
import src.directoryVars as dr
import scipy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
topics = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
          'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt',
          'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast',
          'talk.politics.misc', 'talk.religion.misc','None']
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21]
# dictionary -> key : topic index , value : topic name
topics_map = dict(zip(index, topics))
path = dr.addPath('topic_classification')
remove = ('headers', 'footers', 'quotes')
news_test = fetch_20newsgroups(subset='test', shuffle=True , remove=remove)
news_train = fetch_20newsgroups(subset='train', shuffle=True , remove=remove)
def evaluate():
    model = pickle.load(open(path+"/svm2.sav" , 'rb'))
    print(f"\n\n=================== SVM testing ===================")
    print("score : ", model.score(news_test.data, news_test.target))
    

def testnew(transcript):
    print(path)
    model = pickle.load(open(path+'/svm2.sav', 'rb'))
    transcript = StringIO(transcript)
    trans = read_csv(transcript , error_bad_lines = False)
    loaded_vectorizer = pickle.load(open(path+"/vect.vec" , 'rb'))
    idf = pickle.load(open(path+"/idf.vec" , 'rb'))
    trans=loaded_vectorizer.transform(trans)
    trans=idf.transform(trans)
    predicted = model.predict(trans) 
    #print("Score "+str(model.best_score_))
    print(f"\n\n=================== testing ===================")
    predicted_Topics = []
    
    for i in predicted:
        predicted_Topics.append(topics_map[i])
        #print(topics_map[i])

    topics_probability = model.predict_proba(trans)[:, 1]
    return predicted_Topics , topics_probability





def partial_Fit(transcript,topicsList):
    topics_map[22]='Computers'
    topics_map[23]='Science'
    model = pickle.load(open(path+"/svm2.sav" , 'rb'))
    loaded_vectorizer = pickle.load(open(path+"/vect.vec" , 'rb'))
    idf = pickle.load(open(path+"/idf.vec" , 'rb'))
    #myfile=dr.addPath('topic_classification/testing/987522.txt')
    #transcript = read_csv(myfile, error_bad_lines=False)
    x=transcript
    y=[22,23]
    
    x=loaded_vectorizer.transform(x)
    x=idf.transform(x)
    for i in range(0,x.shape[0]-2):
        y.append(21)
    print(y)
    print(model.classes_)
    classes=np.unique(y)
    model=model.partial_fit(x, y)
    pickle.dump(model , open(path+"/svm2.sav", 'wb'))
    print("\n\n=================== Partial Fit Success ===================")