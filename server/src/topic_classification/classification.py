#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html?highlight=news%20group#sklearn.datasets.fetch_20newsgroups
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_approximation import RBFSampler
import pickle
import src.directoryVars as dr
import numpy as np
# parameters for grid search
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf-svm__alpha': (1e-2, 1e-3)}
# clean the document by removing header , footers and fetch the dataset
remove = ('headers', 'footers', 'quotes')
news_train = fetch_20newsgroups(subset='train', shuffle=True , remove=remove)
news_test = fetch_20newsgroups(subset='test', shuffle=True , remove=remove)

def train():

    path = dr.addPath('topic_classification')

    
    text_clf_svm = SGDClassifier(loss='log', penalty='l2',alpha=1e-3, max_iter=10, random_state=42)
    x=news_train.data
    count_vect = CountVectorizer(stop_words='english')
    idf=TfidfTransformer()
    x=count_vect.fit_transform(x)
    x=idf.fit_transform(x)
    y=news_train.target

    classes=[]
    for i in range(0,200):
        classes.append(i)
    text_clf_svm=text_clf_svm.partial_fit(x, y,classes=classes)

    
    pickle.dump(text_clf_svm , open(path+"/svm2.sav", 'wb'))
    pickle.dump(count_vect , open(path+"/vect.vec", 'wb'))
    pickle.dump(idf , open(path+"/idf.vec", 'wb'))
    print("Training model is done")