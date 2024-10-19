import numpy as np
# 1. Define two custom numpy arrays, say A and B. Generate two new numpy
# arrays by stacking A and B vertically and horizontally.

A = np.array([1,2,3,4])
B = np.array([5,6,7,8])

C = np.vstack((A, B))
D = np.hstack((A, B))
print("The vertical stack", C)
print("The Horizontal stack", D)

# 2. Find common elements between A and B. [Hint : Intersection of two sets]

A = np.array([1,3,4,5])
B = np.array([5,6,1,8])
C = np.intersect1d(A,B)
print("The common elements of A & B are", C)

# 3.  Extract all numbers from A which are within a specific range. eg between 5 and 10

A = np.array([1,3,4,5,6,7,8])
B = A[np.where((A>5) & (A<10))]
print("The extracted value is ", B)

# 4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
# This did not work for me Thus using an alternate method 

import requests
from io import StringIO

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(url).text
iris_2d = np.genfromtxt(StringIO(data), delimiter=',', dtype='float', usecols=[0,1,2,3])
result = []
for i in iris_2d:
    if i[2]>1.5 and i[0]<5.0:
        result.append(i)

print(len(result))
print(result)




