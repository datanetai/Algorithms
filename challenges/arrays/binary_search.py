# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
# see this https://leetcode.com/problems/search-insert-position/discuss/249092/Come-on-forget-the-binary-search-patterntemplate!-Try-understand-it!
# and https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101 

# Time complexity: O(log n)
# Space complexity: O(1)
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        
        elif target < nums[mid]:
            right = mid - 1
        
        elif target > nums[mid]:
            left = mid + 1

    return -1


# recursive 
def search2(nums: list[int], target: int) -> int:
    def binary_search(left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        
        elif target < nums[mid]:
            return binary_search(left, mid - 1)
        
        elif target > nums[mid]:
            return binary_search(mid + 1, right)
    
    return binary_search(0, len(nums) - 1)

arr = [-1,0,3,5,9,12]
target = 9
print(search(arr, target))

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

def firstBadVersion( n: int) -> int:
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    # since left is the smallest that the condition is true, we can return left
    return left
def isBadVersion(version):
    # some condition ??
    return True
# the above code can be use as a general template for binary search

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity

def searchInsert (nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        
        elif target < nums[mid]:
            right = mid - 1
        
        elif target > nums[mid]:
            left = mid + 1

    return left

# similar version of the above problem

def searchInsert2 (nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    while l<r:
        mid = l + (r - l)/2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l =  mid+1
        else:
            r = mid
    return l+1 if nums[l] < target else l