/*
 * @lc app=leetcode id=118 lang=golang
 *
 * [118] Pascal's Triangle
 *
 * https://leetcode.com/problems/pascals-triangle/description/
 *
 * algorithms
 * Easy (73.24%)
 * Likes:    12120
 * Dislikes: 388
 * Total Accepted:    1.5M
 * Total Submissions: 2M
 * Testcase Example:  '5'
 *
 * Given an integer numRows, return the first numRows of Pascal's triangle.
 *
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it as shown:
 *
 *
 * Example 1:
 * Input: numRows = 5
 * Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 * Example 2:
 * Input: numRows = 1
 * Output: [[1]]
 *
 *
 * Constraints:
 *
 *
 * 1 <= numRows <= 30
 *
 *
 */

// @lc code=start
func generate(numRows int) [][]int {
	memo := make(map[string]int)
	// use helper function to generate each row
	res := make([][]int, numRows)
	for i := 0; i < numRows; i++ {
		res[i] = make([]int, i+1)
		for j := 0; j < i+1; j++ {
			res[i][j] = helper(i, j, memo)
		}
	}
	return res

}

// recursive relation f(i,j)=f(i-1,j-1)+f(i-1,j)
func helper(i, j int, memo map[string]int) int {
	// base case
	key := fmt.Sprintf("%d,%d", i, j)
	if val, found := memo[key]; found {
		return val
	}

	// Base case
	if j == 0 || j == i {
		return 1
	}

	// Recursive case with memoization
	memo[key] = helper(i-1, j-1, memo) + helper(i-1, j, memo)
	return memo[key]
}

// iterative solution
func generate2(numRows int) [][]int {
	if numRows == 0 {
		return [][]int{}
	}
	res := [][]int{{1}}
	for i := 1; i < numRows; i++ {
		row := make([]int, i+1)
		row[0], row[i] = 1, 1
		for j := 1; j < i; j++ {
			row[j] = res[i-1][j-1] + res[i-1][j]
		}
		res = append(res, row)
	}
	return res
}

// @lc code=end

