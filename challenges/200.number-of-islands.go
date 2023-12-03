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

	// Iterate over the grid
	for i := range grid {
		for j := range grid[i] {
			// If the current cell is '1', increment the counter and call a helper function
			if grid[i][j] == '1' {
				numIslands++
				bfs(grid, i, j)
			}
		}
	}
	return numIslands
}
func bfs(grid [][]byte, i, j int) {
	queue := list.New()
	queue.PushBack([]int{i, j})

	for queue.Len() > 0 {
		cell := queue.Remove(queue.Front()).([]int)
		x, y := cell[0], cell[1]

		if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[0]) || grid[x][y] == '0' {
			continue
		}

		grid[x][y] = '0'

		queue.PushBack([]int{x - 1, y})
		queue.PushBack([]int{x + 1, y})
		queue.PushBack([]int{x, y - 1})
		queue.PushBack([]int{x, y + 1})
	}
}

// @lc code=end

