# Given an array, rotate the array to the right by k steps, where k is non-negative.

# naive solution 
# Space complexity: O(n)
def rotate1( nums: list[int], k: int) -> None: 
    if k > len(nums):
        k = k % len(nums)

    ans = []
    i = 0
    n = len(nums) - k
    while k > 0:
        ans.append(nums[-k])
        k -= 1
 
    while i < n:
        ans.append(nums[i])
        i += 1
    for i in range(len(ans)):
        nums[i] = ans[i]

# using shift (brute force)
# Space complexity: O(n)
def rotate2( nums: list[int], k: int) -> None: 
    for i in range(k):
        nums.insert(0, nums.pop())
    


# using reverse
# Space complexity: O(1)
def rotate3( nums: list[int], k: int) -> None:
    if k > len(nums):
        k = k % len(nums)

    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

# using cyclic replacement
# Space complexity: O(1)
def rotate4( nums: list[int], k: int) -> None:
    def GCD(a, b):
        if b == 0:
            return a
        return GCD(b, a % b)
    
    if k == 0 or k == len(nums):
        return
    n = len(nums)
    k = k % n
    count = GCD(n, k)

    lcm = (len(nums) * k) // count
    for i in range(count):
        prev = nums[i]
        from_ = i
        j = 0
        while j < lcm/k:
            to_ = (from_ + k) % len(nums)
            nums[to_], prev = prev, nums[to_]
            from_ = to_
            j += 1



arr = [1,2,3,4,5,6,7]
k = 3
rotate4(arr, k)# [5, 6, 7, 1, 2, 3, 4]
print(arr)