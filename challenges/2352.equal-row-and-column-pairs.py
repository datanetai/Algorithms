#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#
# https://leetcode.com/problems/equal-row-and-column-pairs/description/
#
# algorithms
# Medium (72.39%)
# Likes:    2042
# Dislikes: 129
# Total Accepted:    171.9K
# Total Submissions: 240.6K
# Testcase Example:  '[[3,2,1],[1,7,6],[2,7,7]]'
#
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri,
# cj) such that row ri and column cj are equal.
# 
# A row and column pair is considered equal if they contain the same elements
# in the same order (i.e., an equal array).
# 
# 
# Example 1:
# 
# 
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# 
# 
# Example 2:
# 
# 
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                col = [grid[l][j] for l in range(n)]
                row = grid[i]
                if row == col:
                    pairs += 1

        return pairs
    
class Solution:
    def equalPairs2(self, grid: List[List[int]]) -> int:
        pairs = 0
        row_map = {}
        col_map = {}
        n = len(grid)
        # populate row and column map 
        for i in range(n):
            row = grid[i]
            col = [grid[l][i] for l in range(n)]
            row_map[i] = row
            col_map[i] = col
        
        # check for equal pairs
        for i in range(n):
            for j in range(n):
                if row_map[i] == col_map[j]:
                    pairs += 1
                    
        return pairs
    


        
# @lc code=end

