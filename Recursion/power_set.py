'''
@Author: yangxingchen
@Date: 2020-03-27 10:34:51
@LastEditors: yangxingchen
@LastEditTime: 2020-03-27 22:23:36
@Description: 
'''
"""
字符串的超集
"""

def power_set(string, index, cur):
    if index == len(string):
        print(cur)
        return cur

    # 固定当前的字符串，那么下一个有两种情况，
    # 1、+后面的字符串
    # 2、+一个空字符串
    power_set(string, index + 1, cur + string[index])
    power_set(string, index + 1, cur + "_")

if __name__ == "__main__":
    power_set("abc", 0, "")