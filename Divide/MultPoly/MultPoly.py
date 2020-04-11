'''
@Author: yangxingchen
@Date: 2020-04-07 11:37:46
@LastEditors: yangxingchen
@LastEditTime: 2020-04-08 19:08:24
@Description: 
'''
"""多项式乘法
    eg：
        input: A [3, 2, 5], B[5, 1, 2]
        output: B [15， 13， 33， 9， 10]
"""

def mult_poly(A, B, n):
    # 构造C
    C = [0] * (2 * n - 1)
    for i in range(0, n):
        for j in range(0, n):
            C[i + j] += A[i] * B[j]
    return C

def mult_poly2(A, B, n, a1, b1):
    r = []
    if n = 1:
        r.append(A[a1]* B[b1])
    return r

if __name__ == "__main__":
    A = [3, 2, 5]
    B = [5, 1, 2]
    print(mult_poly(A, B, 3))