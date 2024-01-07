/*
 * @lc app=leetcode id=151 lang=golang
 *
 * [151] Reverse Words in a String
 *
 * https://leetcode.com/problems/reverse-words-in-a-string/description/
 *
 * algorithms
 * Medium (38.05%)
 * Likes:    7831
 * Dislikes: 5004
 * Total Accepted:    1.3M
 * Total Submissions: 3.2M
 * Testcase Example:  '"the sky is blue"'
 *
 * Given an input string s, reverse the order of the words.
 *
 * A word is defined as a sequence of non-space characters. The words in s will
 * be separated by at least one space.
 *
 * Return a string of the words in reverse order concatenated by a single
 * space.
 *
 * Note that s may contain leading or trailing spaces or multiple spaces
 * between two words. The returned string should only have a single space
 * separating the words. Do not include any extra spaces.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "the sky is blue"
 * Output: "blue is sky the"
 *
 *
 * Example 2:
 *
 *
 * Input: s = "  hello world  "
 * Output: "world hello"
 * Explanation: Your reversed string should not contain leading or trailing
 * spaces.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "a good   example"
 * Output: "example good a"
 * Explanation: You need to reduce multiple spaces between two words to a
 * single space in the reversed string.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^4
 * s contains English letters (upper-case and lower-case), digits, and spaces '
 * '.
 * There is at least one word in s.
 *
 *
 *
 * Follow-up: If the string data type is mutable in your language, can you
 * solve it in-place with O(1) extra space?
 *
 */

// @lc code=start
// split into words, reverse and join
func reverseWords(s string) string {
	words := strings.Fields(s)
	for i, j := 0, len(words)-1; i < j; i, j = i+1, j-1 {
		words[i], words[j] = words[j], words[i]
	}
	return strings.Join(words, " ")
}

// reverse the whole string, then reverse each word
func reverseWords(s string) string {
	bytes := []byte(s)
	// Reverse the entire slice
	reverse(bytes, 0, len(bytes)-1)

	wordStart, wordEnd, i := 0, 0, 0
	for i < len(bytes) {
		// Skip spaces
		for i < len(bytes) && bytes[i] == ' ' {
			i++
		}
		// If we're at the end of the string, break
		if i == len(bytes) {
			break
		}
		// If this is not the first word, add a space before it
		if wordEnd > 0 {
			bytes[wordEnd] = ' '
			wordEnd++
		}
		// Set the start of the word
		wordStart = wordEnd
		// Move to the end of the word
		for i < len(bytes) && bytes[i] != ' ' {
			bytes[wordEnd] = bytes[i]
			i++
			wordEnd++
		}
		// Reverse the word
		reverse(bytes, wordStart, wordEnd-1)
	}
	return string(bytes[:wordEnd])
}

func reverse(bytes []byte, start int, end int) {
	for start < end {
		bytes[start], bytes[end] = bytes[end], bytes[start]
		start++
		end--
	}
}

// @lc code=end

