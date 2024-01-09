/*
 * @lc app=leetcode id=238 lang=golang
 *
 * [238] Product of Array Except Self
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (65.08%)
 * Likes:    21074
 * Dislikes: 1230
 * Total Accepted:    2.2M
 * Total Submissions: 3.3M
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an integer array nums, return an array answer such that answer[i] is
 * equal to the product of all the elements of nums except nums[i].
 *
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 *
 * You must write an algorithm that runs in O(n) time and without using the
 * division operation.
 *
 *
 * Example 1:
 * Input: nums = [1,2,3,4]
 * Output: [24,12,8,6]
 * Example 2:
 * Input: nums = [-1,1,0,-3,3]
 * Output: [0,0,9,0,0]
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 10^5
 * -30 <= nums[i] <= 30
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 *
 *
 *
 * Follow up: Can you solve the problem in O(1) extra space complexity? (The
 * output array does not count as extra space for space complexity analysis.)
 *
 */

// @lc code=start
func productExceptSelf(nums []int) []int {
	left_product := make([]int, len(nums))
	right_product := make([]int, len(nums))
	left_product[0] = 1
	right_product[len(nums)-1] = 1
	for i := 1; i < len(nums); i++ {
		left_product[i] = left_product[i-1] * nums[i-1]
	}
	for i := len(nums) - 2; i >= 0; i-- {
		right_product[i] = right_product[i+1] * nums[i+1]
	}
	for i := 0; i < len(nums); i++ {
		nums[i] = left_product[i] * right_product[i]
	}
	return nums
}

// O(1) space
func productExceptSelf2(nums []int) []int {
	length := len(nums)
	answer := make([]int, length)

	// answer[i] contains the product of all the numbers to the left of i
	answer[0] = 1
	for i := 1; i < length; i++ {
		answer[i] = nums[i-1] * answer[i-1]
	}

	// right_product contains the product of all the numbers to the right of i
	right_product := 1
	for i := length - 1; i >= 0; i-- {
		// For the index 'i', answer[i] contains the product of all the numbers to the left and right_product contains the product of all the numbers to the right
		// Hence, answer[i] * right_product gives the product of all numbers except the one at index i
		answer[i] = answer[i] * right_product
		right_product *= nums[i]
	}

	return answer
}

// @lc code=end

