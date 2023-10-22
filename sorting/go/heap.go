// heap implemetaion in go
package main

import "fmt"

func left(i int) int {
	return 2*i + 1
}
func right(i int) int {
	return 2*i + 2
}
func parent(i int) int {
	return (i - 1) / 2
}

func maxHeapify(arr []int, i int, heapSize int) {
	l := left(i)
	r := right(i)
	largest := i
	if l < heapSize && arr[l] > arr[i] {
		largest = l
	}
	if r < heapSize && arr[r] > arr[largest] {
		largest = r
	}
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		maxHeapify(arr, largest, heapSize)
	}

}

func buildMaxHeap(arr []int) {
	heapSize := len(arr)
	for i := len(arr)/2 - 1; i >= 0; i-- {
		maxHeapify(arr, i, heapSize)
	}
}

func heapSort(arr []int) {
	heapSize := len(arr)
	buildMaxHeap(arr)
	for i := len(arr) - 1; i >= 1; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapSize--
		maxHeapify(arr, 0, heapSize)
	}
}

func main() {
	arr := []int{9, 9, 7, 6, 5, 4, 3, 22, 1}
	fmt.Println("Before sorting:", arr)
	heapSort(arr)
	fmt.Println("After sorting:", arr)
}
