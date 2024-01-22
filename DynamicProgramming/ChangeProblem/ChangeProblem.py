'''
Author: yangxingchen
Date: 2020-04-14 11:08:53
LastEditors: yangxingchen
LastEditTime: 2021-01-21 12:07:56
Description: 
'''
"""
找零钱问题
要求，使用的硬币最少找领
"""

def change_greedy(coin_list, money):
    # 先排序
    coin_list.sort(reverse=True)
    result = []
    for i in coin_list:
        while money >= i:
            money -= i
            result.append(i)
    return result

def change_recursion(coin_list, money):
    """
    递归解法
    Args:
        coin_list (list): 找零的单元列表
        money (int): 需要找多少钱
    Returns:
        int: 返回次数
    """
    if money == 0:
        return 0
    best = -1
    for coin in coin_list:
        if (coin > money):   # 硬币面值比需要找零的大，因此找不了
            continue
        next_try = change_recursion(coin_list, money - coin)
        if best < 0 or best > next_try + 1:     # best初始化会为-1
            best = next_try + 1
    return best

def coinChange(coins, amount) -> int:
    MAX_INT = 999999999
    # 第一步，构建状态数组
    f = [0] * (amount + 1)
    f[0] = 0
    # 划分子问题，子问题，为，需要使用多少枚硬币拼出27-a_k枚硬币
    for i in range(1, amount + 1):
        # 计算拼出1、2...amount块钱最少的情况。
        # 这种方式是从底层到上层 一层层的构建
        f[i] = MAX_INT
        # last coin A[j]
        # f[i] = min {f[i-A[0] + 1], f[i - A[n - 1] + 1 ...]}
        for j in coins:
            if j > i:      # coins 的值大于要找零的,这次循环将无效
                continue
            if f[i - j] != MAX_INT:    # 这里其实就是转移方程使用了。
                f[i] = min(f[i - j] + 1, f[i])
        # 转移方程如下
    print(f)
    return f[amount] if f[amount] != MAX_INT else -1

if __name__ == "__main__":
    coin_list = [2, 5, 7]
    n = 3
    # print(change_greedy(coin_list, n))
    # print(change_recursion(coin_list, n))
    # 贪心算法已经达不到正确的解答了
    print("最少使用%d枚硬币拼出%d块钱" % (coinChange(coin_list, n), n))
