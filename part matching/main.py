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



