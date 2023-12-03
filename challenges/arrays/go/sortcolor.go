package main

func sortColors(nums []int) {
	low := 0
	mid := 0
	high := len(nums) - 1
	for mid <= high {
		if nums[mid] == 0 {
			nums[mid], nums[low] = nums[low], nums[mid]
			mid++
			low++
		} else if nums[mid] == 1 {
			mid++
		} else {
			nums[mid], nums[high] = nums[high], nums[mid]
			high--
		}
	}
}
