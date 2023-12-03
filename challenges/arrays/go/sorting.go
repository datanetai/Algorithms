package main

import (
	"container/heap"
	"math/rand"
	"sort"
	"time"
)

// using go sort function
func sortArray(nums []int) []int {
	buckets := make([][]int, 100001)
}

// insertion sort (in-place) iterative
func sortArray2(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	for i := 1; i < len(nums); i++ {
		j := i
		for j > 0 && nums[j-1] > nums[j] {
			nums[j-1], nums[j] = nums[j], nums[j-1]
			j -= 1
		}
	}
	return nums
}

// insertion sort (in-place) recursive
func sortArray3(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	insertionSort(nums, len(nums)-1)
	return nums
}
func insertionSort(nums []int, n int) {
	if n <= 0 {
		return
	}
	insertionSort(nums, n-1)
	j := n
	for j > 0 && nums[j-1] > nums[j] {
		nums[j-1], nums[j] = nums[j], nums[j-1]
		j -= 1
	}
}

// implementing heap

type IntHeap []int

func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i int, j int) bool {
	return h[i] < h[j]
}
func (h IntHeap) Swap(i int, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

// implementing heapsort
func sortArray4(nums []int) []int {
	// heapify
	h := &IntHeap{}
	heap.Init(h)
	for _, v := range nums {
		heap.Push(h, v)
	}
	for i := 0; i < len(nums); i++ {
		nums[i] = heap.Pop(h).(int)
	}
	return nums
}

// merge sort
func sortArray5(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	mid := len(nums) / 2
	left := sortArray2(nums[:mid])
	right := sortArray2(nums[mid:])
	return merge(left, right)
}

func merge(left []int, right []int) []int {
	result := []int{}
	l, r := 0, 0
	for l < len(left) && r < len(right) {
		if left[l] <= right[r] {
			result = append(result, left[l])
			l += 1
		} else {
			result = append(result, right[r])
			r += 1
		}
	}
	result = append(result, left[l:]...)
	result = append(result, right[r:]...)
	return result
}

// quick sort (in-place)
func sortArray6(nums []int) []int {
	quickSort(nums, 0, len(nums)-1)
	return nums
}

func quickSort(nums []int, start int, end int) {
	if start < end {
		pivot := partition(nums, start, end)
		quickSort(nums, start, pivot-1)
		quickSort(nums, pivot+1, end)
	}
}

func partition(nums []int, start int, end int) int {
	// random pivot
	rand.Seed(time.Now().UnixNano())
	pivotIndex := start + rand.Intn(end-start+1)
	nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex] // Swap pivot to end
	pivot := nums[end]
	i := start
	for j := start; j <= end; j++ { // Include end in the loop
		if nums[j] < pivot {
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
		}
	}
	nums[i], nums[end] = nums[end], nums[i]
	return i
}

// hoare's partition
func hoarepartition(nums []int, start int, end int) int {
	pivot := nums[start]
	i, j := start-1, end+1
	for {
		for {
			i += 1
			if nums[i] >= pivot {
				break
			}
		}
		for {
			j -= 1
			if nums[j] <= pivot {
				break
			}
		}
		if i >= j {
			return j
		}
		nums[i], nums[j] = nums[j], nums[i]
	}
}

// generalize counting sort
func countingSort(nums []int) []int {
	if len(nums) == 0 {
		return nums
	}

	// Find minimum and maximum values
	minVal, maxVal := nums[0], nums[0]
	for _, num := range nums {
		if num < minVal {
			minVal = num
		}
		if num > maxVal {
			maxVal = num
		}
	}

	// Create count array
	offset := -minVal // This is used to adjust negative indices
	counts := make([]int, maxVal-minVal+1)

	// Count the occurrences
	for _, num := range nums {
		counts[num+offset]++
	}

	// Sort the array
	index := 0
	for i, count := range counts {
		for count > 0 {
			nums[index] = i - offset
			index++
			count--
		}
	}

	return nums
}

// for only positive integers
func radixSort(nums []int) []int {
	if len(nums) == 0 {
		return nums
	}

	// Find maximum value
	maxVal := nums[0]
	for _, num := range nums {
		if num > maxVal {
			maxVal = num
		}
	}

	// Perform counting sort for each digit
	exp := 1
	for maxVal/exp > 0 {
		countingSortByDigit(nums, exp)
		exp *= 10
	}

	return nums
}

// handling negative integers by separating them from positive integers

func radixSort2(nums []int) []int {
	if len(nums) == 0 {
		return nums
	}

	// Separate negative and positive numbers
	negatives, positives := []int{}, []int{}
	for _, num := range nums {
		if num < 0 {
			negatives = append(negatives, -num) // Store as positive for sorting
		} else {
			positives = append(positives, num)
		}
	}

	// Sort negative and positive numbers separately
	radixSort(negatives)
	radixSort(positives)

	// Combine results, remembering to re-negate the negative numbers
	i := 0
	for j := len(negatives) - 1; j >= 0; j-- {
		nums[i] = -negatives[j]
		i++
	}
	for _, num := range positives {
		nums[i] = num
		i++
	}

	return nums
}

func countingSortByDigit(nums []int, exp int) {
	offset := 0
	counts := make([]int, 10)

	// Count the occurrences
	for _, num := range nums {
		digit := (num / exp) % 10
		counts[digit]++
	}

	// Compute the offset
	for i := 0; i < 10; i++ {
		counts[i], offset = offset, counts[i]+offset
	}

	// Sort the array
	sorted := make([]int, len(nums))
	for _, num := range nums {
		digit := (num / exp) % 10
		sorted[counts[digit]] = num
		counts[digit]++
	}

	// Copy the sorted array back to nums
	copy(nums, sorted)
}

func bucketSort(nums []int, bucketCount int) {
	min, max := nums[0], nums[0]
	// Find minimum and maximum values
	for _, num := range nums {
		if num < min {
			min = num
		} else if num > max {
			max = num
		}
	}

	// Define the range for each bucket
	rangePerBucket := max - min
	if rangePerBucket == 0 {
		rangePerBucket = 1
	} else {
		rangePerBucket = (rangePerBucket / bucketCount) + 1
	}

	// Create and distribute elements into buckets
	buckets := make([][]int, bucketCount)
	for _, num := range nums {
		index := (num - min) / rangePerBucket
		if index >= bucketCount {
			index = bucketCount - 1
		}
		buckets[index] = append(buckets[index], num)
	}
	// Sort individual buckets and merge
	sortedIndex := 0
	for _, bucket := range buckets {
		sort.Ints(bucket)
		for _, num := range bucket {
			nums[sortedIndex] = num
			sortedIndex++
		}
	}
}
