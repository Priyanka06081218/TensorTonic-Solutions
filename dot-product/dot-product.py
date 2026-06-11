import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    result=0.0
    if len(x) != len(y):
        raise ValueError("Vectors must have the same length")
    for i in range(len(x)):
        result += x[i]*y[i] 
    return float(result)
        
    pass