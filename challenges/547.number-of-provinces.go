/*
 * @lc app=leetcode id=547 lang=golang
 *
 * [547] Number of Provinces
 *
 * https://leetcode.com/problems/number-of-provinces/description/
 *
 * algorithms
 * Medium (65.59%)
 * Likes:    9399
 * Dislikes: 342
 * Total Accepted:    831.3K
 * Total Submissions: 1.3M
 * Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
 *
 * There are n cities. Some of them are connected, while some are not. If city
 * a is connected directly with city b, and city b is connected directly with
 * city c, then city a is connected indirectly with city c.
 *
 * A province is a group of directly or indirectly connected cities and no
 * other cities outside of the group.
 *
 * You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
 * i^th city and the j^th city are directly connected, and isConnected[i][j] =
 * 0 otherwise.
 *
 * Return the total number of provinces.
 *
 *
 * Example 1:
 *
 *
 * Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
 * Output: 2
 *
 *
 * Example 2:
 *
 *
 * Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 200
 * n == isConnected.length
 * n == isConnected[i].length
 * isConnected[i][j] is 1 or 0.
 * isConnected[i][i] == 1
 * isConnected[i][j] == isConnected[j][i]
 *
 *
 */

// @lc code=start
func findCircleNum(isConnected [][]int) int {
	provinceCount := 0
	visited := make([]bool, len(isConnected))
	cityQueue := make([]int, 0)

	for city := 0; city < len(isConnected); city++ {
		if !visited[city] {
			provinceCount++
			cityQueue = append(cityQueue, city)

			for len(cityQueue) > 0 {
				currentNode := cityQueue[0]
				cityQueue = cityQueue[1:]
				visited[currentNode] = true

				for neighbor := 0; neighbor < len(isConnected); neighbor++ {
					if isConnected[currentNode][neighbor] == 1 && !visited[neighbor] {
						cityQueue = append(cityQueue, neighbor)
					}
				}
			}
		}
	}
	return provinceCount
}

// @lc code=end

