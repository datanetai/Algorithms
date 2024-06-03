# 790. Domino and Tromino Tiling
# Medium
# Topics
# Companies
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:

# Input: n = 1
# Output: 1
 

# Remember our states for the right edge of a partially tiled board:

# FT: Fully Tiled (both squares in the last column are tiled)
# TSO: Top Square Only
# BSO: Bottom Square Only
# Our Goal: For each state (FT, TSO, BSO) and a given board size n (2 x n), we want to express the number of valid tilings in terms of tilings for smaller board sizes.

# Recurrences
# Base Cases:
# dp[0][0] = 0  (No tilings possible for a 2x0 board)
# dp[0][1] = 0  (Cannot tile an empty board partially)
# dp[0][2] = 0  (Cannot tile an empty board partially)

# dp[1][0] = 1  (A vertical domino can cover a 2x1 board)
# dp[1][1] = 0  (No valid tiling for partial coverage of a 2x1 board)
# dp[1][2] = 0  (No valid tiling for partial coverage of a 2x1 board)

# dp[2][0] = 2  (Two ways to fully tile a 2x2 board)
# dp[2][1] = 1  (One way to tile a 2x2 board with only the top square of the last column)
# dp[2][2] = 1  (One way to tile a 2x2 board with only the bottom square of the last column)

# Recurrence Relations:
# For n >= 3:
# Fully Tiled (FT):
# dp[n][0] = dp[n-1][0] + dp[n-2][0] + dp[n-1][1] + dp[n-1][2]
# (Extend a fully tiled 2x(n-1) with a vertical domino, or a fully tiled 2x(n-2) with two horizontal dominos,
# or add a tromino to a board with the top or bottom square of the last column only tiled)

# Top Square Only (TSO):
# dp[n][1] = dp[n-2][0] + dp[n-1][2]
# (Place a tromino on a fully tiled 2x(n-2) board to cover the top square only of the last two columns,
# or extend a board that has the bottom square only of the last column tiled with a horizontal domino)

# Bottom Square Only (BSO):
# dp[n][2] = dp[n-2][0] + dp[n-1][1]
# (Place a tromino on a fully tiled 2x(n-2) board to cover the bottom square only of the last two columns,
# or extend a board that has the top square only of the last column tiled with a horizontal domino)

# Recursive approach


class Solution:
    def numTilings(self, n: int) -> int:
        # state: FT, TSO, BSO represented as 0, 1, 2
        def recurse(n, state):
            if n == 0:
                return 0
            if n == 1:
                return 1 if state == 0 else 0
          
            if n == 2:
                return 2 if state == 0 else 1
            if (n, state) in memo:
                return memo[(n, state)]
            if state == 0:
                memo[(n, state)] = recurse(n - 1, 0) + recurse(n - 2, 0) + recurse(n - 1, 1) + recurse(n - 1, 2)
            elif state == 1:
                memo[(n, state)] = recurse(n - 1, 2) + recurse(n - 2, 0)
            else:
                memo[(n, state)] = recurse(n - 1, 1) + recurse(n - 2, 0)
            return memo[(n, state)]

        memo = {}
        return recurse(n, 0) % (10**9 + 7)

              
# tabulation

class  Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [[0, 0, 0] for _ in range(n + 1)]
        dp[1][0] = 1
        dp[2][0] = 2
        dp[2][1] = 1
        dp[2][2] = 1
        for i in range(3, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 1][1] + dp[i - 1][2]) % (10**9 + 7)
            dp[i][1] = (dp[i - 1][2] + dp[i - 2][0]) % (10**9 + 7)
            dp[i][2] = (dp[i - 1][1] + dp[i - 2][0]) % (10**9 + 7)
        return dp[n][0]