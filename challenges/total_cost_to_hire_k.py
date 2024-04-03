# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.

 

# Example 1:

# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.
# Example 2:

# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
# - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
# - In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
# The total hiring cost is 4.
 

# Constraints:

# 1 <= costs.length <= 105 
# 1 <= costs[i] <= 105
# 1 <= k, candidates <= costs.length



# Problem Summary:
# You are tasked with hiring k workers from a pool of n workers, where each worker has an associated cost costs[i]. The hiring process follows these rules:
# Hiring Sessions: You will conduct k hiring sessions, selecting one worker in each session.
# Candidate Selection: In each session, you consider two groups of candidates:
# The first candidates workers in the costs array.
# The last candidates workers in the costs array.
# Lowest Cost Selection: From these two groups, you choose the worker with the lowest cost. If there's a tie (multiple workers with the same lowest cost), you select the worker with the smallest index.
# Worker Uniqueness: A worker can only be hired once.
import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        # Initialize the heaps with the first and last 'candidates' elements
        first_heap = [(cost, i) for i, cost in enumerate(costs[:candidates])]
        last_heap = [(-cost, -i) for i, cost in enumerate(costs[-candidates:])]
        
        # Convert the lists into heaps
        heapq.heapify(first_heap)
        heapq.heapify(last_heap)
        
        total_cost = 0
        for _ in range(k):
            # Choose the minimum cost worker from the two heaps
            if first_heap[0][0] <= -last_heap[0][0]:
                cost, _ = heapq.heappop(first_heap)
                if candidates < len(costs):
                    heapq.heappush(first_heap, (costs[candidates], candidates))
                    candidates += 1
            else:
                cost, _ = heapq.heappop(last_heap)
                cost = -cost
                if len(costs) - candidates < len(costs):
                    heapq.heappush(last_heap, (-costs[-candidates-1], -len(costs) + candidates + 1))
                    candidates += 1
            
            total_cost += cost
        
        return total_cost
