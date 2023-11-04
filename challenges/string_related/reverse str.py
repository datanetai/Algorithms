# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s[start],s[end] = s[end],s[start]
            start = start + 1
            end = end - 1
    
# solution 2 using for loop
def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]
# solution 3 using recursion
def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left,right):
            if left < right:
                s[left],s[right] = s[right],s[left]
                helper(left+1,right-1)
        helper(0,len(s)-1)

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s: str) -> str:
    start = 0
    end = 0
    s = list(s)
    while end < len(s):
        if s[end] == ' ':
            reverse(s,start,end-1)
            start = end + 1
        end = end + 1
    reverse(s,start,end-1)
    return ''.join(s)
def reverse(s,start,end):
    while start < end:
        s[start],s[end] = s[end],s[start]
        start = start + 1
        end = end - 1

# solution 2 ans 3 are pythonic
# solution 2
def reverseWords(s: str) -> str:
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    return ' '.join(s)
# solution 3
def reverseWords(s: str) -> str:
    return ' '.join([i[::-1] for i in s.split()])

arr = ["h","e","l","l","o"]

reverseString(arr)
print(arr)
word_arr = "Let's take LeetCode contest"
print(reverseWords(word_arr))
