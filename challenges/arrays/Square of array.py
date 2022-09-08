# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# solution 1 Complexity O(nlogn)
def sortedSquares(nums: list[int]) -> list[int]:
    return sorted([i**2 for i in nums])

# solution 2 two pointer Complexity O(n)
def sortedSquares2(nums: list[int]) -> list[int]:
    n = len(nums)
    negative = -1
    for i, v in enumerate(nums):
        if v < 0:
            negative = i
        else:
            break
    ans = list()
    i, j = negative, negative + 1
    while i >= 0 or j < n:
        if i < 0:
            ans.append(nums[j] ** 2)
            j += 1
        elif j == n:
            ans.append(nums[i] ** 2)
            i -= 1
        elif nums[i] ** 2 < nums[j] ** 2:
            ans.append(nums[i] ** 2)
            i -= 1
        else:
            ans.append(nums[j] ** 2)
            j += 1
    return ans

arr = [-4,-1,0,3,10]
print(sortedSquares(arr))
print(sortedSquares2(arr))
    