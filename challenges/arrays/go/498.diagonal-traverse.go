/*
 * @lc app=leetcode id=498 lang=golang
 *
 * [498] Diagonal Traverse
 *
 * https://leetcode.com/problems/diagonal-traverse/description/
 *
 * algorithms
 * Medium (58.86%)
 * Likes:    3203
 * Dislikes: 644
 * Total Accepted:    262.7K
 * Total Submissions: 446.3K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given an m x n matrix mat, return an array of all the elements of the array
 * in a diagonal order.
 *
 *
 * Example 1:
 *
 *
 * Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [1,2,4,7,5,3,6,8,9]
 *
 *
 * Example 2:
 *
 *
 * Input: mat = [[1,2],[3,4]]
 * Output: [1,2,3,4]
 *
 *
 *
 * Constraints:
 *
 *
 * m == mat.length
 * n == mat[i].length
 * 1 <= m, n <= 10^4
 * 1 <= m * n <= 10^4
 * -10^5 <= mat[i][j] <= 10^5
 *
 *
 */

package main

// @lc code=start
// approach 1 using direction boolean
// func findDiagonalOrder(mat [][]int) []int {
// 	direction := true
// 	m, n := len(mat), len(mat[0])
// 	result := []int{}

// 	row, col := 0, 0
// 	// loop until we row and col are valid
// 	for row < m && col < n {
// 		result = append(result, mat[row][col])
// 		if direction {
// 			if row == 0 || col == n-1 {
// 				direction = !direction
// 				if col == n-1 {
// 					row++
// 				} else {
// 					col++
// 				}
// 			} else {
// 				row--
// 				col++
// 			}
// 		} else {
// 			if row == m-1 || col == 0 {
// 				direction = !direction
// 				if row == m-1 {
// 					col++
// 				} else {
// 					row++
// 				}
// 			} else {
// 				row++
// 				col--
// 			}
// 		}

// 	}
// 	return result
// }

// approach 2 using snake pattern
func findDiagonalOrder(mat [][]int) []int {
	m, n := len(mat), len(mat[0])
	result := []int{}
	// dict
	dict := make(map[int][]int)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dict[i+j] == nil {
				dict[i+j] = []int{}
			}
			dict[i+j] = append(dict[i+j], mat[i][j])
		}
	}

	for i := 0; i < m+n-1; i++ {
		if i%2 == 0 {
			for j := len(dict[i]) - 1; j >= 0; j-- {
				result = append(result, dict[i][j])
			}
		} else {
			for j := 0; j < len(dict[i]); j++ {
				result = append(result, dict[i][j])
			}
		}
	}

	return result

}

// @lc code=end
