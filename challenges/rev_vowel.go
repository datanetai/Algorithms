// 345. Reverse Vowels of a String
// Solved
// Easy
// Topics
// Companies
// Given a string s, reverse only all the vowels in the string and return it.

// The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

// Example 1:

// Input: s = "hello"
// Output: "holle"
// Example 2:

// Input: s = "leetcode"
// Output: "leotcede"
 

// Constraints:

// 1 <= s.length <= 3 * 105
// s consist of printable ASCII characters.


func reverseVowels(s string) string {
	start := 0
	end := len(s)-1
	vowels := "aeiouAEIOU"
	for start<end{
		 if !strings.Contains(vowels, string(s[start])){
			start++
			continue
		 }
		if !strings.Contains(vowels, string(s[end])){
			end--
			continue
		}
		s = swap(s, start, end)
		start++
		end--
	}
	return s
}
func swap(s string, i, j int) string{
	temp := s[i]
	s = s[:i] + string(s[j]) + s[i+1:]
	s = s[:j] + string(temp) + s[j+1:]
	return s
}

// version 2 with byte array more efficient
func reverseVowels(s string) string {
    vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
    b := []byte(s)
    start, end := 0, len(b)-1
    for start < end {
        if !vowels[b[start]] {
            start++
            continue
        }
        if !vowels[b[end]] {
            end--
            continue
        }
        b[start], b[end] = b[end], b[start]
        start++
        end--
    }
    return string(b)
}
