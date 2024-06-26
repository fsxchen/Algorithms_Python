"""
coin change

2, 5, 7

27
"""

def f(x:int):
    if x == 0:
        return 0
    res = 100
    if x >=2:
        res = min(f(x - 2) + 1, res)
    if x >= 5:
        res = min(f(x - 5) + 1, res)
    if x >= 7:
        res = min(f(x-7) + 1, res)
    return res

"""
使用动态规划
"""
def coin(x):
    dp = [None] * (x + 1)
    dp[0] = 0
    res = 100
    for i in range(1, x+1):
        dp[i] = 100
        if i >= 2 and dp[i - 2] != 100 and dp[i-2] + 1 < dp[i]:
            dp[i] = dp[i-2] + 1
        if i >= 5 and dp[i - 5] != 100 and dp[i-5] + 1 < dp[i]:
            dp[i] = dp[i-5] + 1
        if i >= 7 and dp[i - 7] != 100 and dp[i-7] + 1 < dp[i]:
            dp[i] = dp[i-7] + 1
    return dp[27]
        

if __name__ == "__main__":
    print(f(27))
    print(coin(27))
