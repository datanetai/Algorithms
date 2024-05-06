# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

 

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 

# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# Dynamic programming problems can be done in multiple steps.
# Step1: Find recurrence relation
# Step2: Recursive solution
# Step3: Memoization
# Step4: Tabulation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def min_cost_recursive(cost, i):
            if i >= len(cost):
                return 0
            
            one_step_cost = cost[i] + min_cost_recursive(cost,i+1)
            two_step_cost = cost[i]+min_cost_recursive(cost,i+2)

            return min(one_step_cost,two_step_cost)
        
        return min(min_cost_recursive(cost,0),min_cost_recursive(cost,1))
        
# Dynamic programming 1: Top Down/ Memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def min_cost_recursive( cost, i, dp={}):  # Default mutable argument
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            min_cost = cost[i] + min(min_cost_recursive(cost, i+1 , dp), min_cost_recursive(cost, i+2, dp))
            dp[i] = min_cost
            return min_cost
        
        return min(min_cost_recursive(cost, 0), min_cost_recursive(cost, 1)) 

# DP 2: Bottom up/ tabulation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)  # Create DP  table with additional 2 steps

        # Base cases
        dp[n] = 0  # Cost to reach the end from the end is 0
        dp[n + 1] = 0  # Cost to reach the end from one step after the end is 0

        #  Fill the dp table from the second last step
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0],  dp[1])  # Minimum cost to reach the top from either starting step
