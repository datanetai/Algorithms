package main

// A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

// You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

// Return the number of indices where heights[i] != expected[i].

// approach 1: using counting sort O(n)
func heightChecker(heights []int) int {
	freqs := make([]int, 101)
	for _, h := range heights {
		freqs[h]++
	}
	misplaced := 0
	j := 0
	for i := 1; i < len(freqs); i++ {
		for freqs[i] > 0 {
			if heights[j] != i {
				misplaced++
			}
			j++
			freqs[i]--
		}
	}
	return misplaced
}
