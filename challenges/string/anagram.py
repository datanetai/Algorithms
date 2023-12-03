# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# complexity: O(m+n)
def isAnagram( s: str, t: str) -> bool:
    count = {}
    # we can also use list instead of dict as in next solution
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in t:
        if i in count:
            count[i] -= 1
        else:
            count[i] = 1
    for i in count:
        if count[i] != 0:
            return False
    return True
        
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


def canConstruct( ransomNote: str, magazine: str) -> bool:
    alphabets = [0]*26
    for letter in ransomNote:
        alphabets[ord(letter)-ord('a')] += 1
    for letter in magazine:
        if alphabets[ord(letter)-ord('a')] == 0:
            continue
        alphabets[ord(letter)-ord('a')] -= 1

    for i in alphabets:
        if i != 0:
            return False
    return True


        