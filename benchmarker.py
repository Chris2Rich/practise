import timeit as tm
import time

def add1(x):
    return x+1

print(tm.timeit(stmt=lambda:add1,number=100))