"""
see: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
比较典型的滑动窗口问题
"""

def lengthOfLongSubstring(s: str) -> int:
    l = len(s)
    if l == 0: 
        return 0

    max_len = 1
    for i in range(l):
        tmp_set = set()
        cur_len = 0
        for j in range(i, l):
            if s[j] in tmp_set:
                break
            else:
                tmp_set.add(s[j])
            cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    return max_len


if __name__ == "__main__":
    print(lengthOfLongSubstring("bbbbbbb"))
    print(lengthOfLongSubstring("abcabcbb"))
