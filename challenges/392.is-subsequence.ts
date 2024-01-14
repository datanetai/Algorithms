/*
 * @lc app=leetcode id=392 lang=typescript
 *
 * [392] Is Subsequence
 *
 * https://leetcode.com/problems/is-subsequence/description/
 *
 * algorithms
 * Easy (47.97%)
 * Likes:    9214
 * Dislikes: 496
 * Total Accepted:    1.2M
 * Total Submissions: 2.6M
 * Testcase Example:  '"abc"\n"ahbgdc"'
 *
 * Given two strings s and t, return true if s is a subsequence of t, or false
 * otherwise.
 * 
 * A subsequence of a string is a new string that is formed from the original
 * string by deleting some (can be none) of the characters without disturbing
 * the relative positions of the remaining characters. (i.e., "ace" is a
 * subsequence of "abcde" while "aec" is not).
 * 
 * 
 * Example 1:
 * Input: s = "abc", t = "ahbgdc"
 * Output: true
 * Example 2:
 * Input: s = "axc", t = "ahbgdc"
 * Output: false
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= s.length <= 100
 * 0 <= t.length <= 10^4
 * s and t consist only of lowercase English letters.
 * 
 * 
 * 
 * Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
 * >= 10^9, and you want to check one by one to see if t has its subsequence.
 * In this scenario, how would you change your code?
 */

// @lc code=start
function isSubsequence(s: string, t: string): boolean {
    let i = 0;
    let j = 0;
    while (i < t.length && j < s.length) {
        if (s[j] === t[i]) {
            i++;
            j++;
        } else {
            i++;
        }
    }
    if (j === s.length)
        return true;
    return false

};


// approach 2 using for loop

function isSubsequence(s: string, t: string): boolean {
    let j = 0;
    for (let i = 0; i < t.length && j < s.length; i++) {
        if (s[j] === t[i]) {
            j++;
        }
    }
    return j === s.length;
}
// @lc code=end

