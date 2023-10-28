package main

import "fmt"

// quicksort
func partition(arr []int, low, high int) int {
	pivot := arr[high]
	i := low - 1
	for j := low; j < high; j++ {
		if arr[j] < pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}

	}
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1
}

func quickSort(arr []int, low, high int) {
	if low < high {
		pivot := partition(arr, low, high)
		quickSort(arr, low, pivot-1)
		quickSort(arr, pivot+1, high)
	}
}

func main() {
	arr := []int{10, 80, 30, 90, 40, 50, 70}
	arr = append(arr, 0)
	quickSort(arr, 0, len(arr)-1)
	fmt.Println(arr)
}
