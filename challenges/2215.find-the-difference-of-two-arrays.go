/*
 * @lc app=leetcode id=2215 lang=golang
 *
 * [2215] Find the Difference of Two Arrays
 *
 * https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
 *
 * algorithms
 * Easy (78.37%)
 * Likes:    2183
 * Dislikes: 89
 * Total Accepted:    257.4K
 * Total Submissions: 327.9K
 * Testcase Example:  '[1,2,3]\n[2,4,6]'
 *
 * Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
 * size 2 where:
 *
 *
 * answer[0] is a list of all distinct integers in nums1 which are not present
 * in nums2.
 * answer[1] is a list of all distinct integers in nums2 which are not present
 * in nums1.
 *
 *
 * Note that the integers in the lists may be returned in any order.
 *
 *
 * Example 1:
 *
 *
 * Input: nums1 = [1,2,3], nums2 = [2,4,6]
 * Output: [[1,3],[4,6]]
 * Explanation:
 * For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1
 * and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
 * For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4
 * and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
 *
 * Example 2:
 *
 *
 * Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
 * Output: [[3],[]]
 * Explanation:
 * For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] ==
 * nums1[3], their value is only included once and answer[0] = [3].
 * Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums1.length, nums2.length <= 1000
 * -1000 <= nums1[i], nums2[i] <= 1000
 *
 *
 */

// @lc code=start
func findDifference(nums1 []int, nums2 []int) [][]int {
	find1 := make([]int, 2002)
	find2 := make([]int, 2002)
	for _, i := range nums1 {
		find1[i+1000] = 1
	}
	for _, i := range nums2 {
		find2[i+1000] = 1
	}
	result := make([][]int, 2)
	result[0] = []int{}
	result[1] = []int{}
	for i := 0; i < 2002; i++ {
		if find1[i] == 1 && find2[i] == 0 {
			result[0] = append(result[0], i-1000)
		}
		if find2[i] == 1 && find1[i] == 0 {
			result[1] = append(result[1], i-1000)
		}
	}
	return result
}

// solution 2 using map
func findDifference2(nums1 []int, nums2 []int) [][]int {
	find1 := make(map[int]bool)
	find2 := make(map[int]bool)
	for _, i := range nums1 {
		find1[i] = true
	}
	for _, i := range nums2 {
		find2[i] = true
	}
	result := make([][]int, 2)
	result[0] = []int{}
	result[1] = []int{}
	func findDifference(nums1 []int, nums2 []int) [][]int {
		// Create maps to store the presence of numbers in nums1 and nums2
		map1 := make(map[int]bool)
		map2 := make(map[int]bool)
	
		// Populate the maps
		for _, num := range nums1 {
			map1[num] = true
		}
		for _, num := range nums2 {
			map2[num] = true
		}
	
		// Initialize the result arrays
		res1 := []int{}
		res2 := []int{}
	
		// Find numbers in nums1 that are not in nums2
		for num := range map1 {
			if !map2[num] {
				res1 = append(res1, num)
			}
		}
	
		// Find numbers in nums2 that are not in nums1
		for num := range map2 {
			if !map1[num] {
				res2 = append(res2, num)
			}
		}
	
		// Return the result
		return [][]int{res1, res2}
	}
	
// @lc code=end

