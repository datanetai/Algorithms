# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.
def lengthOfLastWord(s: str) -> int:
    l = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == ' ' and l>0:
            return l
        elif s[i] == ' ':
            continue
        else:
            l += 1
    return l

# this is little faster
def lengthOfLastWord2(s: str) -> int:
    end = len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1
    start = end
    while start >= 0 and s[start] != ' ':
        start -= 1
    return end - start

    
s = "I fly in the air "
print(lengthOfLastWord2(s))
