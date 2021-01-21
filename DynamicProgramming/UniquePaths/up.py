'''
Author: yangxingchen
Date: 2021-01-21 16:06:16
LastEditors: yangxingchen
LastEditTime: 2021-01-21 17:41:55
Description: 
'''
"""
题目描述，给定m行n列的网格，有一个机器人从左上角（0，0）出发，每一步可以向下或者向右，
问：有多少种不同的方式走到右下角。
"""

def unique_path(m, n) -> int:
    if m <= 0 or n <=0:
        return 0
    # 理论上，这种题目构造一个一维数组也可以
    # 需要分析出转移方程，
    # 机器人最后一步要不是往下，要不是往右边
    # 令f(x, y) 表示走到x，y的步数，那么f(x+1, y+1) = f(x, y+1) + f(x+1, y)

    # 开状态数组
    dp = [[0]*(n+1) for _ in range(m+1)]
    # 构建初始状态
    # dp = 1
    for x in dp:
        print(x)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if j == 1 or i == 1:
                dp[i][j] = 1        # 初始化，把初始化放到了这里
                continue
            print(i, j, '===')
            dp[i][j] = dp[i][j -1] + dp[i-1][j]
    for x in dp:
        print(x)
    print(dp[m][n])

if __name__ == "__main__":
    unique_path(3, 4)