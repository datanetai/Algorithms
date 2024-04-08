# 2300. Successful Pairs of Spells and Potions
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

# Example 1:

# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
# Example 2:

# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
# Thus, [2,0,2] is returned.
 

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort in ascending order for binary search
        result = []
        for spell in spells:
            # Calculate the minimum required potion strength for success
            min_strength = success // spell if success % spell == 0 else success // spell + 1
            # Use binary search to find the first potion that is successful
            index = self.binarySearch(potions, min_strength)
            # If binary search returns true, calculate the number of successful pairs
            if index != -1:
                count = len(potions) - index
            else:
                count = 0
            result.append(count)
        return result

    def binarySearch(self, potions: List[int], target: int) -> int:
        left, right = 0, len(potions) - 1
        while left <= right:
            mid = (left + right) // 2
            if potions[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        # If left is within the bounds of the array and the potion at 'left' meets the target
        if left < len(potions) and potions[left] >= target:
            return left
        return -1
