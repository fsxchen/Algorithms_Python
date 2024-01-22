"""
https://leetcode-cn.com/problems/maximum-product-subarray/
"""

def maxProduct(nums):
    # 1、判断状态
    # 如果在k处有最大值, 那么在前k-1处，必定是最大/最小值
    # 因此次
    # 如果 k > 0 
    # 如果k == 0 ，最大值必然是 a
    n = len(nums)
    f = [None] * n
    f_n = [None] * n  # 存放最小的负数子集
    f[0] = nums[0]
    f_n[0] = nums[0]
    best = 0    # 最大值
    for i in range(1, n):
        if f[i] == None:
            f[i] = nums[i] * f[i - 1]
            f_n[i] = nums[i] * f[i - 1]
    
        
        f_n[i] = min(f[i], nums[i] * f_n[i - 1], nums[i])
        f[i] = max(f[i], nums[i] * f[i - 1], nums[i], nums[i] * f_n[i - 1])
    
    return max(f)

if __name__ == "__main__":
    nums = [2,3,-2,4]
    # nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
    # nums = [-2,2, 0, -2]
    print(maxProduct(nums))