#!/usr/bin/python
#coding:utf-8

"""
堆和堆排序
"""

def PARRENT(i):
    return int(i/2)

def LEFT(i):
    return 2 * i + 1

def RIGHT(i):
    return 2 * i + 2

def MAX_HEAPIFY(A, i, heap_size=None):
    l = LEFT(i)
    r = RIGHT(i)
    # if heap_size is None:
    #     heap_size = len(A) - 1
    # else:
    #     heap_size -= 1

    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        # print "Exchage %d and %d" %(i, largest)
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, largest, heap_size)

def BUILD_MAX_HEAP(A):
    for i in range(int(len(A))//2, -1, -1):
        MAX_HEAPIFY(A, i)

def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    heap_size = len(A)

    for i in range((len(A) - 1), 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1                                   
        MAX_HEAPIFY(A, 0, heap_size)



A = range(0, 10)
print(A)
BUILD_MAX_HEAP(A)
print(A)
HEAPSORT(A)

print(A)