/*
 * @lc app=leetcode id=345 lang=golang
 *
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (51.63%)
 * Likes:    4274
 * Dislikes: 2726
 * Total Accepted:    710.3K
 * Total Submissions: 1.4M
 * Testcase Example:  '"hello"'
 *
 * Given a string s, reverse only all the vowels in the string and return it.
 *
 * The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
 * lower and upper cases, more than once.
 *
 *
 * Example 1:
 * Input: s = "hello"
 * Output: "holle"
 * Example 2:
 * Input: s = "leetcode"
 * Output: "leotcede"
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s consist of printable ASCII characters.
 *
 *
 */

// @lc code=start
func reverseVowels(s string) string {
	i, j := 0, len(s)-1

	vowels := "aeiouAEIOU"

	sRunes := []rune(s)

	for i < j {
		for i < j && !strings.Contains(vowels, string(sRunes[i])) {
			i++

		}
		for i < j && !strings.Contains(vowels, string(sRunes[j])) {
			j--

		}
		sRunes[i], sRunes[j] = sRunes[j], sRunes[i]

		i++

		j--

	}
	return string(sRunes)
}

// @lc code=end

