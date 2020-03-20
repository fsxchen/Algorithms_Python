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
求x^n的结果.

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

start = time.time()
chengji(2, 100000)
end = time.time()
print(end-start)


start = time.time()
chengji_dg(2, 100000)
end = time.time()
print(end-start)
