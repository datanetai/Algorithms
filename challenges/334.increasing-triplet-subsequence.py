#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (40.84%)
# Likes:    7724
# Dislikes: 436
# Total Accepted:    497.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] ==
# 4 < nums[5] == 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you implement a solution that runs in O(n) time complexity
# and O(1) space complexity?
#

# @lc code=start
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min1 = min2 = float('inf')
        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True
            
        return False

            


        
# @lc code=end

