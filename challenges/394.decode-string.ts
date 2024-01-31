/*
 * @lc app=leetcode id=394 lang=typescript
 *
 * [394] Decode String
 *
 * https://leetcode.com/problems/decode-string/description/
 *
 * algorithms
 * Medium (58.59%)
 * Likes:    12250
 * Dislikes: 571
 * Total Accepted:    752K
 * Total Submissions: 1.3M
 * Testcase Example:  '"3[a]2[bc]"'
 *
 * Given an encoded string, return its decoded string.
 * 
 * The encoding rule is: k[encoded_string], where the encoded_string inside the
 * square brackets is being repeated exactly k times. Note that k is guaranteed
 * to be a positive integer.
 * 
 * You may assume that the input string is always valid; there are no extra
 * white spaces, square brackets are well-formed, etc. Furthermore, you may
 * assume that the original data does not contain any digits and that digits
 * are only for those repeat numbers, k. For example, there will not be input
 * like 3a or 2[4].
 * 
 * The test cases are generated so that the length of the output will never
 * exceed 10^5.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "3[a]2[bc]"
 * Output: "aaabcbc"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "3[a2[c]]"
 * Output: "accaccacc"
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "2[abc]3[cd]ef"
 * Output: "abcabccdcdcdef"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 30
 * s consists of lowercase English letters, digits, and square brackets
 * '[]'.
 * s is guaranteed to be a valid input.
 * All the integers in s are in the range [1, 300].
 * 
 * 
 */

// @lc code=start
function decodeString(s: string): string {
    let countStack: number[] = [];
    let stringStack: string[] = [];
    let currentString = '';
    let currentNumber = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '[') {
            countStack.push(currentNumber)
            stringStack.push(currentString);
            currentNumber = 0;
            currentString = '';
        }
        else if (s[i] === ']') {
            let count = countStack.pop() as number;
            let lastString = stringStack.pop() as string;
            currentString = lastString + currentString.repeat(count);

        }
        else if (isNaN(Number(s[i]))) {
            currentString += s[i];
        }
        else {
            currentNumber = currentNumber * 10 + Number(s[i]);
        }
    }
    return currentString;
};
// @lc code=end

