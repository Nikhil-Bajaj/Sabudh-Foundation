import numpy as np
import random
a =np.random.random((3,3)) #return a 3, 3 array
print(a)
print("hiiii")
b = np.random.rand(5,3,3) #returns positive random float number i 5 sets of 3,3 array
print(b)
c = np.random.randn(2,3,3) #returns negative 2 sets of 3,3 array
print(c)
d = np.random.randint(100,200) #It returns a int value b/w 100-200
print(d)
e = np.random.randint(200,500,size=(200,2))
print(e)
name_list=['Hi','Dear','hw','are','you']
f=np.random.choice(name_list, size=(3,3))
print(f)
g=np.random.choice(name_list, size=(3,3),p=[0.1,0.2,0,0.5,0.2])
print(f)
random.seed(3000)

