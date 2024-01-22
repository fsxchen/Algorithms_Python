'''
@Author: yangxingchen
@Date: 2020-04-01 10:38:45
@LastEditors: yangxingchen
@LastEditTime: 2020-04-01 11:05:46
@Description: 
'''
"""活动选择问题
问题描述：
    有n项活动，按照结束的时间排序，
    start[]  =  {10, 12, 20};
    finish[] =  {20, 25, 30};
    可以看到可以最多选择2给我活动 {0, 2}
"""

def printf_max_activities(s, f):
    n = len(f)
    print("length", n)
    i = 0       # 记录当前可选择的坐标， 第一个肯定是符合的
    print(i, sep=",")
    for j in range(n):
        if s[j] >= f[i]:
            print(j, sep=",")
            i = j

if __name__ == "__main__":
    s = [1 , 3 , 0 , 5 , 8 , 5] 
    f = [2 , 4 , 6 , 7 , 9 , 9] 
    printf_max_activities(s , f) 
