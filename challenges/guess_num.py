# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

 

# Example 1:

# Input: n = 10, pick = 6
# Output: 6
# Example 2:

# Input: n = 1, pick = 1
# Output: 1
# Example 3:

# Input: n = 2, pick = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 231 - 1
# 1 <= pick <= n


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


# 1. Define the Search Space:
# Our search space is the range of possible numbers, from 1 to n (inclusive).
# Therefore, we initialize l = 1 and r = n.
# 2. Binary Search Loop:
# We use a while (l < r) loop since we want to exit when we have narrowed down to a single element (the picked number).
# Inside the loop:
# Calculate the middle element: m = l + (r - l) / 2 (avoiding potential overflow).
# Call the guess(m) API to get a hint.
# Analyze the result:
# If guess(m) == 0, we found the picked number! Return m.
# If guess(m) == 1, the picked number is higher, so we need to search in the right half. Update l = m + 1.
# If guess(m) == -1, the picked number is lower, so search in the left half. Update r = m.
# 3. Post Processing:
# After the loop, we are left with a single element (l or r, they are equal).
# This element is the picked number, so return l (or r).

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == 1:
                l = m + 1
            else:
                r = m
        return l  # or r, they are equal