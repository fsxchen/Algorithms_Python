def numSquares(n) -> int:
    # 直接求解好像没有比较好的思路
    # 但是按照自底向上的构建思路会比较好处理
    # 1 2 3 4 5 6 7 8
    # 1 2 3 2 3 4 5 4
    # 规律
    # dp[i] = min[(dp[k] + [dp[i - k]]) for k in range(1, k)]

    # 初始化，所有的完全平方数都初始化为1
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i ** 2 >= n + 1:
            break
        dp[i ** 2] = 1
    for i in range(2, n + 1):
        min_num = None
        if dp[i] == 1:
            continue
        min_num = None
        for k in range(1, i):
            if dp[k] == 1:
                if min_num == None or min_num > 1 + dp[i - k]:
                    min_num = 1 + dp[i - k]
        dp[i] = min_num
    return dp[n]

if __name__ == "__main__":
    import time
    start = time.time()
    print(numSquares(6665))
    print(time.time() - start)