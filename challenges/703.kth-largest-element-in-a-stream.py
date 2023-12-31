#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (56.57%)
# Likes:    5200
# Dislikes: 3257
# Total Accepted:    484.2K
# Total Submissions: 855.5K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n' +'[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# Design a class to find the k^th largest element in a stream. Note that it is
# the k^th largest element in the sorted order, not the k^th distinct element.
# 
# Implement KthLargest class:
# 
# 
# KthLargest(int k, int[] nums) Initializes the object with the integer k and
# the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the
# element representing the k^th largest element in the stream.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
# 
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= 10^4
# 0 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# -10^4 <= val <= 10^4
# At most 10^4 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you
# search for the k^th element.
# 
# 
#

# @lc code=start
from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

