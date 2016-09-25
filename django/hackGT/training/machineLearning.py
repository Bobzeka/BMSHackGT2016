import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import string
class machineLearning:
    gnb = MultinomialNB()
    def __init__(self):
        mydata = pd.read_csv("training.csv")
        training = mydata["Training"]
        for i in range(0, len(training)):
            training[i] = unicode(training[i], errors = 'replace')
        self.count_vect = CountVectorizer()
        counts = self.count_vect.fit_transform(training)
        counts.shape
        self.count_vect.vocabulary_.get(u'algorithm')
        tf_transformer = TfidfTransformer(use_idf=False).fit(counts)
        X_count_tf = tf_transformer.transform(counts)
        X_count_tf.shape
        self.tfidf_transformer = TfidfTransformer()
        X_count_tfidf = self.tfidf_transformer.fit_transform(counts)
        X_count_tfidf.shape
        self.gnb.fit(X_count_tfidf, mydata['Target'])
    def predict(self, predict):
        predict = pd.read_csv(predict)
        docs_new = predict['Testing']
        X_new_counts = self.count_vect.transform(docs_new)
        X_new_tfidf = self.tfidf_transformer.transform(X_new_counts)
        predicted = self.gnb.predict(X_new_tfidf)
        return predicted
