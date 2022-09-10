# Given a string s, find the length of the longest substring without repeating characters.

# Time complexity: O(n)
# Space complexity: O(m) where m is the unique characters in the string
def lengthOfLongestSubstring(s: str) -> int:
    # Create a dictionary to store the characters and their index
    char_dict = {}
    # Create a variable to store the length of the longest substring
    longest = 0
    # Create a variable to store the current length of the substring
    current = 0
    # Create a variable to store the index of the start of the substring
    start = 0
    # Loop through the string
    for i in range(len(s)):
        # If the character is in the dictionary and the index is greater than or equal to the start of the substring
        if s[i] in char_dict and char_dict[s[i]] >= start:
            # Set the start of the substring to the index of the character plus one
            start = char_dict[s[i]] + 1
            # Set the current length of the substring to the index minus the start of the substring plus one
            current = i - start + 1
        # Otherwise
        else:
            # Increment the current length of the substring
            current += 1
        # Set the index of the character in the dictionary to the current index
        char_dict[s[i]] = i
        # If the current length of the substring is greater than the longest length
        if current > longest:
            # Set the longest length to the current length
            longest = current
    # Return the longest length
    return longest


s = "dvdf"
print(lengthOfLongestSubstring(s)) # 3