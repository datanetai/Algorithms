package main

import (
	"fmt"
	"math"
	"strconv"
)

// find number of consective 1s in a binary array
// complexity O(n)
func findMaxConsecutiveOnes(nums []int) int {
	count := 0
	maxcount := 0
	for _, v := range nums {
		if v != 1 {
			if count > maxcount {
				maxcount = count
			}
			count = 0
		} else {
			count++
		}
	}
	if count > maxcount {
		maxcount = count
	}
	return maxcount
}

// second solution
func findMaxConsecutiveOnes2(nums []int) int {
	maxCount := 0
	pos := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			maxCount = max(maxCount, i-pos)
			pos = i + 1
		}
	}
	return max(maxCount, len(nums)-pos)
}

// Find Numbers with Even Number of Digits
// complexity O(mlgn)
func hasEvenDigits(num int) bool {
	count := 0
	for num != 0 {
		num /= 10
		count++
	}
	return (count & 1) == 0
}
func findNumbers(nums []int) int {
	evens := 0
	for _, v := range nums {
		if hasEvenDigits(v) {
			evens++
		}
	}
	return evens
}

// using string
func findNumbers2(nums []int) int {
	evens := 0
	for _, v := range nums {
		if len(strconv.Itoa(v))&1 == 0 {
			evens++
		}
	}
	return evens
}

// using log10
func findNumbers3(nums []int) int {
	even := 0
	for _, v := range nums {
		if int(math.Log10(float64(v)))%2 == 1 {
			even++
		}
	}
	return even
}

// using constraint integers in the range [1,100000][1, 100000][1,100000]
func findNumbers4(nums []int) int {
	even := 0
	for _, v := range nums {
		if (v > 9 && v < 100) || (v > 999 && v < 10000) || v == 100000 {
			even++
		}
	}
	return even
}

// Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

// Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
// complexity O(n^2)
func duplicateZeros(arr []int) {
	i := 0
	for i < len(arr) {
		if arr[i] == 0 {
			insert(arr, i, 0)
			i++
		}
		i++
	}
}

func insert(arr []int, index int, value int) {
	for i := len(arr) - 1; i > index; i-- {
		arr[i] = arr[i-1]
	}
	arr[index] = value
}

// approach 2 complexity O(n)
func duplicateZeros2(arr []int) {
	possibleDups := 0
	length := len(arr) - 1
	for left := 0; left <= length-possibleDups; left++ {
		if arr[left] == 0 {
			if left == length-possibleDups {
				arr[length] = 0
				length--
				break
			}
			possibleDups++
		}
	}
	last := length - possibleDups
	for i := last; i >= 0; i-- {
		if arr[i] == 0 {
			arr[i+possibleDups] = 0
			possibleDups--
			arr[i+possibleDups] = 0
		} else {
			arr[i+possibleDups] = arr[i]
		}
	}
}

// solution 3 using queue space complexity O(n)
func duplicateZeros3(arr []int) {
	queue := []int{}
	for i := 0; i < len(arr); i++ {
		queue = append(queue, arr[i])
		if arr[i] == 0 {
			queue = append(queue, 0)
		}
		arr[i] = queue[0]
		queue = queue[1:]
	}
}
func main() {
	arr := []int{1, 1, 1, 0, 1, 1}
	fmt.Println(findMaxConsecutiveOnes(arr))
	println("Hello World")
}
