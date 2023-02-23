"""
字符串全排列, 给出a, b,能够输出
a, b
b, a

1、一个数的全排列，如排列{1}，就是这个数本身这一种情况

2、两个数的全排列，如排列{1,2}：

 第一步：将{1}放在第零个位置，剩下的{2}进行一个数的全排列，结果为{1,2}

 第二步：将{2}放在第零个位置，剩下的{1}进行一个数的全排列，结果为{2,1}

 即两个数的全排列为以上2种情况。

3、三个数的全排列，如排列{1,2,3}：

 第一步：将{1}放在第零个位置，剩下的{2,3}进行两个数的全排列，结果为{1,2,3}  {1,3,2}

 第二步：将{2}放在第零个位置，剩下的{1,3}进行两个数的全排列，结果为{2,1,3}  {2,3,1}

 第三步：将{3}放在第零个位置，剩下的{1,2}进行两个数的全排列，结果为{3,1,2}  {3,2,1}

 即三个数的全排列为以上6种情况。

4、即m个数（无重）的全排列，就是将m个数分别放在第零个位置，再将剩下的m-1个数的全排列加在后面，当m-1=1时为递归的出口。

上程序实例：
"""

def recurision_arrangement(arr, postion, end):
    if postion == end:   # the last postion
        print(arr)
    
    else:
        for i in range(postion, end):
            arr[i], arr[postion] = arr[postion], arr[i]
            recurision_arrangement(arr, postion+1, end)
            arr[i], arr[postion] = arr[postion], arr[i]

def permutations(str_list):
    if len(str_list) == 1:
        return str_list
    else:
        
        recurision_arrangement(str_list, 0, len(str_list))

if __name__ == "__main__":
    s = ["h", "e"]
    print(permutations(s))