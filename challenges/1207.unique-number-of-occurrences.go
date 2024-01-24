/*
 * @lc app=leetcode id=1207 lang=golang
 *
 * [1207] Unique Number of Occurrences
 *
 * https://leetcode.com/problems/unique-number-of-occurrences/description/
 *
 * algorithms
 * Easy (74.38%)
 * Likes:    4841
 * Dislikes: 122
 * Total Accepted:    536.4K
 * Total Submissions: 697.3K
 * Testcase Example:  '[1,2,2,1,1,3]'
 *
 * Given an array of integers arr, return true if the number of occurrences of
 * each value in the array is unique or false otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [1,2,2,1,1,3]
 * Output: true
 * Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
 * values have the same number of occurrences.
 *
 * Example 2:
 *
 *
 * Input: arr = [1,2]
 * Output: false
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
 * Output: true
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 1000
 * -1000 <= arr[i] <= 1000
 *
 *
 */

// @lc code=start
func uniqueOccurrences(arr []int) bool {
	occurences := make(map[int]int)
	for _, v := range arr {
		occurences[v]++
	}
	unique := make(map[int]bool)
	for _, v := range occurences {
		if unique[v] {
			return false
		}
		unique[v] = true
	}
	return true

}

// @lc code=end

