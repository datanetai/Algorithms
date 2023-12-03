// Write a function that reverses a string. The input string is given as an array of characters s.

// You must do this by modifying the input array in-place with O(1) extra memory.
// recursive string in place
func reverseString(s []byte) {
	reverseStringRecursive(s, 0, len(s)-1)
}

func reverseStringRecursive(s []byte, start int, end int) {
	if start >= end {
		return
	}
	s[start], s[end] = s[end], s[start]
	reverseStringRecursive(s, start+1, end-1)
}

