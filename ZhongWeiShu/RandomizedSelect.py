#!/usr/bin/python
#coding:utf-8

import sys, os

_ = __file__
CurDir = os.path.dirname(os.path.realpath(_))
AlogHome = os.path.dirname(CurDir)

# print AlogHome
sys.path.append(AlogHome)

from QuickSort import RandomQuickSort
def RANDOMIZED_SELECT(A, p, r, i):
    if p == r:
        return A[p]
    q = RandomQuickSort.RANDOM_PARTITION(A, p, r)
    k = q - p + 1
    if i == k:
        return A[k]
    elif i < k:
        return RANDOMIZED_SELECT(A, p, q - 1, i)
    else:
        return RANDOMIZED_SELECT(A, q + 1, r, i - k)

A = [12, 32, 1, 43, 33, 6, 25, 53, 11]

p = 0
r = len(A) - 1
i = 3
RANDOMIZED_SELECT(A, p, r, i)
