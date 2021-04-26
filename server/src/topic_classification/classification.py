#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html?highlight=news%20group#sklearn.datasets.fetch_20newsgroups
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
import pickle


# parameters for grid search
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf-svm__alpha': (1e-2, 1e-3)}
# clean the document by removing header , footers and fetch the dataset
remove = ('headers', 'footers', 'quotes')
news_train = fetch_20newsgroups(subset='train', shuffle=True , remove=remove)
news_test = fetch_20newsgroups(subset='test', shuffle=True , remove=remove)

def train():

    path = "./"

    text_clf_svm = Pipeline([('vect', CountVectorizer(stop_words='english')), ('tfidf', TfidfTransformer()),
                             ('clf-svm', SGDClassifier(loss='log', penalty='l2',alpha=1e-3, max_iter=5, random_state=42))])

    gs_clf = GridSearchCV(text_clf_svm, parameters, n_jobs=-1)

    gs_clf = gs_clf.fit(news_train.data, news_train.target)

    pickle.dump(gs_clf , open(path+"svm.sav", 'wb'))
    print("Training model is done")