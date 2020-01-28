from  sklearn import  datasets
iris=datasets.load_iris()
x=iris.data
y=iris.target
print(x,y)
from sklearn.model_selection import train_test_split

from sklearn import tree
classifier=tree.DecisionTreeClassifier()
classifier.fit(x,y)
a=[]
for x in range(0,4):
    x_test= float(input("enter 4 values"))
    a.append(x_test)
b=[a]
print(b)
predictions=classifier.predict(b)
from sklearn.metrics import accuracy_score
print(predictions)