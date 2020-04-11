'''
@Author: yangxingchen
@Date: 2020-04-10 19:21:16
@LastEditors: yangxingchen
@LastEditTime: 2020-04-10 19:35:39
@Description: 
'''
def select_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                print(i, j)
                min_index = j
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
            
if __name__ == "__main__":
    A = [1, 3, 21, 8, 5, 7, 6]
    select_sort(A)
    print(A)