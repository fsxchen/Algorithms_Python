'''
@Author: yangxingchen
@Date: 2020-04-10 19:21:16
@LastEditors: yangxingchen
@LastEditTime: 2020-04-10 19:35:39
@Description: 
'''

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
base_url = os.path.dirname(cur_dir)
import sys
sys.path.append(base_url)
# from ..time_utils import ti

from utils.time_utils import ti
from utils.test import random_int_list

@ti
def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # 找到最小的元素
            if A[j] < A[min_index]:
                min_index = j
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
            
if __name__ == "__main__":
    A = random_int_list()
    print(A)
    selection_sort(A)
    print(A)