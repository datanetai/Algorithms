#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (67.31%)
# Likes:    3427
# Dislikes: 98
# Total Accepted:    253K
# Total Submissions: 376.6K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level x such that the sum of all the values of nodes at
# level x is maximal.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# Example 2:
# 
# 
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        max_sum_level = 0
        max_sum = float('-inf')  
        level = 1
        while (queue):
            sum_ = 0
            current_level_size = len(queue)
            for i in range(current_level_size):
                node = queue.pop(0)
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if sum_>max_sum:
                max_sum = sum_
                max_sum_level = level
            level = level + 1
        
        return max_sum_level

# @lc code=end

