# <!-- 62. Unique Paths
# Medium
# Topics
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100 -->



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def solve(i,j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = solve(i-1,j) + solve(i,j-1)
            return dp[i][j]
        return solve(m-1,n-1)

# bottom up tabulation

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # Base case moved outside the loop

        for i in range(m):
            for j in range(n):
                if i > 0:  # Calculate 'up' only if not in the first row
                    dp[i][j] += dp[i - 1][j] 
                if j > 0:  # Calculate 'left' only if not in the first column
                    dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]