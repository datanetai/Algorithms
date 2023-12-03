# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1

def firstUniqChar( s: str) -> int:
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1
