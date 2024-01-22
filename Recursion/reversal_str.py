"""
字符串反转
"""

def reversal_str(s):
    if (len(s) == 0):
        return
    reversal_str(s[1:])
    print(s[0], end=",")


if __name__ == "__main__":
    test1 = "hello"
    reversal_str(test1)