# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1: # type: ignore


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for dx, dy in directions:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = 2
                        fresh -= 1
                        queue.append((x+dx,y+dy))
            minutes += 1

    
        return max(0, minutes-1) if fresh == 0 else -1
    