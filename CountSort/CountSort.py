#!/usr/bin/python
#coding:utf-8

def CONTING_SORT(A, B, k):
    C = [0] * (k + 1)
    for i in range(k + 1):
        C[i] = 0
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    # print "Now the C[i] ->", C
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    # print "The count of less i", C
    
    for j in range(len(A) -1, -1, -1):
        print "A[%d] is %d, the count is %d" % (j, A[j], C[A[j]]) 
        B[C[A[j]] - 1] = A[j]
    
        C[A[j]] = C[A[j]] - 1

    print "A is", A
    print "The result is", B
    
A = [12, 3, 18, 29, 9, 17, 6, 8, 9, 3]
print "Input A is", A
B = [0] * len(A)
CONTING_SORT(A, B, 30)