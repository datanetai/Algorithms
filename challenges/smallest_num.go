// 2336. Smallest Number in Infinite Set
// Medium
// Topics
// Companies
// Hint
// You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

// Implement the SmallestInfiniteSet class:

// SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
// int popSmallest() Removes and returns the smallest integer contained in the infinite set.
// void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

// Example 1:

// Input
// ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
// [[], [2], [], [], [], [1], [], [], []]
// Output
// [null, null, 1, 2, 3, null, 1, 4, 5]

// Explanation
// SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
// smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
// smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
// smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
// smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
// smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
// smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
//                                    // is the smallest number, and remove it from the set.
// smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
// smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

package main

import "container/heap"

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


type SmallestInfiniteSet struct {
    heap  IntHeap
    used  map[int]bool
}



func Constructor() SmallestInfiniteSet {
    h := IntHeap{}
    heap.Init(&h)
    return SmallestInfiniteSet{heap: h, used: make(map[int]bool)}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
    if len(this.heap) > 0 {
        smallest := heap.Pop(&this.heap).(int) // Pop from the heap
        this.used[smallest] = true           // Mark as used
        return smallest
    } else { // Heap is empty, find the smallest unused like before
        smallest := 1
        for this.used[smallest] {
            smallest++
        }
        this.used[smallest] = true
        return smallest
    }
}

func (this *SmallestInfiniteSet) AddBack(num int) {
    if this.used[num] {
        delete(this.used, num)
        heap.Push(&this.heap, num)
    }
}
