package main

// Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

// Return any array that satisfies this condition.
func sortArrayByParity(nums []int) []int {
	even := 0
	for i := 0; i < len(nums); i++ {
		if nums[i]&1 == 0 {
			nums[i], nums[even] = nums[even], nums[i]
			even++
		}
	}
	return nums
}
func main() {
	nums := []int{3, 1, 2, 4}
	sortArrayByParity(nums)
	for _, v := range nums {
		println(v)
	}
}
