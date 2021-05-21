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
