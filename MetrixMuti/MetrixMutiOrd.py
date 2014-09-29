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
    C = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            C[i][j] = 0
            for k in range(C.shape[0]):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]

    return C 

print A
print B

print MetrixMuti(A, B)
# print A + B
# print A * B