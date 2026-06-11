import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    if len(x) != len(y):
        raise ValueError("Vectors must have the same length")

    result = 0.0

    for i in range(len(x)):
        result += (x[i] - y[i]) ** 2

    return float(result ** 0.5)