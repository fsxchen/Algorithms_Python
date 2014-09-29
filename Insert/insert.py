#!/usr/bin/env python
#coding:utf-8

A = [1, 3, 5.6, 67, 12, 23]

# print A

def INSERTON_SORT(A):    
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        print "Key is:", key, "and A is:", A
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

INSERTON_SORT(A)
print A 
