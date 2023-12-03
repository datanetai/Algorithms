package main

import "sort"

// Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
func findDisappearedNumbers(nums []int) []int {
	hash := make(map[int]bool)
	for _, num := range nums {
		hash[num] = true
	}
	var res []int
	for i := 1; i <= len(nums); i++ {
		if !hash[i] {
			res = append(res, i)
		}
	}
	return res
}

// approach 2 using boolean array instead of hashset since num is in [1,n] O(n)
func findDisappearedNumbers1(nums []int) []int {
	var res []int
	seen := make([]bool, len(nums)+1)
	for _, num := range nums {
		seen[num] = true
	}
	for i := 1; i < len(seen); i++ {
		if !seen[i] {
			res = append(res, i)
		}
	}
	return res
}

// approach 3 using O(1) space
// this is most efficient for this problem as nums[i] is in the range [1, n]

func findDisappearedNumbers2(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		index := abs(nums[i]) - 1
		if nums[index] > 0 {
			nums[index] = -nums[index]
		}
	}
	var res []int
	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			res = append(res, i+1)
		}
	}
	return res
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// approach 4 using binary search O(nlogn)
func findDisappearedNumbers3(nums []int) []int {
	sort.Ints(nums) // Sort the array
	var res []int
	for i := 1; i <= len(nums); i++ {
		if !binarySearch(nums, i) {
			res = append(res, i) // If i is not found, add it to the result
		}
	}
	return res
}

func binarySearch(nums []int, target int) bool {
	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			return true
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return false
}
