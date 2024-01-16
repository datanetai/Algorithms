#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (43.09%)
# Likes:    3268
# Dislikes: 278
# Total Accepted:    365.8K
# Total Submissions: 847.5K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# You are given an integer array nums consisting of n elements, and an integer
# k.
# 
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10^-5 will be accepted.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# 
# 
# Example 2:
# 
# 
# Input: nums = [5], k = 1
# Output: 5.00000
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = k
        current_sum = sum(nums[start:end])
        max_sum = current_sum
        while end < len(nums):
            current_sum = current_sum - nums[start] + nums[end]
            max_sum = max(max_sum, current_sum)
            start += 1
            end += 1
        return max_sum / k
        s
        
# @lc code=end

