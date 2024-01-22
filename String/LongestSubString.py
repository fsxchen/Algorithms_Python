
def lengthOfLongestSubstring(s):
    if not s:
        return 0
    # ans 存放最大长度
    # i 为当前子串左边界
    ans, i = 0, 0
    counter = 0
    smap = {}
    for j in s:
        if j in smap:
            i = max(smap[j], i)
        ans = max(ans, counter - i + 1)

        smap[j] = counter + 1
        counter += 1
    return ans
            
if __name__ == "__main__":
    test1 = "abba"
    test2 = "bbbb"
    print(lengthOfLongestSubstring(test1))
    print(lengthOfLongestSubstring(test2))