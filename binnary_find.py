"""
二分查找法
"""

def binnary_find(A: list, num: int):
    """
    查找一个数
    """
    n = len(A)
    l, r = 0, n - 1

    while l < r:
        mid = l + ((r - l) >> 1)
        if A[mid] == num:
            return True
        elif A[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return A[l] == num

def main():
    A = [1, 3, 5, 8, 12, 20, 36, 58, 99]
    print(binnary_find(A, 5))

if __name__ == "__main__":
    main()

