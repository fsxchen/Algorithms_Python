#!/usr/bin/env python
#coding:utf-8


import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
base_url = os.path.dirname(cur_dir)
import sys
sys.path.append(base_url)
# from ..time_utils import ti

from utils.time_utils import ti
from utils.test import random_int_list


@ti
def bubble_sort(A: list):
    """
    冒泡排序算法实现
    """
    length = len(A)
    i, j = 0, length

    for i in range(length - 1):
        for j in range(0, length - 1 - i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]



if __name__ == "__main__":
    A = random_int_list(length=100)
    print(A)
    bubble_sort(A)
    print(A) 

    B = [1, 3, 5.6, 67, 12, 23]

