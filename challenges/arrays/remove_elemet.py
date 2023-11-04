# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# O(n) solution
def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start<=end:
            if nums[start]==val:
                nums[start],nums[end]=nums[end],nums[start]
                end-=1
            else:
                start+=1
        return end+1

# approach2 with same complexity O(n)
def removeElement2( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        return count
l = [3,2,2,3]
print(removeElement(l,3))
print(l)
    