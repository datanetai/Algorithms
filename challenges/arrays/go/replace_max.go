package main

// Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

// After doing so, return the array.
func replaceElements(arr []int) []int {
	max := -1
	for i := len(arr) - 1; i >= 0; i-- {
		temp := arr[i]
		arr[i] = max
		if temp > max {
			max = temp
		}
	}
	return arr
}
