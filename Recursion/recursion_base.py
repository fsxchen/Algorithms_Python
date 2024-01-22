#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: digui_xn.py
Description: 
Created_Time: 2016-09-03 17:17:04
Last modified: 2016-09-03 17时21分01秒
'''
_author = 'arron'
_email = 'fsxchen@gmail.com'
import time

"""
一些基础的递归算法实现

"""

def chengji(x, n):
    res = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        res *= x
    return res

def is_odd_num(n):
    return n%2

def chengji_dg(x, n):
    if n == 0:
        return 1
    elif is_odd_num(n):
        return x * chengji_dg(x, (n-1)/2) * chengji_dg(x, (n-1)/2)
    else:
        return chengji_dg(x, n/2) * chengji_dg(x, n/2)


def get_max(A, l, r):
    if l == r:
        return A[l]
    else:
        mid = l + ((r - l)>> 1)

        l_max = get_max(A, l, mid)
        r_max = get_max(A, mid+1, r)
        return max(l_max, r_max)

def find_max(A: list):
    n = len(A)
    return get_max(A, 0, n-1)

# start = time.time()
# chengji(2, 100000)
# end = time.time()
# print(end-start)


# start = time.time()
# chengji_dg(2, 100000)
# end = time.time()
# print(end-start)

if __name__ == "__main__":
    A = [1, 2, 88, 3, 5, 12, 3, 4, 55, 9]
    print(find_max(A))