package main

// Find the Index of the First Occurrence in a String
// approach 1 brute force 1
func strStr(haystack string, needle string) int {
	i := 0
	j := 0
	start := 0
	for ; i < len(haystack); i++ {
		if haystack[i] == needle[j] {
			if j == 0 {
				start = i
			}
			j++

		} else {
			if j > 0 {
				i = start
			}
			j = 0
		}
		if j == len(needle) {
			return start

		}

	}
	return -1
}

// approach 2 - brute force beats 100% of submissions ironicaly!
func strStr2(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	for i := 0; i < len(haystack); i++ {
		if haystack[i] == needle[0] {
			j := 1
			for ; j < len(needle); j++ {
				if i+j >= len(haystack) {
					return -1
				}
				if haystack[i+j] != needle[j] {
					break
				}
			}
			if j == len(needle) {
				return i
			}
		}
	}
	return -1
}

// todo understand this approach  3 - Z algorithm complexity O(n+m)
func strStr3(haystack string, needle string) int {
	if needle == "" {
		return 0
	}

	// Concatenate needle, a special character, and haystack
	concat := needle + "$" + haystack
	Z := createZArray(concat)

	// Iterate through the Z array to find matches
	for i := 0; i < len(Z); i++ {
		if Z[i] == len(needle) {
			return i - len(needle) - 1 // Adjust index for the concatenated string
		}
	}
	return -1
}

func createZArray(s string) []int {
	n := len(s)
	Z := make([]int, n)
	L, R, k := 0, 0, 0

	for i := 1; i < n; i++ {
		if i > R {
			L, R = i, i
			for R < n && s[R-L] == s[R] {
				R++
			}
			Z[i] = R - L
			R--
		} else {
			k = i - L
			if Z[k] < R-i+1 {
				Z[i] = Z[k]
			} else {
				L = i
				for R < n && s[R-L] == s[R] {
					R++
				}
				Z[i] = R - L
				R--
			}
		}
	}
	return Z
}

func main() {
	println(strStr("breakiking", "king"))

}
