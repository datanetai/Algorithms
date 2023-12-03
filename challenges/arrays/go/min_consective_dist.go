package main

import "sort"

// Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

// Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
// complexity: O(nlogn)
func minimumAbsDifference(arr []int) [][]int {
	// sort
	sort.Ints(arr)
	// find min diff
	minDiff := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		diff := arr[i] - arr[i-1]
		if diff < minDiff {
			minDiff = diff
		}
	}
	// find pairs
	var pairs [][]int
	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] == minDiff {
			pairs = append(pairs, []int{arr[i-1], arr[i]})
		}
	}
	return pairs

}
