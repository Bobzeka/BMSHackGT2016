import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import string
class machineLearning:
    gnb = MultinomialNB()
    def __init__(self, predict):
        self.predict = predict
    def learn():
        mydata = pd.read_csv("training.csv")
        predict = pd.read_csv(predict)
        training = mydata["Training"]
        for i in range(0, len(training)):
            training[i] = unicode(training[i], errors = 'replace')
        count_vect = CountVectorizer()
        counts = count_vect.fit_transform(training)
        counts.shape
        count_vect.vocabulary_.get(u'algorithm')
        tf_transformer = TfidfTransformer(use_idf=False).fit(counts)
        X_count_tf = tf_transformer.transform(counts)
        X_count_tf.shape
        tfidf_transformer = TfidfTransformer()
        X_count_tfidf = tfidf_transformer.fit_transform(counts)
        X_count_tfidf.shape
        gnb.fit(X_count_tfidf, mydata['Target'])
    def predict(predict):
        docs_new = predict['Testing']
        X_new_counts = count_vect.transform(docs_new)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)
        predicted = gnb.predict(X_new_tfidf)
        return predicted
