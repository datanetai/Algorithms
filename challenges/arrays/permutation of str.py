# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Time complexity: O(nlogn)
# Space complexity: O(1)

def checkInclusion(s1: str, s2: str) -> bool:
    # sort 
    s1 = sorted(s1)
    # loop through s2
    for i in range(len(s2)-len(s1)+1):
        # check if s1 is in s2
        if sorted(s2[i:i+len(s1)]) == s1:
            return True
    return False

# solution 2 using hash table
# Time complexity: O(n)
# Space complexity: O(1)
def checkInclusion2(s1: str, s2: str) -> bool:
    # create a hash table
    hash_table = {}
    # loop through s1
    for char in s1:
        # if the character is in the hash table
        if char in hash_table:
            # increment the value
            hash_table[char] += 1
        # otherwise
        else:
            # set the value to 1
            hash_table[char] = 1
    # loop through s2
    for i in range(len(s2)-len(s1)+1):
        # create a copy of the hash table
        hash_table_copy = hash_table.copy()
        s_tmp = s2[i:i+len(s1)]
        # loop through s_tmp
        for char in s_tmp:
            # if the character is in the hash table
            if char in hash_table_copy:
                # decrement the value
                hash_table_copy[char] -= 1
                # if the value is 0
                if hash_table_copy[char] == 0:
                    # remove the key
                    del hash_table_copy[char]
            # otherwise
            else:
                # break
                break
        # if the hash table is empty
        if not hash_table_copy:
            # return true
            return True
    # return false
    return False

# solution 3 using sliding window
# Time complexity: O(n)
# Space complexity: O(1)
def checkInclusion3(s1: str, s2: str) -> bool:
    hash_table = {}
    # loop through s1
    for char in s1:
        # if the character is in the hash table
        if char in hash_table:
            # increment the value
            hash_table[char] += 1
        # otherwise
        else:
            # set the value to 1
            hash_table[char] = 1
    # create a variable to store the number of unique characters
    unique = len(hash_table)
    # create a variable to store the number of characters
    count = 0
    # create a variable to store the start of the window
    start = 0
    # loop through s2
    for i in range(len(s2)):
        # if the character is in the hash table
        if s2[i] in hash_table:
            # decrement the value
            hash_table[s2[i]] -= 1
            # if the value is 0
            if hash_table[s2[i]] == 0:
                # increment the number of unique characters
                unique -= 1
        # if the number of unique characters is 0
        if unique == 0:
            # return true
            return True
        # if the window is the length of s1
        if i - start + 1 == len(s1):
            # if the character is in the hash table
            if s2[start] in hash_table:
                # increment the value
                hash_table[s2[start]] += 1
                # if the value is 1
                if hash_table[s2[start]] == 1:
                    # increment the number of unique characters
                    unique += 1
            # increment the start of the window
            start += 1
    # return false
    return False
s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2)) # False
