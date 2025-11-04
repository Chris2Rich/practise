import numpy as np
import math
import matplotlib.pyplot as plt
from typing import Optional

lengths = (1,3) #Array of lengths separating each motor
target = (2,2)

mag = lambda v: np.sqrt(np.sum(np.square(v)))
def solvefk2d(angles: np.array, lengths: np.array, target: tuple) -> float: # returns distance from target squared
    d = (target[0] - np.sum(np.cos(angles) * lengths)) ** 2 + (target[0] - np.sum(np.sin(angles) * lengths)) ** 2
    return None

def solveik2d(lengths: tuple, target: tuple) -> Optional[tuple]:
    if mag(lengths) < mag(target):
        return None
    
    return None

print(mag(lengths), mag(target))