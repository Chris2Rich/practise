import numpy as np

x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
y = np.array([[1,3],
              [4,6]])

print(y in x)