import numpy as np

def relu(y):
    y=np.array(y,dtype=float)
    return np.maximum(0,y)