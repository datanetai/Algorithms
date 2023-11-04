package main

import "sort"

// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct
// O(n)
func containsDuplicate(nums []int) bool {
	numSet := make(map[int]bool)
	for _, num := range nums {
		if numSet[num] {
			return true
		}
		numSet[num] = true
	}
	return false
}

// approach 2 O(nlogn)
func containsDuplicate2(nums []int) bool {
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			return true
		}
	}
	return false
}
