package main

// You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

// You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:

// Trim each number in nums to its rightmost trimi digits.
// Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
// Reset each number in nums to its original lengt

type Pair struct {
	index int
	value string
}

func smallestTrimmedNumbers(nums []string, queries [][]int) []int {
	res := make([]int, len(queries))
	for i := 0; i < len(queries); i++ {
		k := queries[i][0]
		trim := queries[i][1]

		// Create pairs of index and trimmed string
		pairs := make([]Pair, len(nums))
		for j := 0; j < len(nums); j++ {
			numStr := nums[j]
			trimmedStr := numStr[len(numStr)-trim:]
			pairs[j] = Pair{j, trimmedStr}
		}

		// Sort pairs based on trimmed string values
		radixSort(pairs)

		// Get index of kth smallest
		res[i] = pairs[k-1].index
	}
	return res
}

func radixSort(pairs []Pair) {
	maxLength := 0
	for _, pair := range pairs {
		if len(pair.value) > maxLength {
			maxLength = len(pair.value)
		}
	}

	// Sort from least significant digit to most significant
	for digit := 0; digit < maxLength; digit++ {
		countingSortByDigit(pairs, digit)
	}
}

func countingSortByDigit(pairs []Pair, digit int) {
	counts := make([]int, 10)
	sorted := make([]Pair, len(pairs))

	// Count digit occurrences at the current position
	for _, pair := range pairs {
		d := charAt(pair.value, digit)
		counts[d]++
	}

	// Cumulative count
	for i := 1; i < 10; i++ {
		counts[i] += counts[i-1]
	}

	// Build the sorted array
	for i := len(pairs) - 1; i >= 0; i-- {
		d := charAt(pairs[i].value, digit)
		sorted[counts[d]-1] = pairs[i]
		counts[d]--
	}

	// Copy back to the original array
	copy(pairs, sorted)
}

// charAt returns the digit at the specified position from the right, or 0 if out of range
func charAt(s string, pos int) int {
	if pos < len(s) {
		return int(s[len(s)-1-pos] - '0')
	}
	return 0 // Shorter strings are treated as if they have leading zeros
}

func main() {
	nums := []string{"89288488870527604910029", "36097185739782752175822", "66626740310751086142991", "39210310199276100943112", "27763774389382535382104", "38417381130871656561097", "88045540666254006395713", "95788007927435793172832", "15831923319620654311625", "45043895456202186804606", "87291364237858759125697", "88163116582250002569968", "00507332488046565482379", "57170661333341274356658", "06401271520738451116188", "21731485952024837866860"}

	queries := [][]int{{3, 17}, {10, 22}, {13, 21}, {12, 16}, {1, 23}, {10, 19}, {12, 21}, {10, 5}, {12, 9}, {12, 10}, {9, 5}, {12, 8}, {14, 6}, {5, 10}, {11, 4}, {15, 15}, {13, 9}, {1, 19}, {5, 12}, {10, 15}, {4, 18}, {4, 3}, {16, 13}, {6, 19}, {4, 18}, {2, 6}, {15, 12}}
	res := smallestTrimmedNumbers(nums, queries)
	for i := 0; i < len(res); i++ {
		print(res[i], " ")
	}
}
