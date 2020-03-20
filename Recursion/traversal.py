"""
字符串遍历
"""

def traversal_str(s):
    print(s[0])
    if (len(s) == 1):
        return
    return traversal_str(s[1:])

def reversal_traversal_str(s):
    if len(s) == 1:
        print(s[0])
        return
    reversal_traversal_str(s[1:])
    print(s[0])

if __name__ == "__main__":
    test = "hello"
    traversal_str(test)
    reversal_traversal_str(test)