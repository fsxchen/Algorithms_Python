#!/usr/bin/env python
import time

def zhishu1(x, n):
    res = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        res *= x
    return res

def isJs(n):
    return n%2

def zhishu_dg(x, n):
    if n == 0:
        return 1
    elif isJs(n):
        return x * zhishu_dg(x, (n-1)/2) * zhishu_dg(x, (n-1)/2)
    else:
        return zhishu_dg(x, n/2) * zhishu_dg(x, n/2)

start = time.time()
zhishu1(2, 100000)
end = time.time()
print end-start


start = time.time()
zhishu_dg(2, 1000000)
end = time.time()
print end-start
