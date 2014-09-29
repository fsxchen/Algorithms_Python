#!/usr/bin/python
#coding:utf-8
def megre_sort(A, p, r): 
    if p < r:
        q = (p + r) // 2
        print "first: p, q, r", p, q, r, "megre_sort(A, %s, %s)" %(p, q)
        megre_sort(A, p, q)
        print "two: p, q, r", p, q, r, q, "megre_sort(A, %s, %s)" %(p, q)
        megre_sort(A, q + 1, r)
        print "three: p, q, r", p, q, r, "megre_sort(A, %s, %s)" %(p, q)
        megre(A, p, q, r)
    print "The result is:", A
    return A
 
def megre(A, p, q, r):
    print "to begin the megre and exec: megre(A, %s, %s, %s)" %(p, q, r)
    n1 = q - p + 1
    n2 = r - q
 
    L = [None] *n1
    R = [None] *n2
    # print A

    for i in range(n1):
       L[i] = A[i + p]
    L.append(float("inf"))
    for j in range(n2):
        R[j] = A[q + j + 1]
    R.append(float("inf"))
 
    i = j = 0;
    print "L is:", L, "R is:", R
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    print "The megre result is:", A
    return A
 
A = [1, 90, 23, 13, 67, 53, 76, 100]
print megre_sort(A, 0, len(A)-1)
