'''
Author: yangxingchen
Date: 2017-08-19 15:54:05
LastEditors: yangxingchen
LastEditTime: 2022-02-09 17:08:58
Description: 
'''
#!/usr/bin/python
#coding:utf-8

def quick_sort(A, p, r):
    if p < r:
        q = parttion(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def parttion(A, p, r):
    x = A[r]
    i = p - 1        # i其实就是<=区域的边界
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            if i != j:
                A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def merge(A, p, q, r):
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

   

def quick_sort2(A: list):
    if not A:
        return
    n = len(A)
    merge_size = 1
    while merge_size < n:
        l = 0      # 左边字数组
        while l < n:
            m = l + merge_size - 1
            if m >= n:
                break

            r = min(m + merge_size, n-1)    # 右边可能不够
            print(merge_size, 'oooo', l, m, r)

            parttion(A, l,  r)
            print(A[l:r+1], 'AA')
            l = r + 1
        if merge_size > n // 2:
            break

        merge_size <<= 1

if __name__ == '__main__':
    A = [12, 123, 22, 66, 5, 134, 56, 1241, 541]
    quick_sort2(A)
    print(A)