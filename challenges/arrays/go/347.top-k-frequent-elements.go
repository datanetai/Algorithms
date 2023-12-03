/*
 * @lc app=leetcode id=347 lang=golang
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
package main

import "container/heap"

// func topKFrequent(nums []int, k int) []int {
// 	hash := make(map[int]int)
// 	for _, num := range nums {
// 		hash[num]++
// 	}
// 	// now we will use heap to maintain top k frequent elements
// 	h := &IntHeap{}
// 	heap.Init(h)
// 	for num, freq := range hash {
// 		heap.Push(h, key_freq{freq, num})
// 		if h.Len() > k {
// 			heap.Pop(h)
// 		}
// 	}
// 	res := make([]int, k)
// 	for i := 0; i < k; i++ {
// 		res[i] = heap.Pop(h).(key_freq).num
// 	}
// 	return res
// }

// approach 2 use array instead of hash
func topKFrequent(nums []int, k int) []int {
	// first we will count the frequency of each element
	offset := 10000
	freq := make([]int, 2*offset+1)
	for _, num := range nums {
		freq[num+offset]++
	}
	// now we will use heap to maintain top k frequent elements
	h := &IntHeap{}
	heap.Init(h)
	for num, f := range freq {
		if f > 0 {
			heap.Push(h, key_freq{f, num - offset})
			if h.Len() > k {
				heap.Pop(h)
			}
		}
	}
	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[i] = heap.Pop(h).(key_freq).num
	}
	return res
}

// implement heap (key, value) = (freq, num)
type key_freq struct {
	freq int
	num  int
}

type IntHeap []key_freq

func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i int, j int) bool {
	return h[i].freq < h[j].freq
}
func (h IntHeap) Swap(i int, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(key_freq))
}
func (h *IntHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

// @lc code=end
