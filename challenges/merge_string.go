// 1768. Merge Strings Alternately
// Solved
// Easy
// Topics
// Companies
// Hint
// You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

// Return the merged string.

 

// Example 1:

// Input: word1 = "abc", word2 = "pqr"
// Output: "apbqcr"
// Explanation: The merged string will be merged as so:
// word1:  a   b   c
// word2:    p   q   r
// merged: a p b q c r
// Example 2:

// Input: word1 = "ab", word2 = "pqrs"
// Output: "apbqrs"
// Explanation: Notice that as word2 is longer, "rs" is appended to the end.
// word1:  a   b 
// word2:    p   q   r   s
// merged: a p b q   r   s
// Example 3:

// Input: word1 = "abcd", word2 = "pq"
// Output: "apbqcd"
// Explanation: Notice that as word1 is longer, "cd" is appended to the end.
// word1:  a   b   c   d
// word2:    p   q 
// merged: a p b q c   d
 
func mergeAlternately(word1 string, word2 string) string {
    i := 0
	j := 0
	var result string
	for i < len(word1) && j < len(word2) {
		result += string(word1[i])
		result += string(word2[j])
		i = i + 1
		j = j + 1
	}

	for i < len(word1){
		result += string(word1[i])
		i = i + 1
	}
	for j < len(word2){
		result += string(word2[j])  
		j = j + 1
	}
	return result
}