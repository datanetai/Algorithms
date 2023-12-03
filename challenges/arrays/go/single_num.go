package main

//  Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

// You must implement a solution with a linear runtime complexity and use only constant extra space.
// Complexity: O(n) time and O(n) space
func singleNumber(nums []int) int {
	hash := make(map[int]int)
	for _, num := range nums {
		hash[num]++
	}
	for key, value := range hash {
		if value == 1 {
			return key
		}
	}
	return -1
}

// using XOR
// A XOR 0 = A
// A XOR A = 0 so it works for even number of elements
// Complexity: O(n) time and O(1) space
func singleNumber2(nums []int) int {
	result := 0
	for _, num := range nums {
		result ^= num
	}
	return result
}
