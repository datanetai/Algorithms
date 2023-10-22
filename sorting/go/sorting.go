package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	test()
}

func selectionSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		min := i
		for j := i + 1; j < len(arr); j++ {
			if arr[j] < arr[min] {
				min = j
			}
		}
		arr[i], arr[min] = arr[min], arr[i]
	}
	return arr
}

func bubbleSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for j := len(arr) - 1; j > i; j-- {
			if arr[j] < arr[j-1] {
				arr[j], arr[j-1] = arr[j-1], arr[j]
			}
		}

	}
	return arr
}

func insertionSort(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		current := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > current {
			arr[j+1] = arr[j]
			j--

		}
		arr[j+1] = current
	}
	return arr
}
func merge(left_arr []int, right_arr []int) []int {
	left_index := 0
	right_index := 0
	result := make([]int, len(left_arr)+len(right_arr))
	for left_index < len(left_arr) && right_index < len(right_arr) {
		if left_arr[left_index] < right_arr[right_index] {
			result[left_index+right_index] = left_arr[left_index]
			left_index++
		} else {
			result[left_index+right_index] = right_arr[right_index]
			right_index++
		}

	}
	for left_index < len(left_arr) {
		result[left_index+right_index] = left_arr[left_index]
		left_index++
	}
	for right_index < len(right_arr) {
		result[left_index+right_index] = right_arr[right_index]
		right_index++
	}

	return result
}

// using sentinel
func merge2(left_arr []int, right_arr []int) []int {
	left_arr = append(left_arr, 999999999)
	right_arr = append(right_arr, 999999999)
	left_index := 0
	right_index := 0
	result := make([]int, len(left_arr)+len(right_arr))
	for i := 0; i < len(result); i++ {
		if left_arr[left_index] < right_arr[right_index] {
			result[i] = left_arr[left_index]
			left_index++
		} else {
			result[i] = right_arr[right_index]
			right_index++
		}

	}
	return result
}

func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	mid := len(arr) / 2
	left_arr := mergeSort(arr[:mid])
	right_arr := mergeSort(arr[mid:])
	return merge(left_arr, right_arr)
}
func isSorted(arr []int) bool {
	for i := 1; i < len(arr); i++ {
		if arr[i] < arr[i-1] {
			return false
		}
	}
	return true
}

func test() {
	rand.Seed(time.Now().UnixNano())
	start := time.Now()
	// Testing with random numbers
	for i := 0; i < 10; i++ {
		arr := make([]int, 100)
		for j := 0; j < 100; j++ {
			arr[j] = rand.Intn(1000)
		}

		if !isSorted(selectionSort(arr)) {
			fmt.Println("Selection Sort failed")
		}
		if !isSorted(bubbleSort(arr)) {
			fmt.Println("Bubble Sort failed")
		}

		if !isSorted(insertionSort(arr)) {
			fmt.Println("Insertion Sort failed")
		}

		if !isSorted(mergeSort(arr)) {
			fmt.Println("Merge Sort failed")
		}

	}
	// print time
	fmt.Println("Time elapsed: ", time.Since(start))

}
