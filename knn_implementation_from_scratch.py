'''
    HOW DOES KNN WORK?

    Given a data point,
    1. Calculate the distance between the data point and all other data points in the dataset,
    2. Choose the K closest points,

    3. THEN,
    In case of regression: Take the average of the closest K values and assign it to the data point.
    In case of classification: Take the majority vote and assign that class to the data point.
'''

from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np


def euclidean_dist(x1, x2):
    return np.sqrt(np.sum(x1-x2)**2)


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self.get_class(x) for x in X]
        return predictions

    def get_class(self, x):
        # Compute the distances between all other data points in X_train
        distances = [euclidean_dist(x, x_train) for x_train in self.X_train]

        # Get the closest K neighbors
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [y_train[i] for i in k_indices]

        # Get the majority vote
        return self.get_majority_vote(k_labels)

    def get_majority_vote(self, k_labels):
        label_counts = {}

        for label in k_labels:
            if label not in label_counts:
                label_counts[label] = 1
            else:
                label_counts[label] = label_counts[label] + 1

        max_label = 0
        max_occurence = 0

        for key, value in label_counts.items():
            if max_occurence < label_counts[key]:
                max_label = key
                max_occurence = label_counts[key]

        return max_label


# Testing on IRIS Dataset
iris_ds = datasets.load_iris()
X, y = iris_ds.data, iris_ds.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

knn = KNN(k=5)

knn.fit(X_train, y_train)
print(knn.predict(X_test[:10]))
print(y_test[:10])
print('Accuracy: ' + str(np.sum(knn.predict(X_test) == y_test) / len(y_test)))
