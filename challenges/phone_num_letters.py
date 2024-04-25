
# 17. Letter Combinations of a Phone Number
# Medium
# Topics
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def recurse(digits: str) -> List[str]:
            if len(digits) == 1:  # Base case: single digit
                return list(keyboard[digits[0]])
            result = []
            letters = keyboard[digits[0]]
            for letter in letters:
                for comb in recurse(digits[1:]):
                    result.append(letter + comb)
            return result

        return recurse(digits)

# using backtracking, the previous one only use recursion. Previous one was faster but the below is to illustrate the backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtract(path: list, position: int):
            if position == len(digits):
                paths.append("".join(path))
                return
            
            cur_digit_letters = keyboard[digits[position]]
            for letter in cur_digit_letters:
                path.append(letter)
                backtract(path,position+1)
                path.pop()

        paths = []
        backtract([],0)
        return paths
