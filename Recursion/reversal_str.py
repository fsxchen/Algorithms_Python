"""
字符串反转
"""

def reversal_str(s):
    """
    s ["H", "E"]
    """
    if (len(s) == 1):
        return s
    else:
        return reversal_str(s[1:]) + s[0]


if __name__ == "__main__":
    test1 = "hello"
    print(reversal_str(test1))