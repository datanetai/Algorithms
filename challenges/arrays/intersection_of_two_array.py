# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# solution 1 complexty O(nlog(n) + mlog(m))
def intersect( nums1: list[int], nums2: list[int]) -> list[int]:
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    i,j = 0,0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

# solution 2 complexty O(n + m) Space O(n) for n > m in worst case
def intersect2( nums1: list[int], nums2: list[int]) -> list[int]:
    counts = {}
    res = []
    for num in nums1:
        counts[num] = counts.get(num, 0) + 1
    for num in nums2:
        if num in counts and counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res