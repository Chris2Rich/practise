import numpy as np

def MSE(data, func):
    return ((np.vectorize(lambda x: x*x))(np.vectorize(func)(np.array(list(range(0,data.size)))) - data)).mean()

data = np.array([1,3,6,5,6,12,24])
func = lambda x: x + 2

print(MSE(data, func))