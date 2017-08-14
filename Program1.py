from sklearn import tree
import numpy as py
import matplotlib


features = [[140 ,0], [130, 0], [150, 1], [170, 1]]
labels = [0, 0, 1, 1]
toPredict = py.array([150, 1]);
toPredict = toPredict.reshape(1,-1);
print toPredict.shape
clf = tree.DecisionTreeClassifier();
clf = clf.fit(features, labels); 


print py
print matplotlib

print (clf.predict(toPredict)); 

#0 = smooth / apple
#1 = bumpy / orange
# look at file IO options


