#!/usr/bin/python
#coding:utf-8

def BUCKET_SORT(A):
    n = len(A)

    B = [None] * len(A)     # let B a new array!
    for i in range(n):
        B[i] = []           # let B become an empty array!

    for i in range(n):
        B[int(n*A[i])].append(A[i])
    
    C = []
    for j in range(n):
        if B[j]:
            B[j].sort()
    for k in B:
        if k:
            if type(k) == list:
                for l in k:
                    print l,
            else:
                print k,

A = [0.12, 0.23, 0.14, 0.5, 0.02, 0.1, 0.09, 0.9, 0.73, 0.08]

BUCKET_SORT(A)



