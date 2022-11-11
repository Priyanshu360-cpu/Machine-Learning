import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import svm
X, y = make_classification(n_samples=10, random_state=0)
X_train , X_test , y_train, y_test = train_test_split(X, y, random_state=0)
clf = svm.SVC(kernel='precomputed')
gram_train = np.dot(X_train, X_train.T)
clf.fit(gram_train, y_train)
gram_test = np.dot(X_test, X_train.T)
clf.score(gram_test, y_test)
print(clf.predict(gram_test))