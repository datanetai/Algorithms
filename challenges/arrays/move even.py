# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

def sortArrayByParity(nums: list[int]) -> list[int]:
    even = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[even], nums[i] = nums[i], nums[even]
            even += 1
    return nums

if __name__ == "__main__":
    nums = [3,1,2,4]
    print(sortArrayByParity(nums)) # [2,4,3,1]