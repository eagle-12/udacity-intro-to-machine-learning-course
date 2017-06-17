#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# to get the number of features bein used to train the classifier
ans = len(features_train[0])
print ans


#########################################################
### your code goes here ###
from sklearn import tree

# to consider only 1 per cent of the training data
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
clf = tree.DecisionTreeClassifier(min_samples_split = 40)
clf = clf.fit(features_train,labels_train)
pre = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pre,labels_test)

print acc

#########################################################


