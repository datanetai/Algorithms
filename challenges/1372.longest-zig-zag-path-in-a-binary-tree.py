#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
#
# algorithms
# Medium (66.48%)
# Likes:    3308
# Dislikes: 67
# Total Accepted:    144.7K
# Total Submissions: 219.2K
# Testcase Example:  '[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]'
#
# You are given the root of a binary tree.
# 
# A ZigZag path for a binary tree is defined as follow:
# 
# 
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current
# node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# 
# 
# Zigzag length is defined as the number of nodes visited - 1. (A single node
# has a length of 0).
# 
# Return the longest ZigZag path contained in that tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# 
# 
# Example 2:
# 
# 
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left ->
# right).
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 100
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def dfs(node: Optional[TreeNode], direction: bool, length: int):
            if node is None:
                return
            self.max_length = max(self.max_length, length)
            if direction:
                dfs(node.left, not direction, length + 1)
                dfs(node.right, direction, 1)
            else:
                dfs(node.right, not direction, length + 1)
                dfs(node.left, direction, 1)
        dfs(root.left, False, 1)
        dfs(root.right, True, 1)
        return self.max_length


# @lc code=end

