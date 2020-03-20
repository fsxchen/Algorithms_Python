#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: hanoi.py
Description: 
Created_Time: 2016-09-03 17:22:49
Last modified: 2020-03-20 19:34:56
'''
_author = 'arron'
_email = 'fsxchen@gmail.com'

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import time_utils

def hanoi(n, a, b, c):
    if n == 1:
        print("%s -> %s" % (a, c))
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

if __name__ == "__main__":
    time_utils.ti(hanoi)(3,"A", "B", "C")
