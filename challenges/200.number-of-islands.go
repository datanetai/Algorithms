/*
 * @lc app=leetcode id=200 lang=golang
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (58.04%)
 * Likes:    21587
 * Dislikes: 471
 * Total Accepted:    2.4M
 * Total Submissions: 4.1M
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given an m x n 2D binary grid grid which represents a map of '1's (land) and
 * '0's (water), return the number of islands.
 *
 * An island is surrounded by water and is formed by connecting adjacent lands
 * horizontally or vertically. You may assume all four edges of the grid are
 * all surrounded by water.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [
 * ⁠ ["1","1","1","1","0"],
 * ⁠ ["1","1","0","1","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","0","0","0"]
 * ]
 * Output: 1
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","1","0","0"],
 * ⁠ ["0","0","0","1","1"]
 * ]
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 300
 * grid[i][j] is '0' or '1'.
 *
 *
 */

// @lc code=start
func numIslands(grid [][]byte) int {
	var numIslands int

	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == '1' {
				numIslands++
				dfs(grid, i, j)
			}
		}
	}
	return numIslands
}

// dfs performs a depth-first search on the grid starting from the cell at (i, j).
// It uses an explicit stack to avoid stack overflow.
func dfs(grid [][]byte, i, j int) {
	// Initialize the stack with the starting cell.
	stack := [][]int{{i, j}}

	// Continue until the stack is empty.
	for len(stack) > 0 {
		// Pop a cell from the stack.
		s := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		x, y := s[0], s[1]

		// Check the cell above the current cell.
		if x-1 >= 0 && grid[x-1][y] == '1' {
			// If it's '1', push it into the stack and mark it as visited.
			stack = append(stack, []int{x - 1, y})
			grid[x-1][y] = '0'
		}

		// Check the cell below the current cell.
		if x+1 < len(grid) && grid[x+1][y] == '1' {
			// If it's '1', push it into the stack and mark it as visited.
			stack = append(stack, []int{x + 1, y})
			grid[x+1][y] = '0'
		}

		// Check the cell to the left of the current cell.
		if y-1 >= 0 && grid[x][y-1] == '1' {
			// If it's '1', push it into the stack and mark it as visited.
			stack = append(stack, []int{x, y - 1})
			grid[x][y-1] = '0'
		}

		// Check the cell to the right of the current cell.
		if y+1 < len(grid[0]) && grid[x][y+1] == '1' {
			// If it's '1', push it into the stack and mark it as visited.
			stack = append(stack, []int{x, y + 1})
			grid[x][y+1] = '0'
		}
	}
}

// @lc code=end

