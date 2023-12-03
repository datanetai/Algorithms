package main

// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

// Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

// Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
// Return k.
// -100 <= nums[i] <= 100

// approach 1 - counting sort
func removeDuplicates(nums []int) int {``
	count := make([]int, 201)
	for _, num := range nums {
		count[num+100] = 1
	}
	k := 0
	for i := 0; i < 201; i++ {
		if count[i] == 1 {
			nums[k] = i - 100
			k++
		}
	}
	return k
}

// approach 2 - two pointers
func removeDuplicates2(nums []int) int {
	k := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			nums[k] = nums[i]
			k++
		}
	}
	return k
}
