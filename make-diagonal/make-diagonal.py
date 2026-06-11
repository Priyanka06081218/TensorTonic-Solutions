import numpy as np

def make_diagonal(v):
    result = []

    for i in range(len(v)):
        row = []

        for j in range(len(v)):
            if i == j:
                row.append(v[i])
            else:
                row.append(0)

        result.append(row)

    return np.array(result)