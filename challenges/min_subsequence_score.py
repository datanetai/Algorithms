# Problem: Maximum Subsequence Score (LeetCode 2542)
# Description:
# You are given two arrays of integers, nums1 and nums2, both of length n. You are also given an integer k. Your task is to choose a subsequence of k indices from nums1 such that the following score is maximized:
# Score = (sum of selected elements from nums1) * (minimum of selected elements from nums2)
# More formally, if you choose indices i0, i1, ..., ik-1, then the score is:
# (nums1[i0] + nums1[i1] + ... + nums1[ik-1]) * min(nums2[i0], nums2[i1], ..., nums2[ik-1])
# Return the maximum possible score you can achieve.
# Constraints:
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[j] <= 10^5
# 1 <= k <= n
# Examples:
# Example 1:
# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation: Choosing indices 0, 2, and 3 gives the maximum score: (1 + 3 + 2) * min(2, 3, 4) = 12
# Example 2:
# Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
# Output: 30
# Explanation: Choosing index 2 gives the maximum score: 3 * 10 = 30
from heapq import heappush, heappop
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0
        h = []
        nums = sorted(list(zip(nums1, nums2)), key=lambda ab: -ab[1])
        for i in range(len(nums)):
            a, b = nums[i]
            heappush(h, a)
            total += a
            if len(h) > k:
                total -= heappop(h)
            if len(h) == k:
                res = max(res, total * b)
        return res