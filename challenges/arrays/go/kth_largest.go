package main

import (
	"container/heap"
	"math/rand"
	"time"
)

// approach 1 using quicksort recursive O(n) in average case
func findKthLargest(nums []int, k int) int {
	return quickSelect(nums, 0, len(nums)-1, len(nums)-k)
}

func quickSelect(nums []int, left, right, k int) int {
	if left == right {
		return nums[left]
	}

	pivotIndex := partition(nums, left, right)

	if k == pivotIndex {
		return nums[k]
	} else if k < pivotIndex {
		return quickSelect(nums, left, pivotIndex-1, k)
	} else {
		return quickSelect(nums, pivotIndex+1, right, k)
	}
}

// approach 2 quicksort iterative O(n) in average case
func findKthLargest2(nums []int, k int) int {
	rand.Shuffle(len(nums), func(i, j int) {
		nums[i], nums[j] = nums[j], nums[i]
	})
	k = len(nums) - k
	left, right := 0, len(nums)-1
	for left < right {
		pivotIndex := partition(nums, left, right)
		if pivotIndex < k {
			left = pivotIndex + 1
		} else if pivotIndex > k {
			right = pivotIndex - 1
		} else {
			break
		}
	}
	return nums[k]
}

// random pivot
func partition(nums []int, start int, end int) int {
	localRand := rand.New(rand.NewSource(time.Now().UnixNano()))
	// Generating a random index using the local random generator
	pivotIndex := start + localRand.Intn(end-start+1)
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

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// approach 3 using heap O(nlogk)
func findKthLargest3(nums []int, k int) int {
	h := &IntHeap{}
	heap.Init(h)
	for _, v := range nums {
		heap.Push(h, v)
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	return heap.Pop(h).(int)
}
