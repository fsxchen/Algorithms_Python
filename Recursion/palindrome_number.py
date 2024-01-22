'''
@Author: yangxingchen
@Date: 2020-03-28 17:37:01
@LastEditors: yangxingchen
@LastEditTime: 2020-03-28 19:18:20
@Description: 
'''
"""回文数字判断
"""

def is_single_num(num):
    return num < 10 and num >= 0

def is_palindrome_num(num, dup_num):
    """是否为回文数
    
    Arguments:
        num {[int]} -- [description]
    """
    # base case
    if is_single_num(num):
        return num == (dup_num % 10)

    if (is_palindrome_num(num // 10, dup_num) == False):
        return False


def is_pal(num):
    if num < 0:
        num = -num
    dum_num = (num)
    
    if is_palindrome_num(num, dum_num) == False:
        return False
    dum_num = dum_num // 10
    return True

if __name__ == "__main__":
    print(is_pal(10000))
    print(is_pal(88))