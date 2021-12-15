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
def insertion_sort(A: list):
    """
    插入排序算法实现
    """
    n = len(A)
    for j in range(1, n):
        # 从第二元素开始，因为默认的第一个元素是有序的
        key = A[j]
        i = j - 1
        # print "Key is:", key, "and A is:", A
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key                 # 为什么每轮结束之后，有一个赋值的操作呢？在代码中可以得到答案，其实这里的操作并不是交换两个的位置，而是把当前的值
                                       # 往后挪动了一个位置。

@ti
def insertion_sort_v2(A: list):
    """
    插入排序的另一种实现，如果是采用交换元素的话，那么就不用占坑了。
    """
    n = len(A)
    for j in range(1, n):
        # 从第二元素开始，因为默认的第一个元素是有序的
        key = A[j]
        i = j - 1
        # print "Key is:", key, "and A is:", A
        while i >= 0 and A[i] > key:
            A[i + 1], A[i] = A[i], A[i+1]
            i = i - 1
        # A[i + 1] = key



if __name__ == "__main__":
    A = random_int_list()
    insertion_sort_v2(A)
    print(A) 

    B = [1, 3, 5.6, 67, 12, 23]

