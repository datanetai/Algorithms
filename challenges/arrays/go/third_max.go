package main

import (
	"container/heap"
	"math"
)

func thirdMax(nums []int) int {
	maxes := []int{math.MinInt64, math.MinInt64, math.MinInt64}
	for i := 0; i < len(nums); i++ {
		if nums[i] > maxes[0] {
			maxes[2] = maxes[1]
			maxes[1] = maxes[0]
			maxes[0] = nums[i]

		}
		if nums[i] > maxes[1] && nums[i] < maxes[0] {
			maxes[2] = maxes[1]
			maxes[1] = nums[i]

		}
		if nums[i] > maxes[2] && nums[i] < maxes[1] {
			maxes[2] = nums[i]

		}

	}
	max := maxes[2]
	if max == math.MinInt64 {
		max = maxes[0]
	}
	return max
}

// approach 2 using heap O(nlogn)

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
func thirdMax2(nums []int) int {
	h := &IntHeap{}
	heap.Init(h)
	m := map[int]bool{}
	for _, n := range nums {
		if !m[n] {
			m[n] = true
			heap.Push(h, n)
			if h.Len() > 3 {
				heap.Pop(h)
			}
		}
	}
	if h.Len() == 2 {
		heap.Pop(h)
	}

	return heap.Pop(h).(int)
}

func main() {
	arr := []int{3, 2, 1}
	thirdMax(arr)
}
