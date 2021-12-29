#Big thanks to faykc on GitHub for the open source file
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

class Model():
    def __init__(self):
        # Load the trained model and TFIDF Vector
        tf1 = pickle.load(open("Models/tfidf_vocab.pickle", 'rb'))
        self.tfid = TfidfVectorizer(stop_words = "english",vocabulary = tf1.vocabulary_)
        self.model = pickle.load(open('Models/pa_clf.sav', 'rb'))
    def transformData(self, newCorpus):
        return self.tfid.fit_transform(newCorpus)
    def predict(self, data):
        return self.model.predict(self.transformData(data))
