# 问题分类器
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
from questions import *


class Question_classify():
    def __init__(self):
        self.train_x, self.train_y = self.load_data
        self.model = self.train_NB()

    @property
    def load_data(self):
        train_x = []
        train_y = []
        questions = [q0, q1, q2, q3, q4, q5, q6, q7, q8]
        for q in questions:
            label = questions.index(q)
            for line in q:
                word_list = list(jieba.cut(str(line).strip()))
                train_x.append(" ".join(word_list))
                train_y.append(label)
        return train_x, train_y

    def train_NB(self):
        x_train, y_train = self.train_x, self.train_y
        self.tv = TfidfVectorizer()
        train_data = self.tv.fit_transform(x_train).toarray()
        clf = MultinomialNB(alpha=0.01)
        clf.fit(train_data, y_train)
        return clf

    def predict(self, question):
        question = [" ".join(list(jieba.cut(question)))]
        test_data = self.tv.transform(question).toarray()
        predict = self.model.predict(test_data)[0]
        return predict
