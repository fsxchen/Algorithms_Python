#!/usr/bin/python
#coding:utf-8

def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q - 1)
        QUICKSORT(A, q + 1, r)

def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            if i != j:
                A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

if __name__ == '__main__':
    A = [12, 123, 22, 66, 5, 134, 56, 1241, 541]
    QUICKSORT(A, 0, len(A) - 1)
    print(A)