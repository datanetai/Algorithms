# find number of consective 1s in a binary array
def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    return max_count

#  Find Numbers with Even Number of Digits
def findNumbers(nums: list[int]) -> int:
    count = 0
    for n in nums:
        c = 0 
        while n > 0:
            n //= 10
            c += 1
        if c % 2 == 0:
            count += 1
    return count

arr = [12,345,2,6,7896]
print(findNumbers(arr))

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


def duplicateZeros(arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def insert(arr, index, value):
            for i in range(len(arr)-1, index, -1):
                arr[i] = arr[i-1]
            arr[index] = value
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                insert(arr, i, 0)
                i += 1
            i += 1
        