"""
基础的概念
"""

"""
异或问题？
一个数组中，有一种数出现了奇数次，其他数出现了偶数次，怎么找到
"""

def find_odd_num(A):
    res = 0
    for i in A:
        res ^= i
    return res

"""
把一个整型的数据右侧的1提取出来。
"""
"""
一个数组中，有2种数出现了奇数次，其他数出现了偶数次，怎么找到
"""


def find_odd_num2(A):
    n = len(A)
    res = 0
    for i in A:
        res ^= i
    
    right_one = res & (~res + 1)

    only_one: int = 0

    for i in range(n):
        if (i & right_one != 0):
            only_one ^= i

    return only_one, only_one^res

"""
计算一个二进制数中，1的个数
"""
def count1(num: list):
    count = 0
    while num != 0:
        right_one = num & (~num + 1)
        num ^= right_one
        count += 1
    return count

if __name__ == "__main__":
    A = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 6, 6]
    print(find_odd_num2(A))

    print(count1(9))