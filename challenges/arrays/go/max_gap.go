package main

func maximumGap(nums []int) int {
	// sort nums using bucket sort
	bucketSort(nums, 350)
	// print nums
	for _, num := range nums {
		println(num)
	}
	maxgap := 0
	for i := 1; i < len(nums); i++ {
		gap := abs(nums[i] - nums[i-1])
		if gap > maxgap {
			maxgap = gap
		}
	}
	return maxgap
}
func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}
func radixSort(nums []int) {
	max := 0
	for _, num := range nums {
		if num > max {
			max = num
		}
	}

	exp := 1
	for max/exp > 0 {
		countingSortByDigit(nums, exp)
		exp *= 10
	}

}

func countingSortByDigit(nums []int, exp int) {
	counts := make([]int, 10)
	sorted := make([]int, len(nums))

	for _, num := range nums {
		d := (num / exp) % 10
		counts[d]++
	}

	for i := 1; i < 10; i++ {
		counts[i] += counts[i-1]
	}

	for i := len(nums) - 1; i >= 0; i-- {
		d := (nums[i] / exp) % 10
		sorted[counts[d]-1] = nums[i]
		counts[d]--
	}
	copy(nums, sorted)
}

func bucketSort(nums []int, bucketCount int) {
	min, max := nums[0], nums[0]
	for _, num := range nums {
		if num < min {
			min = num
		} else if num > max {
			max = num
		}
	}

	// Define the range for each bucket
	bucketRange := (max - min + 1 + bucketCount - 1) / bucketCount

	// Create buckets
	buckets := make([][]int, bucketCount)
	for i := 0; i < bucketCount; i++ {
		buckets[i] = []int{}
	}

	// Place elements in respective buckets
	for _, num := range nums {
		idx := (num - min) / bucketRange
		buckets[idx] = append(buckets[idx], num)
	}

	// Sort buckets and merge
	index := 0
	for _, bucket := range buckets {
		radixSort(bucket)
		for _, num := range bucket {
			nums[index] = num
			index++
		}
	}
}

// Suppose there are N elements in the array, the min value is min and the max value is max. Then the maximum gap will be no smaller than ceiling[(max - min ) / (N - 1)].

// Let gap = ceiling[(max - min ) / (N - 1)]. We divide all numbers in the array into n-1 buckets, where k-th bucket contains all numbers in [min + (k-1)gap, min + k*gap). Since there are n-2 numbers that are not equal min or max and there are n-1 buckets, at least one of the buckets are empty. We only need to store the largest number and the smallest number in each bucket.
// apprach 2

func maximumGap2(nums []int) int {
	// If the array has less than two elements, return 0
	if len(nums) < 2 {
		return 0
	}

	// Find the minimum and maximum value in the array
	min, max := nums[0], nums[0]
	for _, num := range nums {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	// If the minimum and maximum are equal, return 0
	if min == max {
		return 0
	}

	// Calculate the gap size
	gap := (max - min + len(nums) - 2) / (len(nums) - 1)

	// Create an array of buckets, each with a min and max value
	buckets := make([][2]int, len(nums)-1)
	for i := range buckets {
		// Initialize the min and max value to -1, indicating empty bucket
		buckets[i] = [2]int{-1, -1}
	}

	// Iterate over the array and assign each number to a bucket
	for _, num := range nums {
		// Skip the minimum and maximum value
		if num == min || num == max {
			continue
		}
		// Find the index of the bucket
		index := (num - min) / gap
		// Update the min and max value of the bucket
		if buckets[index][0] == -1 || num < buckets[index][0] {
			buckets[index][0] = num
		}
		if buckets[index][1] == -1 || num > buckets[index][1] {
			buckets[index][1] = num
		}
	}

	// Initialize the maximum gap and the previous value
	maxGap := 0
	prev := min

	// Iterate over the buckets and update the maximum gap
	for _, bucket := range buckets {
		// Skip the empty buckets
		if bucket[0] == -1 {
			continue
		}
		// Update the maximum gap with the difference between the current bucket's min and the previous value
		maxGap = maxInt(maxGap, bucket[0]-prev)
		// Update the previous value with the current bucket's max
		prev = bucket[1]
	}

	// Update the maximum gap with the difference between the maximum value and the previous value
	maxGap = maxInt(maxGap, max-prev)

	// Return the maximum gap
	return maxGap
}

// Helper function to return the maximum of two integers
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	nums := []int{1, 3, 100}
	println(maximumGap2(nums))
}
