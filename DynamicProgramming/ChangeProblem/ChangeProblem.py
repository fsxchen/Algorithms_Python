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
    if money == 0:
        return 0
    best = -1
    for coin in coin_list:
        if (coin <= money):
            next_try = change_recursion(coin_list, money - coin)
            if best < 0 or best > next_try + 1:
                best = next_try + 1
    return best

def coinChange(coins, amount) -> int:
    MAX_INT = 999999999
    f = [0] * (amount + 1)
    f[0] = 0

    for i in range(1, amount + 1):
        f[i] = MAX_INT
        # last coin A[j]
        # f[i] = min {f[i-A[0] + 1], f[i - A[n - 1] + 1 ...]}
        for j in coins:
            if i >= j and f[i - j] != MAX_INT:
                f[i] = min(f[i - j] + 1, f[i])
    
    return f[amount] if f[amount] != MAX_INT else -1

if __name__ == "__main__":
    coin_list = [1, 4, 6, 10]
    n = 12
    # print(change_greedy(coin_list, n))
    # print(change_recursion(coin_list, n))
    # 贪心算法已经达不到正确的解答了
    print(coinChange([1, 2, 5], 11))
