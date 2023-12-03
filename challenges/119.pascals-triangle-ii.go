/*
 * @lc app=leetcode id=119 lang=golang
 *
 * [119] Pascal's Triangle II
 *
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 *
 * algorithms
 * Easy (63.30%)
 * Likes:    4656
 * Dislikes: 323
 * Total Accepted:    819.8K
 * Total Submissions: 1.3M
 * Testcase Example:  '3'
 *
 * Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
 * Pascal's triangle.
 *
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it as shown:
 *
 *
 * Example 1:
 * Input: rowIndex = 3
 * Output: [1,3,3,1]
 * Example 2:
 * Input: rowIndex = 0
 * Output: [1]
 * Example 3:
 * Input: rowIndex = 1
 * Output: [1,1]
 *
 *
 * Constraints:
 *
 *
 * 0 <= rowIndex <= 33
 *
 *
 *
 * Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
 * space?
 *
 */

// @lc code=start
func getRow(rowIndex int) []int {
	if rowIndex == 0 {
		return []int{1}
	}
	memo := make(map[string]int)
	row := make([]int, rowIndex+1)
	row[0], row[rowIndex] = 1, 1
	for i := 1; i <= rowIndex-1; i++ {
		row[i] = helper(rowIndex, i, memo)
	}
	return row

}
func helper(i, j int, memo map[string]int) int {
	if i == 0 || j == 0 || i == j {
		return 1
	}
	key := fmt.Sprintf("%d,%d", i, j)
	if val, found := memo[key]; found {
		return val
	}
	memo[key] = helper(i-1, j-1, memo) + helper(i-1, j, memo)
	return memo[key]
}

// @lc code=end

