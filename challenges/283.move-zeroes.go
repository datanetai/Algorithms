/*
 * @lc app=leetcode id=283 lang=golang
 *
 * [283] Move Zeroes
 *
 * https://leetcode.com/problems/move-zeroes/description/
 *
 * algorithms
 * Easy (61.43%)
 * Likes:    15975
 * Dislikes: 416
 * Total Accepted:    2.7M
 * Total Submissions: 4.4M
 * Testcase Example:  '[0,1,0,3,12]'
 *
 * Given an integer array nums, move all 0's to the end of it while maintaining
 * the relative order of the non-zero elements.
 *
 * Note that you must do this in-place without making a copy of the array.
 *
 *
 * Example 1:
 * Input: nums = [0,1,0,3,12]
 * Output: [1,3,12,0,0]
 * Example 2:
 * Input: nums = [0]
 * Output: [0]
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^4
 * -2^31 <= nums[i] <= 2^31 - 1
 *
 *
 *
 * Follow up: Could you minimize the total number of operations done?
 */

// @lc code=start
func moveZeroes(nums []int) {
	snowballsize := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			snowballsize++
		} else {
			nums[i], nums[i-snowballsize] = nums[i-snowballsize], nums[i]
		}
	}
}

// @lc code=end

