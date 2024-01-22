#!/usr/bin/python
#coding:utf-8

"""
求一个数组中最小的数
"""

def MINIMUM(A):
    MIN = A[0]
    for i in range(1, len(A)):
        if MIN > A[i]:
            MIN = A[i]
    return MIN

A = [1, 3, 4, 5, 0, -2, 3]
print MINIMUM(A)
