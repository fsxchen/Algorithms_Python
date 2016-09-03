#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: hanoi.py
Description: 
Created_Time: 2016-09-03 17:22:49
Last modified: 2016-09-03 17时38分12秒
'''
_author = 'arron'
_email = 'fsxchen@gmail.com'


def hanoi(n, a, b, c):
    if n == 1:
        print "%s -> %s" % (a, c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

if __name__ == "__main__":
    hanoi(3,"A", "B", "C")
