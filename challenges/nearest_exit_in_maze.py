# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        queue = deque([(entrance[0], entrance[1], 0)])
        m, n = len(maze), len(maze[0])
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        is_exit = lambda x, y: x in (0, m - 1) or y in (0, n - 1)

        while queue:
            i, j, step = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if is_exit(i, j) and (i, j) != (entrance[0], entrance[1]):
                return step
            for x, y in moves:
                if 0 <= i + x < m and 0 <= j + y < n and maze[i + x][j + y] == '.':
                    queue.append((i + x, j + y, step + 1))
        return -1
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)

        