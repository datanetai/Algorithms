# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = i + 1
    while i < len(nums) and j < len(nums):
        if nums[i] == 0:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
        else:
            i += 1
            j += 1 

# solution 2 snowball method
# see https://leetcode.com/problems/move-zeroes/discuss/172432/THE-EASIEST-but-UNUSUAL-snowball-JAVA-solution-BEATS-100-(O(n))-%2B-clear-explanation
#  for details
def moveZeroes2(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    snowball_size = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            snowball_size += 1
        elif snowball_size > 0:
            nums[i - snowball_size] = nums[i]
            nums[i] = 0
            

arr = [0,1,0,3,12]
moveZeroes2(arr)
print(arr) # [1,3,12,0,0]