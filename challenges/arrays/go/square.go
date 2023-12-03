package main

import (
	"sort"
)

//	Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

// complexity: O(nlogn) time
func sortedSquares(nums []int) []int {
	// take squares of all elements
	for i := 0; i < len(nums); i++ {
		nums[i] *= nums[i]
	}
	// sort the array
	sort.Ints(nums)
	return nums
}

// approach 2 - two pointers - O(n) time
func sortedSquares2(nums []int) []int {
	start := 0
	end := len(nums) - 1
	result := make([]int, len(nums))
	for i := len(nums) - 1; i >= 0; i-- {
		if abs(nums[start]) > abs(nums[end]) {
			result[i] = nums[start] * nums[start]
			start++
		} else {
			result[i] = nums[end] * nums[end]
			end--
		}
	}
	return result
}
func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

// approach 3 - counting sort - O(n) time and use extra space beacuse of contraints 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
func sortedSquares3(nums []int) []int {
	// create a frequency array
	freq := make([]int, 10001)
	for _, num := range nums {
		freq[abs(num)]++
	}
	// commulative sum
	for i := 1; i < len(freq); i++ {
		freq[i] += freq[i-1]
	}
	// create a result array
	result := make([]int, len(nums))
	for _, num := range nums {
		result[freq[abs(num)]-1] = num * num
		freq[abs(num)]--
	}
	return result
}

func main() {
	nums := []int{-4, -1, 0, 3, 10}
	result := sortedSquares3(nums)
	for _, num := range result {
		println(num)
	}
}
