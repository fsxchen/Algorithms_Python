#!/usr/bin/python
#coding:utf-8

"""
同时数组中最小和最大的数
method1:
    第一遍求最小值
    第二次求最大值
    时间复杂度2O(n)
method2:
    遍历的时候，同时处理最大值和最小值
    复杂度：O(n)
"""

def MINIMUM(A):
    MIN = A[0]
    for i in range(1, len(A)):
        if MIN > A[i]:
            MIN = A[i]
    return MIN

A = [1, 3, 4, 5, 0, -2, 3]
print MINIMUM(A)
