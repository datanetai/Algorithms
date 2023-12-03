package main

import "sort"

// simple sort the array than sum the odd index
// proof here https://leetcode.com/problems/array-partition/solutions/102170/java-solution-sorting-and-rough-proof-of-algorithm/
// Time complexity: O(nlogn)
func arrayPairSum(nums []int) int {
	// sort the array
	sort.Ints(nums)
	s := 0
	for i := 0; i < len(nums); i += 2 {
		s += nums[i]
	}
	return s
}

// using counting sort
// Time complexity: O(n)
func arrayPairSum2(nums []int) int {
	exist := make([]int, 20001)
	for _, v := range nums {
		exist[v+10000]++
	}
	odd := true
	s := 0
	for i := 0; i < len(exist); i++ {
		for exist[i] > 0 {
			if odd {
				s += i - 10000
			}
			odd = !odd
			exist[i]--

		}
	}
	return s
}
