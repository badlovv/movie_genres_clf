from joblib import load
import sklearn


class GenreClassifier:

    def __init__(self):
        self.tfidf = load("model/tfidf.joblib")
        self.clf = load("model/clf.joblib")
        self.count_vectorizer = load("model/count_vectorizer.joblib")
        self.genres = self.count_vectorizer.get_feature_names()

    def predict(self, text):
        tfidf_ = self.tfidf.transform([text])[0]
        return self.clf.predict(tfidf_)

    def predict_genre(self, text):
        pred = self.predict(text)
        pred_genres = [[name for name, el in zip(self.genres, list(y)) if el == 1] for y in pred]
        return pred_genres


if __name__ == '__main__':
    clf = GenreClassifier()
    # print(clf.genres)
    print(clf.predict_genre("All these protocols and procedures to make it seem "
                            "like you have it under control. But you're a bunch of boys "
                            "making models out of balsa wood. You don't have anything under control!"))
