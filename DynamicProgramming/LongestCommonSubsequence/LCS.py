def longestCommonSubsequence(text1, text2) -> int:
    m = len(text1)
    n = len(text2)

    if m == 0 or n == 0:
        return 0

    dp1 = [[0] * (n + 1)] * (m + 1)     # m 行 n 列的数组
    
    dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
    for i in dp1:
        print("====")
        print(i)
    print("+++++++++++")
    for i in dp:
        print("====")
        print(i)
    # for i in range(m):
    for i in range(len(text1)):

        # for j in range(n):
        #     if text2[j] != text1[i]:
        #         dp[i + 1][ j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        #     else:
        #         dp[i+1][j+1] = dp[i][j] + 1
        for j in range(len(text2)):
            if text1[i] != text2[j]:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            else:
                dp[i+1][j+1] = dp[i][j] + 1
    # for i in range(m):
    #     print("====")
    #     print(i)
    #     print(f[i])

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