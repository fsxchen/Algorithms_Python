'''
Author: yangxingchen
Date: 2020-04-15 13:44:20
LastEditors: yangxingchen
LastEditTime: 2021-01-21 15:12:22
Description: 
'''
def longestCommonSubsequence(text1, text2) -> int:
    m = len(text1)
    n = len(text2)

    if m == 0 or n == 0:
        return 0
    # 构建m行n列的数组
    # dp1 = [[0] * (n + 1)] * (m + 1)     # m 行 n 列的数组
    
    dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] != text2[j]:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            else:
                dp[i+1][j+1] = dp[i][j] + 1

    # dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
    # for i in range(len(text1)):
    #     for j in range(len(text2)):
    #         if text1[i] != text2[j]:
    #             dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    #         else:
    #             dp[i+1][j+1] = dp[i][j] + 1
    # return dp[-1][-1]

    return dp[-1][-1]

if __name__ == "__main__":
    text1 = "pmjghexybyrgzczy"
    text2 = "hafcdqbgncrcbihkd"
    # h b

    print(longestCommonSubsequence(text1, text2))