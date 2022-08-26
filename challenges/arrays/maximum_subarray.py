# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# brute force O(n^3) really slow timeout on leetcode
import sys  
def maxSubArray(nums: list) -> int:
    # brute force method
    max_sum = -sys.maxsize - 1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i, j + 1):
                sum += nums[k]
            if sum > max_sum:
                max_sum = sum
    return max_sum

# solution O(n) time complexity aka Kadane's algorithm
def maxSubArray2(nums: list) -> int:
    # dynamic programming method
    max_sum = -sys.maxsize - 1
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum

# same compleixty but different implementation
def maxSubArray3(nums: list) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1,len(nums)):
        curr_sum = nums[i] + max(0, curr_sum)
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Solution 3 divide and conquer O(n log n) time complexity
def maxSubArray4(nums: list) -> int:
    return maxSubArray4_helper(nums, 0, len(nums) - 1)
def maxSubArray4_helper(nums: list, left: int, right: int) -> int:
    if left == right:
        return nums[left]
    mid = (left + right) // 2
    left_max = maxSubArray4_helper(nums, left, mid)
    right_max = maxSubArray4_helper(nums, mid + 1, right)
    cross_max = maxSubArray4_cross(nums, left, mid, right)
    return max(left_max, right_max, cross_max)
def maxSubArray4_cross(nums: list, left: int, mid: int, right: int) -> int:
    left_sum = -sys.maxsize - 1
    sum = 0
    for i in range(mid, left - 1, -1):
        sum += nums[i]
        if sum > left_sum:
            left_sum = sum
    right_sum = -sys.maxsize - 1
    sum = 0
    for i in range(mid + 1, right + 1):
        sum += nums[i]
        if sum > right_sum:
            right_sum = sum
    return left_sum + right_sum