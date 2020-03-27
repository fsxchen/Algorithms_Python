'''
@Author: yangxingchen
@Date: 2020-03-20 22:47:51
@LastEditors: yangxingchen
@LastEditTime: 2020-03-27 22:35:32
@Description: 
'''
"""
字符串遍历
"""

def traversal_str(s, index, cur):
    if (len(s) == index):
        print(cur)
        return
    traversal_str(s, index + 1, cur + s[index])

def reversal_traversal_str(s, index, cur):
    if -1 == index:
        print(cur)
        return cur
    reversal_traversal_str(s, index - 1, cur + s[index])

if __name__ == "__main__":
    test = "hello"
    traversal_str(test, 0, "")
    reversal_traversal_str(test, len(test) - 1, "")