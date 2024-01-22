'''
@Author: yangxingchen
@Date: 2020-03-27 10:10:44
@LastEditors: yangxingchen
@LastEditTime: 2020-03-27 10:32:26
@Description: 
'''
#!/bin/env python

def binary_to_decimal(binary_str, i = 0):
    n = len(binary_str)
    if n - 1 == i:
        return int(binary_str[i])
    else:
        return (int(binary_str[i]) - 0 << (n -1 -i )) + binary_to_decimal(binary_str, i + 1)

if __name__ == "__main__":
    print(binary_to_decimal("1"))
    print(binary_to_decimal("1010"))
    print(binary_to_decimal("101011111100001111"))