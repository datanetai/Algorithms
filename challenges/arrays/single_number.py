# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# solution 1: Time complexity: O(n) Space complexity: O(n)
def singleNumber(nums: list) -> int:
    h = {}
    for i in nums:
        if i in h:
            h.pop(i)
        else:
            h[i] = 1
    return list(h.keys())[0]

# solution 2: Time complexity: O(n) Space complexity: O(1) using XOR because xor of two same number is 0
def singleNumber2(nums: list) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res
