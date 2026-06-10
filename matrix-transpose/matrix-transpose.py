import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    transpose=[]
    for col  in range(len(A[0])):
        row=[]
        for r in A:
            row.append(r[col])
        transpose.append(row)
    return np.array(transpose)
