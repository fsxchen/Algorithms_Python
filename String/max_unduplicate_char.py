# coding:utf-8
"""
最大子序列的长度
"""


def lenghtofLongesSubsgring(s):
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
    print(st)
    return ans;

if __name__ == "__main__":
    test_s = "abcabcbb"
    print(lenghtofLongesSubsgring(test_s))

"""
1、
st = {}
i = 0
j = 1, s[j] = a
ans = 1

2、
st = {a: 1}
i = 0
ans = 2
...4
st = {a: 1, b: 2, c: 3}
"""
