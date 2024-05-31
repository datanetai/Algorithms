# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 


# we have two choice either loot house i or skip it so recurrence relation is
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])

from typing import List

# top down approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # If the list is empty, return 0
        if n == 0:
            return 0

        # If the list has only one element, return that element
        if n == 1:
            return nums[0]

        # Initialize a list to store the maximum amount of money that can be robbed up to each house
        dp = [-1] * n

        # Recursive function to calculate the maximum amount of money that can be robbed up to the i-th house
        def recurse(i):
            if i < 0:
                return 0

            # If we have already calculated the maximum amount of money that can be robbed up to the i-th house, return it
            if dp[i] >= 0:
                return dp[i]

            # If we are at the first house, the maximum amount of money that can be robbed is the amount of money in the first house
            if i == 0:
                dp[i] = nums[0]
            # If we are at the second house, the maximum amount of money that can be robbed is the maximum of the amount of money in the first house and the amount of money in the second house
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            # For any other house, the maximum amount of money that can be robbed is the maximum of the amount of money that can be robbed up to the (i-1)-th house and the amount of money in the i-th house plus the amount of money that can be robbed up to the (i-2)-th house
            else:
                dp[i] = max(recurse(i - 1), recurse(i - 2) + nums[i])

            # Return the maximum amount of money that can be robbed up to the i-th house
            return dp[i]

        # Return the maximum amount of money that can be robbed up to the last house
        return recurse(n - 1)
    

# bottom up approach tabulation

class Solution:
    def rob(self, nums: List[int]) -> int:
         # Get the length of the input list
        n = len(nums)
        if n == 1:
            return nums[0]
        dp= [0] * n

        # Initialize the base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # Iterate through the list starting from the third element
        for i in range(2, n):
            # Calculate the maximum amount of money that can be robbed up to the i-th house
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

            # Return the maximum amount of money that can be robbed up to the last house
        return dp[-1]
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Get the length of the input list
        n = len(nums)

        # Initialize the base cases
        prev1 = 0
        prev2 = 0

        # Iterate through the list
        for i in range(n):
            # Calculate the maximum amount of money that can be robbed up to the i-th house
            curr = max(prev1, prev2 + nums[i])

            # Update the previous two houses
            prev2 = prev1
            prev1 = curr

        # Return the maximum amount of money that can be robbed up to the last house
        return prev1

        