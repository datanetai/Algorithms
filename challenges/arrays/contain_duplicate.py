# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Time complexity O(n) and Space complexity O(n)
def containsDuplicate( nums: list) -> bool:
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i) 
    return False


