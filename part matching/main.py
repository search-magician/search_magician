import gensim
from nltk import probability
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from heatmap import heatMap
import requests

print("Enter Video ID:")
Video_ID = input()
response = requests.get('http://127.0.0.1:5000/vidoes/youtube/' + Video_ID)
data = response.json()
Sentences= []
time = []
for x in data:
    Sentences.append(x['text'])
    time.append(x['start'])


def filteredSearch(str):

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(str)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    print(word_tokens)
    print(filtered_sentence)
    return filtered_sentence

def getSimilarityScore(raw_documents, words):
    gen_docs = [[w.lower() for w in word_tokenize(text)]
            for text in raw_documents]
    dictionary = gensim.corpora.Dictionary(gen_docs)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity(None,tf_idf[corpus],
                                      num_features=len(dictionary))

    query_doc_bow = dictionary.doc2bow(words)
    query_doc_tf_idf = tf_idf[query_doc_bow]

    return sims[query_doc_tf_idf]

def chooseBestWindow(sentences):
    sz = len(sentences)
    l = -1
    r = -1
    maxProbability = 0

    for k in range(max(int(0.05 * sz), 10), int(sz * 0.95)):
        print(k)
        Probability = 0
        for i in range(sz - 1 - k):
            if(i <= k):
                Probability += sentences[i]
            else:
                Probability += sentences[i]
                Probability -= sentences[i - k]
                if(Probability  >= maxProbability * k):
                    maxProbability = Probability / k
                    l = i - k
                    r = i
    return maxProbability, l , r

def fromMstoMinutes(milliseconds):
    Min = int(milliseconds / 60)
    sec = milliseconds % 60
    print(Min, ":", sec)
    return Min, sec

