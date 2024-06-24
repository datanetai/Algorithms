# 1143. Longest Common Subsequence
# Medium
# Topics
# Companies
# Hint
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize a 2D array to store the lengths of common subsequences
        dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        def recurse(i, j):
            # Base case: if either string is empty, the common subsequence is empty
            if i == 0 or j == 0:
                return 0
            # If the result is already computed, return it
            if dp[i][j] != -1:
                return dp[i][j]
            # If the characters at the current positions are equal
            if text1[i - 1] == text2[j - 1]:
                # Include the character in the common subsequence and move to the previous positions
                dp[i][j] = 1 + recurse(i - 1, j - 1)
            else:
                # Exclude the character from the common subsequence and consider two possibilities
                dp[i][j] = max(recurse(i - 1, j), recurse(i, j - 1))
            return dp[i][j]
        
        # Call the recursive function with the lengths of the input strings 
        return recurse(len(text1), len(text2))