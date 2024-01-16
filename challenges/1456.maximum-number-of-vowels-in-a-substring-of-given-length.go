/*
 * @lc app=leetcode id=1456 lang=golang
 *
 * [1456] Maximum Number of Vowels in a Substring of Given Length
 *
 * https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
 *
 * algorithms
 * Medium (57.91%)
 * Likes:    3308
 * Dislikes: 114
 * Total Accepted:    245.3K
 * Total Submissions: 421.3K
 * Testcase Example:  '"abciiidef"\n3'
 *
 * Given a string s and an integer k, return the maximum number of vowel
 * letters in any substring of s with length k.
 *
 * Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abciiidef", k = 3
 * Output: 3
 * Explanation: The substring "iii" contains 3 vowel letters.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "aeiou", k = 2
 * Output: 2
 * Explanation: Any substring of length 2 contains 2 vowels.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "leetcode", k = 3
 * Output: 2
 * Explanation: "lee", "eet" and "ode" contain 2 vowels.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of lowercase English letters.
 * 1 <= k <= s.length
 *
 *
 */

// @lc code=start
func maxVowels(s string, k int) int {
	// Define vowels
	vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
	vowelCount := 0
	maxVowels := 0

	// Count vowels in first window of size k
	for i := 0; i < k; i++ {
		if vowels[rune(s[i])] {
			vowelCount++
		}
	}
	maxVowels = vowelCount

	// Slide the window over the string
	for i := k; i < len(s); i++ {
		// Decrease count if character leaving window is a vowel
		if vowels[rune(s[i-k])] {
			vowelCount--
		}
		// Increase count if character entering window is a vowel
		if vowels[rune(s[i])] {
			vowelCount++
		}
		// Update maxVowels
		if vowelCount > maxVowels {
			maxVowels = vowelCount
		}
	}
	return maxVowels
}

// @lc code=end

