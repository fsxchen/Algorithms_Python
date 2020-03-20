#!/usr/bin/env python
#coding:utf-8


import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
base_url = os.path.dirname(cur_dir)
import sys
sys.path.append(base_url)
# from ..time_utils import ti

from time_utils import ti
A = [1, 3, 5.6, 67, 12, 23]

# print A

@ti
def INSERTON_SORT(A):    
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        # print "Key is:", key, "and A is:", A
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

INSERTON_SORT(A)
print A 

B = [1, 3, 5.6, 67, 12, 23]
@ti
def INSERTON_SORT_X(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > 0:
            if A[i] > key:
                A[i + 1] = A[i]
                i = i -1
            else:
                break
        A[i+1]
INSERTON_SORT_X(B)

def MAO_PAO(A):
    for j in range(len(A)):
        for i in range(j+1, len(A)):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
#MAO_PAO(A)
#print(A)
