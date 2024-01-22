"""
最大子数组和问题

问题描述

输入一个数组
输出：和最大的子数组
"""

def find_max_crossing_subarray(nums, s, e, mid):
    rigth = -99999
    left = -99999

    sum = 0

    for i in range(mid, s-1, -1):
        sum = sum + nums[i]

        if sum > left:
            left = sum

    sum = 0
    for j in range(mid + 1, e + 1):
        sum += nums[j]

        if sum > rigth:
            rigth = sum

    return left + rigth




def max_sub_arr(nums, s, e):
    if s == e:
        return nums[s]
    else:
        mid = (s + e) // 2

        print("mid is", mid)

        m1 = max_sub_arr(nums, s, mid)
        m2 = max_sub_arr(nums, mid+1, e)

        m3 = find_max_crossing_subarray(nums, s, e, mid)

        return max(m1, m2, m3)
        

def main():
    test_arr = [1, 2, -1, 2]
    print(max_sub_arr(test_arr, 0, len(test_arr)-1))

if __name__ == '__main__':
    main()

