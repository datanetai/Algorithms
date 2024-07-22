// Code
// Testcase
// Testcase
// Test Result
// 1071. Greatest Common Divisor of Strings
// Solved
// Easy
// Topics
// Companies
// Hint
// For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

// Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

// Example 1:

// Input: str1 = "ABCABC", str2 = "ABC"
// Output: "ABC"
// Example 2:

// Input: str1 = "ABABAB", str2 = "ABAB"
// Output: "AB"
// Example 3:

// Input: str1 = "LEET", str2 = "CODE"
// Output: ""
 

// Constraints:

// 1 <= str1.length, str2.length <= 1000
// str1 and str2 consist of English uppercase letters.
// Seen this question in a real interview before?
// 1/5
// Yes
// No
// Accepted
// 496.5K
// Submissions
// 963.9K
// Acceptance Rate
// 51.5%
// Topics
// Companies
// Hint 1
// The greatest common divisor must be a prefix of each string, so we can try all prefixes.
// Similar Questions
// Discussion (274)

// Choose a type






func gcdOfStrings(str1 string, str2 string) string {
    if str1 == str2 {
        return str1
    }
    if len(str1) < len(str2) {
        return gcdOfStrings(str2, str1)
    }
    if str1[:len(str2)] == str2 {
        return gcdOfStrings(str1[len(str2):], str2)
    }
    return ""
}