import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(2000)
X = np.random.rand(200,2)


X[0:100,:] = X[0:100,:]*4 + 10
X[100:,:] = X[100:,:]*4 + 13
Y = np.ones(200)
Y[:100] = 0


plt.scatter(X[0:100,0],X[0:100,1],color="red")
plt.scatter(X[100:,0],X[100:,1],color="blue")
plt.show()

def dist(x1,x2):
    return np.sqrt(np.sum(np.power(np.subtract(x1,x2),2)))


def KNN(X, Y, queryPoint, k=5):
    vals = []
    m = X.shape[0]

    for i in range(m):
        d = dist(queryPoint, X[i])
        vals.append((d, Y[i]))

    vals = sorted(vals)
    vals = vals[:k]

    vals = np.array(vals)

    # print(vals)

    new_vals = np.unique(vals[:, 1], return_counts=True)

    # print(new_vals)

    index = new_vals[1].argmax()
    pred = new_vals[0][index]

    return pred
KNN(X,Y,[13,14])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

print(X_train.shape,X_test.shape)

print(Y_train.shape,Y_test.shape)
plt.scatter(X_train[:,0],X_train[:,1],c=Y_train)
plt.show()
query_1 = X_test[17]
query_2 = X_test[59]
plt.scatter(X_train[:,0],X_train[:,1],c=Y_train)
plt.scatter(query_1[0],query_1[1],color="red")
plt.scatter(query_2[0],query_2[1],color="blue")
plt.show()


def score(X_train, X_test, Y_train, Y_test):
    m = X_test.shape[0]

    y_pred = []

    for i in range(m):
        pred = KNN(X_train, Y_train, X_test[i])
        y_pred.append(pred)

    acc = accuracy_score(Y_test, y_pred)

    return acc

score(X_train,X_test,Y_train,Y_test)