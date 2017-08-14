import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm


digits = datasets.load_digits()

classifier = svm.SVC(gamma=0.001, C=100)

#print digits.data
#print digits.target
#print digits.images[0]
#print ("data= ", digits.data[-1])
#print len(digits.data)

x,y = digits.data[:-10], digits.target[:-10]

classifier.fit(x,y)


print("Predictoin:", classifier.predict(digits.data[-1]));
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest");
plt.show()






#my_cmap = matplotlib.cm.get_cmap('gray_r')




## USE http://python-guide-pt-br.readthedocs.io/en/latest/scenarios/scrape/
