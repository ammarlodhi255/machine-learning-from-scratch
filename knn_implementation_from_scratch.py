'''
    HOW DOES KNN WORK?

    Given a data point,
    1. Calculate the distance between the data point and all other data points in the dataset,
    2. Choose the K closest points,

    3. THEN,
    In case of regression: Take the average of the closest K values and assign it to the data point.
    In case of classification: Take the majority vote and assign that class to the data point.
'''


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [get_majority_vote(x) for x in X]
        return predictions


`


def get_majority_vote(self, x):
    # Compute the distances between all other data points in X_train
    return x
