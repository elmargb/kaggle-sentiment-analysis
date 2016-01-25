#!/usr/bin/python

"""
decision_trees.py
Authors: Gabriela Tavares,      gtavares@caltech.edu
         Juri Minxha,           jminxha@caltech.edu
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree

import util

X_train, Y_train, X_test = util.loadData()


error_train = list()
error_test = list()
for i in xrange(10,13):
    clf = tree.DecisionTreeClassifier(criterion="gini", min_samples_leaf=i)
    clf = clf.fit(X_train, Y_train)
    error_train.append((1 - clf.score(X_train, Y_train)) * 100)
plt.figure()
plt.plot(range(10,13), error_train)
plt.xlabel('Min leaf node size')
plt.ylabel('Error %')
plt.legend(['Training', 'Test'], loc='lower right')
plt.show()

# error_train = list()
# error_test = list()
# for i in xrange(2,21):
#     clf = tree.DecisionTreeClassifier(criterion="gini", max_depth=i)
#     clf = clf.fit(X_train, Y_train)
#     error_train.append((1 - clf.score(X_train, Y_train)) * 100)
#     error_test.append((1 - clf.score(X_test, Y_test)) * 100)
# plt.figure()
# plt.plot(range(2,21), error_train)
# plt.plot(range(2,21), error_test)
# plt.xlabel('Max tree depth')
# plt.ylabel('Error %')
# plt.legend(['Training', 'Test'], loc='lower right')
# plt.show()