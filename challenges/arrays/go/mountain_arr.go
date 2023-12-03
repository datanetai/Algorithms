package main

import "fmt"

// Given an array of integers arr, return true if and only if it is a valid mountain array.

// Recall that arr is a mountain array if and only if:

// arr.length >= 3
// There exists some i with 0 < i < arr.length - 1 such that:
// arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
// arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
func validMountainArray(arr []int) bool {
	n := len(arr)
	if len(arr) < 3 {
		return false
	}
	// climb up
	i := 0
	for i < n-1 && arr[i+1] > arr[i] {
		i++
	}
	if i == 0 || i == n-1 {
		return false
	}
	// climb down
	for i < n-1 && arr[i+1] < arr[i] {
		i++
	}
	return i == n-1
}

// approach 2 more concise two pointers	
func validMountainArray2(arr []int) bool {
	i := 0
	j := len(arr) - 1
	for i < j && arr[i] < arr[i+1] {
		i++
	}
	for j > 0 && arr[j] < arr[j-1] {
		j--
	}
	return i > 0 && i == j && j < len(arr)-1
}
func main() {
	arr := []int{0, 3, 2, 1}
	fmt.Println(validMountainArray(arr))
	arr = []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(validMountainArray(arr))
}
