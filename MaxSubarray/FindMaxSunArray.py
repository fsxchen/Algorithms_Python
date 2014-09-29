#!/usr/bin/python
#coding:utf-8

def FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high):
    left_Sum = -float("inf")
    Sum = 0
    for i in range(mid, low - 1, -1):
        Sum = Sum + A[i]
        if Sum > left_Sum:
            left_Sum = Sum
            max_left = i

    right_Sum = -float("inf")
    Sum = 0
    max_right = 0
    print mid, high
    for j in range(mid + 1, high + 1):
        Sum = Sum + A[j]
        if Sum > right_Sum:
            right_Sum = Sum
            max_right = j

    return max_left, max_right, left_Sum + right_Sum

def FIND_MAXIMUM_SUBARRAY(A, low, high):
    if low == high:
        return (low, high, A[low])
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_Sum = \
            FIND_MAXIMUM_SUBARRAY(A, low, mid)
        right_low, right_high, right_Sum = \
            FIND_MAXIMUM_SUBARRAY(A, mid + 1, high)
        cross_low, cross_high, cross_Sum = \
            FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)

        if max([left_Sum, right_Sum, cross_Sum]) == left_Sum:
            return left_low, left_high, left_Sum
        elif max([left_Sum, right_Sum, cross_Sum]) == right_Sum:
            return right_low, right_high, right_Sum
        else:
            return cross_low, cross_high, cross_Sum
A = [13, 24, -23, -34, -67, -11, 45, 36, -5, 6, 100,]

low = 0
high = len(A) - 1
mid = int(high / 2)
print low, mid, high
# print FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)

print FIND_MAXIMUM_SUBARRAY(A, low, high)