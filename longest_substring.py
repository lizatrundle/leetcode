"""
Given a string s, find the length of 
the longest substring
 without repeating characters.
"""
#sliding window
#Runtime: 103 ms, faster than 69.26% of Python3 online submissions
def lengthOfLongestSubstring( s: str) -> int:
    left = 0
    right = 0
    longest = 0
    characters = set()
    length = len(s)

    while right<length:
        if s[right] not in characters:
            characters.add(s[right])
            right+=1
            longest = max(len(characters), longest)
        else:
            characters.remove(s[left])
            left+=1
    return longest
