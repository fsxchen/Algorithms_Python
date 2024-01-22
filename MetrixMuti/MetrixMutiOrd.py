#!/usr/bin/python
#coding:utf-8

import numpy as np

A = np.array([[1, 2, 3, 4],
            [3, 4, 5, 6],
            [5, 6, 7, 8],
            [7, 8, 9, 10]])

B = np.array([[9, 8, 7, 6],
            [1, 1, 1, 1],
            [2, 3, 4, 5],
            [3, 4, 5, 6]])

def MetrixMuti(A, B):
    """
    native function
    """
    C = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            C[i][j] = 0
            for k in range(C.shape[0]):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]

    return C



def MetrixMutiDiGui(A, B):
    """
    di gui method
    C11 = A11*B11 + A12*B21
    C12 = A11*B12 + A12*B22

    """
    C = np.zeros_like(A)
    ln = len(A[0])
    if ln == 1:
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        lln = ln/2
        An1 = A[ :lln, : lln]
        An2 = A[ :lln , lln:]
        An3 = A[lln: , : lln]
        An4 = A[lln: , lln: ]

        Bn1 = B[ :lln, : lln]
        Bn2 = B[ :lln , lln:]
        Bn3 = B[lln: , : lln]
        Bn4 = B[lln: , lln: ]

        #devid




print A
print B

print MetrixMuti(A, B)
# print A + B
# print A * B

M = np.array([[1]])
N = np.array([[2]])

print MetrixMutiDiGui(M, N)