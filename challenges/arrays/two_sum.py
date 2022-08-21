# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

# solution 1
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n1 = 0
        n2 = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]

# test
nums = [2,7,11,15]
target = 9
# print(twoSum(nums,target))

# solution 2 O(n)
# use hashmap to store the values and their index
# if we find the value in the hashmap, we return the index and the value
# if we don't find the value in the hashmap, we put the value and the index in the hashmap
# we return -1 if we don't find the value in the hashmap
def twoSum2( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    vals = {}
    for i in range(len(nums)):
        b = target - nums[i]
        if b in vals:
            return [i,vals[b]]
        else:
            vals[nums[i]]=i

def twoSum3( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    buffer = {}
    for i in range(len(nums)):
        if nums[i] in buffer:
            return [buffer[nums[i]],i]
        else:
            buffer[target-nums[i]]=i
            S
                       

print(twoSum2(nums,target))
