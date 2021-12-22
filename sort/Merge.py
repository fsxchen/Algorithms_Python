#!/usr/bin/python
#coding:utf-8

"""
归并排序
"""

def megre_sort(A, p, r): 
    if p < r:
        # q = (p + r) // 2
        q = p + ((r - p) >> 1)
        megre_sort(A, p, q)
        megre_sort(A, q + 1, r)
        merge2(A, p, q, r)
    return A

def merge2(A, l, m, r):
    print(l, m, r)
    """
    0, 1, 3
    第二个版本的merge，和下面的本稍微不同
    """
    n1 = l
    n2 = m+1
    n = r -l + 1
    help = [None] * n

    i = 0
    while n1 <=m and n2 <= r:
        if A[n1] <= A[n2]:
            help[i] = A[n1]
            n1 += 1
        else:
            help[i] = A[n2]
            n2 += 1
        i += 1


    while n1 <= m:
        help[i] = A[n1]
        i += 1
        n1 += 1
    
    while n2 <= r:
        help[i] = A[n2]
        n2 += 1
        i += 1

    for j in range(n):
        A[l + j] = help[j]

    return A
 
def megre(A, p, q, r):
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
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A

A = [1, 90, 23, 13, 67, 53, 76, 100]
print(megre_sort(A, 0, len(A)-1))
