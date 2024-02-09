import numpy as np
import timeit

def mse(data, func):
    return ((np.vectorize(lambda x: x*x))(np.vectorize(func)(np.array(list(range(0,data.size)))) - data)).mean()
    
def variance(data):
    return (np.vectorize(lambda x: x*x)(np.array([data.mean()]*data.size) - data)).sum() / data.size

data = np.array([1,2,3,6])
func = lambda x: x + 2
